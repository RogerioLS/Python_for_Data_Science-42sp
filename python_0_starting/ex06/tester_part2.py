import subprocess
import sys
import inspect
import os

print("=" * 60)
print("EX06 PART 2 - FILTERSTRING TESTS")
print("=" * 60)

print("\n1. Checking source code constraints:")
print("-" * 60)

script_dir = os.path.dirname(os.path.abspath(__file__))
filterstring_path = os.path.join(script_dir, "filterstring.py")

with open(filterstring_path, "r") as f:
    source = f.read()

has_list_comp = "[" in source and "for" in source and "]" in source
has_lambda = "lambda" in source
has_assertion = "AssertionError" in source

print(f"List comprehension: {'PASS' if has_list_comp else 'FAIL'}")
print(f"Lambda function: {'PASS' if has_lambda else 'FAIL'}")
print(f"AssertionError handling: {'PASS' if has_assertion else 'FAIL'}")

print("\n2. Running functional tests:")
print("-" * 60)

test_cases = [
    {
        "args": ["python3", "filterstring.py", "Hello the World", "4"],
        "expected": "['Hello', 'World']",
        "name": "Test 1: Filter words length > 4"
    },
    {
        "args": ["python3", "filterstring.py", "Hello the World", "99"],
        "expected": "[]",
        "name": "Test 2: Filter with length > 99 (empty)"
    },
    {
        "args": ["python3", "filterstring.py", "A robot may not injure a human being or through inaction allow a human being to come to harm", "5"],
        "expected": "['injure', 'through', 'inaction']",
        "name": "Test 3: Complex text with length > 5"
    },
    {
        "args": ["python3", "filterstring.py", "3", "Hello the World"],
        "expected_error": "AssertionError: the arguments are bad",
        "name": "Test 4: Wrong argument type (int first)"
    },
    {
        "args": ["python3", "filterstring.py"],
        "expected_error": "AssertionError: the arguments are bad",
        "name": "Test 5: Missing arguments"
    }
]

passed = 0
failed = 0

for test in test_cases:
    args = list(test["args"])
    if args[0] == "python3":
        args[0] = "python3.10"
    if "filterstring.py" in args:
        idx = args.index("filterstring.py")
        args[idx] = filterstring_path
    result = subprocess.run(args, capture_output=True, text=True)
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
        if test["expected"] in output:
            print(f"✓ {test['name']}")
            print(f"  Output: {output}")
            passed += 1
        else:
            print(f"✗ {test['name']}")
            print(f"  Expected: {test['expected']}")
            print(f"  Got: {output}")
            failed += 1
    print()

print("=" * 60)
print(f"Results: {passed} passed, {failed} failed")
print("=" * 60)
