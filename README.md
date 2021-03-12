# pyScreenSaverPrevention
## ツール
本ツールはPythonで作られた数秒間隔でマウスを動かす＆「Ctrl」キーを入力して<br>
スクリーンセイバーの起動などを抑止するためのツールです。

## 使い方
pyScreenSaverPrevention.pyを実行するか、<br>
pyScreenSaverPrevention.exeを実行してください。<br>
<br>
exe名は変更しても動作します。

## 停止方法
以下のどちらかで停止できます。
- マウスをスクリーンの四隅のどちらかに移動
- 実行コマンドプロンプト上でCtrl + cを入力（１度目は認識しない可能性があるので念のため二度入力）

## 必須モジュール
exeで使う場合は不要です。
```
pip install pyautogui
```

## English
A tool made in Python to prevent the screen saver from starting.<br>
Move the mouse and press "Ctrl" on a regular basis.

- usage
Execute pyScreenSaverPrevention.py or pyScreenSaverPrevention.exe.<br>
You can rename pyScreenSaverPrevention.exe.

- how to stop
Please move mouse cursor to screen's courner<br>
or key press "Ctrl + C" on command prompt.
