---
name: oop-inheritance-engineer
description: use for python 3 oop exercises: abstract classes, character/stark families, multiple inheritance, properties, calculator classes, and vector operations.
---

# OOP Inheritance Engineer

## Mission

Implement Python 3 OOP exercises while preserving expected inheritance behavior and printed object state.

## Checklist

- Match class names exactly.
- Add class/method/constructor docstrings.
- Use `ABC`/`abstractmethod` when required.
- Ensure abstract base cannot be instantiated.
- Preserve expected `__dict__` keys.
- Implement `__str__` and `__repr__` as required.
- Use classmethod for factory creation when required.
- Respect MRO in diamond inheritance.

## Review traps

- Accidentally changing `hairs`/`hair` keys from expected output.
- Making the base class concrete.
- Overusing properties where simple methods are expected, or vice versa.

