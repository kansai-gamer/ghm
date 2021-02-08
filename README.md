# 企画  

## 想定利用環境  

* Linux系OS & macOSを対象とする。  
* PythonバージョンはPython3系を対象とする。

## 依存モジュール

* PyGithub (pipでインストール可)  
その他モジュールは標準のもの

## アプリケーション概要

Github管理補助ツール

## 機能一覧  

* 選択したリポジトリをクローンする
* 簡易的なREADME表示
* 超簡易的なリポジトリ内フォルダ表示

## 動作イメージ  
```bash
$ python3 ghm.py
welcome to Github Manager
plz select to repo

1 : autospacekey
2 : bash
3 : cheating
4 : html_and_css
5 : javascript
6 : kansai-gamer.github.io
7 : php
8 : private
9 : Python
10 : SQL
11 : todays-code
12 : Upside-down

waiting:
```
> キーボードからリポジトリの番号を選択します。

```bash
waiting:2
pls select
1 : clone
2 : Read README.md
3 : View folder
4 : View branch
5 : View Issue
6 : back to select repo

waiting:
```
> キーボードから利用する機能の番号を選択します。  
※現時点ではこうなっていますが、気が向いたら機能追加予定です。
```bash
waiting: 1

waiting:1
pls select branch
Note: you can go back by typing [back]
1 : master
waiting:
```
>ブランチを選択します。

```bash

1 : master
waiting:1
Cloning into 'bash'...
remote: Enumerating objects: 72, done.
remote: Counting objects: 100% (72/72), done.
remote: Compressing objects: 100% (54/54), done.
remote: Total 72 (delta 33), reused 48 (delta 15), pack-reused 0
Unpacking objects: 100% (72/72), 11.10 KiB | 541.00 KiB/s, done.
clone is done
pls select
1 : clone
2 : Read README.md
3 : View folder
4 : View branch
5 : View Issue
6 : back to select repo
waiting:

```
> 選択したブランチをcloneし機能選択画面へ戻ります。

```bash
waiting: 2

# bash
再利用禁止
```
>リポジトリのREADME.mdファイルを表示します。

```bash
waiting:3
['README.md', 'graph.sh', 'hikisuu.sh', 'nums.log', 'randomgame.sh', 'readlog.sh', 'script13_select.sh', 'sentaku.sh', '入数数値前後比較.sh']
pls select
1 : clone
2 : Read README.md
3 : View folder
4 : View branch
5 : View Issue
6 : back to select repo
waiting:
```
>かなり簡易的にリポジトリ内のフォルダを表示します。

```bash
waiting:4
['master']
pls select
1 : clone
2 : Read README.md
3 : View folder
4 : View branch
5 : View Issue
6 : back to select repo
waiting:
```

>かなり簡易的にブランチを表示します

```bash
waiting:5
['README.mdの内容が古い', 'Issueを簡易的に表示したい']
pls select
1 : clone
2 : Read README.md
3 : View folder
4 : View branch
5 : View Issue
6 : back to select repo
waiting:
```
>Issueのタイトルを簡易的に表示します(今後仕様変更予定)

---
# 設計

## ファイル一覧

* ghm.py  
    * プログラム本体
* ghm_class.py
    * GHM動作に必要なクラスファイル
* gh_token.txt
    * 動作に必要なトークンを保存しているファイル（プログラム初回起動時に生成）

## クラス一覧
* GhmRepo

## クラス詳細

### GhmRepo
* メソッド
    * get_repo
        * リポジトリを取得し配列で返す、起動時に必ず実行される。  
        Githubへのログインエラーが発生した場合は例外を返す
    * read_folder_names
        * フォルダ名を返す
    * read_readme
        * README.md をprintで返す
    * get_issues
        * issues のタイトルを取得し配列で返す
    * get_branch
        * ブランチを取得し配列で返す
