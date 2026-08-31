# Process

## Work organization

- Tasks are defined in `backlog.md`, one at a time
- Read the acceptance criteria before starting and before closing
- Commit regularly

## Roles

- PM - grooms a task before anyone implements it, follows `_docs/team/pm.md`
- Engineer - implements one groomed task, follows `_docs/team/software-engineer.md`
- QA - checks the result against the acceptance criteria, follows `_docs/team/qa-engineer.md`

## Orchestrator

The main session is the orchestrator. It launches the PM, the engineer and
QA as subagents. It does not groom, implement or test itself.

### Lifecycle

1. Pick the next open task from the backlog
2. PM grooms it
3. Engineer implements it
4. QA verifies it
5. On FAIL, back to step 3 with the QA comment as input
6. On PASS, mark the task done in the backlog
7. Repeat until the backlog is empty

### Rules

- Do not skip step 2
- The engineer does not close the task
- QA does not fix the code, only outputs PASS or FAIL
- The orchestrator marks the task done only after QA outputs PASS
