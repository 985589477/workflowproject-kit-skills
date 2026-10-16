---
name: ui-designer-kit
description: Use for UI design work such as UI briefs, design system audit, page patterns, information architecture, component library planning, responsive adaptation, accessibility/usability review, component states, design handoff, and design-to-development constraints. Do not use for code implementation or product strategy unless the user asks for UI-facing deliverables.
---

# ui-designer-kit

## Entry Gate (do not skip)

Loading this kit on its own does **not** exempt the task from the entry gate. Before touching any
code, load the `workflowproject-kit` skill and execute its §1「开跑门禁」: output the status block it
defines and write it into the project `AGENTS.md`. Runnable gate check:
`workflowproject-kit/scripts/check_gates.py`.

Use this skill when the user asks for UI design deliverables.

For design specifications, first confirm the target platform, UI framework, theme or styling integration, and whether multiple platforms share one design system. Use a platform-neutral `design-tokens.json` as the source of truth, then create platform-specific mappings only after the platform is confirmed. Do not default to CSS.

Start by reading:

```text
START-HERE.md
README.md
usage-guide.md
workflows/ui-designer/ui-designer-workflow.md
```
