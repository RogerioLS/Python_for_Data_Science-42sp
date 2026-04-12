# Piscine Python for Data Science – Module 00 (Starting)

## Overview

This repository contains the solutions for **Module 00 – Starting** from the **42 Piscine Python for Data Science** training.

The goal of this module is to introduce the fundamental concepts of the Python programming language and basic software engineering practices used throughout the program.

The exercises progressively cover:

- Python data structures
- Functions and typing
- CLI argument handling
- String analysis
- Functional programming concepts
- Generators
- Dictionary usage
- Python package creation

All exercises are implemented using **Python 3.10**, following the constraints and coding standards defined by the subject.

---

# Project Structure

```
.
├── ex00/
│   └── Hello.py
├── ex01/
│   └── format_ft_time.py
├── ex02/
│   └── find_ft_type.py
├── ex03/
│   └── NULL_not_found.py
├── ex04/
│   └── whatis.py
├── ex05/
│   └── building.py
├── ex06/
│   ├── ft_filter.py
│   └── filterstring.py
├── ex07/
│   └── sos.py
├── ex08/
│   └── Loading.py
├── ex09/
│   ├── ft_package/
│   ├── README.md
│   ├── LICENSE
│   └── pyproject.toml
└── README.md
```

---

# General Rules

The following rules apply to all exercises:

- Python **3.10** must be used.
- **No global variables** are allowed.
- Imports must be **explicit**.

Example:

```python
import numpy as np
```

Forbidden:

```python
from numpy import *
```

- Programs must **not crash** (no uncaught exceptions).
- Code must follow **flake8** standards.

Install flake8:

```bash
pip install flake8
```

Run lint check:

```bash
flake8 .
```

---

# Execution

Each exercise can be executed directly using Python.

Example:

```bash
python ex04/whatis.py 14
```

Example output:

```
I'm Even.
```

---

# Exercises

## ex00 – First Python Script

Manipulation of Python data structures:

- list
- tuple
- set
- dictionary

Goal: modify values in each structure to produce specific outputs.

<details>

<summary><b>📘 Exercise 00 – Learning Notes</b></summary>

## Exercise 00 – Key Concepts Learned

This exercise focuses on understanding how different Python data structures behave when modifying their contents. The goal is not only to change values, but to understand **mutability, indexing, and internal structure behavior**.

### 1. Lists

Lists are **mutable and ordered** collections.

Internally, a list behaves like a **dynamic array of references to objects**. Each position in the list stores a reference to an object rather than the object itself.

Example:

```python
ft_list = ["Hello", "tata!"]
```

Because lists are mutable, elements can be modified directly using their index:

```python
ft_list[1] = "World!"
```

This operation replaces the reference stored at index `1` with a new object.

Key properties:

- ordered
- mutable
- indexed access
- dynamic size

---

### 2. Tuples

Tuples are **ordered but immutable** collections.

Once created, their elements **cannot be modified, added, or removed**. This immutability allows tuples to be **hashable**, which means they can be used as dictionary keys or stored in sets.

Example:

```python
ft_tuple = ("Hello", "toto!")
```

Since tuples cannot be modified directly, changing a value requires creating a **new tuple**:

```python
ft_tuple = ("Hello", "Brazil!")
```

Key properties:

- ordered
- immutable
- hashable (if elements are hashable)

---

### 3. Sets

Sets are **unordered collections of unique elements**.

Internally, they are implemented using a **hash table**, meaning elements are stored based on their hash values rather than their insertion order.

Example:

```python
ft_set = {"Hello", "tutu!"}
```

Because sets are unordered, they **do not support indexing**.

Elements are modified using value-based operations:

```python
ft_set.remove("tutu!")
ft_set.add("Sao Paulo!")
```

Due to the hash-based implementation, the printed order of elements may change between executions.

Key properties:

- unordered
- mutable
- unique elements
- no indexing

---

### 4. Dictionaries

Dictionaries are **key–value mappings**, also implemented using a **hash table**.

Each key is hashed to locate the corresponding value efficiently.

Example:

```python
ft_dict = {"Hello": "titi!"}
```

To update a value, we reference the key directly:

```python
ft_dict["Hello"] = "42SaoPaulo!"
```

Since Python 3.7, dictionaries **preserve insertion order**, although lookup is still performed using hashing.

Key properties:

- key–value structure
- mutable
- fast lookups via hashing
- insertion order preserved (Python ≥ 3.7)

---

### Summary

| Structure | Ordered | Mutable | Indexed | Based on Hash |
|-----------|--------|--------|--------|---------------|
| List      | Yes    | Yes    | Yes    | No |
| Tuple     | Yes    | No     | Yes    | No |
| Set       | No     | Yes    | No     | Yes |
| Dict      | Yes*   | Yes    | No     | Yes |

\* Dictionaries preserve insertion order starting from Python 3.7.

This exercise demonstrates how each data structure requires **different modification strategies**, reinforcing the importance of understanding mutability and internal data structure behavior in Python.

</details>

---

## ex01 – First Use of Package

Use Python libraries (`time`, `datetime`) to format and display:

- seconds since the Unix epoch
- formatted date output

<details>
<summary><b>📘 Exercise 01 – Learning Notes</b></summary>

## Exercise 01 – Key Concepts Learned

This exercise introduces how Python interacts with system time and how numeric and date values can be formatted for human-readable output.

The goal is not only to obtain the current timestamp, but also to understand **Unix time, numeric formatting, scientific notation, and date formatting in Python**.

---

### 1. Unix Timestamp

Python can retrieve the current time as a **Unix timestamp**, which represents the number of seconds that have elapsed since:

```
January 1, 1970 (00:00:00 UTC)
```

This reference point is known as the **Unix Epoch**.

Example in Python:

```python
import time

timestamp = time.time()
```

This returns a floating-point number such as:

```
1713648000.1234
```

The decimal part represents **fractions of a second**.

---

### 2. Numeric Formatting

Python allows numbers to be formatted using **format specifiers** inside f-strings.

Example:

```python
f"{timestamp:,.4f}"
```

Explanation of the format:

| Specifier | Meaning |
|----------|--------|
| `,` | Adds thousands separators |
| `.4f` | Keeps 4 decimal places |
| `f` | Fixed-point notation |

Example output:

```
1,713,648,000.1234
```

This improves readability for large numbers.

---

### 3. Scientific Notation

Scientific notation expresses large numbers in the form:

```
a × 10ⁿ
```

Python formats numbers this way using the `e` format specifier.

Example:

```python
f"{timestamp:.2e}"
```

Explanation:

| Specifier | Meaning |
|----------|--------|
| `.2` | Two digits after the decimal |
| `e` | Scientific notation |

Example output:

```
1.71e+09
```

This format is widely used in **scientific computing and data science**.

---

### 4. Date Formatting with `strftime`

Python's `time` module can convert timestamps into human-readable date formats.

Example:

```python
time.strftime("%b %d %Y", time.localtime())
```

Format codes used:

| Code | Meaning | Example |
|-----|--------|--------|
| `%b` | Month abbreviation | Oct |
| `%d` | Day of month | 21 |
| `%Y` | Full year | 2022 |

Example result:

```
Oct 21 2022
```

---

### Summary

| Concept | Purpose |
|-------|--------|
| `time.time()` | Retrieve Unix timestamp |
| Numeric formatting (`:,.4f`) | Improve readability of large numbers |
| Scientific notation (`:.2e`) | Represent large numbers compactly |
| `strftime()` | Format dates for human-readable output |

This exercise demonstrates how Python can **retrieve system time and present it in different numeric and textual formats**, which is a common requirement in logging systems, data processing, and scientific applications.

</details>

---

## ex02 – First Function Python

Create a function that:

- detects the type of an object
- prints a message depending on the type
- always returns `42`

<details>
<summary><b>📘 Exercise 02 – Learning Notes</b></summary>

## Exercise 02 – Key Concepts Learned

This exercise introduces the fundamentals of **functions, type detection, and conditional logic in Python**.

The goal is to understand how Python handles different data types dynamically and how to create behavior based on those types.

---

### 1. Functions in Python

Functions allow us to encapsulate logic and reuse code.

Example:

```python
def all_thing_is_obj(obj: any) -> int:
    ...
```

Key elements:

| Concept | Meaning |
|--------|--------|
| `def` | Function definition |
| `obj: any` | Type hint (accepts any type) |
| `-> int` | Return type hint |
| `return` | Value returned by the function |

In this exercise, the function must always return:

```
42
```

---

### 2. Dynamic Typing

Python is a **dynamically typed language**, meaning that variable types are determined at runtime.

We can inspect the type of any object using:

```python
type(obj)
```

Example:

```python
type([1, 2, 3])   → <class 'list'>
type("Hello")     → <class 'str'>
type(10)          → <class 'int'>
```

---

### 3. Type-Based Conditional Logic

The function behavior changes depending on the object's type.

Example:

```python
if type(obj) == list:
    ...
elif type(obj) == tuple:
    ...
```

Each type produces a specific output format.

---

### 4. Special Case: Strings

Strings receive special handling in this exercise.

Instead of printing:

```
Str : <class 'str'>
```

The expected output is:

```
Brian is in the kitchen : <class 'str'>
```

This demonstrates how logic can be customized based on both:

- the type
- the value of the object

---

### 5. Default Case Handling

If the object does not match any expected type, the function must handle it safely:

```python
print("Type not found")
```

This ensures robustness and prevents unexpected behavior.

---

### 6. `type()` vs `isinstance()`

Although this exercise uses `type()`, Python also provides a more flexible alternative:

```python
isinstance(obj, list)
```

Difference:

| Method | Behavior |
|--------|--------|
| `type(obj) == list` | Exact type match |
| `isinstance(obj, list)` | Accepts subclasses |

`isinstance()` is generally preferred in real-world Python applications.

---

### Summary

| Concept | Purpose |
|--------|--------|
| Functions (`def`) | Encapsulate reusable logic |
| `type()` | Identify object type at runtime |
| Conditional logic | Control behavior based on type |
| Special-case handling | Customize output for specific types |
| `return 42` | Ensure consistent function output |

This exercise reinforces how Python handles **dynamic typing and conditional logic**, which are essential for writing flexible and robust programs.

</details>

---

## ex03 – NULL Not Found

Create a function that detects different **null-like values** in Python:

- `None`
- `NaN`
- `0`
- `""`
- `False`

The function must return:

```
0 → success
1 → error
```

<details>
<summary><b>📘 Exercise 03 – Learning Notes</b></summary>

## Exercise 03 – Key Concepts Learned

This exercise explores how Python represents different forms of **"null-like" values**, and how to distinguish them safely.

The goal is to understand that in Python, the concept of "null" is **not a single value**, but a set of different representations depending on context.

---

### 1. `None` – Absence of Value

`None` represents the absence of a value and is the only instance of the `NoneType`.

Example:

```python
x = None
```

Detection:

```python
if obj is None:
```

Key point:

- Always use `is`, not `==`

---

### 2. `NaN` – Not a Number (Critical Concept)

`NaN` represents an undefined or unrepresentable floating-point value.

Example:

```python
float("nan")
```

---

#### ⚠️ Special Behavior

```python
float("nan") == float("nan")  # False
```

This happens because of the **IEEE 754 floating-point standard**, where:

```
NaN is not equal to anything, including itself
```

---

#### Correct Detection

```python
import math

math.isnan(obj)
```

Key point:

- `NaN` must be detected using a specific function
- Direct comparison **does not work**

---

### 3. `0` vs `False` – Subtle Difference

In Python:

```python
False == 0  # True
```

However:

```python
type(False) != type(0)
```

This means:

- `0` is an integer (`int`)
- `False` is a boolean (`bool`)

Correct detection requires checking **both type and value**.

---

### 4. Empty String `""`

An empty string represents a lack of textual content.

Example:

```python
obj == ""
```

Output format:

```
Empty: <class 'str'>
```

Note:

- The value itself is not printed, only the type

---

### 5. Boolean `False`

Represents a false logical value.

Detection:

```python
type(obj) is bool and obj is False
```

Output:

```
Fake: False <class 'bool'>
```

---

### 6. Handling Unknown Types

If the object does not match any expected "null-like" type:

```python
print("Type not Found")
return 1
```

Otherwise:

```python
return 0
```

---

### 7. Truthy vs Falsy Values

Python treats several values as "falsy":

```
None, False, 0, "", [], {}, etc.
```

However, in this exercise, it is important to:

- **distinguish each case explicitly**
- not rely only on truthiness

---

### Summary

| Value | Type | Detection Method |
|------|------|----------------|
| `None` | NoneType | `obj is None` |
| `NaN` | float | `math.isnan(obj)` |
| `0` | int | `type(obj) is int and obj == 0` |
| `""` | str | `type(obj) is str and obj == ""` |
| `False` | bool | `type(obj) is bool and obj is False` |

---

### Key Takeaway

This exercise demonstrates that Python handles "null" in multiple ways, and robust programs must:

- explicitly identify each case
- avoid ambiguous comparisons
- understand edge cases like `NaN`

Mastering these distinctions is essential for **data validation, data science, and defensive programming**.

</details>

---

## ex04 – Even or Odd

Create a CLI program that:

- accepts a number as argument
- determines if it is **Even or Odd**

Errors must be handled using `AssertionError`.

<details>
<summary><b>📘 Exercise 04 – Learning Notes</b></summary>

## Exercise 04 – Key Concepts Learned

This exercise introduces how Python programs interact with the **command line**, how to validate user input, and how to control execution flow based on different input scenarios.

It marks the transition from simple scripts to **real executable programs**.

---

### 1. Command-Line Arguments (`sys.argv`)

Python provides access to command-line arguments through the `sys` module.

Example:

```python
import sys

print(sys.argv)
```

Running:

```bash
python whatis.py 14
```

Produces:

```
['whatis.py', '14']
```

Key points:

- `sys.argv[0]` → script name  
- `sys.argv[1]` → first argument  
- Arguments are always **strings**

---

### 2. Input Validation

The program must validate:

| Case | Behavior |
|-----|--------|
| No arguments | Do nothing |
| One argument | Process it |
| More than one | Raise error |

Example:

```python
if len(sys.argv) > 2:
    raise AssertionError("more than one argument is provided")
```

---

### 3. Type Conversion

Arguments from the CLI are strings and must be converted:

```python
number = int(sys.argv[1])
```

If conversion fails:

```python
ValueError
```

This must be handled and converted into:

```
AssertionError: argument is not an integer
```

---

### 4. Even and Odd Detection

Even and odd numbers are determined using the modulo operator:

```python
number % 2
```

Rules:

- Even → remainder is `0`
- Odd → remainder is `1`

Example:

```python
if number % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
```

---

### 5. Error Handling

The exercise requires converting runtime errors into **specific messages**.

Two main errors:

| Scenario | Output |
|--------|--------|
| More than one argument | `AssertionError: more than one argument is provided` |
| Invalid integer | `AssertionError: argument is not an integer` |

This is typically handled using:

```python
try:
    ...
except ValueError:
    ...
except AssertionError:
    ...
```

---

### 6. Silent Execution Case

If no argument is provided:

```bash
python whatis.py
```

The program must:

- produce **no output**
- exit silently

This tests correct control flow handling.

---

### 7. Separation of Concerns

A good design separates:

- **input handling (CLI)**
- **business logic (even/odd check)**

Example:

```python
def check_odd_even(number: int):
    ...
```

This improves readability and reusability.

---

### Summary

| Concept | Purpose |
|--------|--------|
| `sys.argv` | Access command-line input |
| Input validation | Ensure correct number of arguments |
| `int()` conversion | Convert string to integer |
| `%` operator | Determine even/odd |
| Exception handling | Control program flow and errors |
| Silent execution | Handle edge case with no input |

---

### Key Takeaway

This exercise demonstrates how to build a **robust command-line program** by:

- validating user input
- handling errors explicitly
- controlling execution flow

These patterns are fundamental for writing reliable Python scripts and applications.

</details>

---

## ex05 – Text Analyzer

Standalone program that analyzes a string and counts:

- uppercase letters
- lowercase letters
- punctuation
- spaces
- digits

<details>
<summary><b>📘 Exercise 05 – Learning Notes</b></summary>

## Exercise 05 – Key Concepts Learned

This exercise marks the transition from simple scripts to **fully structured programs**, combining command-line interaction, input validation, string processing, and program organization.

It introduces the foundation for building **robust and maintainable CLI applications**.

---

### 1. Program Structure (`main()`)

Unlike previous exercises, this one enforces proper structure:

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

Key idea:

- Separate **program entry point** from logic
- Improve readability and maintainability
- Follow standard Python conventions

---

### 2. Command-Line vs Interactive Input

The program must support two modes:

| Scenario | Behavior |
|--------|--------|
| Argument provided | Use it as input |
| No argument | Prompt user with `input()` |
| More than one argument | Raise error |

Example:

```python
sys.argv[1:]
```

If no argument:

```python
input("What is the text to count?\n")
```

---

### 3. Input Validation

The program must validate the number of arguments:

```python
if len(arguments) > 1:
    raise AssertionError("more than one argument is provided")
```

And handle errors safely:

```python
try:
    ...
except AssertionError:
    ...
```

Key rule:

- **No uncaught exceptions allowed**

---

### 4. Character Classification

Each character in the string must be classified into one category:

| Category | Method |
|--------|--------|
| Uppercase | `char.isupper()` |
| Lowercase | `char.islower()` |
| Digits | `char.isdigit()` |
| Spaces | `char.isspace()` |
| Punctuation | `char in string.punctuation` |

This avoids manual comparisons and leverages Python’s built-in features.

---

### 5. Counting Strategy

The program iterates through the string and updates counters:

```python
for char in text:
    ...
```

Using a dictionary initialized with zero values:

```python
types = {
    "upper": 0,
    "lower": 0,
    "punctuation": 0,
    "spaces": 0,
    "digits": 0,
}
```

This ensures:

- consistent output
- simpler logic
- no need for `.get()`

---

### 6. Handling Whitespace Correctly

Using:

```python
char.isspace()
```

captures:

- spaces (`" "`)
- tabs (`\t`)
- newlines (`\n`)

This is important because the exercise specifies that **carriage returns count as spaces**.

---

### 7. Output Formatting

The output must strictly follow the format:

```
The text contains X characters:
Y upper letters
Z lower letters
...
```

Key points:

- spacing and wording must match exactly
- no extra text or formatting allowed

---

### 8. Error Handling and Flow Control

Errors must be handled explicitly:

| Error | Output |
|------|--------|
| Too many arguments | `AssertionError: more than one argument is provided` |

The program must:

- not crash
- not show traceback
- handle all expected edge cases

---

### Summary

| Concept | Purpose |
|--------|--------|
| `main()` | Organize program entry point |
| `sys.argv` | Handle CLI input |
| `input()` | Support interactive mode |
| Validation | Ensure correct usage |
| `str` methods | Classify characters |
| Dictionary counters | Aggregate results |
| Exception handling | Prevent crashes |

---

### Key Takeaway

This exercise demonstrates how to build a **complete, reliable Python program** by combining:

- structured code organization
- robust input handling
- efficient use of built-in language features

It represents a major step toward writing **real-world Python applications**.

</details>

---

## ex06 – Custom Filter

Reimplement Python's built-in `filter()` function.

Constraints:

- `filter()` cannot be used
- must use **list comprehension**

A program is also created to filter words by length.

---

## ex07 – Morse Code Encoder

Create a program that:

- converts alphanumeric text into **Morse code**
- uses a **dictionary mapping**

Rules:

- characters separated by spaces
- word spaces represented by `/`

---

## ex08 – Progress Bar (tqdm clone)

Implement a custom progress bar similar to **tqdm** using:

- `yield`
- iteration tracking
- terminal width handling (`os.get_terminal_size`)

---

## ex09 – Python Package Creation

Create and distribute a simple Python package:

```
ft_package
```

The package must be installable using:

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

Example usage:

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
```

Expected output:

```
2
```

---

# Learning Objectives

This module focuses on developing the following skills:

- Python syntax fundamentals
- data structure manipulation
- functional programming
- CLI programs
- error handling
- generators
- Python packaging

---

# Author

Student at **42 School – Piscine Python for Data Science**