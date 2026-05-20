import click

@click.command()
@click.argument('repo_url')
@click.option('--output', default='json', help='Output format')
@click.option('--dry-run', is_flag=True, help='Enable dry run mode')
def main(repo_url, output, dry_run):
    print(f'Repository: {repo_url}')
    print(f'Output Format: {output}')
    print(f'Dry Run: {dry_run}')
