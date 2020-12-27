import os
import subprocess
import sys
from ghm_class import GhmRepo

#ファイルが存在するかの確認だけなので if not
if not os.path.isfile("gh_token.txt"):
    #ユーザーIDも必要ぽいので同じファイルに格納する
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
                            #↑改行コードの削除

print("welcome to Github Manager")
#デバッグ用 ID読み取り確認
# print(token[0].strip())
#デバッグ用 トークン読み取り確認
#print(token[1].strip())

#あとで戻ってこれるように関数化、先生のアドバイスを参考
def Listen_repo(ghm):

    while True:

        try:
            print("pls select to repo")
            #こう書くと数字付きで出せるとクラスメイトにアドバイス貰ったので参考にしました。
            for number, repos in enumerate(ghm.get_repo()):
                print(number + 1, ":", repos)
            user_type_repo = input("waiting:")
        except :
            print("\033[1m" + "pls check token or id\033[0m")
            sys.exit(1)

        #↓ユーザーの入力文章が数値かどうかの判定これもクラスメイト（ｒｙ
        if user_type_repo.isdecimal():
            user_type_repo_int = int(user_type_repo)
            #リポ選択で範囲外を入力していないかの確認（これをしないと存在しない物をモジュールに渡そうとするのでエラーが起きる）
            if user_type_repo_int <= len(ghm.get_repo()):
                return user_type_repo_int
            else:#先生からのアドバイスのおかげで正しく太文字に出来ました。
                print("\033[1m" + "Out of range\033[0m")
        else:
            print("\033[1m" + "pls type number\033[0m")

def Function_selection(user_type_repo_int):
    while True:

        print("pls select")
        options = ["clone", "Read README.md", "View folder", "back to select repo"]
        for number, option in enumerate(options):
            print(number + 1, ":", option)
        user_type_option = input("waiting:")
        if user_type_option.isdecimal():
            user_type_option_int = int(user_type_option)
            
        else:
            print("\033[1m" + "pls type number\033[0m")
            continue

        if user_type_option_int == 1:#なんか長いけど、ファイルから読み込んだユーザー名＆ユーザーが選択したリポ名を代入して実行してるだけ
            command = 'git clone '+'https://github.com/'+token[0].strip()+'/'+ghm.get_repo()[user_type_repo_int - 1]
            #https://qiita.com/mistletoe/items/6b293710c3911d1fab59
            subprocess.call(command, shell=True)
        elif user_type_option_int == 2:#こっちも長いけど、クラスへファイルから読み込んだトークンとユーザーが選択したリポ名を投げてREADME.mdの内容が帰ってきてるだけ
            print(ghm.read_readme(token[0].strip(),ghm.get_repo()[user_type_repo_int - 1]))
            continue
        elif user_type_option_int == 3:#こっちも投げて値が帰ってきてるだけ
            print(ghm.read_folder_names(token[0].strip(),ghm.get_repo()[user_type_repo_int - 1]))
            continue
        elif user_type_option_int == 4:#定義した関数を呼び出してリポジトリ選択へ戻る
            user_type_repo_int = Listen_repo(ghm)
        elif user_type_option_int == 5:#ブランチ情報を表示
            print(ghm.get_branch(token[0].strip(),ghm.get_repo()[user_type_repo_int - 1]))
        else:
            print("\033[1m" + "Out of range\033[0m")
            continue

#最初は関数化してなかったのでとりあえずこうして変数に値を代入
#もっとスマートなやり方ありそうな気がするけど、とりあえずこうする
user_type_repo_int = Listen_repo(ghm)

Function_selection(user_type_repo_int)