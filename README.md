# Calculator V2

Calculator V2 is a terminal-based Python calculator created as an educational project for learning Python and OpenAI Codex. It supports repeated calculations in one session and keeps a history of successful calculations for that session.

## Features

- Addition, subtraction, multiplication, and division
- Negative and decimal number support
- A menu for calculating, viewing or clearing session history, and exiting
- Numbered history that preserves calculation order
- Validation for invalid numeric input, invalid operators, and division by zero
- Rejection of non-finite numeric values: `nan`, `inf`, and `-inf`
- Graceful exit with `Goodbye!` when input ends (`EOFError`) or is interrupted with `Ctrl+C` (`KeyboardInterrupt`)
- No external dependencies

## Requirements

- Python 3

## Installation

Clone or download this repository, then open a terminal in the project directory. No packages need to be installed.

## Usage

Run the calculator:

```sh
python calculator.py
```

The program displays this menu:

```text
1. Calculate
2. Show history
3. Exit
4. Clear history
Choose an option:
```

- Choose `1` to enter a first number, an operator, and a second number.
- Choose `2` to display successful calculations from the current session.
- Choose `3` to print `Goodbye!` and exit.
- Choose `4` to clear the current session's history immediately, without confirmation. The program prints `History cleared.` even when history is already empty, then returns to the menu.

After clearing, viewing history prints `No calculations yet.` New calculations are stored normally, with history numbering starting again at `1`.

Only successful calculations are added to history. Invalid numbers, invalid operators, division by zero, and non-finite values are rejected and are not recorded.

### Example

```text
Choose an option: 1
Enter the first number: 9
Enter an operator (+, -, *, /): /
Enter the second number: 2
Result: 4.5

Choose an option: 2
1. 9.0 / 2.0 = 4.5
```

## Input Handling

The calculator accepts finite values that Python can convert to `float`. It reports `Error: Please enter valid numbers.` for malformed numeric input and for `nan`, `inf`, and `-inf`.

It also reports clear errors for unsupported operators and division by zero. If standard input ends or the user presses `Ctrl+C` while choosing a menu option or entering a calculation, the current session ends cleanly without a traceback.

## Running Tests

Run the complete unit-test suite from the project directory:

```sh
python -B -m unittest -v test_calculator
```

The `-B` option prevents Python from writing bytecode files during the test run.

The tests cover:

- Arithmetic operations, negative values, decimal values, and surrounding whitespace
- Invalid numeric input, non-finite values, invalid operators, and division by zero
- Menu choices, repeated calculations, graceful exits, and invalid menu input
- Empty history, history ordering, successful-only history records, and independent sessions
- Clearing populated or empty history, repeated clearing, whitespace around option `4`, new calculations after clearing, and interrupted input after clearing
- `EOFError` and `KeyboardInterrupt` during menu and calculation input
- Direct script execution and importing the module without starting interaction

## Project Structure

```text
calculator.py        Application code
test_calculator.py   Unit tests
README.md            Project documentation
```

## Limitations

- Calculations use binary floating-point values, so decimal rounding artifacts can occur. The calculator is not intended for exact financial calculations.
- Floating-point overflow has no special handling.
- History exists only in memory for the current session and has no record limit.
- The project provides a terminal interface only; it has no graphical interface or persistent storage.

## License

This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for the full text.

## AI-Assisted Development

OpenAI Codex was used as an assistant during the documented development workflow, including planning, implementation iterations, diff review, and test-related work. This is an educational project, and AI assistance does not guarantee correctness; the code and tests should be reviewed independently.
