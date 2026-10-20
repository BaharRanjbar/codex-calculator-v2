import importlib.util
import io
from pathlib import Path
import runpy
import unittest
from contextlib import redirect_stdout
from unittest.mock import call, patch

import calculator


class CalculatorTests(unittest.TestCase):
    def check_calculation(self, inputs, expected_output):
        with patch("builtins.input", side_effect=inputs) as mock_input:
            with redirect_stdout(io.StringIO()) as output:
                record = calculator.perform_calculation()
        self.assertEqual(output.getvalue(), expected_output + "\n")
        if expected_output.startswith("Error:"):
            self.assertIsNone(record)
        self.assertEqual(mock_input.call_args_list, [
            call("Enter the first number: "),
            call("Enter an operator (+, -, *, /): "),
            call("Enter the second number: "),
        ])

    def test_four_operations(self):
        cases = [
            (["2", "+", "3"], "Result: 5.0"),
            (["7", "-", "10"], "Result: -3.0"),
            (["4", "*", "2"], "Result: 8.0"),
            (["9", "/", "2"], "Result: 4.5"),
        ]
        for inputs, expected in cases:
            with self.subTest(inputs=inputs):
                self.check_calculation(inputs, expected)

    def test_negative_and_decimal_numbers(self):
        self.check_calculation(["-4", "*", "2.5"], "Result: -10.0")

    def test_whitespace(self):
        self.check_calculation([" 2 ", " + ", " 3 "], "Result: 5.0")

    def test_invalid_numbers(self):
        for inputs in (["abc", "+", "2"], ["2", "+", "abc"],
                       ["", "+", "2"], ["2", "+", ""]):
            with self.subTest(inputs=inputs):
                self.check_calculation(inputs, "Error: Please enter valid numbers.")

    def test_invalid_operators(self):
        for operator in ("%", "", "exit"):
            with self.subTest(operator=operator):
                self.check_calculation(
                    ["2", operator, "3"],
                    "Error: Invalid operator. Use +, -, *, or /.",
                )

    def test_division_by_zero(self):
        for zero in ("0", "-0.0"):
            with self.subTest(zero=zero):
                self.check_calculation(
                    ["5", "/", zero], "Error: Cannot divide by zero."
                )

    def check_session(self, inputs, expected_output):
        with patch("builtins.input", side_effect=inputs) as mock_input:
            with redirect_stdout(io.StringIO()) as output:
                calculator.main()
        self.assertEqual(mock_input.call_count, len(inputs))
        self.assertEqual(output.getvalue(), expected_output)

    def test_main_reuses_calculation(self):
        with patch("calculator.perform_calculation") as calculation:
            self.check_session(
                ["1", "3"],
                "1. Calculate\n2. Show history\n3. Exit\n1. Calculate\n2. Show history\n3. Exit\nGoodbye!\n",
            )
        calculation.assert_called_once_with()

    def test_exit_immediately(self):
        with patch("calculator.perform_calculation") as calculation:
            self.check_session(["3"], "1. Calculate\n2. Show history\n3. Exit\nGoodbye!\n")
        calculation.assert_not_called()

    def test_repeated_calculations(self):
        self.check_session(
            ["1", "2", "+", "3", "1", "9", "/", "2", "3"],
            "1. Calculate\n2. Show history\n3. Exit\nResult: 5.0\n"
            "1. Calculate\n2. Show history\n3. Exit\nResult: 4.5\n"
            "1. Calculate\n2. Show history\n3. Exit\nGoodbye!\n",
        )

    def test_invalid_menu_choices(self):
        for choice in ("", " ", "4", "abc", "exit"):
            with self.subTest(choice=choice):
                self.check_session(
                    [choice, "3"],
                    "1. Calculate\n2. Show history\n3. Exit\n"
                    "Error: Invalid option. Choose 1, 2, or 3.\n"
                    "1. Calculate\n2. Show history\n3. Exit\nGoodbye!\n",
                )

    def test_menu_whitespace(self):
        self.check_session(
            [" 1 ", "2", "+", "3", " 3 "],
            "1. Calculate\n2. Show history\n3. Exit\nResult: 5.0\n"
            "1. Calculate\n2. Show history\n3. Exit\nGoodbye!\n",
        )

    def test_calculation_errors_return_to_menu(self):
        cases = [
            (["abc", "+", "2"], "Error: Please enter valid numbers."),
            (["2", "+", ""], "Error: Please enter valid numbers."),
            (["2", "%", "3"], "Error: Invalid operator. Use +, -, *, or /."),
            (["5", "/", "0"], "Error: Cannot divide by zero."),
        ]
        for inputs, error in cases:
            with self.subTest(inputs=inputs):
                self.check_session(
                    ["1"] + inputs + ["1", "2", "+", "3", "3"],
                    "1. Calculate\n2. Show history\n3. Exit\n" + error + "\n"
                    "1. Calculate\n2. Show history\n3. Exit\nResult: 5.0\n"
                    "1. Calculate\n2. Show history\n3. Exit\nGoodbye!\n",
                )

    def test_script_starts_menu_and_exits(self):
        with patch("builtins.input", side_effect=["3"]) as mock_input:
            with redirect_stdout(io.StringIO()) as output:
                runpy.run_path(calculator.__file__, run_name="__main__")
        mock_input.assert_called_once_with("Choose an option: ")
        self.assertEqual(output.getvalue(), "1. Calculate\n2. Show history\n3. Exit\nGoodbye!\n")

    def test_import_does_not_start_interaction(self):
        spec = importlib.util.spec_from_file_location(
            "calculator_import_test", Path(calculator.__file__)
        )
        module = importlib.util.module_from_spec(spec)
        with patch("builtins.input", side_effect=AssertionError("Unexpected input")):
            with redirect_stdout(io.StringIO()) as output:
                spec.loader.exec_module(module)
        self.assertEqual(output.getvalue(), "")

    def test_successful_calculation_returns_record(self):
        cases = [
            (["2", "+", "3"], "2.0 + 3.0 = 5.0"),
            (["7", "-", "10"], "7.0 - 10.0 = -3.0"),
            (["-4", " * ", "2.5"], "-4.0 * 2.5 = -10.0"),
            (["9", "/", "2"], "9.0 / 2.0 = 4.5"),
        ]
        for inputs, expected in cases:
            with self.subTest(inputs=inputs):
                with patch("builtins.input", side_effect=inputs):
                    with redirect_stdout(io.StringIO()):
                        record = calculator.perform_calculation()
                self.assertEqual(record, expected)

    def test_show_empty_history(self):
        history = []
        with redirect_stdout(io.StringIO()) as output:
            calculator.show_history(history)
        self.assertEqual(output.getvalue(), "No calculations yet.\n")
        self.assertEqual(history, [])

    def test_show_history_preserves_order_and_contents(self):
        history = ["2.0 + 3.0 = 5.0", "9.0 / 2.0 = 4.5"]
        original = history.copy()
        with redirect_stdout(io.StringIO()) as output:
            calculator.show_history(history)
            calculator.show_history(history)
        expected = "1. 2.0 + 3.0 = 5.0\n2. 9.0 / 2.0 = 4.5\n"
        self.assertEqual(output.getvalue(), expected * 2)
        self.assertEqual(history, original)

    def test_empty_history_returns_to_menu(self):
        menu = "1. Calculate\n2. Show history\n3. Exit\n"
        self.check_session(
            ["2", "3"], menu + "No calculations yet.\n" + menu + "Goodbye!\n"
        )

    def test_session_history_records_successes_once(self):
        menu = "1. Calculate\n2. Show history\n3. Exit\n"
        records = "1. 2.0 + 3.0 = 5.0\n2. 9.0 / 2.0 = 4.5\n"
        self.check_session(
            ["1", "2", "+", "3", "1", "9", "/", "2", "2", "2", "3"],
            menu + "Result: 5.0\n" + menu + "Result: 4.5\n"
            + menu + records + menu + records + menu + "Goodbye!\n",
        )

    def test_failed_calculations_are_not_in_history(self):
        menu = "1. Calculate\n2. Show history\n3. Exit\n"
        cases = [
            (["abc", "+", "2"], "Error: Please enter valid numbers."),
            (["2", "+", ""], "Error: Please enter valid numbers."),
            (["2", "%", "3"], "Error: Invalid operator. Use +, -, *, or /."),
            (["5", "/", "0"], "Error: Cannot divide by zero."),
        ]
        for inputs, error in cases:
            with self.subTest(inputs=inputs):
                self.check_session(
                    ["1"] + inputs + ["2", "1", "2", "+", "3", "2", "3"],
                    menu + error + "\n" + menu + "No calculations yet.\n"
                    + menu + "Result: 5.0\n" + menu + "1. 2.0 + 3.0 = 5.0\n"
                    + menu + "Goodbye!\n",
                )

    def test_separate_sessions_have_independent_history(self):
        menu = "1. Calculate\n2. Show history\n3. Exit\n"
        self.check_session(
            ["1", "2", "+", "3", "2", "3"],
            menu + "Result: 5.0\n" + menu + "1. 2.0 + 3.0 = 5.0\n"
            + menu + "Goodbye!\n",
        )
        self.check_session(
            ["2", "3"], menu + "No calculations yet.\n" + menu + "Goodbye!\n"
        )


if __name__ == "__main__":
    unittest.main()
