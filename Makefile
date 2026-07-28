# ==============================================================================
#                       42 PYTHON PISCINE MASTER MAKEFILE
# ==============================================================================

PYTHON := python3

# ANSI Color Codes & Formatting
RESET   := \033[0m
BOLD    := \033[1m
DIM     := \033[2m
CYAN    := \033[36m
GREEN   := \033[32m
YELLOW  := \033[33m
RED     := \033[31m
MAGENTA := \033[35m
BLUE    := \033[34m
WHITE   := \033[97m

.PHONY: help test test-m00 test-m01 norm compile audit clean

help:
	@title="42 PYTHON PISCINE — COMMAND CENTER"; \
	width=78; \
	len=$$(printf "%s" "$$title" | wc -m); \
	left=$$(( (width - len) / 2 )); \
	right=$$(( width - len - left )); \
	printf "$(CYAN)┌──────────────────────────────────────────────────────────────────────────────┐$(RESET)\n"; \
	printf "$(CYAN)│$(RESET)%*s$(BOLD)$(MAGENTA)%s$(RESET)%*s$(CYAN)│$(RESET)\n" \
		$$left "" "$$title" $$right ""; \
	printf "$(CYAN)├──────────────────────────────────────────────────────────────────────────────┤$(RESET)\n"; \
	printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)%-15s$(RESET) $(DIM)─$(RESET) %-56s $(CYAN) │$(RESET)\n" \
		"make help" "Show this interactive help menu"; \
	printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)%-15s$(RESET) $(DIM)─$(RESET) %-56s $(CYAN) │$(RESET)\n" \
		"make test" "Run all unit test suites (Module 00 & Module 01)"; \
	printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)%-15s$(RESET) $(DIM)─$(RESET) %-56s $(CYAN) │$(RESET)\n" \
		"make test-m00" "Run unit tests for Module 00 (Starting)"; \
	printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)%-15s$(RESET) $(DIM)─$(RESET) %-56s $(CYAN) │$(RESET)\n" \
		"make test-m01" "Run unit tests for Module 01 (Array)"; \
	printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)%-15s$(RESET) $(DIM)─$(RESET) %-56s $(CYAN) │$(RESET)\n" \
		"make norm" "Run 42 Norm & Clean Code Auditor (docstrings, guards)"; \
	printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)%-15s$(RESET) $(DIM)─$(RESET) %-56s $(CYAN) │$(RESET)\n" \
		"make compile" "Compile Python 3.10 syntax across all exercise files"; \
	printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)%-15s$(RESET) $(DIM)─$(RESET) %-56s $(CYAN) │$(RESET)\n" \
		"make audit" "Full audit: compile + norm + unit tests"; \
	printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)%-15s$(RESET) $(DIM)─$(RESET) %-56s $(CYAN) │$(RESET)\n" \
		"make clean" "Remove temporary cache files (__pycache__, .pyc)"; \
	printf "$(CYAN)└──────────────────────────────────────────────────────────────────────────────┘$(RESET)\n"

test:
	@echo "\n$(BOLD)$(BLUE)🚀 [TESTS] Running all unit test suites...$(RESET)"
	@$(PYTHON) -m unittest discover -s tests -p "test_*.py"

test-m00:
	@echo "\n$(BOLD)$(BLUE)🚀 [TESTS] Running Module 00 (Starting) unit tests...$(RESET)"
	@$(PYTHON) -m unittest tests/test_module_00.py

test-m01:
	@echo "\n$(BOLD)$(BLUE)🚀 [TESTS] Running Module 01 (Array) unit tests...$(RESET)"
	@$(PYTHON) -m unittest tests/test_module_01.py

norm:
	@echo "\n$(BOLD)$(YELLOW)🛡️ [NORM] Running 42 Norm & Clean Code Auditor...$(RESET)"
	@$(PYTHON) scripts/norm_check.py

compile:
	@echo "\n$(BOLD)$(MAGENTA)⚡ [COMPILE] Verifying Python 3.10 syntax compilation...$(RESET)"
	@$(PYTHON) -m py_compile $$(find python_0_starting python_1_array -name "*.py")
	@echo "$(GREEN)✔ Syntax compilation successful!$(RESET)"

audit: compile norm test
	@echo "\n$(BOLD)$(GREEN)======================================================================$(RESET)"
	@echo "$(BOLD)$(GREEN)   ✅ FULL AUDIT COMPLETE: Code is compliant & ready for evaluation!   $(RESET)"
	@echo "$(BOLD)$(GREEN)======================================================================$(RESET)\n"

clean:
	@echo "\n$(BOLD)$(RED)🧹 [CLEAN] Removing temporary cache files...$(RESET)"
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name ".pytest_cache" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@echo "$(GREEN)✔ Clean completed successfully.$(RESET)\n"
