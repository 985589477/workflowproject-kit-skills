---
name: team-orchestration-kit
description: Use for cross-role AI team orchestration across product manager, UI designer, developer, and tester workflows. Use when a request may require multiple roles, lifecycle routing, handoff checks, mutual review, delivery acceptance, or badcase feedback. Do not use for a clearly single-role task unless the user asks for cross-role coordination.
---

# team-orchestration-kit

Use this skill when the user asks for cross-role collaboration or when a request may span product, UI design, development, and testing. This is a dispatch capability, not a requirement to create a child agent for every request.

## Required Reading

Before acting, read the local kit files in this order:

```text
START-HERE.md
README.md
usage-guide.md
workflows/mixed/team-orchestration-workflow.md
```

## Execution Rules

- First decide whether the task is cross-role or single-role.
- If this kit is present, product/UI/development/testing related tasks should route through this kit first, even when they may later become single-role tasks.
- For a simple single-role task, call the matching skill directly in the current agent. Do not create a child agent just to pass through one skill.
- For a composite task, the parent agent must create real child agents when the runtime provides subagent tools. Each child receives a bounded task brief and returns a structured result report.
- If the runtime does not provide real subagent tools, state that limitation and ask before using sequential single-agent fallback. Never describe fallback execution as child-agent collaboration.
- If it is cross-role, identify participating roles and the current owner.
- State the selected workflow, template, and scorecard before executing.
- Do not stop after one role produces output; decide whether downstream roles need to review or continue.
- Check handoff quality between roles before moving forward.
- If a downstream role cannot understand upstream output, stop and report the collaboration blockage.
- After development delivery, require product, UI, and testing acceptance when applicable.
- If communication failure repeats, recommend recording a badcase and returning it to the relevant capability-building project.
- Use existing documentation directories in external projects; do not default to WorkflowProject internal paths.

## Execution Mode Output

Every run must state one of these modes:

```text
执行模式：单 Agent + Skill
执行模式：父 Agent + 子 Agent
执行模式：单 Agent 降级模拟，不是真实子 Agent
```

The first mode is required for simple tasks. The second mode is required for composite tasks when real subagent tools are available.

## Expected Sibling Kits

Recommended sibling folders:

```text
product-manager-kit/
ui-designer-kit/
developer-kit/
tester-kit/
team-orchestration-kit/
```

If a sibling kit is missing, explain what is missing and continue with best-effort orchestration.
