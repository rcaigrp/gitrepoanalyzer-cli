# GitRepoAnalyzer CLI

A Python CLI tool to analyze GitHub repositories for health metrics.

## Goal
Scan GitHub repos for stale branches, outdated dependencies, and generate health reports.

## Acceptance Criteria
1. Accept a GitHub repo URL.
2. Fetch repo data via GitHub API.
3. Identify stale branches.
4. Identify outdated dependencies.
5. Output formatted rich terminal table.
6. Support dry-run and JSON export.

## Installation
pip install click rich pyyaml jsonschema

## Usage
git-repo-analyzer https://github.com/user/repo --dry-run

## Project Status
- Status: Active
- Meetings Held: 0
- Meeting Budget: 5