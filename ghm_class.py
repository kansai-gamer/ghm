from github import Github
import base64
#Githubとのやり取りはすべてモジュール便り
#このサイトを見て「なんか作れるんじゃね?」と思ったのが始まり
#https://dev.classmethod.jp/articles/get-github-info-using-pygithub/

class GhmRepo:
    def __init__(self,token):
        self.g = Github(token)

    def get_repo(self):#リポジトリを取得する、プログラム内で再利用できるようにリストで戻り値を返す
        reponames = []
        #多分元データがリストのはずなんだが、元のリストで返す方法が分からずとりあえず新しくリストを作成して対応
        for repo in self.g.get_user().get_repos(type='owner'):
            reponames.append(repo.name)
        return reponames

    def read_folder_names(self,user,repo):#フォルダを取得する、こっちも拡張性を考えリストで返してるが、現状再利用予定なし
        #ユーザーIDをリポ名を貰ってフォルダ情報を取得
        repo = self.g.get_repo(user+"/"+repo)
        contents = repo.get_contents("")
        filenames = []
        #取得したフォルダ情報をリストで返す
        for content_file in contents:
            filenames.append(content_file.name)
        return filenames

        
    def read_readme(self,user,repo):#README.mdを取得する、これが地味に大変だったよ
        #ユーザーIDをリポ名を貰う
        repo = self.g.get_repo(user+"/"+repo)
        #README.mdを取得、余談だが"README.md"の部分を他のファイル名に書き換えて読み込むことも可能
        #ただしGithubの仕様上容量制限が厳しいので実質テキストファイルしか無理
        contents = repo.get_contents("README.md")
        #base64で帰ってくるのでデコードして返す
        content = base64.b64decode(contents.content)
        return content.decode()
        #参考元 https://www.python.ambitious-engineer.com/archives/2066