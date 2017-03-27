import requests
import json

class GitRepos(object):
    def __init__(self, oauth_token):
        self.oauth_token = oauth_token

    def list_for_user(self, username):
        request_url = "https://api.github.com/users/%s/repos" % username
        request_url += "?access_token="+self.oauth_token
        response = requests.get(request_url)
        if response.status_code == 200:
            return [repo.get('name') for repo in json.loads(response.content)]
        else:
            raise Exception(response.content)

