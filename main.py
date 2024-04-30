import sympy
import tkinter 
from tkinter import filedialog
import ctypes


try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

import pandas as pd

def load_data():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if file_path:
        try:
            df = pd.read_excel(file_path)
            display_data(df)
        except Exception as e:
            # error_label.config(text=f"Error: {str(e)}")
            pass

def display_data(df):
    font = ("Noto Sans JP",15)
    for widget in data_frame.winfo_children():
        widget.destroy()
        
    columns = df.columns
    for i, col in enumerate(columns):
        tkinter.Label(data_frame, text=col, borderwidth=1, relief="solid",font=font).grid(row=0, column=i, sticky="nsew")
        for j, value in enumerate(df[col]):
            tkinter.Label(data_frame, text=value, borderwidth=1, relief="solid",font=font).grid(row=j+1, column=i, sticky="nsew")

# Tkinterウィンドウの設定
root = tkinter.Tk()
root.title("Excel Data Viewer")

# データ表示用のフレーム
data_frame = tkinter.Frame(root)
data_frame.grid(row=0,column=0)

# ファイル読み込みボタン
load_button = tkinter.Button(root, text="Load Data", command=load_data)
load_button.grid(row=1,column=0,sticky=tkinter.NSEW)

# エラーメッセージ表示用ラベル
# error_label = tkinter.Label(root, fg="red")
# error_label.pack()

input_entry_label = tkinter.Label(text="input symbol:")
input_entry_label.grid(row=2,column=0)

input_entry = tkinter.Entry()
input_entry.grid(row=2,column=1)

target_entry_label = tkinter.Label(text="target symbol:")
target_entry_label.grid(row=3,column=0)

target_entry = tkinter.Entry()
target_entry.grid(row=3,column=1)

root.mainloop() 