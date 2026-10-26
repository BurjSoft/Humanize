---
name: humanize
description: Use when drafting, refining, reviewing or humanizing any prose so it reads like a specific person wrote it rather than a template - Upwork proposals, cover letters, CVs, resumes, screening answers, professional bios, outreach messages, emails, posts, READMEs and docs. Triggers on "humanize", "make this sound less AI", "remove AI tone", "make this more natural", or polishing career documents. Focuses on natural voice, reader relevance and factual accuracy; never fabricates facts or promises undetectability.
---

# Humanize

## Purpose
Make writing sound like a specific, experienced person instead of a template. Informed by the editorial approach of `blader/humanizer` and the pattern / false-positive checks of `Aboudjem/humanizer-skill` (both MIT). This is an original workflow, not a copy or port of either project.

Reader response and factual truth come before any AI-detector score. This skill is instruction-only: it runs no detector, CLI or API and produces no numeric "AI score". Never promise undetectability, and never claim a detector was used unless one actually returned results in this session.

## Source of truth
- Use only facts present in the user's text, files they point to (resume, profile, project notes) and their corrections in the conversation.
- Never invent clients, roles, projects, features, outcomes, metrics, years, tools, certifications or personal anecdotes.
- Preserve proper nouns, versions, dates, URLs, numbers, ownership of work and eligibility/location constraints exactly, even when they hurt the pitch.
- If a claim cannot be verified, qualify it or cut it. Ask rather than guess when a missing fact matters.
- Respect explicit user instructions (include/exclude a project, keep a phrase, length limit) over these defaults.

## Workflow
1. Identify document type, audience, purpose and length limit. Find the single strongest claim the reader cares about.
2. Scan for AI-sounding patterns:
   - stock openers and closers ("I hope this finds you well", "I'm excited to", "Feel free to reach out")
   - redundant setup and restating the question
   - "It's not X, it's Y" contrasts and dramatic one-line paragraphs
   - ritual three-item lists, repeated sentence openings, uniform paragraph shape
   - vague corporate verbs and inflated adjectives
   - em dashes used as a default connector
   - unearned enthusiasm, generic praise of the reader, hedging stacks
   - summaries that repeat what was just said
3. Check for false positives before changing anything: correct grammar, tight technical prose, necessary repeated technology names, a deliberate list or one short sentence are not robotic in themselves. Stylistic statistics are meaningless on very short text.
4. Rewrite around meaning, not word-by-word synonym swaps. Vary sentence length where it helps reading. Do not add typos, slang, fake memories or deliberate errors to look human.
5. Diff the revision against the source: every number, name, version, date, responsibility and implied level of involvement must survive. Fix anything that drifted.
6. Reread as the target reader on a quick skim: is the point clear in the first lines, is every sentence earning its place?
7. Output the polished text by default, with no commentary about the writing process inside it. Explain the edits only if asked.

## Word and style defaults
Avoid unless accurate or quoted from the user: "delve", "seamless", "cutting-edge", "leverage" (fine when technically precise), "unlock", "transformative", "robust solutions", "foster", "passionate about", "game-changer", "in today's fast-paced world", "I am the perfect fit". Avoid em dashes by default; use commas, periods or parentheses. Tone: professional, direct, slightly conversational, confident without boasting.

## Upwork proposals
- The first 1-2 lines must stand alone in the truncated preview: lead with the client's concrete problem and an actionable insight or a closely related verified project.
- No greetings, self-introductions, "I believe", generic promises or stack dumps.
- Show a pragmatic approach with concrete steps or deliverables. One strong verified proof point; a second only if it adds distinct evidence.
- Short paragraphs, mobile-readable. Close with a specific question only if it moves the conversation.
- Disclose real gaps (missing required tech, location, licensing). Never humanize away a deal-breaker.
- If the project has its own job-qualification rules (match score, apply/skip, bid), those control the decision. This skill refines wording only; re-verify the proposal after humanizing.

## CVs and resumes
- Keep ATS-friendly headings, job titles, chronology, bullet structure, technology keywords and original metrics.
- Do not swap "Angular", "React", "Node.js", "AWS" or project names for elegant synonyms; repetition of keywords is often required.
- Strong but defensible verbs; no padding adjectives, no invented quantified impact. Resumes can stay more standardized than proposals; do not force burstiness.

## Cover letters, screening answers, outreach
- Answer the actual question in the first sentence, then support it with relevant verified examples.
- Match the employer's tone without pretending to know their internal problems.
- Do not mechanically repeat resume bullets. Keep work-authorization and location facts intact.

## Other writing (emails, posts, docs, READMEs)
- Same pattern scan and fact preservation. Keep code, commands, identifiers and technical terms verbatim.
- Docs may stay neutral and structured; humanizing means cutting filler and hype, not adding personality.

## Final self-check
- Do the opening lines work on their own?
- Does every claim have verified support?
- Is there a concrete problem and approach (proposals) or direct answer (questions)?
- Is the tone natural without contrived informality?
- For resumes, are ATS keywords and metrics preserved?
- Would deleting any remaining sentence make it better? If so, delete it.

## Limitations
No heuristic or commercial detector reliably proves human authorship. Detector results, if a real one is run, are advisory: review false positives and never trade credibility for a score.
