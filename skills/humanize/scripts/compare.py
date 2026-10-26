#!/usr/bin/env python3
"""Before/after fact check for the humanize skill. Python 3.10+, stdlib only.

Usage: python compare.py [--strict] <original> <rewrite>    (one of them may be - for stdin)

Lists facts that appear in the original but not in the rewrite (numbers,
versions, dates, URLs, emails, technology and project names, quoted text,
negations, qualifiers), and certainty words the rewrite added. It matches
strings, not meaning: a fact that was reworded on purpose shows as missing,
and a meaning change with the same tokens passes. In particular it cannot see
swapped roles ("helped build X and led Y" becoming "led X and helped build Y")
or a fact that appears fewer times; it is a prompt for review, not a validator.

Exit code 1 when a fact, negation or qualifier is missing or an absolute
("guaranteed", "always") was added. A capitalized word seen only at a sentence
start is reported as a possible name to confirm, not a failure, because
rewrites change openers constantly. With --strict, possible names and new terms
in the rewrite also fail.
Read every item before acting on it.
"""
import re
import sys
from collections import Counter

NUMBER = re.compile(r"(?<![\w.])(?:[vV](?=\d))?[$\u00a3\u20ac]?\d[\d,]*(?:\.\d+)*(?:%|k|K|m|M|x|\+)?(?![\w])")
URL = re.compile(r"https?://[^\s)>\]]+")
EMAIL = re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.]+\b")
# Words with internal capitals, dots or digits, or all caps: Node.js, PostgreSQL, AWS, S3, MotoMate123.
TERM = re.compile(r"\b(?:[A-Za-z]+[.#+][A-Za-z0-9]+|[A-Z][a-z0-9]*[A-Z0-9][A-Za-z0-9]*|[A-Z]{2,}\d*)\b")
CAPITALIZED = re.compile(r"(?<![.!?]\s)(?<!^)\b[A-Z][a-z]{2,}\b", re.M)
QUOTED = re.compile(r"\"([^\"\n]{3,80})\"|\u201c([^\u201d\n]{3,80})\u201d")
NEGATIONS = ["not", "never", "no", "without", "don't", "didn't", "can't", "won't", "isn't",
             "wasn't", "haven't", "hasn't", "unconfirmed"]
QUALIFIERS = ["helped", "assisted", "contributed", "co-led", "supported", "about",
              "approximately", "around", "roughly", "up to", "nearly", "almost", "over",
              "more than", "could", "may", "might", "can", "typically", "usually", "some",
              "partly", "part of", "familiar", "exposure", "basic"]
ABSOLUTES = ["always", "never", "every", "all", "only", "guaranteed", "guarantee",
             "completely", "fully", "100%", "sole", "solely", "single-handedly", "expert",
             "extensively", "extensive", "deep", "proven"]
STOP_CAPS = {"The", "This", "That", "These", "Those", "And", "But", "For", "With", "When",
             "Where", "Then", "Our", "Your", "Their", "You", "She", "They", "What", "How",
             "Why", "Who", "Its", "His", "Her", "Also", "Each", "Any", "Some", "Most"}
SENTENCE_START = re.compile(r"(?:^|(?<=[.!?:]\s))\s*([A-Z][a-z]{2,})\b", re.M)
# Ordinary words that open sentences. Anything else capitalized there is treated as a
# name ("Stripe handles payments."), so a dropped client or tool is still reported.
COMMON_OPENERS = STOP_CAPS | {
    "After", "Before", "During", "Since", "Until", "While", "Once", "Today", "Now", "Next",
    "Later", "First", "Second", "Third", "Finally", "Last", "Here", "There", "Yes", "Not",
    "All", "Both", "Many", "Several", "Every", "Few", "More", "Other", "Such", "One",
    "Two", "Three", "Can", "Could", "Would", "Should", "Will", "Did", "Does", "Have",
    "Has", "Had", "Was", "Were", "Are", "Use", "Run", "See", "Let", "Please", "Thanks",
    "Thank", "Sorry", "Happy", "Glad", "Just", "Only", "Even", "Still", "However", "Instead",
    "Otherwise", "Because", "Although", "Though", "Unless", "Whether", "Without", "From",
    "Into", "About", "Over", "Under", "Between", "Through", "Within", "Across", "Along",
    "Hello", "Dear", "Regards", "Best", "Note", "Hey"}


def norm(text):
    return text.replace("\u2019", "'").replace("\u2018", "'").lstrip("\ufeff")


def facts(text):
    found = Counter()
    for m in URL.finditer(text):
        found["url: " + m.group(0).rstrip(".,")] += 1
    no_urls = URL.sub(" ", text)
    for m in EMAIL.finditer(no_urls):
        found["email: " + m.group(0)] += 1
    for m in NUMBER.finditer(no_urls):
        found["number: " + m.group(0).replace(",", "")] += 1
    for m in TERM.finditer(no_urls):
        found["term: " + m.group(0)] += 1
    for m in CAPITALIZED.finditer(no_urls):
        if m.group(0) not in STOP_CAPS:
            found["name: " + m.group(0)] += 1
    # A capitalized word seen only at a sentence start may be a name ("Stripe handles
    # payments.") or just an opener ("Deployment happens on Friday."), so it is kept
    # apart and only fails the run in --strict mode.
    for m in SENTENCE_START.finditer(no_urls):
        word = m.group(1)
        if word not in COMMON_OPENERS and "name: " + word not in found \
                and "term: " + word not in found:
            found["possible name: " + word] += 1
    for m in QUOTED.finditer(text):
        found["quote: " + (m.group(1) or m.group(2))] += 1
    return found


def words(text, vocabulary):
    low = text.lower()
    return Counter({w: len(re.findall(r"(?<![\w-])" + re.escape(w) + r"(?![\w-])", low))
                    for w in vocabulary})


def contains_fact(key, extracted, text):
    kind, value = key.split(": ", 1)
    if kind in {"number", "url", "email"}:
        return key in extracted
    # Names can move to sentence starts or change case without changing facts.
    return re.search(r"(?<!\w)" + re.escape(value) + r"(?!\w)", text, re.I) is not None


def compare(original, rewrite, strict=False):
    original, rewrite = norm(original), norm(rewrite)
    out = []
    before, after = facts(original), facts(rewrite)
    absent = sorted(k for k in before
                    if not contains_fact(k, after, rewrite))
    missing = [k for k in absent if not k.startswith("possible name: ")]
    possible = [k for k in absent if k.startswith("possible name: ")]
    failed = bool(missing) or (strict and bool(possible))
    if missing:
        out.append("missing from rewrite:")
        out.extend("  " + k for k in missing)
    if possible:
        out.append("possible names missing (sentence-start words; confirm, fails only with --strict):")
        out.extend("  " + k.removeprefix("possible ") for k in possible)
    for label, vocab in (("negations", NEGATIONS), ("qualifiers", QUALIFIERS)):
        b, a = words(original, vocab), words(rewrite, vocab)
        lost = sorted(w for w in vocab if a[w] < b[w])
        if lost:
            failed = True
            out.append(f"fewer {label} (check certainty and scope): {lost}")
    b, a = words(original, ABSOLUTES), words(rewrite, ABSOLUTES)
    gained = sorted(w for w in ABSOLUTES if a[w] > b[w])
    if gained:
        failed = True
        out.append(f"absolutes added (check for overclaiming): {gained}")
    # New sentence openers are routine in a rewrite, so they are not listed as new facts.
    new = sorted(k for k in after
                 if not k.startswith("possible name: ") and not contains_fact(k, before, original))
    if new:
        failed = failed or strict
        out.append("new in rewrite (confirm each is a verified fact):")
        out.extend("  " + k for k in new)
    if not out:
        out.append("no missing facts found by string match")
    return out, failed


def read(path):
    if path == "-":
        return sys.stdin.read()
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except OSError as e:
        sys.exit(f"cannot read {path}: {e.strerror}")


def main():
    for stream in (sys.stdin, sys.stdout):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    args = sys.argv[1:]
    strict = "--strict" in args
    paths = [a for a in args if a != "--strict"]
    if len(paths) != 2 or paths == ["-", "-"]:
        sys.exit("usage: python compare.py [--strict] <original> <rewrite>  (only one may be -)")
    report, failed = compare(read(paths[0]), read(paths[1]), strict)
    print("\n".join(report))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
