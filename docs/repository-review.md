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

## GPTZero public material, 2026-10-26

Read the [home page](https://gptzero.me/), [How it Works](https://gptzero.me/how-it-works), [How AI detectors work](https://gptzero.me/news/how-ai-detectors-work), [Introducing GPTZero 4o](https://gptzero.me/news/introducing-gptzero-4o), [10 AI Patterns](https://gptzero.me/news/ai-patterns), the UN General Assembly analysis and the cover-letter guide. No text was submitted to GPTZero; all accuracy figures below are the vendor's own or vendor-selected benchmarks.

- **AI Patterns.** GPTZero lists ten patterns it finds disproportionately in AI text: Overblown Importance, Name Dropping, Empty Commentary, Sales-pitch Tone, Phantom Experts, Dressed-up Verbs, Not just X but Y, Everything in Threes, Unnecessary Caveats and Chatbot Language. It states that none is exclusive to AI and that a pattern is not proof of authorship. Eight were already covered. Added Name Dropping and Unnecessary Caveats to the skill and tell list, and checker flags for dressed-up verbs, vague authority, name dropping and caveats.
- **Punctuation.** The 4o post says adding or removing a semicolon or em dash does not determine classification. The skill now treats dash removal as a style choice, not a detection fix.
- **Classes and editing.** GPTZero reports AI, human and mixed results and evaluates AI-polished human text. Heavy AI editing of a person's own draft can still be classified as AI-assisted, which supports targeted edits and the writer's own material over full recomposition.
- **Reliability limits.** GPTZero says results are probabilistic, weaker on short and non-English text, and should not be a final verdict; it recommends writing-process evidence (Writing Replay, writing reports). Most proposals and screening answers are short, so a score on them is weak evidence. Added to the skill's limitations.
- **Not adopted.** The perplexity and burstiness framing is presented by GPTZero as superseded by a trained deep-learning classifier, so no perplexity heuristic was added. The cover-letter guide's generic structure (thank the reader, express enthusiasm) conflicts with the skill's no-stock-closer rule for Upwork and was not imported.

## Commercial detectors and humanizers, 2026-10-26

Reviewed NoteGPT, Grammarly, HumanizeAI.pro, Okara and ZeroGPT product pages, Grammarly's AI Detector and Authorship docs, and the privacy policies of all except HumanizeAI.pro (blocked; no policy found). Findings and links are in [detector review guidance](../skills/humanize/references/detector-review.md#other-detectors-and-humanizer-services). Adopted: a disclosure rule in the skill (humanizing does not change authorship, and the skill does not hide required AI disclosure), skepticism toward vendor bypass figures and detector-plus-humanizer bundles, per-provider score definitions (GPTZero's confidence is not Grammarly's share estimate), and reading the privacy policy rather than the landing page before any authorized upload. Okara's "never stored" page claim conflicts with its policy; Grammarly trains on user content by default with an opt-out. No technique was imported; their listed AI hallmarks were already covered.

## Five public platforms, 2026-10-26

Reviewed public product pages and available official guidance. No accounts were created, drafts uploaded, rewriting tools run or detector claims independently tested. No service dependency was added. Public descriptions are insufficient to reproduce proprietary models.

| Platform and available documentation | Useful finding and decision |
| --- | --- |
| [NoteGPT detector](https://notegpt.io/ai-detector), [comparison blog](https://notegpt.io/blog/are-ai-detectors-accurate-top-10-comparison), [privacy policy](https://notegpt.io/privacy) | The product advertises near-perfect accuracy, while its blog discusses errors and disagreement. These claims do not supply independent validation for our use case. The policy describes content collection, possible processing providers and retention. Added provider-specific score interpretation and rejected the inference that no login means no storage. No public detector API specification was established in this review. |
| [Grammarly humanizer](https://www.grammarly.com/ai-humanizer), [Humanizer guide](https://support.grammarly.com/hc/en-us/articles/38552339652109-Humanizer-user-guide), [voice profile guide](https://support.grammarly.com/hc/en-us/articles/23153676821773-View-and-customize-your-voice-profile) | Useful: a supplied sample guides voice and individual suggestions remain reviewable. The Humanizer guide requests 200+ words for its custom voice feature; this is its product requirement, not a universal threshold. Added genre-aware sample use without a fixed minimum. The product explicitly distinguishes readability improvement from bypassing detectors. Existing audit mode already supports reviewing individual edits. |
| [HumanizeAI.pro](https://www.humanizeai.pro/), [about](https://www.humanizeai.pro/about), [ethics](https://www.humanizeai.pro/ethics), [privacy](https://www.humanizeai.pro/privacy) | Tone and rewrite-level controls are distinct useful concepts. Added that distinction without importing preset names or mandatory controls. The homepage promises detector bypass and plagiarism-free output, whereas the ethics page discourages bypass use. Neither establishes originality or accuracy. Added an originality-versus-detection case. The site's API link led to an account page; no public API contract was verified. |
| [Okara tool](https://okara.ai/tools/ai-humanizer), [skill overview](https://okara.ai/skills/humanize-ai-text), [general docs](https://okara.ai/docs/introduction), [privacy policy](https://okara.ai/privacy) | Useful: diagnose specific problems and calibrate tone. Its public skill description encourages hedge removal; our adaptation explicitly retains meaningful uncertainty. The full skill requires login and was not read or copied. General docs cover its marketing agents, not a reproducible humanizer algorithm. The tool claims no storage, while the broader policy describes provider processing and retention; feature-specific scope remains unresolved. No blanket privacy promise adopted. |
| [ZeroGPT humanizer](https://www.zerogpt.com/ai-humanizer), [FAQ](https://www.zerogpt.com/faq) | The humanizer distinguishes a Basic model and an advanced offering from Undetectable.ai. Record website and disclosed processing provider separately; do not assume which backend handled a particular scan. The FAQ distinguishes source matching from origin detection and recommends longer text. Added that distinction without padding short proposals. Bypass and human-score marketing was not adopted. The public API route was inaccessible during this review; no endpoint or schema was verified. |

These additions extend the existing skill and detector reference. Four manual cases cover tone versus certainty, cross-genre samples, incompatible score scales and originality claims. They are criteria, not an executed writing-quality benchmark. The existing automated suite validates scripts and packaging, not these semantic decisions.

## Verification boundaries

[Behavioral evaluation cases](../evals/editorial-cases.md) cover the consequential decisions targeted by these changes. They require reading actual outputs for meaning; checking for words in the skill would not establish compliance. Package validation checks syntax and links only. No detector score, blind comparison or measured writing-quality improvement is claimed for Humanize by this report.
