import click
from git_repo_analyzer.analyzer import get_repo_metadata, get_branches, get_dependencies

@click.command()
@click.argument('repo_url')
@click.option('--output', default='text', help='Output format')
@click.option('--dry-run', is_flag=True, help='Dry run mode')
def cli(repo_url, output, dry_run):
    """Analyze a GitHub repository."""
    click.echo(f"Analyzing repository: {repo_url}")
    
    if dry_run:
        click.echo("Dry run mode enabled.")
        return

    metadata = get_repo_metadata(repo_url)
    if metadata:
        click.echo(f"Name: {metadata.get('full_name')}")
        click.echo(f"Stars: {metadata.get('stargazers_count')}")
    
    branches = get_branches(repo_url)
    click.echo(f"Branches: {len(branches)}")
    
    deps = get_dependencies(repo_url)
    click.echo(f"Dependencies: {deps}")

if __name__ == '__main__':
    cli()
