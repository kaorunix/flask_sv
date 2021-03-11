## 事前準備

* gitインストール
* pythonインストール
* pipインストール
* pipenvインストール

[pipenv参考](https://qiita.com/y-tsutsu/items/54c10e0b2c6b565c887a)

* gitの設定など

```bash
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

* python設定

```bash
#Virtual Environment設定
$ sudo apt-get install python3-venv
```

### リポジトリのClone・仮想環境の設定

実行環境にclone

```
git clone git@github.com:kaorunix/python_template.git
```

Pipenvを起動

```
pipenv shell
```

必要なパッケージをインストール

```
pipenv install --ignore-pipfile
pipenv install --ignore-pipfile --dev
```


## ディレクトリ構成

```
$ tree
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── app.py
│           ・
├── requirements.txt
├── setup.py
└── tests
    ├── __init__.py
    ├── conftest.py

```


### testsディレクトリ

* テストコードを配置するディレクトリ

## プログラムの実行

次のどちらかで実行できます。

* pipenv shellの中で実行

```
$ pipenv shell
$ python helloworld/main.py
```
* pipenvコマンドを使って直接実行


```
$ pipenv run python main.py
```


## Testの実行

すべてのテストを実行(カバレッジも出る)

```
pipenv run test
```

対象を指定してテストを実行

```
pytest -v -s [対象のファイルパス]
```




