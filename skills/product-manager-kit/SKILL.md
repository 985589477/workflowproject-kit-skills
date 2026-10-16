---
name: product-manager-kit
description: Use for product manager work such as product ideas, requirement analysis, PRDs, user stories, acceptance criteria, prioritization, version planning, roadmaps, competitor analysis, feedback synthesis, change evaluation, and retrospectives. Do not use for code implementation, UI visual design, or project management unless the user asks for product-facing deliverables.
---

# product-manager-kit

Use this skill when the user asks for product manager work or product-facing deliverables.

## Required Reading

Before acting, read the local kit files in this order:

```text
START-HERE.md
README.md
usage-guide.md
workflows/product-manager/product-manager-workflow.md
```

If the task needs broader product capability context, also read:

```text
knowledge/product-manager-capability-system.md
```

## Execution Rules

- First classify the product stage and task type.
- Select the matching workflow, template, and scorecard.
- State the selected workflow before executing.
- Before each phase, report current stage, task classification, selected workflow, whether user confirmation is required, and next step.
- Do not stop just because one document was produced; determine the next product lifecycle stage.
- Do not generate PRD before requirement analysis is clear enough.
- Preserve facts, AI inferences, assumptions, and open questions separately.
- Ask the user when target users, scenarios, scope, priority, acceptance criteria, constraints, or decision owner are unclear.
- For long-running product work, maintain or update a project memory summary when key conclusions, decisions, scope changes, risks, roadmap changes, or next actions change.
- Prefer existing project memory or rule files such as `AGENTS.md`, `AI-WORKFLOW-RULES.md`, `docs/project-memory.md`, or `docs/ai-context.md`; otherwise use `docs/ai-memory-summary.md` when the user wants persistent context.
- After output, report saved location, scorecard result, open questions, and recommended next step.

## Output Location Rules

When saving documents in an external project:

1. Use the user-specified output directory if provided.
2. Otherwise use an existing documentation directory such as `docs/`, `documents/`, `docs/product/`, or `docs/prd/`.
3. If no suitable directory exists, create `docs/`.

Do not default to WorkflowProject internal directories such as `04-outputs/` or `12-projects/` in external projects.

## First-Time Setup

When this kit is copied into a new project, read:

```text
INSTALL.md
examples/quick-start-example.md
```

For tool-specific usage, read:

```text
integrations/codex-usage.md
integrations/cursor-usage.md
```
