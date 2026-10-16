---
name: project-governance-kit
description: Use before AI-driven development to inspect project rules, architecture, module boundaries, design standards, task lists, module documentation, and verification requirements. Use when starting or taking over a real code project, or when a request may change project structure. Do not force role kits when the project governance check does not require them.
---

# project-governance-kit

Use this skill as the project-level entry point before development work.

## Required behavior

1. Read the project's local rules and existing documentation first.
2. Check the technical baseline: target platform, language, framework, runtime, build, deployment, and test approach.
3. Check architecture, module boundaries, design standards, task list, module docs, tests, and project memory.
4. Separate confirmed facts, AI inferences, and questions requiring user confirmation.
5. If this is a new project, ask the user to confirm the technical baseline before scaffolding or installing dependencies.
6. If this is a new module, report the existing baseline and ask whether to reuse it; do not silently introduce a new language or framework.
7. If key governance material is missing, report the gap and collaborate with the user to fill it.
8. Before code changes, produce an overall plan and a task list appropriate to project risk.
9. Execute one task at a time and verify it before moving to the next task.
10. Sync affected architecture, module, design, test, task, and memory documents.
11. Call product, UI, developer, or tester capabilities only when their expertise is needed.

## Do not

- Do not treat this skill as a replacement for the project's actual architecture.
- Do not assume that a generic role kit is a project-specific rule.
- Do not force every task through every role.
- Do not silently invent security, permissions, data ownership, design direction, device scope, or release behavior.
- Do not claim a document or test was read or executed when it was not.

## Main workflow

```text
project rules
-> governance check
-> gap clarification
-> overall plan
-> task list
-> implementation
-> verification
-> documentation sync
```
