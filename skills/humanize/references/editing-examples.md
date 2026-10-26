# Meaning checks for difficult edits

These are fictional editorial cases, not facts about any candidate. Read the relevant case when a rewrite risks changing meaning. Equivalent wording is welcome.

| Source | Acceptable revision | Change to reject |
| --- | --- | --- |
| "I helped implement the Node.js queue; another engineer designed it." | "I helped build the Node.js queue, which another engineer designed." | "I designed and built the Node.js queue." This upgrades ownership. |
| "The cache could reduce latency for repeat requests after warm-up." | "After warm-up, the cache could make repeat requests faster." | "The cache reduces latency." This loses uncertainty, scope and timing. |
| "We'll send an estimate within two business days after we receive the logs." | "Once we receive the logs, we'll send an estimate within two business days." | "We'll fix it in two days." This changes the deliverable and deadline. |
| "It is not available in the EU, except for existing accounts." | Leave unchanged. | "It is available in the EU." Negation and exceptions matter. |
| "I live in Pakistan, can work remotely as a contractor and do not hold US work authorization." | Preserve these facts when answering eligibility questions. | "I'm authorized to work remotely in the US." Contractor availability does not establish legal authorization. |
| "We use AWS Lambda and AWS SQS to process queued jobs." | Leave unchanged. | Replacing AWS service names solely to avoid repetition. Technical names carry meaning. |
| "We're sorry the export failed. We'll email you when it's ready." | "Sorry the export failed. We'll email you when it's ready." | "Your export will be ready today." This invents a deadline. |

In documentation, edit nearby prose while preserving exact regions:

Source:

```markdown
To seamlessly get started, run `npm run build -- --mode production`.
See [build notes](https://example.com/build?mode=production#flags).
> The client said: "Keep robust in the product name."
```

Possible revision:

```markdown
Run `npm run build -- --mode production` to get started.
See [build notes](https://example.com/build?mode=production#flags).
> The client said: "Keep robust in the product name."
```

The command, URL and quotation remain exact. A style-watchlist word inside a quotation is not permission to edit it.

For notes, retain reasoning: "The first import failed because the CSV dates were ambiguous, so I added explicit parsing" preserves a failure, its cause and a corrective step. Do not replace it with a broad claim about building a reliable import platform.

For an approach, preserve intent: "I'd inspect the retry logs before changing the queue" is a plan, not evidence of a completed fix.
