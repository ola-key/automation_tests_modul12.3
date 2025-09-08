import requests

class GitHub:

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body
    
    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name}
        )
        body = r.json()

        return body
    
    

    BASE_URL = 'https://api.github.com'

    def get_user(self, username):
        r = requests.get(f'{self.BASE_URL}/users/{username}')
        return r.json()

    def search_repo(self, name):
        r = requests.get(f'{self.BASE_URL}/search/repositories', params={'q': name})
        return r.json()

    def get_emojis(self):
        r = requests.get(f'{self.BASE_URL}/emojis')
        return r.json()

    def get_commits(self, owner, repo):
        r = requests.get(f'{self.BASE_URL}/repos/{owner}/{repo}/commits')
        return r.json()    
    