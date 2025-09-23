# get_next_line (Python Version)

**Goal:**  
Implement a function and command-line tool that reads and returns a single line from a file, one at a time—mirroring the classic “get_next_line” project (originally written in C), which can be found [here](https://github.com/yahiaelboukili/get_next_line).

---

## What You’ll Learn

- How file input/output (I/O) is handled in Python versus C
- The ease and power of Python generators for simple, memory-efficient reading
- The simplicity of error handling and resource management in a high-level language
- Key differences in code structure and expressiveness between C and Python

---

## Key Differences (C vs. Python)

- In Python, `with ... as file:` automatically opens and closes the file, ensuring safe resource management without manual calls to `close()`.
- `for` loops over files are simpler in Python; no manual buffer or line parsing is required.
- `rstrip('\n')` in Python removes the newline at the end of each line (somewhat like `ft_strtrim` in C, but only on the right side).
- CLI arguments (`argv`) are supported in Python by importing the `sys` library.


## Project Structure

- `GNL.py` — Defines a generator function `get_next_line()` that yields lines from a file object, plus a simple CLI to demo usage.

---

## How to Use

**Command-line:**  
```bash
python GNL.py somefile.txt
```
You can use the existing `test.txt` as a sample file for testing.
