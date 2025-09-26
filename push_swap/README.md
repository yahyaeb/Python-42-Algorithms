# push_swap

A Python implementation of the **push_swap** project, which I originally implemented in [C](https://github.com/yahyaeb/push_swap). The goal is to sort a stack of integers using a limited set of stack operations, optimizing for the least number of moves.

## Features

- Efficient sorting algorithm using only allowed stack operations.
- Handles input validation and error management.
- Designed for performance and clarity.

## Allowed Commands

- `sa` / `sb` / `ss`: Swap the first two elements of stack A/B/both.
- `pa` / `pb`: Push the top element from stack B/A to stack A/B.
- `ra` / `rb` / `rr`: Rotate stack A/B/both upwards.
- `rra` / `rrb` / `rrr`: Rotate stack A/B/both downwards.

## Implemented Sorting Functions

To meet the project requirements, three sorting functions are provided:

- `sort_three()`: Sorts 3 elements or fewer.
- `sort_five()`: Sorts 5 elements or fewer (calls `sort_three()` internally).
- `sort_large()`: Sorts any number of elements by dividing them into chunks and merging them efficiently.

Project requirements specify:
- 3 elements: Must be sorted in fewer than 3 operations.
- 5 elements: Must be sorted in fewer than 12 operations.

## Example Walkthrough of the Algorithm

**Initial State:**

```
Stack A: 3  8  20  193  39  0  199  38  24
Stack B: (empty)
```

**Step 1: Divide Stack A into Chunks**

The input elements are divided into smaller chunks.

**Step 2: Push Elements from Stack A to Stack B**

_Chunk 1: 0  3  8_

Push 0, 3, and 8 to Stack B:

```
Stack A: 20  193  39  199  38  24
Stack B: 8  3  0
```

Continue pushing all elements from subsequent chunks to Stack B until Stack A is empty.

**Step 3: Push Elements from Stack B to Stack A**

Push the largest values first:

```
Stack A: 0  3  8  20  24  38  39  193  199
Stack B: (empty)
```

## Usage

Since the file includes the shebang `#!/usr/bin/env python3`, you can call the program directly:

```bash
./push_swap.py [list of integers]
```

`tester`
I have added two testers, one for mac and one for linux. that will confirm if the results is correct. in order to use it, you will need to run
./push_swap 3 2 1 | ./checker_mac 3 2 1
and it will check if the results are correct.

`Note:`
make sure you give the executable permission to the checker.
Pass each number as a separate CLI argument:
./push_swap.py 3 2 1 6 5 8
Do not use quotes or a single string.

**Example:**

```bash
./push_swap.py 3 2 1 6 5 8
```
