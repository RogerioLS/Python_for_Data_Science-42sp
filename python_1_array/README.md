# Piscine Python for Data Science – Module 01 (Array)

## Overview

This repository contains the solutions for **Module 01 – Array** from the **42 Piscine Python for Data Science** training.

The goal of this module is to introduce array manipulations, vector/matrix operations using NumPy, and basic image processing tasks (slicing, loading, zooming, transposing, and applying custom filters).

All exercises are implemented using **Python 3.10**, following the constraints, coding standards, and error-handling requirements defined by the subject.

---

# Project Structure

```
.
├── ex00/
│   ├── give_bmi.py
│   ├── main.py
│   ├── README.md
│   └── notes.md
├── ex01/
│   ├── array2D.py
│   ├── main.py
│   ├── README.md
│   └── notes.md
├── ex02/
│   ├── load_image.py
│   ├── main.py
│   ├── README.md
│   └── notes.md
├── ex03/
│   ├── load_image.py
│   ├── zoom.py
│   ├── main.py
│   ├── README.md
│   └── notes.md
├── ex04/
│   ├── load_image.py
│   ├── rotate.py
│   ├── main.py
│   ├── README.md
│   └── notes.md
├── ex05/
│   ├── load_image.py
│   ├── pimp_image.py
│   ├── main.py
│   ├── README.md
│   └── notes.md
└── README.md
```

---

# General Rules

The following rules apply to all exercises:

- Python **3.10** must be used.
- **No global variables** are allowed.
- Imports must be **explicit**.
- Programs must **not crash** (no uncaught exceptions, even for inputs we are asked to test).
- Code must follow **flake8** standards.
- All functions must have documentation (`__doc__`).

---

# Reference Guide

| Exercise | File / Turn-in Files | Required Function Prototypes | Allowed Libraries | Critical Rules & Error Handling |
| :--- | :--- | :--- | :--- | :--- |
| [**ex00**](#ex00--give-my-bmi) | `give_bmi.py` | `give_bmi(height: list[int \| float], weight: list[int \| float]) -> list[int \| float]`<br>`apply_limit(bmi: list[int \| float], limit: int) -> list[bool]` | NumPy or any table manipulation library. | Handle error cases if lists are not the same size, or contain values that are not `int` or `float`. |
| [**ex01**](#ex01--2d-array) | `array2D.py` | `slice_me(family: list, start: int, end: int) -> list` | NumPy or any table manipulation library. | Print initial shape, perform mandatory slicing using python slicing method, and print the new shape. Handle errors if input is not a list or if row sizes are inconsistent. |
| [**ex02**](#ex02--load-my-image) | `load_image.py` | `ft_load(path: str) -> array` (NumPy array) | Any library for loading images and table manipulation. | Load image in **RGB** format. Print format (shape) and pixels content. Handle JPG/JPEG formats. Manage errors with clear messages without crashing. |
| [**ex03**](#ex03--zoom-on-me) | `load_image.py`<br>`zoom.py` | Main script: `zoom.py`<br>Reuses `ft_load` from ex02. | Any library for load, manipulate, display image and table manipulation. | Load `animal.jpeg`. Print initial dimensions. Slice a square part (zoom `400x400`). Convert/display in grayscale/1 channel. Display the final image using `matplotlib` showing scale on X and Y axes. Must handle errors with a clear message and not crash. |
| [**ex04**](#ex04--rotate-me) | `load_image.py`<br>`rotate.py` | Main script: `rotate.py`<br>Reuses `ft_load` from ex02. | Any library for load, manipulate, display image and table manipulation (except transposition). | Cut a square part and **transpose it manually** (swap X and Y axes by yourself, **no transpose/rotation libraries allowed**). Display the transposed image and print its new shape. |
| [**ex05**](#ex05--pimp-my-image) | `load_image.py`<br>`pimp_image.py` | `ft_invert(array) -> array`<br>`ft_red(array) -> array`<br>`ft_green(array) -> array`<br>`ft_blue(array) -> array`<br>`ft_grey(array) -> array` | Any library for load, manipulate, display image and table manipulation. | Apply filters using **only** the allowed operators in each function:<br>• *Invert*: `=, +, -, *`<br>• *Red*: `=, *`<br>• *Green*: `=, -`<br>• *Blue*: `=`<br>• *Grey*: `=, /` |

---

# Exercises

## ex00 – Give my BMI

Calculates the Body Mass Index (BMI) and checks if a list of BMIs exceeds a given limit.

<details>
<summary><b>📘 Exercise 00 – Learning Notes & Specifications</b></summary>

### Objective & Requirements
- Implement `give_bmi(height, weight)` and `apply_limit(bmi, limit)`.
- Use `numpy` for vectorized math calculations.
- Raise `ValueError` if list sizes differ or if heights/weights are $\le 0$.
- Raise `TypeError` for non-numeric types.

### 1. Vectorized Calculation with NumPy
Instead of looping over height and weight lists manually, we convert the lists to NumPy arrays (`np.array`) to execute mathematical operations element-wise:
$$BMI = \frac{weight}{height^2}$$

In NumPy:
```python
bmi_arr = w_arr / (h_arr ** 2)
```
This is significantly faster and cleaner than manual loops.

### 2. Type Strictness and Boolean Subclassing
In Python, `bool` is a subclass of `int`. This means:
```python
isinstance(True, int)  # True
```
To strictly reject booleans from list validation check, we check the type directly instead of using `isinstance`:
```python
if type(val) not in (int, float):
    # Reject boolean and string inputs safely
```

### 3. Error Prevention
To prevent errors such as `ZeroDivisionError` or math inconsistencies:
- Assert that inputs are lists.
- Assert that lists have identical lengths.
- Assert that height and weight are strictly positive numbers ($> 0$).

</details>

---

## ex01 – 2D Array

Prints the shape of a 2D array and returns a sliced version of it.

<details>
<summary><b>📘 Exercise 01 – Learning Notes & Specifications</b></summary>

### Objective & Requirements
- Implement `slice_me(family, start, end)`.
- Print the initial shape of a 2D array and its new shape after slicing.
- Return the sliced 2D array.
- Raise `ValueError` if the lists have inconsistent row sizes.
- Raise `TypeError` if inputs are invalid.

### 1. Shape of multi-dimensional arrays
A 2D array in Python is represented as a list of lists. By converting it to a NumPy array `np.array(family)`, we can easily inspect its dimensions using the `.shape` attribute, which returns a tuple representing the sizes of each dimension:
```python
import numpy as np
arr = np.array(family)
print(arr.shape) # Output: (rows, columns)
```

### 2. Native Python Slicing
Unlike NumPy's array slicing, native Python slicing for a 2D list only operates on the first dimension (rows):
```python
sliced = family[start:end]
```
Negative indices (e.g. `-1`, `-2`) are natively supported and count backwards from the end of the list.

### 3. Rectangular Matrix Validation
A valid 2D array must have consistent dimensions, meaning all sublists (rows) must have the exact same size. If row lengths differ:
- NumPy might create an array of `object` dtype with shape `(N,)` rather than a `(N, M)` matrix.
- We validate this explicitly by checking:
```python
if len(family) > 0:
    first_row_len = len(family[0])
    if any(len(row) != first_row_len for row in family):
        raise ValueError("All rows in the 2D array must have the same size")
```

</details>

---

## ex02 – Load my image

Loads an image and prints its metadata (shape) and pixel content in RGB format.

<details>
<summary><b>📘 Exercise 02 – Learning Notes & Specifications</b></summary>

### Objective & Requirements
- Implement `ft_load(path: str) -> np.ndarray`.
- Use the **PIL (Pillow)** library to load the image.
- Explicitly convert the image to the **RGB** format.
- Convert the PIL image to a **NumPy array**.
- Print the shape of the image: `"The shape of image is: {shape}"`.
- Handle error cases gracefully (e.g., file not found, bad format/corrupted file) by catching exceptions without letting the program crash.

### 1. PIL (Pillow) & NumPy Integration
Pillow is a standard library for image processing in Python. Since NumPy arrays represent multi-dimensional numerical data, we can seamlessly bridge PIL and NumPy:
```python
with Image.open(path) as img:
    img_rgb = img.convert("RGB")
    img_array = np.array(img_rgb)
```
- `.convert("RGB")` guarantees that any image format (RGBA, Grayscale, CMYK, Palette-based) is uniformly converted into 3 color channels (Red, Green, Blue).
- `np.array(img_rgb)` creates an array of shape `(Height, Width, 3)` with `uint8` data type (values from 0 to 255).

### 2. Error Handling & Exception Management
Image loading is highly prone to runtime IO failures. We catch specific exceptions:
- `FileNotFoundError`: Triggers if the file path is incorrect.
- `PIL.UnidentifiedImageError`: Triggers if the file exists but Pillow cannot identify it as an image (e.g., a corrupted file or an incompatible text file).
- `TypeError`: Triggers if the path argument is of an incorrect type.

</details>

---

## ex03 – Zoom on me

Cuts a square part from an image and displays it with a scale on the axes.

<details>
<summary><b>📘 Exercise 03 – Learning Notes</b></summary>

### Objective & Requirements
- Implement `zoom.py` which loads `animal.jpeg`.
- Print the original image shape and pixel content.
- Slice a $400 \times 400$ region from the image with 1 color channel (e.g. `img[100:500, 380:780, 0:1]`).
- Print the new shape: `"New shape after slicing: (400, 400, 1) or (400, 400)"`.
- Print the sliced array pixel content.
- Display the zoomed image using `matplotlib.pyplot` in grayscale with scales on both the X and Y axes.
- Handle potential errors gracefully (e.g. `FileNotFoundError`, `ImportError`, and matplotlib issues).

### 1. Image Slicing (Cropping) in NumPy
Slicing allows us to extract sub-regions of multi-dimensional arrays without copying the underlying data:
```python
sliced = img[100:500, 380:780, 0:1]
```
Here, we select:
- Rows `100` to `500` (height index).
- Columns `380` to `780` (width index).
- Color channel `0` (the Red channel, which acts as our grayscale representation when treated as a single channel).

### 2. Displaying with Matplotlib
We use `matplotlib.pyplot.imshow` to display the 2D array. Matplotlib displays a 1-channel or 2D array in colormap colors. Specifying `cmap="gray"` displays the single channel as a standard grayscale image.
By default, `imshow` includes ticks and labels indicating the pixel coordinates on both the X and Y axes, satisfying the requirement to show the scales.

### 3. Graceful Error Handling
Since loading graphics libraries (like `matplotlib`) and images can fail (e.g. in headless environments, or if dependency imports fail, or if `animal.jpeg` is missing), the entire execution is wrapped inside a try-except block to output clean messages rather than stack traces.

</details>

---

## ex04 – Rotate me

Transposes an image (x and y swap) manually without using high-level libraries for the rotation.

<details>
<summary><b>📘 Exercise 04 – Learning Notes</b></summary>

### 1. Objective
Slice a 400x400 region with one color channel (Red channel, index `0`) from an image and transpose it manually. Display the transposed image showing coordinate scales on both the X and Y axes.

### 2. Requirements & Constraints
- Load `animal.jpeg` using `ft_load` from `load_image.py`.
- Crop a 400x400 slice (e.g., `[100:500, 380:780, 0:1]`).
- Print the sliced array shape and content.
- Transpose the 400x400 slice manually using **nested loops** in Python, swapping the X and Y axes (e.g. `transposed[j, i] = sliced[i, j, 0]`).
- Do **NOT** use `np.transpose`, `np.rot90`, `T`, or PIL's transpose/rotate functions.
- Print the transposed shape and content.
- Display the transposed grayscale image with axes/ticks enabled using `matplotlib.pyplot`.

### 3. Manual Transposition Logic
In linear algebra, transposing a matrix $A$ results in a new matrix $A^T$ where elements are swapped along the main diagonal:
$$A^T[j][i] = A[i][j]$$

By iterating through the height and width of the sliced image array using nested loops, we copy each pixel to its swapped coordinate position in the target array:
```python
# Height and width are both 400
transposed = np.zeros((width, height), dtype=sliced.dtype)
for i in range(height):
    for j in range(width):
        transposed[j, i] = sliced[i, j, 0]
```
This converts the shape from `(400, 400, 1)` to `(400, 400)` and rotates/transposes the image counter-clockwise or clockwise with vertical flip.

</details>

---

## ex05 – Pimp my image

Applies custom filters to an image using specific math operators.

<details>
<summary><b>📘 Exercise 05 – Learning Notes</b></summary>

*(Pending implementation)*

</details>
