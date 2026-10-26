# Tell lists

Supporting lists for the scan and the mechanical sweep in `SKILL.md`. A single hit is weak evidence; several in one passage are the tell. Leave a word alone inside a quotation, a product or technology name, or a passage that discusses the word itself. Keep a word when it is the precise technical term.

## Stock AI vocabulary
delve, bolster, illuminate, elucidate, underscore, underpin, tapestry, synergy, beacon, interplay, intricate, intricacies, myriad, plethora, multifaceted, holistic, pivotal, realm, landscape (figurative), testament, meticulous, vibrant, cutting-edge, game-changing, unparalleled, unwavering, ever-evolving, commendable

Phrases: shed light on, grapple with, navigate the complexities, stands as a testament, rich tapestry, paving the way, a key takeaway, look no further, that being said, in the realm of

## Marketing register (fine in an ad, a tell elsewhere)
empower, unlock, elevate, seamless, seamlessly, streamline, revolutionize, supercharge, harness the power of, next-level, best-in-class, world-class, robust (figurative), transformative, game-changer, take it to the next level, we're thrilled / excited to announce, in today's fast-paced world, in an ever-changing landscape

## Career-writing clichés
passionate about, I am the perfect fit, perfect candidate, results-driven, detail-oriented (unsupported), team player, hit the ground running, go above and beyond, wear many hats, proven track record (without the record), I'm excited to apply, I came across your job post, I have carefully read your requirements, I am confident that I can, dear hiring manager (on Upwork)

## Filler transitions (sentence start)
Additionally, Furthermore, Moreover, Importantly, Notably, Ultimately, In conclusion, Lastly, That said, Needless to say, In other words, At the end of the day, As we can see. Plain "But", "So" and "And" are fine when they do work.

## Pause-and-point and staged candor
Here's the thing / Here's what matters / Here's why this matters / Let me be clear / Let's break it down / Let's dive in / The truth is / What nobody tells you / The best part: ... / The secret: ... / In the interest of full disclosure / To be fair / One honest caveat

## Contrast and staging formulas
It's not X, it's Y / not just X but Y / This isn't about X. It's about Y. / less about X, more about Y / No X. No Y. Just Z. / X? Y. (rhetorical question answered at once) / a count announced before a list ("Three things changed:")

## Restating and engagement closers
The bottom line / Key takeaway / That's the real win / And that's why X is the future / The future looks bright / What do you think? / Thoughts? / Let that sink in / Looking forward to hearing from you / Feel free to reach out

## Doing the reader's work
This means that / In other words / What this shows is / Notice how / As you can see / This is exciting / trailing riders: ", highlighting ...", ", underscoring ...", ", reflecting ...", ", ensuring ..."

## Possible filler hedges (preserve meaningful uncertainty)
arguably, it's worth noting, it's important to note, it could potentially, may eventually, to some extent, in many ways

## Constructions nobody says out loud
serves as (use "is"), boasts / features (use "has"), the recommended approach is X (use "do X"), perform an evaluation of (use "evaluate"), posits / contends / asserts (use "says")

Inflated verbs: utilize (use), facilitate (help), commence (start), endeavor (try), ascertain (find out). On resumes, "spearheaded", "orchestrated" and "led" require verified leadership. Otherwise choose a verb matching the documented contribution, such as "helped implement" or "built".

Filler phrases: in order to (to), due to the fact that (because), has the ability to (can), at this point in time (now), it goes without saying (delete).

## Chat residue
Great question, Certainly!, Absolutely!, I hope this helps, I hope this email finds you well, Let me know if you'd like, Here's a revised version, As an AI, As of my last update, Happy to help

Acknowledgment loops: restating the question or the job post before answering ("You're looking for a developer who can build a RAG assistant..."). Cut the restatement and answer. A short pointer to which question is being answered is fine.

## Tool residue
These can indicate pasted chat output. Check context before editing: templates and documentation may contain them intentionally. Remove clear residue only from editable prose. Flag missing content or sourcing; never invent it. Protected regions retain their exact content unless their cleanup is explicitly requested.
- Unfilled placeholders: `[Your Name]`, `[Client Name]`, `[Insert link]`, `[Company]`, `2025-XX-XX`. Keep them in a template the user is deliberately building.
- Citation markup leaks: `citeturn0search0`, `contentReference[oaicite:0]`, `oai_citation`, `[attached_file:1]`.
- AI referrer parameters on URLs: `utm_source=chatgpt.com`, `utm_source=openai`, `utm_source=claude.ai`, `utm_source=perplexity.ai`, `utm_source=copilot.com`. Flag by default. When URL cleanup is explicitly requested, remove only that parameter and preserve all other query fields and fragments.

## Em dash substitutes
| Context | Substitute | Example |
|---|---|---|
| Label then description | Colon | "Exports: CSV and PDF" |
| Two complete thoughts | Period | "We cut the query time. Checkout stopped timing out." |
| A real aside | Parentheses | "the API (Node.js on AWS Lambda) handled it" |
| A light pause inside one thought | Comma | "The fix, shipped Tuesday, cut errors by half." |
| Avoid | Semicolon, or a colon that sets up a reveal | |

## Invisible or look-alike characters
Zero-width spaces and joiners (U+200B to U+200D, U+2060, U+FEFF), scattered non-breaking spaces or other Unicode spaces (U+2000 to U+200A, U+202F, U+205F, U+3000) in place of normal ones, and Cyrillic or Greek letters standing in for Latin ones can result from detector-bypass tools. Do not insert them for disguise. Do not remove them blindly: joiners can be required in scripts and emoji, Greek letters can name variables, and Cyrillic can be ordinary language. Preserve valid content; correct confirmed accidental or deceptive substitutions only within the requested scope.
