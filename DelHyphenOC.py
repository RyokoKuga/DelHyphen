# coding: utf-8
# DelHyphenOC Ver.1.0.0
#インポート
import tkinter as tk

### 関数 ###
# テキスト操作
def txt_func():
    try:
        # テキスト取得
        txt = root.clipboard_get()
        # 改行削除
        delnl = txt.replace("-\n","").replace("\n"," ")
        root.clipboard_append(delnl)
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