# Python Libft

his project is a **Python re-implementation** of selected functions from the [C `libft` library](https://github.com/yahyaeb/libft) I built during my studies at **École 42**.  
It serves as a bridge between **low-level programming in C** and **Python scripting for DevOps**, helping me explore how core algorithms and utilities behave across languages.

## Overview

The goal of this mini-library is to recreate familiar **string and memory manipulation** functions, as well as **character classification** utilities, inspired by their C counterparts.  
Each function is implemented manually without relying on Python’s built-in equivalents, for educational and comparative purposes.

## Implemented Functions

| Category | Functions |
|-----------|------------|
| **Character checks** | `isalpha`, `isdigit`, `isalnum`, `isascii`, `isprint`, `toupper`, `tolower` |
| **String handling** | `strlen`, `strncmp`, `strchr`, `strrchr`, `strlcpy`, `split`, `strnstr` |
| **Memory operations** | `memchr`, `memcmp`, `memset` |
| **Conversion** | `atoi` |


## Example Usage

```python
from atoi import ft_atoi
from strlen import ft_strlen

print(ft_atoi("42"))       # → 42
print(ft_strlen("Hello"))  # → 5
```

## Inspiration

This library is inspired by the C standard libraries and the `libft` project I already completed, aiming to bring similar functionality to Python for educational purposes and practice.
