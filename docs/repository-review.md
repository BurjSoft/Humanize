# Repository comparison and adoption decisions

## Follow-up: four requested repositories, 2026-10-26

This follow-up inspected the GitHub `main` pages linked below; they are moving references, not additional pinned checkouts. Existing staged improvements were present before this follow-up. No upstream service, detector or benchmark was run. The older five-repository review below retains its original scope and commit references.

| Repository and inspected paths | Assessment and action |
| --- | --- |
| [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing/blob/main/skills/avoid-ai-writing/SKILL.md): editing contract, modes, fidelity and protected content | Strong scope discipline: a match is not automatically a finding or permission to edit. Our workflow already follows this. Fixed a conflicting residue rule so ordinary polishing preserves source URLs; explicit URL cleanup preserves other query parameters and fragments. Did not import mandatory full-reference loading or convergence loops. |
| [lynote-ai/humanize-text-skill](https://github.com/lynote-ai/humanize-text-skill/blob/main/SKILL.md), [engine](https://github.com/lynote-ai/humanize-text-skill/blob/main/detector/patterns.js), README | Useful separation of writing quality, target voice and fidelity. The README explicitly says fidelity is enforced by instructions, not returned as an engine field. Its numeric score and voice distance do not establish meaning preservation. Our existing voice-sample rules already prevent copying sample facts. Kept the lightweight workflow rather than importing its bilingual policy and scoring engine. |
| [Oct4Pie/zero-zerogpt](https://github.com/Oct4Pie/zero-zerogpt), [App.js](https://github.com/Oct4Pie/zero-zerogpt/blob/main/src/App.js), Unicode-space definitions | Space substitution is a detector experiment, not editorial improvement. No substitution or export code adopted. Our checker already counted unusual spacing; it now names the code points and counts, with a legitimate-use caution. It never changes input. Joiners in emoji or language remain valid. No current detector bypass claim was tested. |
| [phuryn/work-humanizer](https://github.com/phuryn/work-humanizer/blob/main/skills/work-humanizer/SKILL.md), [evidence account](https://github.com/phuryn/work-humanizer/blob/main/evidence/README.md), README | Its emphasis on commitments and separate meaning/readability judgments is useful and already reflected in our ledger. Added an acknowledgment/credit case that catches invented apologies, completed payments and deadlines. Tightened evidence handling: a hedge cannot rescue invented experience. Upstream studies use small sets and model judges; their detector results are not results for this project. |

Added manual cases for protected referrers, unsupported experience, intentional templates and acknowledgment versus admission. These are evaluation criteria, not executed model comparisons. Automated checks cover only checker behavior; package validation covers skill structure. Neither proves writing quality.

## Earlier five-repository review

Reviewed on 2026-10-26 against source checkouts at the commits below. Scope: skill entrypoints, relevant implementation paths, evaluation documentation and selected tests. This was a source review, not an execution of upstream rewriting services, detector models or complete test suites. Upstream benchmarks were not independently reproduced. Links are pinned to the reviewed versions.

All five repositories have MIT license files at these commits. They are research references, not runtime dependencies. This report records editorial conclusions, not a certification of the repositories. Humanize's optional local checker produces pattern counts, not an authorship score.

## avoid-ai-writing

Commit: `209815cdeb4af942616daec89a5e0a706c804e3a`.

Inspected the [skill and editing contract](https://github.com/conorbronsdon/avoid-ai-writing/blob/209815cdeb4af942616daec89a5e0a706c804e3a/skills/avoid-ai-writing/SKILL.md), [Markdown protection implementation](https://github.com/conorbronsdon/avoid-ai-writing/blob/209815cdeb4af942616daec89a5e0a706c804e3a/skills/avoid-ai-writing/scripts/markdown-prose.js), package scripts and [rewrite evaluation documentation](https://github.com/conorbronsdon/avoid-ai-writing/blob/209815cdeb4af942616daec89a5e0a706c804e3a/evals/rewrite/README.md).

Useful: separate audit from rewrite and file edits; preserve clean passages; protect exact content; examine contextual exceptions before acting on a phrase. Its evaluation documentation explicitly distinguishes literal checks from semantic fidelity and historical preparation from executed evidence.

Application to Humanize: scope-aware editing, unchanged output for clean text, protected content and source-as-data handling. Added behavioral cases for these decisions. Did not import the detector, severity tiers, mandatory full reference loading, typography commands or numerical style targets. Those would complicate the portable workflow and can misclassify harmless technical language.

## work-humanizer

Commit: `0a9065791d021f3dda695f3887cb2ae4c0eacbcf`.

Inspected the [skill](https://github.com/phuryn/work-humanizer/blob/0a9065791d021f3dda695f3887cb2ae4c0eacbcf/skills/work-humanizer/SKILL.md), [local checker](https://github.com/phuryn/work-humanizer/blob/0a9065791d021f3dda695f3887cb2ae4c0eacbcf/skills/work-humanizer/check.py), its unit tests and [evidence account](https://github.com/phuryn/work-humanizer/blob/0a9065791d021f3dda695f3887cb2ae4c0eacbcf/evidence/README.md).

Useful: preserve claim strength, commitments, actors and conditions; use the writer's own notes; distinguish readability from meaning preservation. Its published evidence includes model judges, fictional test inputs and hand-checked findings. Those are upstream results, not proof of Humanize's performance.

Application to Humanize: fact-and-certainty ledger, notes-led voice, targeted evidence gathering and optional pattern review. Extended the final check to cover negation, exceptions, deadlines and their triggers. Examples contrast acceptable edits with ownership and certainty drift. Prefer targeted cleanup over mandatory fresh recomposition or a fixed rhythm quota. A good existing draft often needs fewer edits.

## longtail

Commit: `52165e73c909ad6ee06a5cfb7a698770b7194e05`.

Inspected the [skill](https://github.com/milesoncken/longtail/blob/52165e73c909ad6ee06a5cfb7a698770b7194e05/skills/longtail/SKILL.md), `shape.py`, `stylo.py` and [evaluation limitations](https://github.com/milesoncken/longtail/blob/52165e73c909ad6ee06a5cfb7a698770b7194e05/skills/longtail/references/science.md).

Useful: structure matters alongside vocabulary; a universal humanizing template becomes repetitive; user samples should guide voice. Its own evaluation describes a small business-blog test set, genre false positives, unsupported claims and detection by a careful model reader even when other detector results improve. The cited paper and its statistical claims were not independently audited here.

Application to Humanize: inspect argument flow and endings, preserve audience and useful structure, and avoid substitute habits after removing dashes. Did not adopt randomized shape cards, authorship inference from a cold-read score, mandatory subagents or detector-targeted rewrite loops. The cold read now permits zero findings and stops after useful corrections rather than requiring three supposedly machine-written passages.

## enHumanizer_Bot

Commit: `9a20789be2fe48293014486a1c7949ffef3563f1`.

Inspected the README and implementation paths in [advanced_humanizer.py](https://github.com/Ramtin-Karbaschi/enHumanizer_Bot/blob/9a20789be2fe48293014486a1c7949ffef3563f1/advanced_humanizer.py), [human_rewriter.py](https://github.com/Ramtin-Karbaschi/enHumanizer_Bot/blob/9a20789be2fe48293014486a1c7949ffef3563f1/human_rewriter.py), [ai_bypasser.py](https://github.com/Ramtin-Karbaschi/enHumanizer_Bot/blob/9a20789be2fe48293014486a1c7949ffef3563f1/ai_bypasser.py), plus bot and Gemini prompt integration.

Useful: recognize document type before choosing register and preserve headings, lists and quotations. These concepts fit Humanize's genre-specific guidance.

Excluded: random filler and perspective changes, automatic synonym substitutions, invisible characters and homoglyphs. Cleanup code includes blanket transformations such as changing "it is" to "its" and "years and years" to "decades", which can corrupt grammar or facts. `is_ai_text()` in `ai_bypasser.py` returns a constant `0.5`; the optimization loop is not empirical detector validation. Its README's indistinguishability promise is not substantiated by that function. Humanize rejects disguise tricks while preserving legitimate multilingual characters and joiners.

## pystylometry

Commit: `ce3c62b5df25489f813333efda8643382e2f0f7d`.

Inspected its README, [dependency configuration](https://github.com/craigtrim/pystylometry/blob/ce3c62b5df25489f813333efda8643382e2f0f7d/pyproject.toml), [sentence statistics](https://github.com/craigtrim/pystylometry/blob/ce3c62b5df25489f813333efda8643382e2f0f7d/pystylometry/syntactic/sentence_stats.py), their tests and [type-token ratios](https://github.com/craigtrim/pystylometry/blob/ce3c62b5df25489f813333efda8643382e2f0f7d/pystylometry/lexical/ttr.py).

Useful: distinguish descriptive measurements from conclusions. Sentence statistics report distributions; standardized TTR requires sufficient text and comparable chunk lengths. Its TTR implementation uses a 2,000-word minimum for standardized calculation. That is an implementation constraint, not a universal minimum for stylistic analysis.

Application to Humanize: explicit cautions about text length, genre, language and interpretation. No dependency was added and lexical diversity is not described as an AI probability. Sentence statistics require an optional spaCy model. A short proposal offers little evidence for a stable style profile; a full analytical stack is unnecessary for the current workflow.

## Verification boundaries

[Behavioral evaluation cases](../evals/editorial-cases.md) cover the consequential decisions targeted by these changes. They require reading actual outputs for meaning; checking for words in the skill would not establish compliance. Package validation checks syntax and links only. No detector score, blind comparison or measured writing-quality improvement is claimed for Humanize by this report.
