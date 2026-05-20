import pytest
from click.testing import CliRunner
from git_repo_analyzer.cli import analyze
from git_repo_analyzer.analyzer import scan_stale_branches, scan_outdated_dependencies, scan_security_issues

def test_criterion_1_cli_runs():
    runner = CliRunner()
    result = runner.invoke(analyze, ['https://github.com/example/repo'])
    assert result.exit_code == 0

def test_criterion_2_parse_repo_url():
    runner = CliRunner()
    result = runner.invoke(analyze, ['https://github.com/example/repo'])
    assert 'https://github.com/example/repo' in result.output

def test_criterion_3_parse_output_format():
    runner = CliRunner()
    result = runner.invoke(analyze, ['https://github.com/example/repo', '--output', 'csv'])
    assert result.exit_code == 0

def test_criterion_4_parse_dry_run():
    runner = CliRunner()
    result = runner.invoke(analyze, ['https://github.com/example/repo', '--dry-run'])
    assert result.exit_code == 0

def test_criterion_5_placeholder_functions():
    assert callable(scan_stale_branches)
    assert callable(scan_outdated_dependencies)
    assert callable(scan_security_issues)

def test_criterion_6_project_structure():
    import git_repo_analyzer
    assert hasattr(git_repo_analyzer, '__file__')
