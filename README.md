# Humanize

A standalone, instruction-only skill and plugin for proposals, resumes, cover letters, screening answers and general prose. It edits for a natural personal voice while preserving facts and avoiding invented experience.

Everything needed for the writing workflow is included in this repository. It needs no Hunt checkout, candidate profile, API key, server, external CLI or AI-detection service. An agent host reads and applies the instructions; this repository is not an executable rewriting program.

## Package layout

```text
Humanize/
  plugin.json                     Portable Agent Plugins 1.0 manifest
  .codex-plugin/plugin.json       Codex compatibility manifest
  .claude-plugin/plugin.json      Claude Code manifest
  .claude-plugin/marketplace.json Claude Code marketplace
  skills/humanize/SKILL.md         Shared writing instructions
  skills/humanize/references/      Tell lists used by the scan and sweep
  skills/humanize/scripts/check.py Optional stdlib-only pattern sweep
  AGENTS.md                       Optional mandatory-use rule
  LICENSE
```

## Install from GitHub

The plugin and marketplace names are both `humanize`.

### Claude Code

```text
/plugin marketplace add BurjSoft/Humanize
/plugin install humanize@humanize
```

Alternatively, copy the complete `skills/humanize` directory to your host's personal skills directory (for Claude Code, `~/.claude/skills/humanize`).

### Codex and other skill-capable agents

Install the repository using your host's supported plugin installation flow, or copy the complete `skills/humanize` directory into its configured skills directory. Keep `SKILL.md` inside the `humanize` directory. The personal skills directory depends on the host and its configuration; no absolute machine path is required by this package.

The root `plugin.json` is the portable manifest. The hidden `.codex-plugin` and `.claude-plugin` directories are compatibility metadata; include them when uploading or cloning this repository. Host support and installation commands vary, so check your host's documentation.

When changing the version or description, update all four manifests together: `plugin.json`, `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json` and the plugin entry in `.claude-plugin/marketplace.json`.

### Make it mandatory

After installing the skill, merge the rule from [AGENTS.md](AGENTS.md) into your project's `AGENTS.md` (or `CLAUDE.md` for Claude Code). Preserve existing project instructions. The rule resolves the installed skill rather than assuming this repository is inside the project.

For use directly from a clone, an agent can read the bundled [skill](skills/humanize/SKILL.md) without installing a plugin.

## Use

Ask "humanize this" or "make this more natural", then supply the text. In Claude Code, the installed skill can also be invoked as `/humanize`.

Supply relevant verified facts with your request when needed. The skill does not include personal candidate data and must not invent missing facts. Existing project qualification rules still control eligibility, scoring and application decisions.

Ordinary cleanup preserves clear passages, useful structure and exact quotations or technical content, including source URLs. It checks conditions, uncertainty, attribution and commitments alongside names and numbers. See the [meaning-preservation examples](skills/humanize/references/editing-examples.md), [repository comparisons](docs/repository-review.md) and [manual evaluation cases](evals/editorial-cases.md) for the rationale and verification limits.

## What it does not do

It runs no AI detector and produces no score. Detector results are advisory; never trade accuracy for a score or promise undetectability. It refuses detector-evasion tricks such as homoglyphs, zero-width characters and planted typos.

The optional sweep counts dashes, semicolons, stock vocabulary, career clichés, staging phrases, sentence-length uniformity and invisible characters. Unicode warnings include character names and code points for review; legitimate language, typography and emoji must be preserved. It flags, never rewrites, and needs only Python 3.8+:

```text
python skills/humanize/scripts/check.py draft.md
```

## How it works

Pick a mode by asking: rewrite (default), gather (the skill asks up to five short questions when a draft lacks what only you know), from notes (your own notes or transcript become the skeleton), or detect (flag only, no rewrite). Every rewrite builds a ledger of facts and their qualifiers first, then audits the result so "helped build" never becomes "built".

## Credits

Inspired by the editorial approaches of [blader/humanizer](https://github.com/blader/humanizer), [Aboudjem/humanizer-skill](https://github.com/Aboudjem/humanizer-skill), [phuryn/work-humanizer](https://github.com/phuryn/work-humanizer) (fact-and-certainty ledger, interview mode, mechanical sweep), [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) (editing scope, never-inject rules, source-as-data) and [milesoncken/longtail](https://github.com/milesoncken/longtail) (polish tells, cold read) and [lynote-ai/humanize-text-skill](https://github.com/lynote-ai/humanize-text-skill) (false-positive boundaries, "clean but flat" guidance, voice-sample limits). [craigtrim/pystylometry](https://github.com/craigtrim/pystylometry) informed the voice-sample guidance. This is an original workflow, not a copy or port of any of them; they are references, not runtime dependencies.

Released under the [MIT License](LICENSE).
