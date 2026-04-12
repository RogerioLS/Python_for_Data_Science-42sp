import subprocess
import sys
from pathlib import Path


SCRIPT = Path(__file__).with_name("building.py")


def run_with_args(args):
    """Run building.py with command line args and return stdout."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip(), result.returncode


def run_with_stdin(stdin_text):
    """Run building.py with stdin input and return stdout."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=stdin_text,
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip(), result.returncode


def test_case(name, output, expected):
    """Test if output matches expected."""
    ok = output == expected
    status = "OK" if ok else "FAIL"
    print(f"[{status}] {name}")
    if not ok:
        print(f"  expected:\n{expected}\n")
        print(f"  got:\n{output}\n")
    return ok


def main():
    """Run all test cases for building.py."""
    tests_passed = 0
    tests_total = 0

    # Test 1: Long string from subject
    long_string = (
        "Python 3.0, released in 2008, was a major revision that is not "
        "completely backward compatible with earlier versions. Python 2 was "
        "discontinued with version 2.7.18 in 2020."
    )
    expected_long = (
        "The text contains 171 characters:\n"
        "2 upper letters\n"
        "121 lower letters\n"
        "7 punctuation marks\n"
        "26 spaces\n"
        "15 digits"
    )
    output, _ = run_with_args([long_string])
    if test_case("Long string argument", output, expected_long):
        tests_passed += 1
    tests_total += 1

    # Test 2: Interactive input "Hello World!"
    expected_hello = (
        "What is the text to count?\n"
        "The text contains 12 characters:\n"
        "2 upper letters\n"
        "8 lower letters\n"
        "1 punctuation marks\n"
        "1 spaces\n"
        "0 digits"
    )
    output, _ = run_with_stdin("Hello World!\n")
    if test_case("Interactive input 'Hello World!'", output, expected_hello):
        tests_passed += 1
    tests_total += 1

    # Test 3: No arguments with EOF (empty input)
    expected_empty = (
        "What is the text to count?\n"
        "The text contains 0 characters:\n"
        "0 upper letters\n"
        "0 lower letters\n"
        "0 punctuation marks\n"
        "0 spaces\n"
        "0 digits"
    )
    output, _ = run_with_stdin("")
    if test_case("No args with EOF", output, expected_empty):
        tests_passed += 1
    tests_total += 1

    # Test 4: More than one argument
    expected_error = "AssertionError: more than one argument is provided"
    output, _ = run_with_args(["arg1", "arg2"])
    if test_case("Multiple arguments error", output, expected_error):
        tests_passed += 1
    tests_total += 1

    print(f"\n{'=' * 50}")
    print(f"Resultado: {tests_passed}/{tests_total} testes passaram")
    sys.exit(0 if tests_passed == tests_total else 1)


if __name__ == "__main__":
    main()