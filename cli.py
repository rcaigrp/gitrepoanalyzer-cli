import click

@click.group()
def cli():
    """GitRepoAnalyzer CLI tool."""
    pass

@cli.command()
@click.argument('repo_url')
@click.option('--output', default='json', help='Output format (json, yaml, text)')
@click.option('--dry-run', is_flag=True, help='Run in dry-run mode')
def analyze(repo_url, output, dry_run):
    """Analyze the repository for issues."""
    click.echo(f"Analyzing repository: {repo_url}")
    click.echo(f"Output format: {output}")
    click.echo(f"Dry run: {dry_run}")
    
    from analyzer import scan_stale_branches, scan_outdated_dependencies, scan_security_issues
    
    scan_stale_branches(repo_url)
    scan_outdated_dependencies(repo_url)
    scan_security_issues(repo_url)
