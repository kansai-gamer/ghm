from github import Github
import os
from ghm_class import GhmRepo

if not os.path.isfile("gh_token.txt"):
    token = input("pls type your Github token")
    with open("gh_token.txt", mode="w", encoding="utf-8") as f:
        f.write(token)

with open("gh_token.txt", mode="r", encoding="utf-8") as f:
    #インスタンス生成
    ghm = GhmRepo(f.read())

# print(ghm.get_repo())

print(ghm.read_folder_names("kansai-gamer","bash"))

# ghm.read_readme("kansai-gamer","bash")