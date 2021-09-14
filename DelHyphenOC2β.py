# coding: utf-8
# DelHyphenOC2 Ver.β1.0.0
#インポート
import tkinter as tk
import re

### 関数 ###
# テキスト操作
def txt_func():
    try:
        # テキスト取得
        txt = root.clipboard_get()
        # 改行＆文献番号削除
        delnl = txt.replace("-\n","").replace("\n"," ")
        delall = re.sub(r" *\[(\d+(|, *\d+|(-|–)\d+)+)\]", "", delnl)
        root.clipboard_append(delall)
    except:
        pass

### GUI ###
# 非表示
root = tk.Tk()
root.withdraw()

# テキスト操作
txt_func()

#更新
root.update()
# 終了
root.destroy()