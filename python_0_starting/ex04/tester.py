import subprocess
import sys
from pathlib import Path


SCRIPT = Path(__file__).with_name("whatis.py")


def run_case(args):
	"""Run whatis.py with args and return captured stdout."""
	result = subprocess.run(
		[sys.executable, str(SCRIPT), *args],
		capture_output=True,
		text=True,
		check=False,
	)
	return result.stdout.strip()


def test_case(name, args, expected_output):
	output = run_case(args)
	ok = output == expected_output
	status = "OK" if ok else "FAIL"
	print(f"[{status}] {name}")
	if not ok:
		print(f"  expected: {expected_output!r}")
		print(f"  got     : {output!r}")
	return ok


def main():
	tests = [
		("sem argumento", [], ""),
		("14 deve ser par", ["14"], "I'm Even."),
		("-5 deve ser impar", ["-5"], "I'm Odd."),
		("0 deve ser par", ["0"], "I'm Even."),
		(
			"argumento nao inteiro",
			["Hi!"],
			"AssertionError: argument is not an integer",
		),
		(
			"mais de um argumento",
			["13", "5"],
			"AssertionError: more than one argument are provided",
		),
	]

	passed = 0
	for name, args, expected in tests:
		if test_case(name, args, expected):
			passed += 1

	total = len(tests)
	print(f"\nResultado: {passed}/{total} testes passaram")
	sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
	main()
