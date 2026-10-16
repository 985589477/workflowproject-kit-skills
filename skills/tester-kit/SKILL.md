---
name: tester-kit
description: Use for testing work such as acceptance criteria review, test strategy, test plans, test data/environment prep, test cases, API/integration tests, compatibility tests, non-functional risk tests, regression scope, exploratory testing, automation planning, defect reproduction, execution reports, release acceptance, and QA review. Do not use for product strategy or code implementation unless the user asks for testing-facing deliverables.
---

# tester-kit

## Entry Gate (do not skip)

Loading this kit on its own does **not** exempt the task from the entry gate. Before touching any
code, load the `workflowproject-kit` skill and execute its §1「开跑门禁」: output the status block it
defines and write it into the project `AGENTS.md`. Runnable gate check:
`workflowproject-kit/scripts/check_gates.py`.

Use this skill when the user asks for testing deliverables.

Start by reading:

```text
START-HERE.md
README.md
usage-guide.md
workflows/tester/tester-workflow.md
```
