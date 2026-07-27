# 42 Python Piscine - Master Makefile
# Automation for Testing, Norm Checks, Syntax Compilation, and Clean up.

PYTHON := python3

.PHONY: help test test-m00 test-m01 norm compile audit clean

help:
	@echo "======================================================================"
	@echo "             42 PYTHON PISCINE - COMMAND CENTER                       "
	@echo "======================================================================"
	@echo "  make help       - Display this help message"
	@echo "  make test       - Run all unit test suites (Module 00 & Module 01)"
	@echo "  make test-m00   - Run unit tests for Module 00 (Starting)"
	@echo "  make test-m01   - Run unit tests for Module 01 (Array)"
	@echo "  make norm       - Audit code against 42 Norm (docstrings, guards, etc.)"
	@echo "  make compile    - Verify Python 3.10 syntax compilation across all files"
	@echo "  make audit      - Full audit: compile + norm check + all unit tests"
	@echo "  make clean      - Clean all temporary cache files (__pycache__, .pyc)"
	@echo "======================================================================"

test:
	@echo "🚀 Running all unit test suites..."
	$(PYTHON) -m unittest discover -s tests -p "test_*.py"

test-m00:
	@echo "🚀 Running Module 00 (Starting) unit tests..."
	$(PYTHON) -m unittest tests/test_module_00.py

test-m01:
	@echo "🚀 Running Module 01 (Array) unit tests..."
	$(PYTHON) -m unittest tests/test_module_01.py

norm:
	@echo "🛡️ Running 42 Norm & Clean Code Auditor..."
	$(PYTHON) scripts/norm_check.py

compile:
	@echo "⚡ Compiling Python syntax across all exercise files..."
	$(PYTHON) -m py_compile $$(find python_0_starting python_1_array -name "*.py")

audit: compile norm test
	@echo "✅ FULL AUDIT COMPLETE: Code is compliant and ready for peer evaluation!"

clean:
	@echo "🧹 Cleaning temporary cache files..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	@echo "Done."
