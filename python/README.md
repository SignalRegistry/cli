# Python Language API Interface for Signal Registry Platform

## Project Setup From Scratch

These are the exact steps used to initialize this repository, in case you need to
recreate or re-initialize the project without external assistance.

### 1. Create the package layout

```
cnf/
├── pyproject.toml
├── README.md
├── .gitignore
├── src/
│   └── SignalRegistry/
│       ├── __init__.py
│       ├── core.py
│       └── cli.py
└── tests/
    └── test_core.py
```

### 2. Configure `pyproject.toml`

Define the PyPI project name, console script entry point, and git repository URL:

```toml
[build-system]
requires = ["setuptools>=68.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "SignalRegistry"
version = "0.0.1"
description = "Signal Registry Platform Python Interface"
readme = "README.md"
requires-python = ">=3.9"
license = { text = "MIT" }
authors = [{ name = "Hüseyin YİĞİT" }]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = []

[project.urls]
Repository = "https://github.com/SignalRegistry/cli.git"

[project.scripts]
SignalRegistryCli = "SignalRegistry.cli:main"

[project.optional-dependencies]
test = ["pytest"]

[tool.setuptools.packages.find]
where = ["src"]

```

### 3. Create a virtual environment and install the package

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -e ".[test]"
```

On bash-like shells (Git Bash, WSL, macOS/Linux) use `.venv/Scripts/python`
(Windows) or `.venv/bin/python` (macOS/Linux). On PowerShell, activate the
environment first so `pytest` and the CLI script resolve on `PATH`:

```powershell
.venv\Scripts\Activate.ps1
pytest -v
SignalRegistryCli
```

### 4. Run the tests

```bash
.venv/Scripts/python -m pytest -v
```

### 5. Verify the CLI

```bash
.venv/Scripts/SignalRegistryCli
```

Expected output: "Hello, Signal Registry!"

### 6. Initialize git and connect the remote

```bash
git init
git remote add origin https://github.com/SignalRegistry/cli.git
git branch -M main
git add -A
git commit -m "Initial commit: SignalRegistry package scaffold"
```

### 7. Push to GitHub (when ready)

```bash
git push -u origin main
```

### 8. Publish to PyPI (when ready)

```bash
.venv/Scripts/python -m pip install build twine
.venv/Scripts/python -m build
.venv/Scripts/python -m twine upload dist/*
```