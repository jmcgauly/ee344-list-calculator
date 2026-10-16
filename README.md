# EE344 Lab 1: List calculator

Start with a working `add` function. Your tasks are to implement `multiply` using a `for` loop and compare your results with NumPy.

You need a GitHub account, Git, and Python 3.9 or newer. Follow the steps below in order. Copy terminal commands one block at a time.

## 1. Fork this repository on GitHub

1. Sign in and open [junkaiwu925/ee344-list-calculator](https://github.com/junkaiwu925/ee344-list-calculator).
2. Click **Fork** near the top-right corner.
3. Choose your account as the owner. Keep the name **ee344-list-calculator**.
4. Click **Create fork**.

Your fork is your own copy on GitHub. Its address should be `https://github.com/YOUR_USERNAME/ee344-list-calculator`.

## 2. Clone your fork onto your computer

Open Terminal on macOS/Linux, or PowerShell on Windows. Replace `YOUR_USERNAME` below with your GitHub username, then run:

```bash
git clone https://github.com/YOUR_USERNAME/ee344-list-calculator.git
cd ee344-list-calculator
```

**Run all remaining commands from this folder.** It contains `demo.py`, `pyproject.toml`, and `labtools/`.

Check that Git will push to your fork:

```bash
git remote -v
```

The `origin` URL should contain **your username**.

## 3. Create and activate a Python environment

Run **one** of the following blocks for your terminal.

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, open **Command Prompt** in the same repository folder and run:

```bat
.venv\Scripts\activate.bat
```

Keep this terminal open for the rest of the lab. If you open a new terminal, enter the repository folder and run the activation command again.

## 4. Install the package and run it

With the environment active, run:

```bash
python -m pip install -e .
python demo.py
```

Expected output:

```text
Numbers: [1, 2, 3, 4]
Sum: 10
```

`-e .` installs the package in the current folder in editable mode. When you edit its Python files, the next run uses your changes.

The package's `labtools/__init__.py` exposes its functions. In a Python file, you can import them with:

```python
from labtools import add, multiply
```

`add` is ready to use. You will implement `multiply` next.

## 5. Assignment 1: Implement multiplication

**In the terminal**, create a branch for your work:

```bash
git switch -c list-calculator
```

**In your code editor:**

1. Open `labtools/arithmetic.py`. Read the `add` function.
2. Implement `multiply` using a `for` loop. Replace the `NotImplementedError`.
3. Open `demo.py`. Below the existing sum printout, add this line and save both files:

```python
print("Product:", multiply(numbers))
```

**Back in the terminal**, run:

```bash
python demo.py
```

The output should now include `Product: 24`. Change `numbers` in `demo.py` to each input below, save, and run the command again:

| Input | Expected sum | Expected product |
| --- | --- | --- |
| `[1, 2, 3, 4]` | `10` | `24` |
| `[2, 0, 3]` | `5` | `0` |
| `[-2, 3]` | `1` | `-6` |
| `[]` | `0` | `1` |

## 6. Assignment 2: Install and use NumPy

**In the same terminal**, install NumPy into your active environment:

```bash
python -m pip install numpy
```

**In your code editor:**

1. Add `import numpy as np` at the top of `demo.py`.
2. Add print statements for `np.sum(numbers)` and `np.prod(numbers)`. Keep your loop functions and their print statements so you can compare the results.
3. In `pyproject.toml`, replace `dependencies = []` with:

```toml
dependencies = ["numpy"]
```

4. Save both files.

Installing NumPy makes it available now. Listing it in `pyproject.toml` lets someone else install it along with your package. `pip` does not edit that file for you.

**Back in the terminal**, reinstall the package to pick up the dependency change and run the demo:

```bash
python -m pip install -e .
python demo.py
```

Check all four inputs from assignment 1. NumPy's sum and product should match your functions.

## 7. Commit and push your work

**In the terminal**, inspect your changes:

```bash
git status
git diff
```

If `git diff` opens a scrollable view, press `q` to return to the prompt. Then save and upload your changes:

```bash
git add labtools/arithmetic.py demo.py pyproject.toml
git commit -m "Add list multiplication and NumPy comparisons"
git push -u origin list-calculator
```

The push uploads your branch to **your fork**. Git may ask you to authenticate with GitHub.

**On GitHub**, open your fork, choose **Pull requests**, then **New pull request**. Set:

| Field | Value |
| --- | --- |
| Base repository | `YOUR_USERNAME/ee344-list-calculator` |
| Base branch | `main` |
| Head repository | `YOUR_USERNAME/ee344-list-calculator` |
| Compare branch | `list-calculator` |

Check the repository fields: GitHub may initially select the instructor's repository as the base. For this lab, use **your fork** for both repositories.

Click **Create pull request**. Review the changed files with a classmate, then merge it into your fork's `main` branch. After merging, run:

```bash
git switch main
git pull --ff-only origin main
python demo.py
```

## Files in this package

| File | Purpose |
| --- | --- |
| `labtools/arithmetic.py` | Your `add` and `multiply` functions |
| `labtools/__init__.py` | Exposes functions for `from labtools import ...` |
| `demo.py` | Calls the functions and prints their results |
| `pyproject.toml` | Package information and dependencies |
| `.gitignore` | Lists generated files Git should ignore |

## Try `.gitignore`

Run these commands in your active environment. The first creates a generated output file:

```bash
python -c "from pathlib import Path; Path('outputs').mkdir(exist_ok=True); Path('outputs/example.txt').write_text('demo')"
git status --short
git check-ignore outputs/example.txt
```

`git status` should not list `outputs/example.txt`. `git check-ignore` should print its path. The repository also ignores `.venv/`, Python caches, and generated package metadata. Ignore rules do not remove files that Git already tracks.

When you finish using the environment, run `deactivate`.
