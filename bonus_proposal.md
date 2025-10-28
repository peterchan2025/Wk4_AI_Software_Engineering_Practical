```markdown
# Bonus: AutoDocAssist — Automated Documentation Assistant

Purpose
AutoDocAssist is an AI-powered tool that automatically generates and maintains developer-facing documentation (API docs, usage examples, changelogs, and high-level design notes) by mining source code, unit tests, commit messages, and pull request discussions.

Key Capabilities
- API Extraction: Parse code (public functions, classes, endpoints) and generate API reference with parameter descriptions inferred from type hints and tests.
- Example Generation: Create runnable examples by synthesizing short scripts using patterns extracted from tests and README snippets.
- Changelog Summaries: Aggregate commit messages and PR descriptions, cluster changes by feature, and produce human-readable changelogs.
- Drift Detection: Identify when code changes make documentation stale (missing or incorrect examples) and create draft PRs to update docs.
- Integration: Hooks into CI to run doc-generation on merges; provides suggested edits as PRs for reviewer approval.

Workflow
1. Ingest code, tests, README, and PR/issue text via repo access.
2. Use language models to summarize behavior and produce Docstrings / markdown.
3. Validate examples by running them in an isolated sandbox (optional).
4. Open a draft PR with documentation changes and confidence scores.
5. Provide interactive UI for reviewers to accept/modify generated docs.

Impact
- Saves engineering time by automating repetitive doc updates.
- Improves onboarding and knowledge sharing.
- Reduces documentation debt and increases code discoverability.

Privacy & Ethics
- Respect repo license and contributor policies.
- Optional mode: only generate PR drafts without pushing changes.
```