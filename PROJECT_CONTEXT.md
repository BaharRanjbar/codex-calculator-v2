# Project Overview

This project was created to learn Python and OpenAI Codex, as documented in the root AGENTS.md.

# Context Verification

Verification date: 2026-10-20.

Phase 4 verification included reading AGENTS.md, calculator.py, test_calculator.py, README.md, and this document; running the full unittest suite; and running one end-to-end calculator subprocess with simulated standard input. No Git commands were run. Only README.md and PROJECT_CONTEXT.md were modified in this phase.

This document must be revalidated after relevant project changes.

# Current Status

Calculator V2 is implemented in calculator.py with addition, subtraction, multiplication, and division using float values. The menu provides `1. Calculate`, `2. Show history`, and `3. Exit`. Multiple calculations can run in one session; successful calculations and handled errors return to the menu. Option 3 prints `Goodbye!` and exits.

perform_calculation() prints the existing result or error and returns a formatted record on success or None on failure. main() stores each successful record once in a local session list. show_history(history) displays numbered records in insertion order without modifying them, or `No calculations yet.` for an empty list. A new session starts with an empty history; nothing is saved to disk. Importing the module does not start interaction.

# Key Decisions

- The former single-calculation flow has been replaced by a session menu. Explicit exit is available from the menu only.
- Invalid numeric input, invalid operators, and division by zero are handled in calculator.py.
- Code should remain simple, readable, and suitable for learning, as required by AGENTS.md.

# Resolved Issue

The previously documented division-by-zero mismatch is resolved. calculator.py and README.md both use `Error: Cannot divide by zero.`; the automated tests and Phase 4 end-to-end run confirmed that message.

# Remaining Limitations

- float arithmetic can introduce decimal rounding artifacts and is not intended for exact financial calculations.
- There is no special validation for nan, inf, or overflow.
- History is non-persistent and has no record limit; long sessions can consume additional memory.
- EOF and Ctrl+C have no custom handling. No graphical interface or persistent storage is implemented.

# Tests Executed During Phase 4

Interpreter: Python 3.12.14 at `C:\Users\user\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`.

Exact PowerShell commands for version and unit verification:

```powershell
& 'C:\Users\user\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' --version
& 'C:\Users\user\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B -m unittest -v test_calculator
```

Observed unittest result: `Ran 21 tests in 0.006s`, `OK`. Tests cover arithmetic, negative/decimal values, invalid inputs and operators, division by zero, menu behavior, repeated calculations, history ordering and numbering, repeated display, exclusion of failed calculations, independent sessions, and import without interaction. Unit-test input/output is simulated.

One real calculator subprocess was also executed with this in-memory verification command (no script file was created):

```powershell
@'
import subprocess
import sys

inputs = "1\n2\n+\n3\n1\n5\n/\n0\n2\n3\n"
run = subprocess.run(
    [sys.executable, "-B", "calculator.py"],
    input=inputs, text=True, capture_output=True, timeout=10,
)
menu = "1. Calculate\n2. Show history\n3. Exit\nChoose an option: "
prompts = "Enter the first number: Enter an operator (+, -, *, /): Enter the second number: "
expected = (
    menu + prompts + "Result: 5.0\n"
    + menu + prompts + "Error: Cannot divide by zero.\n"
    + menu + "1. 2.0 + 3.0 = 5.0\n"
    + menu + "Goodbye!\n"
)
print(run.stdout, end="")
assert run.returncode == 0, (run.returncode, run.stderr)
assert run.stderr == "", run.stderr
assert run.stdout == expected, repr(run.stdout)
print("E2E verified: exact output; only the successful calculation appears in history.")
'@ | & 'C:\Users\user\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B -
```

Observed result: exit code 0, empty stderr, and exact expected output. The session calculated 2 + 3 successfully, rejected 5 / 0, displayed only `1. 2.0 + 3.0 = 5.0` in history, and exited with `Goodbye!`. README examples and messages were compared with source, unittest expectations/results, and this actual output. Piped input is not echoed, so prompts appear adjacent in captured output; README's interactive example includes typed input for readability. No keyboard-driven manual session was performed. These results do not establish correctness for all possible inputs.

# Development History

Verified from the current files:

- calculator.py contains the calculator implementation and input validation.
- test_calculator.py contains the automated unittest suite.
- README.md documents usage and manual test scenarios with expected outputs.
- AGENTS.md records project goals and working guidelines.
- Documented test scenarios do not establish that those tests were executed.

User-provided history, not independently verified from the current files:

- The project was developed with help from Codex using Plan Mode, implementation, Diff review, and testing of various scenarios.
- The user reports Phases 1, 2, and 3 completed and reviewed. Earlier conversation reports described successful test runs; those reports are historical and are distinct from the fresh Phase 4 results above.
- The current files alone do not establish the sequence of past development steps, the reasoning behind earlier decisions, or actual previous test results.

Historical context: the earlier version performed one calculation per run, and the previous context document recorded a division-by-zero message mismatch. Those statements describe the earlier state, not current behavior. Phase 4 updated documentation and performed the verification recorded above without changing calculator.py or test_calculator.py.

# Future Goals

The following goals were provided by the user and are not recorded here as completed work:

- Prepare the project for publication on GitHub.
- Document the AI-assisted development process for a resume.

# How to Continue

In each new conversation, the agent should read this file and the relevant AGENTS.md instructions, including the root AGENTS.md and Practice/AGENTS.md when working inside Practice.

Independently inspect the actual project files to confirm the current state before making changes. Treat this document as context that may become outdated. Keep verified file evidence separate from user-provided history, and do not infer previous decisions or successful test runs without supporting records.

# Context Maintenance Rules

- Recheck relevant project files before relying on recorded status.
- Update current status, known issues, and future goals after related changes.
- Preserve historical decisions separately from current implementation facts.
- Record actual test results only when tests have been executed.
- Do not mark a goal completed without supporting evidence.
