import os
import subprocess
import sys
from ghm_class import GhmRepo

#ファイルが存在するかの確認
if not os.path.isfile("gh_token.txt"):
    #ユーザーIDも必要なので同じファイルに格納する
    #一旦リストにしてから書き込み
    write = []
    write.append(input("pls type your Github ID:"))
    write.append(input("pls type your Github token:"))
    with open("gh_token.txt", mode="w", encoding="utf-8") as f:
        for token_and_user in write:
            f.write(token_and_user+"\n")

with open("gh_token.txt", mode="r", encoding="utf-8") as f:
    #ファイルをリストにして取得
    token = f.readlines()
    #インスタンス生成
    ghm = GhmRepo(token[1].strip())
    #                       ↑改行コードの削除

print("welcome to Github Manager")
#デバッグ用 ID読み取り確認
# print(token[0].strip())
#デバッグ用 トークン読み取り確認
#print(token[1].strip())

#あとで戻ってこれるように関数化、先生のアドバイスを参考
def Listen_repo(ghm):
    """
    リポジトリ選択
    """

    while True:

        try:
            print("pls select to repo")
            #こう書くと数字付きで出せるとクラスメイトにアドバイス貰ったので参考にしました。
            for number, repos in enumerate(ghm.get_repo()):
                print(number + 1, ":", repos)
            user_type_repo = input("waiting:")
            print("test print")
            print(user_type_repo)
        except :
            print("\033[1m" + "pls check token or id\033[0m")
            #確か1でエラー終了扱い
            sys.exit(1)

        #↓ユーザーの入力文章が数値かどうかの判定これもクラスメイト（ｒｙ
        if user_type_repo.isdecimal():
            user_type_repo_int = int(user_type_repo)
            #リポ選択で範囲外を入力していないかの確認
            if user_type_repo_int <= len(ghm.get_repo()):
                return user_type_repo_int
            else:#先生からのアドバイスのおかげで正しく太文字に出来ました。
                print("\033[1m" + "Out of range\033[0m")
        else:
            print("\033[1m" + "pls type number\033[0m")

def Function_selection(user_type_repo_int):
    """
    機能選択
    """
    while True:

        print("pls select")
        options = ["clone", "Read README.md", "View folder", "View branch", "View Issue"]
        #今後機能追加しても絶対最後になるようにappendで追加
        options.append("back to select repo")
        for number, option in enumerate(options):
            print(number + 1, ":", option)
        user_type_option = input("waiting:")
        if user_type_option.isdecimal():
            user_type_option_int = int(user_type_option)
            
        else:
            print("\033[1m" + "pls type number\033[0m")
            continue

        if user_type_option_int == 1:
            clone(user_type_repo_int)

        elif user_type_option_int == 2:#クラスへファイルから読み込んだトークン＆ユーザーが選択したリポ名を投げてREADME.mdの内容が帰ってきてる
            print(ghm.read_readme(token[0].strip(),ghm.get_repo()[user_type_repo_int - 1]))

        elif user_type_option_int == 3:#ここはフォルダ情報が返ってきてる
            print(ghm.read_folder_names(token[0].strip(),ghm.get_repo()[user_type_repo_int - 1]))

        elif user_type_option_int == 4:#ブランチ情報を表示
            print(ghm.get_branch(token[0].strip(),ghm.get_repo()[user_type_repo_int - 1]))

        elif user_type_option_int == 5:#issues情報を表示
            print(ghm.get_issues(token[0].strip(),ghm.get_repo()[user_type_repo_int - 1]))

        elif user_type_option_int == 6:#定義した関数を呼び出してリポジトリ選択へ戻る
            user_type_repo_int = Listen_repo(ghm)

        else:
            print("\033[1m" + "Out of range\033[0m")

def clone(user_type_repo_int):
    """
    Git cloneコマンドをPythonから叩く
    """
    while True:

        print("pls select branch")
        #ブランチ情報を表示する
        branchs = ghm.get_branch(token[0].strip(),ghm.get_repo()[user_type_repo_int - 1])
        #最後に表示されるように追加、Google翻訳で英文作成
        #本当は数字で戻れるようにしようと思ったが、面倒な気がしたので文章
        print("\033[1m" + "Note: you can go back by typing [back]\033[0m")
        for number, branch in enumerate(branchs):
            print(number + 1, ":", branch)
        user_type_option = input("waiting:")
        if user_type_option == "back":
            Function_selection(user_type_repo_int)
        #数値以外を入力していないかのチェック
        if not user_type_option.isdecimal():
            print("\033[1m" + "pls type number\033[0m")
            continue
        user_type_option_int = int(user_type_option)
        #範囲外を選んでないかのチェック
        if len(branchs) < user_type_option_int:
            print("\033[1m" + "out of range\033[0m")
            continue
        #ファイルから読み込んだユーザー名＆ユーザーが選択したリポ名&ブランチ名を代入して実行する
        command = 'git clone -b '+ branchs[user_type_option_int - 1] +' https://github.com/'+token[0].strip()+'/'+ghm.get_repo()[user_type_repo_int - 1]
        #デバッグ用
        # print(command)
        #https://qiita.com/mistletoe/items/6b293710c3911d1fab59
        subprocess.call(command, shell=True)
        print("\033[1m" + "clone is done\033[0m")
        Function_selection(user_type_repo_int)

#もっとスマートなやり方がありそうな気がするが、現状はこうする
user_type_repo_int = Listen_repo(ghm)

Function_selection(user_type_repo_int)