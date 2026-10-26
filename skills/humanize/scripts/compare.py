#!/usr/bin/env python3
"""Before/after fact check for the humanize skill. Python 3.10+, stdlib only.

Usage: python compare.py <original> <rewrite>    (one of them may be - for stdin)

Lists facts that appear in the original but not in the rewrite (numbers,
versions, dates, URLs, emails, technology and project names, quoted text,
negations, qualifiers), and certainty words the rewrite added. It matches
strings, not meaning: a fact that was reworded on purpose shows as missing,
and a meaning change with the same tokens passes. Exit code 1 when anything
is missing, so it can gate a script; read every item before acting on it.
"""
import re
import sys
from collections import Counter

NUMBER = re.compile(r"(?<![\w.])(?:[vV](?=\d))?[$£€]?\d[\d,]*(?:\.\d+)*(?:%|k|K|m|M|x|\+)?(?![\w])")
URL = re.compile(r"https?://[^\s)>\]]+")
EMAIL = re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.]+\b")
# Words with internal capitals, dots or digits, or all caps: Node.js, PostgreSQL, AWS, S3, MotoMate123.
TERM = re.compile(r"\b(?:[A-Za-z]+[.#+][A-Za-z0-9]+|[A-Z][a-z0-9]*[A-Z0-9][A-Za-z0-9]*|[A-Z]{2,}\d*)\b")
CAPITALIZED = re.compile(r"(?<![.!?]\s)(?<!^)\b[A-Z][a-z]{2,}\b", re.M)
QUOTED = re.compile(r"\"([^\"\n]{3,80})\"|“([^”\n]{3,80})”")
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


def norm(text):
    return text.replace("’", "'").replace("‘", "'").lstrip("﻿")


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


def compare(original, rewrite):
    original, rewrite = norm(original), norm(rewrite)
    out = []
    before, after = facts(original), facts(rewrite)
    missing = sorted(k for k in before
                     if not contains_fact(k, after, rewrite))
    has_loss = bool(missing)
    if missing:
        out.append("missing from rewrite:")
        out.extend("  " + k for k in missing)
    for label, vocab in (("negations", NEGATIONS), ("qualifiers", QUALIFIERS)):
        b, a = words(original, vocab), words(rewrite, vocab)
        lost = sorted(w for w in vocab if a[w] < b[w])
        if lost:
            has_loss = True
            out.append(f"fewer {label} (check certainty and scope): {lost}")
    b, a = words(original, ABSOLUTES), words(rewrite, ABSOLUTES)
    gained = sorted(w for w in ABSOLUTES if a[w] > b[w])
    if gained:
        out.append(f"absolutes added (check for overclaiming): {gained}")
    new = sorted(k for k in after
                 if not contains_fact(k, before, original))
    if new:
        out.append("new in rewrite (confirm each is a verified fact):")
        out.extend("  " + k for k in new)
    if not out:
        out.append("no missing facts found by string match")
    return out, has_loss


def read(path):
    if path == "-":
        return sys.stdin.read()
    with open(path, encoding="utf-8") as f:
        return f.read()


def main():
    for stream in (sys.stdin, sys.stdout):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    if len(sys.argv) != 3 or sys.argv[1:] == ["-", "-"]:
        sys.exit("usage: python compare.py <original> <rewrite>  (only one may be -)")
    report, missing = compare(read(sys.argv[1]), read(sys.argv[2]))
    print("\n".join(report))
    sys.exit(1 if missing else 0)


if __name__ == "__main__":
    main()
