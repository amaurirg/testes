from github import Github
from decouple import config
from pprint import pprint

"""
# First create a Github instance:

# using username and password
g = Github("user", "password")

# or using an access token
g = Github("access_token")

# Github Enterprise with custom hostname
g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)
"""

username = config('username')
password = config('password')

github_api = Github(username, password)
user_escopo = github_api.get_user()

lista_repos = [repo.name for repo in user_escopo.get_repos()]

pprint(lista_repos)