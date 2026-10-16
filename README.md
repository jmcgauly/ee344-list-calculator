# EE344 Lab 1: List calculator

A small calculator for lists. Learn how to install a Python package, add a function, install a library, and share changes with Git.

## Get your own copy

Open [the starter on GitHub](https://github.com/junkaiwu925/ee344-list-calculator) and choose **Use this template → Create a new repository**. Then clone your repository and enter its directory:

```bash
git clone <your-repository-url>
cd <your-repository-name>
```

Replace the values in angle brackets with your repository's URL and name.

## Set up the environment

Run these commands from the repository's root directory:

```bash
python -m venv .venv
```

If your system uses `python3` instead of `python`, use `python3 -m venv .venv` for this step.

Activate the environment:

| Terminal | Command |
| --- | --- |
| macOS / Linux | `source .venv/bin/activate` |
| Windows PowerShell | `.venv\Scripts\Activate.ps1` |
| Windows Command Prompt | `.venv\Scripts\activate.bat` |

Then install this package and run the example:

```bash
python -m pip install -e .
python demo.py
```

The example prints `10` as the sum of `[1, 2, 3, 4]`. The `-e` means **editable**: edits to the package are available without reinstalling it after every change. Use `deactivate` when you are done working.

## Find your way around

```text
.
├── README.md
├── pyproject.toml       # Package name, build settings, and dependencies
├── .gitignore          # Files Git should ignore
├── demo.py             # Run the calculator
└── labtools/
    ├── __init__.py      # Makes functions easy to import
    └── arithmetic.py    # Function implementations
```

`__init__.py` exposes the functions, so another script can write:

```python
from labtools import add, multiply
```

## Assignment 1: Multiply a list

First, create a branch for your work:

```bash
git switch -c list-calculator
```

1. Read `add` in `labtools/arithmetic.py`. It adds all the numbers using a `for` loop.
2. Implement `multiply` in the same file using a `for` loop. Replace the `NotImplementedError`.
3. Update `demo.py` to call and print both functions.
4. Run `python demo.py` and check these cases:

| Input | `add` | `multiply` |
| --- | --- | --- |
| `[1, 2, 3, 4]` | `10` | `24` |
| `[2, 0, 3]` | `5` | `0` |
| `[-2, 3]` | `1` | `-6` |
| `[]` | `0` | `1` |

## Assignment 2: Use NumPy

You can install additional libraries into your active environment:

```bash
python -m pip install numpy
```

1. In `demo.py`, import NumPy with `import numpy as np`.
2. Use `np.sum(numbers)` and `np.prod(numbers)` directly in the demo to calculate the same results. Keep your loop implementations in `arithmetic.py`.
3. Print the NumPy results alongside your functions' results and compare them for the inputs above.
4. In `pyproject.toml`, change `dependencies = []` to `dependencies = ["numpy"]`.

Installing a library makes it available in your environment. Recording it in `pyproject.toml` lets a teammate install it with the package. **pip does not update this file automatically.** Run `python -m pip install -e .` again to check the updated package setup.

## Review and share your changes

```bash
git status
git diff
git add labtools/arithmetic.py demo.py pyproject.toml
git commit -m "Add list multiplication and NumPy comparisons"
git push -u origin list-calculator
```

On GitHub, open a pull request from `list-calculator` into `main`. In the team demo, a teammate reviews the changes before the pull request is merged. After the merge, update your local copy:

```bash
git switch main
git pull
```

## What does .gitignore do?

The repository ignores `.venv/`, Python caches, generated package metadata, build files, and `outputs/`. These files can be recreated and do not belong in a commit.

Try creating `outputs/example.txt`, then run `git status`: the generated file will not appear as an untracked file. An ignore rule **does not stop tracking a file that is already committed**.
