import os
import unittest
import vcr
from gitrepos import GitRepos

class GitReposTest(unittest.TestCase):
    def setUp(self):
        self.test_api_token = os.environ.get("GITHUB_API_TOKEN", "ABC123")

    @vcr.use_cassette(
        'fixtures/cassettes/test_list_for_user.yml',
        filter_query_parameters=['access_token']
    )
    def test_list_for_user(self):
        repos = GitRepos(self.test_api_token)
        self.assertTrue('nwalsdev' in repos.list_for_user('jakesen'))
