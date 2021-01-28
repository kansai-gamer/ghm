from github import Github
import base64
# Githubとのやり取りはすべて PyGithub 依存

class GhmRepo(Exception):
    def __init__(self,token):
        self.g = Github(token)

    def get_repo(self):
        """
        リポジトリを取得しリストで返り値を返す
        """
        reponames = []
        #元データがリストのはずだが、元のリストで返す方法が分からず新しくリストを作成して対応
        try:

            for repo in self.g.get_user().get_repos(type='owner'):
                #　　　　　　　　　　 ↓nemeをつけると名前のみの情報で返してくれる（理想通りに返してくれる）
                reponames.append(repo.name)
            return reponames
        except :
            pass

    def read_folder_names(self,user,repo):
        """
        フォルダを取得しリストで返す
        """
        #ユーザーIDとリポ名を貰って、モジュールが扱える形式へくっつける
        repo = self.g.get_repo(user+"/"+repo)
        contents = repo.get_contents("")
        filenames = []
        #取得したフォルダ情報をリストで返す
        for content_file in contents:
            filenames.append(content_file.name)
        return filenames

        
    def read_readme(self,user,repo):
        """
        README.mdを取得しbase64エンコードで返り値を返す
        """
        #ユーザーIDとリポ名を貰う
        repo = self.g.get_repo(user+"/"+repo)
        #README.mdを取得、余談だが"README.md"の部分を他のファイル名に書き換えて読み込むことも可能
        #ただしこの方法だとGithubの仕様上容量制限が厳しいので実質テキストファイルしか無理
        contents = repo.get_contents("README.md")
        #base64で帰ってくるのでデコードして返す
        content = base64.b64decode(contents.content)
        return content.decode()
        #参考元 https://www.python.ambitious-engineer.com/archives/2066

    def get_issues(self,user,repo):
        """
        issuesのタイトルを取得しリストで戻り地を返す
        """
        repo = self.g.get_repo(user+"/"+repo)
        issues = []
        for issue in repo.get_issues(state='open'):
            #ここはtitleで取ってこれる
            issues.append(issue.title)
        return issues

    def get_branch(self,user,repo):
        """
        ブランチを取得しリストで返り値を返す。
        """
        branchs = []
        repo = self.g.get_repo(user+"/"+repo)
        for branch in repo.get_branches():
            branchs.append(branch.name)
        return branchs
        #参考元 https://qiita.com/yshr10ic/items/a416ba6fbea7637be552