#!/usr/bin/env python3
"""Optional mechanical sweep for the humanize skill. Python 3.10+, stdlib only.

Usage: python check.py <file>    (or - to read stdin)

Counts what a final read tends to miss. It flags and never rewrites, and it
does not estimate whether a human or a model wrote the text. A hit is a prompt
to look, not a verdict. Skip the rhythm numbers for text under ~80 words.
"""
import re
import statistics
import sys
import unicodedata
from collections import Counter

STOCK = ["delve", "bolster", "illuminate", "elucidate", "underscore", "underpin",
         "tapestry", "synergy", "beacon", "interplay", "intricate", "myriad",
         "plethora", "multifaceted", "holistic", "pivotal", "realm", "testament",
         "meticulous", "vibrant", "cutting-edge", "game-changing", "unparalleled",
         "unwavering", "ever-evolving", "commendable"]
MARKETING = ["empower", "unlock", "elevate", "seamless", "streamline", "revolutioniz",
             "supercharge", "next-level", "best-in-class", "world-class",
             "transformative", "game-changer", "harness the power"]
CAREER = ["passionate about", "perfect fit", "perfect candidate", "results-driven",
          "hit the ground running", "go above and beyond", "wear many hats",
          "i came across your", "i have carefully read", "i am confident that i can",
          "i'm excited to apply", "looking forward to hearing from you",
          "feel free to reach out", "i hope this", "great question"]
TRANSITIONS = ["Additionally", "Furthermore", "Moreover", "Importantly", "Notably",
               "Ultimately", "In conclusion", "Lastly", "That said",
               "Needless to say", "In other words"]
STAGING = [r"here'?s (the thing|what|why)", r"let me be clear", r"let'?s (break|dive)",
           r"the (best part|secret)\s*:", r"\bthe truth is\b", r"\bnot just\b[^.]{1,60}\bbut\b",
           r"it'?s not [^.]{1,40}[,.;] it'?s", r"this means that", r"as you can see",
           r"notice how", r"the bottom line", r"key takeaway", r"what do you think\?",
           r", (highlighting|underscoring|reflecting|showcasing) "]
HEDGES = ["arguably", "it's worth noting", "it is worth noting", "it's important to note",
          "it is important to note", "could potentially"]
OPENERS = {"the", "it", "it's", "this", "that", "that's", "these", "you", "i"}
INVISIBLE = re.compile("[​‌‍⁠﻿]")
LOOKALIKE = re.compile("[Ѐ-ӿͰ-Ͽ]")
INFLATED = ["utilize", "facilitate", "commence", "endeavor", "ascertain", "in order to",
            "due to the fact that", "has the ability to", "at this point in time"]
DRESSED_UP = re.compile(r"\b(serves|served|stands|stood|functions) as an?\b|\bboasts\b", re.I)
VAGUE_AUTHORITY = re.compile(r"\b(experts|researchers|analysts|studies|research) "
                             r"(agree|argue|say|says|suggest|suggests|show|shows|believe)\b"
                             r"|\bit is widely (recognized|accepted|known)\b", re.I)
NAME_DROPPING = re.compile(r"\b(featured in|as seen (in|on)|trusted by (leading|top)"
                           r"|fortune 500 (companies|clients))\b", re.I)
CAVEATS = ["results may vary", "every project is different", "no solution is perfect",
           "it's important to remember", "it is important to remember"]
PLACEHOLDER = re.compile(r"\[(?:your|insert|add|enter|describe|specify|client|company|name)[^\]]{0,40}\]"
                         r"|\b\d{4}-XX-XX\b", re.I)
CITATION_LEAK = re.compile(r"cite\s*turn\d+\w*|contentReference\[oaicite:\d+\]|oai_citation"
                           r"|\[attached_file:\d+\]")
AI_REFERRER = re.compile(r"utm_source=(?:chatgpt\.com|openai|claude\.ai|perplexity\.ai|copilot\.com)",
                         re.I)
UNICODE_SPACES =re.compile("[   -   　]")


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [p.strip() for p in parts if len(p.split()) >= 2]


def check(text):
    # Word processors insert curly apostrophes; the phrase lists use straight ones.
    text = text.replace("’", "'").replace("‘", "'")
    low = text.lower()
    out = []

    def flag(label, hits):
        if hits:
            out.append(f"{label}: {hits}")

    flag("em dashes / spaced en dashes", text.count("—") + len(re.findall(r" – | -- ", text)))
    flag("semicolons", text.count(";"))
    flag("stock AI words", [w for w in STOCK if re.search(r"\b" + re.escape(w), low)])
    flag("marketing words", [w for w in MARKETING if w in low])
    flag("career cliches", [p for p in CAREER if p in low])
    flag("filler transitions", [t for t in TRANSITIONS
                                if re.search(r"(^|[.!?]\s+|\n)" + t + r"\b", text)])
    flag("staging / pointing", [m.group(0).strip()[:50] for p in STAGING
                                for m in re.finditer(p, text, re.I | re.M)])
    flag("filler hedges", [h for h in HEDGES if h in low])
    flag("inflated verbs / filler phrases", [w for w in INFLATED if re.search(r"\b" + w, low)])
    flag("dressed-up verbs", [m.group(0) for m in DRESSED_UP.finditer(text)])
    flag("vague authority", [m.group(0) for m in VAGUE_AUTHORITY.finditer(text)])
    flag("name dropping", [m.group(0) for m in NAME_DROPPING.finditer(text)])
    flag("unnecessary caveats", [c for c in CAVEATS if c in low])
    flag("unfilled placeholders", PLACEHOLDER.findall(text))
    flag("chat citation leaks", CITATION_LEAK.findall(text))
    flag("AI referrer URL parameters", AI_REFERRER.findall(text))
    flag("bold-label starts", len(re.findall(r"^\s*[-*]?\s*\*\*[^*]{1,60}\*\*\s*[.:]?", text, re.M)))
    flag("exclamation marks", text.count("!"))
    flag("invisible characters", len(INVISIBLE.findall(text)))
    flag("non-standard spaces", len(UNICODE_SPACES.findall(text)))
    unusual = Counter(INVISIBLE.findall(text) + UNICODE_SPACES.findall(text))
    if unusual:
        details = ", ".join(
            f"U+{ord(char):04X} {unicodedata.name(char, 'UNNAMED')} x{count}"
            for char, count in sorted(unusual.items())
        )
        out.append(f"Unicode review (may be legitimate; preserve context): {details}")
    if re.search(r"[A-Za-z]", text):
        flag("Cyrillic/Greek letters (check for look-alikes)", len(LOOKALIKE.findall(text)))

    sents = sentences(text)
    lens = [len(s.split()) for s in sents]
    if len(text.split()) >= 80 and len(lens) >= 4:
        med = statistics.median(lens)
        band = sum(1 for n in lens if abs(n - med) <= 5) / len(lens)
        mean = statistics.mean(lens)
        note = ""
        if band >= 0.7:
            note = " (uniform: merge some short ones)" if mean < 11 else " (uniform: vary length)"
        out.append(f"sentences: {len(lens)}, mean {mean:.1f} words, "
                   f"{band:.0%} within 5 words of the median{note}")
        starts = [s.split()[0].lower().strip("\"'*") for s in sents]
        share = sum(1 for w in starts if w in OPENERS) / len(starts)
        if share >= 0.4:
            out.append(f"openers: {share:.0%} of sentences start with The/It/This/That/You/I")
    out.append(f"words: {len(text.split())}")
    return out


def main():
    for stream in (sys.stdin, sys.stdout):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    if len(sys.argv) < 2 or sys.argv[1] == "-":
        text = sys.stdin.read()
    else:
        with open(sys.argv[1], encoding="utf-8") as f:
            text = f.read()
    # A leading byte-order mark comes from the editor or shell, not the writing.
    if text.startswith("﻿"):
        text = text[1:]
    print("\n".join(check(text)))


if __name__ == "__main__":
    main()
