# Security Policy

## Overview

This repository contains learning projects for the **42 Piscine Python for Data Science**. We take code quality, safety, and responsible disclosure seriously.

---

## Supported Versions

Only the active Python version defined by the 42 Piscine curriculum is officially supported for security updates and exercise validation:

| Version | Supported |
| ------- | --------- |
| Python 3.10.x | :white_check_mark: Yes |
| Python < 3.10 | :x: No |

---

## Security Best Practices in this Repository

When contributing or reviewing code in this repository, ensure the following security standards are met:

1. **No Hardcoded Credentials or Secrets:**
   - Never commit API keys, tokens, passwords, or personal credentials.
   - Use environment variables or `.env` files (ensuring they are listed in `.gitignore`).

2. **Safe Input Validation & Error Handling:**
   - Validate and sanitize input data (CLI arguments, file paths, user inputs).
   - Prevent arbitrary command execution or unsafe file path traversals.
   - Handle exceptions gracefully without leaking sensitive stack traces or environment details.

3. **Dependency Integrity:**
   - Prefer Python's Standard Library whenever possible.
   - Keep external dependencies (NumPy, Pillow, Matplotlib, pandas, etc.) updated to versions free of known CVEs.

4. **Environment Isolation:**
   - Avoid running untrusted code with root/administrator privileges.
   - Use virtual environments (`venv` or `conda`) to isolate dependencies.

---

## Reporting a Vulnerability

If you discover a security vulnerability or accidental exposure of sensitive data within this repository, please report it responsibly:

1. **Do NOT open a public GitHub issue.**
2. Send an email describing the vulnerability to the repository owner or submit a private security advisory via GitHub.
3. Include detailed steps to reproduce the issue, along with any relevant code snippets or logs.

We appreciate your effort in keeping this learning repository secure and reliable.
