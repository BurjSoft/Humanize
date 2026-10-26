# Humanize

A standalone, instruction-only skill and plugin for proposals, resumes, cover letters, screening answers and general prose. It edits for a natural personal voice while preserving facts and avoiding invented experience.

Everything needed for the writing workflow is included in this repository. It needs no Hunt checkout, candidate profile, API key, server, external CLI or AI-detection service. An agent host reads and applies the instructions; this repository is not an executable rewriting program.

## Package layout

```text
humanize/
  plugin.json                     Portable Agent Plugins 1.0 manifest
  .codex-plugin/plugin.json       Codex compatibility manifest
  .claude-plugin/plugin.json      Claude Code manifest
  .claude-plugin/marketplace.json Claude Code marketplace
  skills/humanize/SKILL.md         Shared writing instructions
  AGENTS.md                       Optional mandatory-use rule
  LICENSE
```

## Install from GitHub

Replace `OWNER/REPO` with the actual GitHub owner and repository name after publishing. The repository can have any name; the plugin and marketplace names remain `humanize`.

### Claude Code

```text
/plugin marketplace add OWNER/REPO
/plugin install humanize@humanize
```

Alternatively, copy the complete `skills/humanize` directory to your host's personal skills directory (for Claude Code, `~/.claude/skills/humanize`).

### Codex and other skill-capable agents

Install the repository using your host's supported plugin installation flow, or copy the complete `skills/humanize` directory into its configured skills directory. Keep `SKILL.md` inside the `humanize` directory. The personal skills directory depends on the host and its configuration; no absolute machine path is required by this package.

The root `plugin.json` is the portable manifest. The hidden `.codex-plugin` and `.claude-plugin` directories are compatibility metadata; include them when uploading or cloning this repository. Host support and installation commands vary, so check your host's documentation.

### Make it mandatory

After installing the skill, merge the rule from [AGENTS.md](AGENTS.md) into your project's `AGENTS.md` (or `CLAUDE.md` for Claude Code). Preserve existing project instructions. The rule resolves the installed skill rather than assuming this repository is inside the project.

For use directly from a clone, an agent can read the bundled [skill](skills/humanize/SKILL.md) without installing a plugin.

## Use

Ask "humanize this" or "make this more natural", then supply the text. In Claude Code, the installed skill can also be invoked as `/humanize`.

Supply relevant verified facts with your request when needed. The skill does not include personal candidate data and must not invent missing facts. Existing project qualification rules still control eligibility, scoring and application decisions.

## What it does not do

It runs no AI detector and produces no score. Detector results are advisory; never trade accuracy for a score or promise undetectability.

## Credits

Inspired by the editorial approaches of [blader/humanizer](https://github.com/blader/humanizer) and [Aboudjem/humanizer-skill](https://github.com/Aboudjem/humanizer-skill). This is an original instruction workflow, not a copy or executable port of either project. Those repositories are references, not runtime dependencies.

Released under the [MIT License](LICENSE).
