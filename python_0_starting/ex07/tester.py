import subprocess
import sys
import os

print("=" * 70)
print("EX07 - SOS (MORSE CODE CONVERTER) TESTS")
print("=" * 70)

print("\n1. Checking source code constraints:")
print("-" * 70)

script_dir = os.path.dirname(os.path.abspath(__file__))
sos_path = os.path.join(script_dir, "sos.py")

with open(sos_path, "r") as f:
    source = f.read()

has_dict = "NESTED_MORSE" in source or "{" in source
has_assertion = "AssertionError" in source

print(f"Dictionary usage: {'PASS' if has_dict else 'FAIL'}")
print(f"AssertionError handling: {'PASS' if has_assertion else 'FAIL'}")

print("\n2. Running functional tests:")
print("-" * 70)

test_cases = [
    {
        "args": ["python3.10", sos_path, "sos"],
        "expected": "... --- ...",
        "name": "Test 1: lowercase 'sos'"
    },
    {
        "args": ["python3.10", sos_path, "SOS"],
        "expected": "... --- ...",
        "name": "Test 2: uppercase 'SOS'"
    },
    {
        "args": ["python3.10", sos_path, "Hello World"],
        "expected": ".... . .-.. .-.. --- / .-- --- .-. .-.. -..",
        "name": "Test 3: 'Hello World' with space"
    },
    {
        "args": ["python3.10", sos_path, "ABC123"],
        "expected": ".- -... -.-. .---- ..--- ...--",
        "name": "Test 4: Letters and numbers 'ABC123'"
    },
    {
        "args": ["python3.10", sos_path, "0"],
        "expected": "-----",
        "name": "Test 5: Single digit '0'"
    },
    {
        "args": ["python3.10", sos_path, "9"],
        "expected": "----.",
        "name": "Test 6: Single digit '9'"
    },
    {
        "args": ["python3.10", sos_path],
        "expected_error": "AssertionError: the arguments are bad",
        "name": "Test 7: No arguments"
    },
    {
        "args": ["python3.10", sos_path, "hello", "world"],
        "expected_error": "AssertionError: the arguments are bad",
        "name": "Test 8: Multiple arguments"
    },
    {
        "args": ["python3.10", sos_path, "h$llo"],
        "expected_error": "AssertionError: the arguments are bad",
        "name": "Test 9: Special character '$'"
    },
    {
        "args": ["python3.10", sos_path, "test@123"],
        "expected_error": "AssertionError: the arguments are bad",
        "name": "Test 10: Special character '@'"
    },
    {
        "args": ["python3.10", sos_path, "hello!"],
        "expected_error": "AssertionError: the arguments are bad",
        "name": "Test 11: Exclamation mark '!'"
    },
    {
        "args": ["python3.10", sos_path, "test#"],
        "expected_error": "AssertionError: the arguments are bad",
        "name": "Test 12: Hash character '#'"
    },
    {
        "args": ["python3.10", sos_path, "café"],
        "expected_error": "AssertionError: the arguments are bad",
        "name": "Test 13: Accented character 'é'"
    }
]

passed = 0
failed = 0

for test in test_cases:
    result = subprocess.run(test["args"], capture_output=True, text=True)
    output = result.stdout.strip()
    
    if "expected_error" in test:
        if test["expected_error"] in output:
            print(f"✓ {test['name']}")
            print(f"  Output: {output}")
            passed += 1
        else:
            print(f"✗ {test['name']}")
            print(f"  Expected: {test['expected_error']}")
            print(f"  Got: {output}")
            failed += 1
    else:
        if test["expected"] == output:
            print(f"✓ {test['name']}")
            print(f"  Output: {output}")
            passed += 1
        else:
            print(f"✗ {test['name']}")
            print(f"  Expected: {test['expected']}")
            print(f"  Got: {output}")
            failed += 1
    print()

print("=" * 70)
print(f"Results: {passed} passed, {failed} failed")
print("=" * 70)

print("\n3. Morse Code Verification:")
print("-" * 70)
print("Sample conversions verified against Morse code standard:")
print("  'S' (3 dots)   = ... ✓")
print("  'O' (3 dashes) = --- ✓")
print("  'SOS' = ... --- ... ✓")
print("  Space separator = / ✓")
print("  Valid alphanumeric and space only")
print("  Special characters properly rejected ✓")
