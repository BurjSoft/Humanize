#!/usr/bin/env python3
"""Upwork preview check for the humanize skill. Python 3.8+, stdlib only.

Usage: python preview.py <proposal> [--job <job post file>]

Shows the first ~200 characters, the part a client sees before clicking, and
flags openings that waste it: greetings, self-introductions, restating the job
post, stock enthusiasm. With --job it lists which distinctive terms from the
post the opening mentions. It cannot judge whether the opening addresses the
client's real problem or whether a claim is true; that stays a human check.
"""
import argparse
import re
import sys

PREVIEW_CHARS = 200
OPENING_TELLS = [
    (r"^\s*(hi|hello|hey|dear|greetings|good (morning|afternoon|evening))\b", "greeting"),
    (r"\b(my name is|i am a|i'm a|i am an|i'm an)\b", "self-introduction"),
    (r"\bwith (over )?\d+\+? years of experience\b", "years-of-experience opener"),
    (r"\b(i (have )?(read|reviewed|went through|came across) your (job|post|project|requirements))",
     "says they read the post"),
    (r"\b(you are|you're) looking for\b", "restates the job post"),
    (r"\b(i'm|i am) (excited|thrilled|happy|glad|delighted)\b", "stock enthusiasm"),
    (r"\b(perfect fit|ideal candidate|best candidate|look no further)\b", "self-praise"),
    (r"\bi (believe|think) i can\b", "hedged promise"),
]
STOP = set("""a an the and or but for with from into onto over under about above our your their
this that these those is are was were be been being have has had do does did will would can
could should may might must we you they he she it its i me my us them who what which when where
why how not no yes all any each more most some such than then too very just also only own same
so of in on at by to as if per via up out off again further once here there both few other
nor every work job need needs looking want wants someone project projects team help please
include including well using use used make made new""".split())


def norm(text):
    return text.replace("’", "'").replace("‘", "'").lstrip("﻿")


def job_terms(job):
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9.+#-]*[A-Za-z0-9+#]|\d+%?", job)
    seen, terms = set(), []
    for t in tokens:
        key = t.lower()
        if key in STOP or len(key) < 3 or key in seen:
            continue
        seen.add(key)
        terms.append(t)
    return terms


def preview(proposal, job=None):
    proposal = norm(proposal).strip()
    head = proposal[:PREVIEW_CHARS]
    if len(proposal) > PREVIEW_CHARS and " " in head:
        head = head.rsplit(" ", 1)[0]
    out = [f"preview ({len(head)} chars): {head}"]
    low = head.lower()
    tells = [label for pattern, label in OPENING_TELLS if re.search(pattern, low, re.M)]
    if tells:
        out.append(f"opening tells: {tells}")
    if job:
        terms = job_terms(norm(job))
        hits = [t for t in terms if re.search(r"(?<![\w])" + re.escape(t.lower()) + r"(?![\w])", low)]
        out.append(f"job-post terms in preview: {hits or 'none'}")
    words = len(proposal.split())
    paragraphs = [p for p in re.split(r"\n\s*\n", proposal) if p.strip()]
    longest = max((len(p.split()) for p in paragraphs), default=0)
    count = len(paragraphs)
    out.append(f"length: {words} words, {count} paragraph{'s' if count != 1 else ''}, "
               f"longest {longest} words")
    if longest > 80:
        out.append("long paragraph: over 80 words reads as a wall of text on mobile")
    return out


def main():
    for stream in (sys.stdin, sys.stdout):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Check an Upwork proposal's preview.")
    parser.add_argument("proposal", help="proposal file, or - for stdin")
    parser.add_argument("--job", help="job post file to compare terms against")
    args = parser.parse_args()
    if args.proposal == "-":
        text = sys.stdin.read()
    else:
        with open(args.proposal, encoding="utf-8") as f:
            text = f.read()
    job = None
    if args.job:
        with open(args.job, encoding="utf-8") as f:
            job = f.read()
    print("\n".join(preview(text, job)))


if __name__ == "__main__":
    main()
