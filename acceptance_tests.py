import unittest
import responses

class TestAnalyzer(unittest.TestCase):
    @responses.activate
    def test_parse_repo_url_https(self):
        from git_repo_analyzer.analyzer import parse_repo_url
        owner, repo = parse_repo_url('https://github.com/user/repo')
        self.assertEqual(owner, 'user')
        self.assertEqual(repo, 'repo')

    @responses.activate
    def test_parse_repo_url_short(self):
        from git_repo_analyzer.analyzer import parse_repo_url
        owner, repo = parse_repo_url('user/repo')
        self.assertEqual(owner, 'user')
        self.assertEqual(repo, 'repo')

    @responses.activate
    def test_get_repo_metadata(self):
        from git_repo_analyzer.analyzer import get_repo_metadata
        responses.add(
            responses.GET,
            "https://api.github.com/repos/user/repo",
            json={"full_name": "user/repo", "stargazers_count": 100}
        )
        result = get_repo_metadata('https://github.com/user/repo')
        self.assertEqual(result['stargazers_count'], 100)

    @responses.activate
    def test_get_branches_empty(self):
        from git_repo_analyzer.analyzer import get_branches
        responses.add(
            responses.GET,
            "https://api.github.com/repos/user/repo/branches",
            json=[]
        )
        result = get_branches('https://github.com/user/repo')
        self.assertEqual(result, [])

    @responses.activate
    def test_get_dependencies(self):
        from git_repo_analyzer.analyzer import get_dependencies
        responses.add(
            responses.GET,
            "https://api.github.com/repos/user/repo/contents",
            json=[{"name": "requirements.txt"}, {"name": "README.md"}]
        )
        result = get_dependencies('https://github.com/user/repo')
        self.assertIn('requirements.txt', result)
