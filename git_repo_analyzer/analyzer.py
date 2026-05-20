import requests

def parse_repo_url(repo_url):
    """Parse repository URL to owner and repo name."""
    if repo_url.startswith('https://'):
        parts = repo_url.strip('/').split('/')
        owner = parts[-2]
        repo = parts[-1]
    else:
        parts = repo_url.split('/')
        owner = parts[0]
        repo = parts[1]
    return owner, repo

def get_repo_metadata(repo_url):
    """Fetch repository metadata from GitHub API."""
    owner, repo = parse_repo_url(repo_url)
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_branches(repo_url):
    """Fetch list of branches."""
    owner, repo = parse_repo_url(repo_url)
    url = f"https://api.github.com/repos/{owner}/{repo}/branches"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []

def get_dependencies(repo_url):
    """Check for dependency files."""
    owner, repo = parse_repo_url(repo_url)
    url = f"https://api.github.com/repos/{owner}/{repo}/contents"
    response = requests.get(url)
    if response.status_code == 200:
        files = response.json()
        dep_files = [f['name'] for f in files if 'requirements' in f['name'] or 'package' in f['name']]
        return dep_files
    return []
