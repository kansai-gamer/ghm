import os
from ghm_class import GhmRepo

if not os.path.isfile("gh_token.txt"):
    token = input("pls type your Github token")
    with open("gh_token.txt", mode="w", encoding="utf-8") as f:
        f.write(token)

with open("gh_token.txt", mode="r", encoding="utf-8") as f:
    #インスタンス生成
    ghm = GhmRepo(f.read())

print("welcome to Github Manager")
for number, repos in enumerate(ghm.get_repo()):
    print(number + 1, ":", repos)
usertype = input("plz select to repo:")


print(ghm.read_folder_names("kansai-gamer","bash"))

# ghm.read_readme("kansai-gamer","bash")