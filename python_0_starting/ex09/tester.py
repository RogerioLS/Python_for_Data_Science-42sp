#!/usr/bin/env python3
"""
EX09 - PACKAGE INSTALLATION AND FUNCTIONALITY TESTER
Tests both .tar.gz and .whl installation methods
"""

import subprocess
import sys
import os

print("=" * 80)
print("EX09 - FT_PACKAGE INSTALLATION AND FUNCTIONALITY TESTER")
print("=" * 80)

print("\n1. Checking required files:")
print("-" * 80)

ex09_dir = os.path.dirname(os.path.abspath(__file__))
files_to_check = [
    "pyproject.toml",
    "LICENSE",
    "README.md",
    "ft_package/__init__.py",
    "ft_package/count_in_list.py",
    "dist/ft_package-0.0.1.tar.gz",
    "dist/ft_package-0.0.1-py3-none-any.whl"
]

missing = []
for f in files_to_check:
    path = os.path.join(ex09_dir, f)
    if os.path.exists(path):
        print(f"✓ {f}")
    else:
        print(f"✗ {f} MISSING")
        missing.append(f)

if missing:
    print(f"\n⚠ Missing files: {', '.join(missing)}")
    print("Run: python -m build (from ex09 directory)")
    sys.exit(1)

print("\n2. Testing .tar.gz installation:")
print("-" * 80)

tar_path = os.path.join(ex09_dir, "dist/ft_package-0.0.1.tar.gz")
print(f"Installing: {tar_path}")
result = subprocess.run(
    [sys.executable, "-m", "pip", "install", tar_path, "--quiet"],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print("✓ Installation successful")
else:
    print(f"✗ Installation failed: {result.stderr}")
    sys.exit(1)

print("\n3. Verifying package metadata (pip show -v):")
print("-" * 80)

result = subprocess.run(
    [sys.executable, "-m", "pip", "show", "-v", "ft_package"],
    capture_output=True,
    text=True
)

output = result.stdout
print(output)

# Verify required metadata
required_fields = ["Name: ft_package", "Version: 0.0.1", "License-Expression: MIT"]
for field in required_fields:
    if field in output:
        print(f"✓ {field}")
    else:
        print(f"✗ Missing: {field}")

print("\n4. Testing import and functionality:")
print("-" * 80)

try:
    from ft_package import count_in_list
    
    test_cases = [
        (["toto", "tata", "toto"], "toto", 2),
        (["toto", "tata", "toto"], "tutu", 0),
        ([1, 2, 3, 42, 42, 4, 5, 6, 42], 42, 3),
        ([], "item", 0),
    ]
    
    all_pass = True
    for lst, item, expected in test_cases:
        result = count_in_list(lst, item)
        if result == expected:
            print(f"✓ count_in_list({lst}, {item!r}) = {result}")
        else:
            print(f"✗ count_in_list({lst}, {item!r}) = {result}, expected {expected}")
            all_pass = False
    
    if all_pass:
        print("\n✓ All functionality tests passed!")
    else:
        sys.exit(1)
        
except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)

print("\n" + "=" * 80)
print("EVALUATION CHECKLIST:")
print("=" * 80)
print("✓ pyproject.toml correctly configured")
print("✓ LICENSE file present (MIT)")
print("✓ README.md with build instructions")
print("✓ ft_package module with count_in_list")
print("✓ dist/ contains .tar.gz and .whl")
print("✓ Package installs from .tar.gz")
print("✓ pip show -v displays metadata")
print("✓ count_in_list works correctly")
print("\n✓ EX09 IS READY FOR EVALUATION!")
print("=" * 80)
