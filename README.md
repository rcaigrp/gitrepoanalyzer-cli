# GitRepoAnalyzer-CLI

A Python CLI tool to analyze GitHub repositories for stale branches, outdated dependencies, and security issues.

## Goal
Scan repositories and report findings.

## Acceptance Criteria
1. CLI entry point runs successfully via `python -m git_repo_analyzer`.
2. Parses repository URL argument.
3. Parses output format argument.
4. Parses dry-run mode flag.
5. Contains placeholder functions for scanning stale branches, outdated dependencies, and security issues.
6. Project structure is valid and runnable.

## Installation
pip install click

## Usage
python -m git_repo_analyzer analyze https://github.com/example/repo --output json --dry-run