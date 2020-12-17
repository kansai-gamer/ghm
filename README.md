# 企画  

## 想定利用環境  

* Linux系OSのみを対象とする。  
* PythonバージョンはPython 3.8.5を対象とする。

## アプリケーション概要

Github管理補助ツール

## 機能一覧  

* 選択したリポジトリをクローンする
* 簡易的なREADME表示
* 簡易的なフォルダ表示
* リポジトリで使われているソフトウェア・モジュールバージョンの管理(目標)※  
※現時点ではREDME.mdに仕様に沿って記載してもらい、それを読み込むことで管理する  
といった仕様で考えています。

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
plz select

1: Clone
2: Read README.md
3: View folder
4: View module and Software version

waiting:
```
※現時点ではこうなっていますが、スケジュールが許せば機能追加予定です。
```bash
waiting: 1

Cloning into 'bash'...
remote: Enumerating objects: 72, done.
remote: Counting objects: 100% (72/72), done.
remote: Compressing objects: 100% (54/54), done.
remote: Total 72 (delta 33), reused 48 (delta 15), pack-reused 0
Unpacking objects: 100% (72/72), 11.10 KiB | 51.00 KiB/s, done.

```
```bash
waiting: 2

# bash
再利用禁止
```

```bash
README.md
3 months ago
graph.sh
0917
3 months ago
hikisuu.sh
0917
3 months ago
nums.log
0924
3 months ago
randomgame.sh
0903
3 months ago
readlog.sh
0924
3 months ago
script13_select.sh
0924
3 months ago
sentaku.sh
0924
3 months ago
入数数値前後比較.sh
```

---
# 設計

## ファイル一覧

* ghm.py  
    * プログラム本体
* ghm_class.py
    * GHM動作に必要なクラスファイル
* gh_token.txt
    * 動作に必要なトークンを保存しているファイル

## クラス一覧
* GhmRepo
    * リポジトリを取得
* GHMError
    * 例外処理用
* Readfiles
    * README.mdやフォルダ構成、バージョン情報(README.md)を読む
* 

## クラス詳細

### GhmRepo
* データ属性 token
    * Githubトークン
* メソッド
    * get_repo
        * リポジトリを取得し配列で返す
    * read_folder_names
        * フォルダ名を返す
    * read_readme
        * README.md を返す