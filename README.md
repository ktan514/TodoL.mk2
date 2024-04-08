
# Python開発環境構築 (for Windows)
windowsにPython(PyEnv)開発環境を構築する。

## PyEnvインストール
Powershellで以下のコマンドを実行する。
```ps
pip install pyenv-win --target $HOME\\.pyenv
```

### アプリ実行エイリアスの無効化 (Windows 10 バージョン1903以降)
Windows 10 バージョン1903以降の場合は、
「スタート > 設定 > アプリ > アプリと機能 > アプリ実行エイリアス」で
アプリインストーラー（python.exe と python3.exe）をオフにする

## 環境変数の登録
PYENV、PYENV_HOMEを環境変数に追加する。
以下のコマンドをPowershellで実行する。
```ps
[System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
[System.Environment]::SetEnvironmentVariable('PYENV_HOME',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
[System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + [System.Environment]::GetEnvironmentVariable('path', "User"),"User")
```

## 実行ポリシーの変更
スクリプト実行権限を変更する。
※ポリシー変更は同セッションのみで有効
```ps
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

## 動作確認
Pyenvが使用可能か確認する。
以下のコマンドを任意のコマンドプロンプトで実行する。
```ps
pyenv --version
```

## Pythonインストール
Pyenvにより任意バージョンのPythonをインストールする。
```ps
# インストール可能なバージョンを確認
pyenv install --list
# バージョンを指定してインストール
pyenv install X.X.X
```

## シムス(Shims)再構築

```ps
pyenv rehash
```


# 備考

## インストール済みバージョンの確認
pyenvによりインストール済みのPythonのバージョンを確認するコマンド。
```ps
pyenv versions
```

## グローバル環境へのインストール
```ps
pyenv global x.x.x
```

## ローカル環境へのインストール
```ps
pyenv local x.x.x
```

## 任意バージョンのアンインストール
```ps
pyenv uninstall x.x.x
```

## 文字化け対処法
PyEnv-win環境でコマンドプロンプトの2バイト文字が文字化けする。
以下のファイルの文字コードを変更することで回避可能。
```
C:\Users\ユーザー\.pyenv\pyenv-win\exec.bat(1): chcp 1250 > NUL
C:\Users\ユーザー\.pyenv\pyenv-win\bin\pyenv.bat(3): chcp 1250 >nul
C:\Users\ユーザー\.pyenv\pyenv-win\libexec\pyenv.vbs(72):         .WriteText("chcp 1250 > NUL" & vbCrLf)
C:\Users\ユーザー\.pyenv\pyenv-win\libexec\libs\pyenv-lib.vbs(193):         .WriteLine("chcp 1250 > NUL")
```

### 現在の文字コード確認
1250(CP1250)   <-- 東欧系の言語
932(CP932)     <-- Shift-JIS
65001(CP65001) <-- UTF-8


## PipEnvインストール
Powershellで以下のコマンドを実行する。
```ps
pip install pipenv
```

## 仮想環境の構築
`pipenv`により仮想環境を作成する。
パッケージのインストール先を仮想環境とすることで、他プロジェクトへの影響を断つことができる。
仮想環境のファイルは.venvフォルダに格納される。
以下のコマンドにより、`.venv`フォルダを作成する。
→プロジェクトフォルダ内で実行する。
```ps
# Python3系で初期化する場合
pipenv --python 3 
```
このとき、PC環境に指定バージョンが入っていない場合は
PyEnvと連携してインストールすることが可能。

以下のコマンドで仮想環境をアクティベートする。
```ps
pipenv shell
```

ここで`pipenv install xxx`を実行すると、そのパッケージは仮想環境内(.venv)にのみインストールされ、
グローバル環境にはインストールされない。
パッケージはPipfileおよびPipfile.lockにて管理される。

別の環境で同じ環境を再構築する場合は`Pipfile.lock`ファイルから
関連パッケージのインストールを行う。
最初の環境にインストールしたバージョンと全く同じものを入れることが出来る。
```ps
# 依存パッケージのインストール
pipenv sync
# 開発用パッケージのインストール
pipenv sync --dev
```




