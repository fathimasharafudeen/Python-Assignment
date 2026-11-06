# Python Assignment 2: Data Structures – List, Dictionary, Set & Conditional Statements

## Overview
This project contains solutions for Python Assignment 2, covering:

- **Lists**: creation, modification, and access
- **Dictionary**: creation, access, update, and the `keys()`, `values()`, `items()` methods
- **Sets**: duplicate removal, immutability of indexing, union and intersection
- **Conditional Statements**: a performance category program using `if`, `elif`, `else`

## Requirements
- Python 3.x
- No external libraries

## How to Run
```bash
python Assignment_02_Data_structures.py
```
The last part asks for a score (`Enter your score (0 to 10):`).

## Contents

### 1. Lists
`age_list = [24, 25, 26, 27, 28]` and `name_list` with five names.

| Task | Method |
|------|--------|
| Add "Yazhini" at the end | `append()` |
| Insert 30 at index 2 | `insert(2, 30)` |
| Remove "Yazhini" | `remove()` |
| Remove last element of `age_list` | `pop()` |
| Add `[29, 30, 26]` | `extend()` |
| Sort in descending order | `sort(reverse=True)` |
| Max, min, sum of ages | `max()`, `min()`, `sum()` |

Final `age_list` after all steps: `[30, 30, 29, 27, 26, 26, 25, 24]` (max 30, min 24, sum 217).

Accessing `name_list`: first element `[0]`, last element `[-1]`, index 2 to 4 `[2:5]`, reverse `[::-1]`.

### 2. Dictionary
`student_marks` maps five student names to marks (0 to 100).

- Access a mark: `student_marks["Kiran"]`
- Add "Janani" with 80: `student_marks["Janani"] = 80`
- Update an existing student's mark to 82: `student_marks["Arun"] = 82`
- Print keys, values and pairs: `keys()`, `values()`, `items()`

### 3. Sets
- `my_set = {'a','e','i','o','u','a','a','i'}` gives `{'a','e','i','o','u'}`.
  Sets store only **unique** values and are **unordered**, so duplicates are removed and the print order can change.
- `my_set[4] = 's'` raises `TypeError: 'set' object does not support item assignment`.
  Sets have no index, so items cannot be accessed or changed by position. Use `add()` to insert a value.
- `set1 = {1, 3, 5, 7, 9}` and `set2 = {2, 3, 5, 8, 10}`:
  - Union (`|`): `{1, 2, 3, 5, 7, 8, 9, 10}`
  - Intersection (`&`): `{3, 5}`

### 4. Performance Category Program

| Score | Category |
|-------|----------|
| Greater than 7 | Above Average |
| 4 to 7 (inclusive) | Average |
| Less than 4 | Below Average |

Scores outside 0 to 10 show an "Invalid score" message.

**Sample output**
```
Enter your score (0 to 10): 7
Average: Good effort! Keep practicing, there's room for improvement.
```

## Key Concepts
- `append()` adds at the end, `insert()` adds at a chosen index.
- `remove()` deletes by value, `pop()` deletes by position (last by default).
- Dictionary keys are unique; assigning to an existing key updates it, a new key adds it.
- Sets remove duplicates and do not support indexing.
- In an `if/elif/else` chain, conditions are checked from top to bottom and the first match runs.

## Author
Your Name
