# Project Notes

A log of what I built, what broke, and what I learned, one entry per session.

---

## Phase 0: Setup (13 Oct 2026)

### What I built
- Created the GitHub repo `python-chess-game` (public, with a README and the Python .gitignore).
- Installed Git on Windows and cloned the repo with `git clone`.
- Created the project files: `chess_logic.py`, `main.py`, `test_chess.py`, `NOTES.md`.
- Set up a virtual environment (`python -m venv venv`) and installed `pygame-ce` and `pytest`.
- Saved dependencies to `requirements.txt`.
- Installed VS Code and selected the venv as the Python interpreter.
- Made my first commit and pushed it to GitHub.

### What broke and how I fixed it
1. `git` not recognized in PowerShell. Git wasn't installed yet. Installed Git for Windows, reopened the terminal, and it worked.
2. `pip install pygame` failed with "Failed to build wheel". I'm on Python 3.14, which pygame has no pre-built installer for. Fixed by installing `pygame-ce` instead. The code still uses `import pygame`.
3. Stray file `requirements.txtpython` was created by a typo. Deleted it with `Remove-Item` and re-saved requirements with `pip freeze | Out-File -Encoding utf8 requirements.txt`.
4. VS Code didn't show the venv interpreter at first. Opened the project folder with `code .`, then selected the interpreter. It now shows `venv (3.14.7)` at the bottom.

### What I learned
- Git has a local copy and a remote copy on GitHub. Nothing shows on GitHub until I run `git push`.
- The commit cycle: `git status`, `git add`, `git commit -m`, `git push`.
- A virtual environment keeps this project's packages separate, and `.gitignore` keeps `venv/` out of the repo.
- A new terminal is needed after installing a program so it can find it.

### What I still don't understand
- (Write your own questions here.)

### Next session goal
- Phase 1: represent the board as an 8x8 list of lists and print it in the terminal.

---

## Session template (copy for each new entry)

## Phase X: Title (date)

### What I built
-

### What broke and how I fixed it
-

### What I learned
-

### What I still don't understand
-

### Next session goal
-