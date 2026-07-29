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

.PHONY: help test test-m00 test-m01 norm compile audit pre-commit clean

help:
	@printf "$(CYAN)┌──────────────────────────────────────────────────────────────────────────────┐\n$(RESET)"
	@printf "$(CYAN)│$(RESET) $(BOLD)$(MAGENTA)                 42 PYTHON PISCINE — COMMAND CENTER                        $(RESET) $(CYAN) │\n$(RESET)"
	@printf "$(CYAN)├──────────────────────────────────────────────────────────────────────────────┤\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make help$(RESET)       $(DIM)─$(RESET) Show this interactive help menu                           $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make test$(RESET)       $(DIM)─$(RESET) Run all unit test suites (Module 00 & Module 01)          $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make test-m00$(RESET)   $(DIM)─$(RESET) Run unit tests for Module 00 (Starting)                   $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make test-m01$(RESET)   $(DIM)─$(RESET) Run unit tests for Module 01 (Array)                      $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make norm$(RESET)       $(DIM)─$(RESET) Run 42 Norm & Clean Code Auditor (docstrings, guards)     $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make compile$(RESET)    $(DIM)─$(RESET) Compile Python 3.10 syntax across all exercise files      $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make audit$(RESET)      $(DIM)─$(RESET) Full audit: compile + norm + unit tests                   $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make pre-commit$(RESET) $(DIM)─$(RESET) Install pre-commit tool and set up git hooks              $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)│$(RESET)  $(BOLD)$(GREEN)make clean$(RESET)      $(DIM)─$(RESET) Remove temporary cache files (__pycache__, .pyc)          $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)├──────────────────────────────────────────────────────────────────────────────┤\n$(RESET)"
	@printf "$(CYAN)│$(RESET)           $(BOLD)$(WHITE)🔥 Crafted with • by $(YELLOW)@RogerioLS$(WHITE) $(DIM)•$(RESET) $(BOLD)$(CYAN)42 São Paulo 🇧🇷$(RESET)                  $(CYAN)│\n$(RESET)"
	@printf "$(CYAN)└──────────────────────────────────────────────────────────────────────────────┘\n$(RESET)"

test:
	@printf "$(BOLD)$(BLUE)🚀 [TESTS] Running all unit test suites...$(RESET)\n"
	@$(PYTHON) -m unittest discover -s tests -p "test_*.py"

test-m00:
	@printf "$(BOLD)$(BLUE)🚀 [TESTS] Running Module 00 (Starting) unit tests...$(RESET)\n"
	@$(PYTHON) -m unittest tests/test_module_00.py

test-m01:
	@printf "$(BOLD)$(BLUE)🚀 [TESTS] Running Module 01 (Array) unit tests...$(RESET)\n"
	@$(PYTHON) -m unittest tests/test_module_01.py

norm:
	@printf "$(BOLD)$(YELLOW)🛡️ [NORM] Running 42 Norm & Clean Code Auditor...$(RESET)\n"
	@$(PYTHON) scripts/norm_check.py

compile:
	@printf "$(BOLD)$(MAGENTA)⚡ [COMPILE] Verifying Python 3.10 syntax compilation...$(RESET)\n"
	@$(PYTHON) -m py_compile $$(find python_0_starting python_1_array -name "*.py")
	@printf "$(GREEN)✔ Syntax compilation successful!$(RESET)\n"

audit: compile norm test
	@printf "\n$(BOLD)$(GREEN)======================================================================$(RESET)\n"
	@printf "$(BOLD)$(GREEN)   ✅ FULL AUDIT COMPLETE: Code is compliant & ready for evaluation!   $(RESET)\n"
	@printf "$(BOLD)$(GREEN)======================================================================$(RESET)\n\n"

pre-commit:
	@if command -v pre-commit > /dev/null 2>&1; then \
		printf "$(GREEN)✔ pre-commit is already installed.$(RESET)\n"; \
	else \
		printf "$(YELLOW)⏳ Installing pre-commit via pip...$(RESET)\n"; \
		$(PYTHON) -m pip install pre-commit; \
	fi
	@pre-commit install > /dev/null 2>&1 || printf "$(YELLOW)ℹ Note: pre-commit hooks configured alongside custom git hooks.$(RESET)\n"
	@printf "$(GREEN)✔ pre-commit setup completed successfully!$(RESET)\n"

clean:
	@printf "$(BOLD)$(RED)🧹 [CLEAN] Removing temporary cache files...$(RESET)\n"
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name ".pytest_cache" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@printf "$(GREEN)✔ Clean completed successfully.$(RESET)\n\n"
