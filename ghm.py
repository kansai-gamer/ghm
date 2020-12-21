import os
import subprocess
from ghm_class import GhmRepo

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

def Listen_repo(ghm):

    while True:

        print("pls select to repo")
        for number, repos in enumerate(ghm.get_repo()):
            print(number + 1, ":", repos)
        user_type_repo = input("waiting:")
        if user_type_repo.isdecimal():
            user_type_repo_int = int(user_type_repo)
            if user_type_repo_int <= len(ghm.get_repo()):
                return user_type_repo_int
            else:
                print("\033[1m" + "Out of range\033[0m")
        else:
            # print('\033[1m' + 'pls type number')
            print("\033[1m" + "pls type number\033[0m")


user_type_repo_int = Listen_repo(ghm)

while True:

    # print("\033[1m" + "pls select\033[0m")
    print("pls select")
    options = ["clone", "Read README.md", "View folder", "back to select repo"]
    for number, option in enumerate(options):
        print(number + 1, ":", option)
    user_type_option = input("waiting:")
    if user_type_option.isdecimal():
        user_type_option_int = int(user_type_option)
    else:
        print("\033[1m" + "pls type number\033[0m")
        

    if user_type_option_int == 1:
        command = 'git clone','https://github.com/'+token[0].strip()+'/'+ghm.get_repo()[user_type_repo_int - 1]
        #https://qiita.com/mistletoe/items/6b293710c3911d1fab59
        subprocess.call(command, shell=True)
    elif user_type_option_int == 2:
        print(ghm.read_readme(token[0].strip(),ghm.get_repo()[user_type_repo_int - 1]))
        continue
    elif user_type_option_int == 3:
        print(ghm.read_folder_names(token[0].strip(),ghm.get_repo()[user_type_repo_int - 1]))
        continue
    elif user_type_option_int == 4:
        user_type_repo_int = Listen_repo(ghm)
    else:
        print(print("\033[1m" + "Out of range\033[0m"))