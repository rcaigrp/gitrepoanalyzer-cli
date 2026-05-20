import pytest
import subprocess
import sys
import os
from click.testing import CliRunner


def test_criterion_1_cli_entry_point():
    result = subprocess.run(
        [sys.executable, '-m', 'git_repo_analyzer', '--help'],
        capture_output=True,
        text=True,
        cwd='/workspace/projects/GitRepoAnalyzer-CLI',
    )
    assert result.returncode == 0, f'CLI failed: {result.stderr}'


def test_criterion_2_parse_repo_url():
    from git_repo_analyzer import main
    runner = CliRunner()
    result = runner.invoke(main, ['https://github.com/example/repo'])
    assert result.exit_code == 0
    assert 'https://github.com/example/repo' in result.output


def test_criterion_3_parse_output_format():
    from git_repo_analyzer import main
    runner = CliRunner()
    result = runner.invoke(main, ['https://github.com/example/repo', '--output', 'json'])
    assert result.exit_code == 0
    assert 'json' in result.output


def test_criterion_4_parse_dry_run_flag():
    from git_repo_analyzer import main
    runner = CliRunner()
    result = runner.invoke(main, ['https://github.com/example/repo', '--dry-run'])
    assert result.exit_code == 0
    assert 'Dry Run' in result.output or '--dry-run' in result.output.lower()


def test_criterion_5_placeholder_functions():
    import git_repo_analyzer.analyzer as analyzer
    assert hasattr(analyzer, 'scan_stale_branches')
    assert hasattr(analyzer, 'scan_outdated_dependencies')
    assert hasattr(analyzer, 'scan_security_issues')


def test_criterion_6_valid_structure():
    assert os.path.isdir('/workspace/projects/GitRepoAnalyzer-CLI')
    assert os.path.isfile('/workspace/projects/GitRepoAnalyzer-CLI/README.md')
    assert os.path.isfile('/workspace/projects/GitRepoAnalyzer-CLI/project.json')
