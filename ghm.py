import os
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
    ghm = GhmRepo(token[0].strip())
                            #↑改行コードの削除
    #↓デバッグ用
    # print(token[0].strip())

print("welcome to Github Manager")

while True:

    print("pls select to repo")
    for number, repos in enumerate(ghm.get_repo()):
        print(number + 1, ":", repos)
    user_type_repo = input("waiting:")
    if user_type_repo.isdecimal():
        user_type_repo_int = int(user_type_repo)
        break
    else:
        print('\033[1m' + 'pls type number')


while True:

    print("pls select")
    options = ["clone", "Read README.md", "View folder"]
    for number, option in enumerate(options):
        print(number + 1, ":", option)
    user_type_option = input("waiting:")
    if user_type_option.isdecimal():
        user_type_option_int = int(user_type_option)
    else:
        print('\033[1m' + "pls type number")
        
    if user_type_option_int == 1:
        pass
    elif user_type_option_int == 2:
        print(ghm.read_readme(token[1].strip(),ghm.get_repo()[user_type_repo_int - 1]))
        continue
    elif user_type_option_int == 3:
        print(ghm.read_folder_names(token[1].strip(),ghm.get_repo()[user_type_repo_int - 1]))
        continue

