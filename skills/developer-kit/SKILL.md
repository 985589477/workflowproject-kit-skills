---
name: developer-kit
description: Use for AI-assisted software development governance: project bootstrap, project understanding, requirements-to-architecture, module boundaries, issue diagnosis, data/API/state contracts, security and permission governance, change risk, impact analysis, minimal necessary change / anti-overengineering checks, implementation, testing, documentation sync, code review, architecture decision records, dependency and tech debt governance, environment config governance, release and rollback planning, workflow orchestration, and AI collaboration retrospectives. Do not use for pure product manager deliverables, UI visual design, or unrelated writing tasks.
---

# developer-kit

Use this skill when the user asks for software development governance or AI-assisted coding collaboration.

## Required Reading

Before acting, read the local kit files in this order:

```text
START-HERE.md
README.md
usage-guide.md
workflows/developer/developer-kit-workflow.md
```

If the task needs broader governance context, also read:

```text
knowledge/developer-governance-capability-system.md
```

## Execution Rules

- First classify the task type.
- Select the matching workflow, template, and scorecard.
- State the selected workflow before executing.
- Before each phase, report current stage, task classification, risk level, selected workflow, whether user confirmation is required, and next step.
- Do not stop just because one workflow was selected; determine the next lifecycle stage.
- Before implementation, create an overall feature plan covering scope, affected modules, file/interface/data/config impact, implementation order, validation, and open questions.
- For a new project, ask and confirm the target platform, primary language, framework/version, runtime, build/deployment approach, and test approach before scaffolding or installing dependencies.
- For a new module in an existing project, report the detected technical baseline and ask whether to reuse it; do not silently introduce a new language, framework, or runtime.
- For a new component, page, or feature, confirm project ownership, module placement, project/UI standards, target platforms, adaptation scope, component states, interactions, acceptance criteria, and test scope before coding.
- If project or UI standards are missing, ask whether to reuse existing conventions, establish a minimal standard first, or produce a plan without coding.
- Before implementation, inspect and follow project standards for design, components, interaction, visual style, code style, architecture constraints, directory conventions, naming, testing, documentation, and AI collaboration rules.
- Before implementation, run minimal necessary change governance: decide whether code is actually needed, whether existing project capabilities can be reused, whether platform/standard library/framework-native capabilities are enough, whether installed dependencies are enough, what the smallest complete change is, and what is explicitly out of scope.
- Do not add new abstractions, wrappers, configuration, extension points, files, or dependencies unless they are required for the user's actual goal.
- Never use “write less code” as a reason to skip security checks, permission validation, error handling, accessibility, data-loss protection, or needed tests.
- Look for standard sources such as `AGENTS.md`, `AI-WORKFLOW-RULES.md`, `.cursor/rules/`, `CONTRIBUTING.md`, `docs/`, `docs/design-system.md`, `docs/development-standard.md`, `docs/testing.md`, `.editorconfig`, `.prettierrc`, `.eslintrc`, `biome.json`, `ruff.toml`, and `pyproject.toml`.
- If required standards are missing, state what is missing and either infer lightweight conventions from existing code for low-risk work or ask the user / propose a minimal standard for medium/high-risk work.
- For bugs, runtime errors, blank screens, failed tests, API failures, or performance regressions, run issue diagnosis before implementation.
- For API fields, data models, state ownership, caching, error handling, or frontend/backend collaboration, define a data/API/state contract before implementation.
- For login, auth, role permissions, sensitive data, secrets, uploads/downloads, payment, delete, or batch operations, run security and permission governance before implementation.
- When a task spans multiple phases, use workflow orchestration rules to decide whether to insert a workflow, roll back to an earlier phase, skip a phase with reasons, or pause for user confirmation.
- For medium/high-risk implementation, split work into an ordered task list before editing.
- Implement one task at a time, validate that task, record the result, then decide whether to proceed to the next task.
- For long-running development work, maintain or update a project memory summary when key conclusions, architecture decisions, module boundaries, risks, validation results, pending tasks, or next actions change.
- Prefer existing project memory or rule files such as `AGENTS.md`, `AI-WORKFLOW-RULES.md`, `docs/project-memory.md`, or `docs/ai-context.md`; otherwise use `docs/ai-memory-summary.md` when the user wants persistent context.
- For code changes, inspect the existing project before editing.
- Protect user changes and avoid broad unrelated refactors.
- For high-risk changes, explain risk, rollback, and confirmation points before implementation.
- Ask the user when goals, scope, acceptance criteria, technical choice, data/interface impact, or risk is unclear.
- After execution, report changed files, verification results, and residual risks.
- Before claiming completion, state whether documentation sync, code review, release/rollback planning, or retrospective is needed.

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

## Output Location Rules

When saving documents in an external project:

1. Use the user-specified output directory if provided.
2. Otherwise use an existing documentation directory such as `docs/`, `documents/`, `docs/dev/`, or `docs/engineering/`.
3. If no suitable directory exists, create `docs/`.

Do not default to WorkflowProject internal directories such as `04-outputs/` or `12-projects/` in external projects.
