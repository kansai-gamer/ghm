import os
from ghm_class import GhmRepo

if not os.path.isfile("gh_token.txt"):
    #ユーザーIDも必要ぽいので同じファイルに格納する
    write = []
    write.append(input("pls type your Github token:"))
    write.append(input("pls type your Github ID:"))
    with open("gh_token.txt", mode="w", encoding="utf-8") as f:
        for token_and_user in write:
            f.write(token_and_user+"\n")

with open("gh_token.txt", mode="r", encoding="utf-8") as f:
    token = f.readlines()
    #インスタンス生成
    ghm = GhmRepo(token[0].strip())
    #↑改行コードの削除
    #↓デバッグ用
    # print(token[0].strip())

print("welcome to Github Manager\nplz select to repo")
for number, repos in enumerate(ghm.get_repo()):
    print(number + 1, ":", repos)
usertype = input("waiting:")


# print(ghm.read_folder_names("kansai-gamer","bash"))

# ghm.read_readme("kansai-gamer","bash")