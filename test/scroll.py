import tkinter as tk
import uuid

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

root = tk.Tk()
root.geometry("300x200")

# Canvasの作成
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Frameの作成
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

# ラベルをFrameに追加してスクロールさせる
for i in range(50):
    tk.Label(frame, text=f"Label {i}").pack()

# スクロールバーの作成
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Canvasとスクロールバーの連動
canvas.configure(yscrollcommand=scrollbar.set)

# Canvasのスクロール領域を設定
frame.bind("<Configure>", on_configure)

def on_btn_click():
    tk.Label(frame, text=f"Label {uuid.uuid4()}").pack()

tk.Button(frame,text="button",command=on_btn_click).pack()


root.mainloop()
