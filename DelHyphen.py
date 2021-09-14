# coding: utf-8
#インポート
import tkinter as tk
from tkinter import ttk
import webbrowser

### 関数 ###
# 全削除
def delall_func():
    txtbox.delete("1.0","end")

# テキスト操作
def txt_func():
    # テキスト取得
    txt = txtbox.get("1.0", "end")
    # 改行削除
    delnl = txt.replace("-\n","").replace("\n"," ")
    # テキスト削除
    delall_func()
    # テキスト挿入
    txtbox.insert("1.end", delnl)

# コピー
def copy_func():
    # クリップボードの内容クリア
    root.clipboard_clear()
    # クリップボードへ格納
    root.clipboard_append(txtbox.get("1.0", "end"))

# ペースト
def paste_func():
    try:
        txtbox.insert("insert", root.clipboard_get())
    except:
        pass
    
# 全選択
def select_func():
    txtbox.tag_add("sel", "1.0", "end")
    
# HP(配布ページ)へアクセス
def hp_web():
    hp_url = "http://pc-chem-basics.blog.jp/archives/26966070.html"
    webbrowser.open(hp_url)

### GUI ###
# ウインドウの作成
root = tk.Tk()
root.title("DelHyphen Ver.1.0.0")
root.minsize(width=500, height=400)
# フレーム
frame = ttk.Frame(root, padding = 5)
frame.pack(padx = 5, pady = 5, fill = tk.BOTH, expand =1)
# テキストボックス
txtbox = tk.Text(frame, width = 60, height = 20)
# スクロールバー作成
yscroll = tk.Scrollbar(frame, orient = tk.VERTICAL,
                       command = txtbox.yview)
yscroll.pack(side = tk.RIGHT, fill = tk.Y)
txtbox["yscrollcommand"] = yscroll.set
# テキストボックスの配置
txtbox.pack(fill = tk.BOTH, expand =1)
# メニューバーの作成
menubar = tk.Menu(root)
root.configure(menu = menubar)
# Fileメニュー
filemenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "Exit", command = lambda: root.destroy())
# Editメニュー
editmenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label = "Paste", command = paste_func)
editmenu.add_command(label = "Copy All", command = copy_func)
editmenu.add_separator()
editmenu.add_command(label = "Select All", command = select_func)
editmenu.add_command(label = "Delete All", command = delall_func)
# Helpメニュー
helpmenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "Manual", command = hp_web)

# 変換ボタン
button = tk.Button(root, text = "Here we go!!", command = txt_func)
button.pack(padx = 10, pady = 10, ipady = 10, fill = tk.X)

# ウインドウ状態の維持
root.mainloop()