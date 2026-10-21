# Project Overview

This is an educational project for learning Python and OpenAI Codex.

# Current Implementation

Calculator V2 is a terminal-based calculator that supports addition, subtraction,
multiplication, and division with `float` values.

- `main()` presents a menu for calculating, viewing the session history, or
  exiting.
- `perform_calculation()` validates the two numeric inputs, performs a valid
  calculation, prints the result, and returns a formatted record. It returns
  `None` when the input is invalid so failed calculations are not stored.
- `show_history()` prints successful calculations in numbered order, or reports
  that no calculations exist yet.
- History is stored only in memory for the current session.
- Importing `calculator.py` does not start the interactive program.

## Input and interruption handling

Both numeric inputs must be finite. Malformed values and the special floating-
point values `nan`, `inf`, and `-inf` are rejected with:

```text
Error: Please enter valid numbers.
```

Invalid operators and division by zero are also reported without recording a
calculation. If input raises `EOFError` or `KeyboardInterrupt` at the main menu
or during a calculation, the session ends cleanly, prints `Goodbye!` once, and
does not display a traceback.

# Current Test Verification

The latest verified full-suite run was performed on 2026-10-21 with the
project's `unittest` suite. It reported:

```text
Ran 25 tests in 0.009s
OK
```

The portable command for running the suite is:

```powershell
python -B -m unittest -v test_calculator
```

The tests cover arithmetic operations, decimal and negative values, malformed
and non-finite numeric input, invalid operators, division by zero, menu flow,
session history, module importing, and graceful `EOFError` and
`KeyboardInterrupt` handling.

# Current Limitations

- Calculations use binary floating-point values, so results are not suitable
  for exact financial arithmetic.
- Floating-point overflow is not given a dedicated error message.
- History has no persistence and is lost when the session ends.
- The project is a terminal application and has no graphical interface.

# Historical Verification Records

The following record describes an earlier project state and is retained as
development history rather than a statement about the current suite:

- On 2026-10-20, a Phase 4 documentation review recorded a full `unittest`
  result of 21 passing tests and a successful subprocess end-to-end check.
- That record predates the finite-number and interruption-handling regression
  tests. It must not be interpreted as the current test count or current test
  result.
- The same review documented that Calculator V2 had evolved from a
  single-calculation program into a menu-based application with session
  history, and that a division-by-zero wording discrepancy had been resolved.

# Development History

The following development history was provided by the project user and is kept
separate from facts established solely by the current files:

- The project was developed with assistance from OpenAI Codex through planning,
  implementation, diff review, and testing exercises.
- Earlier Calculator V2 work was organized into separately approved phases for
  planning, implementation, review/testing, and documentation.

The current files verify the implemented calculator behavior and its tests, but
they do not by themselves prove the full sequence of earlier decisions or
executed commands.

# Future Goals

- Prepare the repository for public GitHub publication.
- Continue learning Python and OpenAI Codex through small, reviewable changes.

# Context Maintenance Rules

- Keep this document aligned with the current implementation and tests.
- Distinguish verified current facts, historical verification records, and
  user-provided development history.
- Record a test result only after that test has actually run.
- Do not add machine-specific paths, local runtime details, credentials, or
  other private environment information.
