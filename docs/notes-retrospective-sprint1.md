# DNA Sequence Analyzer

# Sprint 1 – Notes and Retrospective

**Sprint:** 1
**Objective:** Project Setup & Version Control
**Status:** ✅ Completed

---

# Sprint Goal

Establish the project foundation by:

* Creating the GitHub repository.
* Creating the project folder structure.
* Setting up Git and GitHub integration.
* Making the first commit.
* Pushing the project to GitHub.

---

# Work Completed

* Created the GitHub repository.
* Selected the Python `.gitignore` template.
* Created the project folder structure.
* Added `.gitkeep` files for empty directories.
* Connected the local repository to GitHub.
* Configured Git identity (`user.name` and `user.email`).
* Created the initial commit.
* Pushed the project to GitHub.
* Verified the commit was successfully published.

---

# Git Learning Notes

## 1. Git vs GitHub

| Git                            | GitHub                                     |
| ------------------------------ | ------------------------------------------ |
| Version control software       | Cloud hosting service for Git repositories |
| Tracks project history locally | Stores repositories remotely               |
| Works offline                  | Used for backup and collaboration          |

**Key Learning**

Git manages version history on the local machine, while GitHub stores and shares repositories online.

---

## 2. Repository

A repository contains:

* Source code
* Folder structure
* Documentation
* Complete change history

Repository created:

`dna-sequence-analyzer`

---

## 3. .gitignore

### Purpose

A `.gitignore` file tells Git which files or folders should **not** be tracked.

Examples include:

* Python cache files
* Virtual environments
* Temporary files
* IDE-generated files

For this project, we selected the **Python `.gitignore` template** while creating the repository.

---

## 4. Why Git Ignores Empty Folders

Git tracks **files**, not directories.

An empty folder contains no tracked files, so Git ignores it and it does not appear in Source Control.

---

## 5. Preserving Empty Folders

### Option 1 — `.gitkeep` ✅ (Chosen)

Example:

```text
data/
    .gitkeep

tests/
    .gitkeep
```

`.gitkeep` is **not an official Git feature**. It is a community convention used to ensure empty directories are included in a repository.

**Advantages**

* Lightweight
* Easy to understand
* Can be removed once real files exist

---

### Option 2 — `README.md`

Example:

```text
data/
    README.md
```

A README documents the purpose of the directory.

**Advantages**

* Explains intended contents
* Helpful for collaborators
* Useful in larger or open-source projects

---

### Decision

For Sprint 1, we chose the **`.gitkeep`** approach because the folders are intentionally empty and do not yet require documentation.

---

## 6. Git Identity

Git requires every commit to have an author.

Required configuration:

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### Verification

```bash
git config --global --list
```

### Key Learning

Git identity is separate from logging into GitHub in VS Code. Even if GitHub authentication is complete, Git still requires `user.name` and `user.email` for commits.

---

## 7. Commit

A commit is a snapshot of the project at a specific point in time.

Sprint 1 commit recorded:

* Initial project structure
* Git configuration
* Folder organization

Suggested commit message:

```text
chore: initialize project structure for Sprint 1
```

---

## 8. Push

A commit exists only in the local repository until it is pushed.

```text
Working Folder
      │
      ▼
Local Git Repository
      │
   git push
      │
      ▼
GitHub Repository
```

After pushing, the commit became visible on GitHub.

---

## 9. VS Code GUI vs Git Commands

| VS Code Action      | Git Command               |
| ------------------- | ------------------------- |
| Stage All           | `git add .`               |
| Commit              | `git commit -m "message"` |
| Push / Sync         | `git push origin main`    |
| Status              | `git status`              |
| View Commit History | `git log --oneline`       |

### Key Learning

The VS Code Source Control interface executes standard Git commands behind the scenes.

---

## 10. Branching Strategy

### Sprint 1

Committed directly to **main** because only the initial project structure was created.

```text
main
```

### Sprint 2 Onwards

Every new feature will be developed in its own branch.

```text
main
│
├── feature/file-handler
├── feature/validator
├── feature/dna-analyzer
└── feature/tests
```

This keeps the `main` branch stable while features are developed independently.

---

# Git Concepts Learned

By the end of Sprint 1, I understand:

* Git vs GitHub
* Repository
* `.gitignore`
* Why Git ignores empty folders
* `.gitkeep`
* Commit
* Push
* Git identity (`user.name` and `user.email`)
* VS Code Source Control workflow
* Basic branching strategy

---

# Sprint 1 Retrospective

## What did we build?

* Established the project structure.
* Connected the project to GitHub.
* Created the first version-controlled project baseline.

---

## What did we learn?

### Git

* Git fundamentals
* GitHub workflow
* Repository structure
* Commit lifecycle
* Push workflow
* Empty folder handling
* Git identity configuration

### Development Practices

* Organizing a project before writing code.
* Creating meaningful commits.
* Recording technical learning after each sprint.

---

## Challenges Encountered

### Challenge 1

Empty folders (`data` and `tests`) did not appear in Source Control.

**Cause**

Git ignores empty directories.

**Solution**

Added `.gitkeep` files.

---

### Challenge 2

VS Code prevented commits because Git identity was not configured.

**Cause**

Missing `user.name` and `user.email`.

**Solution**

Configured Git identity and verified the settings before committing.

---

## Improvements for Sprint 2

* Begin using feature branches.
* Continue learning the Git command behind each GUI action.
* Make focused, descriptive commits.
* Continue maintaining sprint notes and retrospectives.
* Implement one complete feature before moving to the next.

---

# Confidence Check

| Skill         | Before Sprint 1 | After Sprint 1                            |
| ------------- | --------------- | ----------------------------------------- |
| Git           | Beginner        | Comfortable with basic workflow           |
| GitHub        | Beginner        | Repository creation, commit and push      |
| VS Code Git   | Beginner        | Comfortable using Source Control          |
| Project Setup | Beginner        | Able to initialize a professional project |

---

# Sprint Outcome

Sprint 1 successfully established the foundation of the **DNA Sequence Analyzer** project. The repository is organized, version controlled, and ready for implementation in Sprint 2.

---

# Personal Reflection

This sprint focused on understanding **why** each step was performed, not just **how** to perform it. Building this foundation will make future development, collaboration, and troubleshooting much easier.

The habits established in Sprint 1—small commits, organized project structure, documenting concepts, and reflecting after each sprint—will continue throughout the project and contribute to building both technical skills and a strong professional portfolio.
