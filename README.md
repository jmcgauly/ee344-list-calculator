# EE344 Lab 1: List calculator

Start with a working `add` function. Your tasks are to implement `multiply` using a `for` loop and compare your results with NumPy.

You need a GitHub account, Git, and Python 3.9 or newer. Follow the steps below in order. Copy terminal commands one block at a time.

## 1. Set up SSH access to GitHub

Complete this before cloning. SSH lets Git authenticate to GitHub when you clone, push, or pull. Signing in to the GitHub website does not sign your terminal in.

Use **Terminal on macOS/Linux** or **Git Bash on Windows** for this step. You only need to set up the key once per computer and GitHub account. If you already completed this lab's `github-ee344` setup, run the connection test at the end of this step to check it.

### A. Create a key

Use the email associated with your GitHub account in place of `YOUR_EMAIL`:

```bash
mkdir -p ~/.ssh
```

```bash
ssh-keygen -t ed25519 -C "YOUR_EMAIL" -f ~/.ssh/id_ed25519_ee344
```

Enter a passphrase when prompted, then enter it again. If asked to overwrite an existing key, answer **n**. Reuse that key if it is already yours for this account, or choose a different filename and use it throughout these instructions.

### B. Add the public key to GitHub

**On macOS**, copy the public key:

```bash
pbcopy < ~/.ssh/id_ed25519_ee344.pub
```

**On Linux or Windows Git Bash**, display it and copy the entire line:

```bash
cat ~/.ssh/id_ed25519_ee344.pub
```

On GitHub, sign in to the account you will use for this lab. Open **Settings → SSH and GPG keys → New SSH key**. Enter a title such as `EE344 laptop`, choose **Authentication Key**, paste the public key, and click **Add SSH key**.

Upload only the file ending in `.pub`. The file without `.pub` is your private key and stays on your computer.

### C. Tell SSH which key to use

In your text editor, open or create `~/.ssh/config`. Keep any existing entries and add this block near the top, before any broad `Host *` block. If `Host github-ee344` already exists, update that block instead of adding a second one.

```sshconfig
Host github-ee344
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_ee344
    IdentitiesOnly yes
```

`github-ee344` is a local nickname for GitHub that selects this key. It is useful when another SSH key on your computer belongs to a different GitHub account. Save the file, then test:

```bash
ssh -T git@github-ee344
```

If asked to trust the host, compare the fingerprint with [GitHub's published fingerprints](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints) before answering `yes`.

The response should greet **your GitHub username** and say you authenticated successfully. The message that GitHub does not provide shell access is normal. If it names another account, check which account received your public key and which key the config selects.

You may need to enter your key's passphrase for SSH or Git commands. GitHub's [SSH agent instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) explain how to remember it during your session.

References: [create a key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent), [add it to GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account), [test the connection](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection), [choose a key for each account](https://docs.github.com/en/account-and-profile/how-tos/account-management/managing-multiple-accounts).

## 2. Fork this repository on GitHub

1. Sign in and open [junkaiwu925/ee344-list-calculator](https://github.com/junkaiwu925/ee344-list-calculator).
2. Click **Fork** near the top-right corner.
3. Choose your account as the owner. Keep the name **ee344-list-calculator**.
4. Click **Create fork**.

Your fork is your own copy on GitHub. Its address should be `https://github.com/YOUR_USERNAME/ee344-list-calculator`.

## 3. Clone your fork onto your computer

In the same Terminal or Git Bash window, replace `YOUR_USERNAME` below with your GitHub username, then clone **your fork using SSH**:

```bash
git clone git@github-ee344:YOUR_USERNAME/ee344-list-calculator.git
cd ee344-list-calculator
```

**Run all remaining commands from this folder.** It contains `demo.py`, `pyproject.toml`, and `labtools/`.

Check that Git will push to your fork:

```bash
git remote -v
```

Both `origin` lines should start with `git@github-ee344:` and contain **your username**. The `github-ee344` alias uses the SSH key you configured in step 1.

## 4. Create and activate a Python environment

Run **one** of the following blocks for your terminal. On Windows, open **PowerShell** in the cloned repository folder for this step and the rest of the lab.

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

## 5. Install the package and run it

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

## 6. Assignment 1: Implement multiplication

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

## 7. Assignment 2: Install and use NumPy

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

## 8. Commit and push your work

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

The push uploads your branch to **your fork**. If it fails with an authentication or permission error, rerun the SSH test in [step 1](#1-set-up-ssh-access-to-github) and check that `origin` points to your fork as shown in [step 3](#3-clone-your-fork-onto-your-computer), then retry the push. Creating a commit is local, so a failed push does not remove your work.

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
