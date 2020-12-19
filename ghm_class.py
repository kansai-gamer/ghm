from github import Github
import base64

class GhmRepo:
    def __init__(self,token):
        self.token = token

    def get_repo(self):
        g = Github(self.token)
        reponames = []
        for repo in g.get_user().get_repos(type='owner'):
            reponames.append(repo.name)
        return reponames

    def read_folder_names(self,user,repo):
        g = Github(self.token)
        repo = g.get_repo(user+"/"+repo)
        contents = repo.get_contents("")
        filenames = []
        for content_file in contents:
            filenames.append(content_file.name)
        return filenames

        
    def read_readme(self,user,repo):
        g = Github(self.token)
        repo = g.get_repo(user+"/"+repo)
        contents = repo.get_contents("README.md")
        content = base64.b64decode(contents.content)
        return content.decode()