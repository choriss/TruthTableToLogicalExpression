import sympy
import tkinter 
from tkinter import filedialog
import tkinter.ttk as ttk
import ctypes
import pyperclip
import time

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
            error_label.config(text=f"Error: {str(e)}")
            pass

def display_data(df):
    global input_checkboxes
    global input_checkboxes_var

    global target_checkboxes
    global target_checkboxes_var

    global display_frame

    global all_symbols
    font = ("Noto Sans JP",15)
    for widget in data_frame.winfo_children():
        widget.destroy()
        
    columns = df.columns
    target_combox_temp = []

    input_checkboxes_var = []
    input_checkboxes = []
    
    target_checkboxes_var = []
    target_checkboxes = []

    all_symbols = []

    input_checkbox_label = tkinter.Label(data_frame,text="input:")
    input_checkbox_label.grid(row=0,column=0)

    target_checkbox_label = tkinter.Label(data_frame,text="target:")
    target_checkbox_label.grid(row=1,column=0)



    # スクロールバー
    num_of_symbol = list(enumerate(columns))[-1][0]+1
    # print(num_of_symbol)
    data_frame_y_bar = tkinter.Scrollbar(root,orient=tkinter.VERTICAL)
    data_frame_y_bar.grid(column=1,row=0)
    data_frame_y_bar.config(command=data_frame_canvas.yview)


    

    

    for i, col in enumerate(columns):
        
        tkinter.Label(data_frame, text=col, borderwidth=1, relief="solid",font=font).grid(row=2, column=i+1, sticky="nsew")
        truth_table_dict[col] = []
        target_combox_temp.append(col)
        input_checkboxes_var.append(tkinter.IntVar())
        input_checkboxes.append(tkinter.Checkbutton(data_frame,variable=input_checkboxes_var[-1]))
        input_checkboxes[-1].grid(row=0,column=i+1, sticky="nsew")

        target_checkboxes_var.append(tkinter.IntVar())
        target_checkboxes.append(tkinter.Checkbutton(data_frame,variable=target_checkboxes_var[-1]))
        target_checkboxes[-1].grid(row=1,column=i+1, sticky="nsew")

        all_symbols.append(col)

        for j, value in enumerate(df[col]):
            tkinter.Label(data_frame, text=value, borderwidth=1, relief="solid",font=font).grid(row=j+3, column=i+1, sticky="nsew")
            truth_table_dict[col].append(int(value))

    #time.sleep(10)
    print(data_frame.winfo_reqheight())




    # print(data_frame.winfo_height())
    display_frame = data_frame_canvas.create_window((0, 0), window=data_frame, anchor="nw")
    #data_frame_canvas.config(scrollregion=(0, 0, data_frame.winfo_width(), data_frame.winfo_height()))
    data_frame_canvas.configure(scrollregion=data_frame_canvas.bbox("all"))
    data_frame_canvas.configure(yscrollcommand=data_frame_y_bar.set)
    print(data_frame.winfo_reqheight())
    

    # target_entry_label_combo["values"] = target_combox_temp
    # print(truth_table_dict)

def solve_truth_formula():
    error_label["text"] = ""
    # input_symbols = input_entry.get().split(",")
    # target_symbol = target_var.get()

    input_symbols = []

    for i in range(len(input_checkboxes_var)):
        if input_checkboxes_var[i].get()==1:
            input_symbols.append(all_symbols[i])

    target_symbols = []

    for i in range(len(target_checkboxes_var)):
        if target_checkboxes_var[i].get()==1:
            target_symbols.append(all_symbols[i])

    # print(input_symbols)

    # targetの存在確認
    if target_symbols == []:
        error_label["text"] = "target is not selected."
        return
    
    # inputの存在確認
    if input_symbols == []:
        error_label["text"] = "input is not selected."
        return 
    
    # inputにtargetが存在しないか
    for i in range(len(target_symbols)):
        if target_symbols[i] in input_symbols:
            error_label["text"] = "input includes target."
            return
    truth_formula_answers = {}
    # print(target_symbols)
    for k in range(len(target_symbols)):
        #trueリストの生成
        true_place = []
        for i in range(len(truth_table_dict[target_symbols[k]])):
            if truth_table_dict[target_symbols[k]][i] == 1:
                true_place.append(i)

        true_list = []
        for i in range(len(true_place)):
            true_list_temp = []
            for j in range(len(input_symbols)):
                true_list_temp.append(truth_table_dict[input_symbols[j]][true_place[i]])
            true_list.append(true_list_temp)
        # print(true_list)
        # symbol 定義
        sympy_symbols = sympy.symbols(" ".join(input_symbols))
        trfr = sympy.SOPform(sympy_symbols,true_list)
        truth_formula_answers[target_symbols[k]]=trfr
        
    # print(trfr)
    result_display.delete(0, tkinter.END)
    result_display.insert(tkinter.END,truth_formula_answers)
    # print(truth_formula_answers)

def copy_answer():
    pyperclip.copy(result_display.get())

# Tkinterウィンドウの設定
root = tkinter.Tk()
root.title("Truth Table To Logical Expression")

#データ表示用のcanvas

data_frame_canvas = tkinter.Canvas(root)
data_frame_canvas.grid(row=0,column=0)

# データ表示用のフレーム
data_frame = tkinter.Frame(data_frame_canvas)
data_frame.grid(row=0,column=0)

# Canvas上の座標(0, 0)に対してFrameの左上（nw=north-west）をあてがうように、Frameを埋め込む
# display_frame =  data_frame_canvas.create_window((0, 0), window=data_frame, anchor="nw")

# ファイル読み込みボタン
load_button = tkinter.Button(root, text="Load Data", command=load_data)
load_button.grid(row=1,column=0,sticky=tkinter.NSEW)

# エラーメッセージ表示用ラベル
error_label = tkinter.Label(root, fg="red")
error_label.grid(row=6,column=0)

# input_entry_label = tkinter.Label(root,text="input symbol:")
# input_entry_label.grid(row=2,column=0)

# input_entry = tkinter.Entry(root)
# input_entry.grid(row=2,column=1)

# target_entry_label = tkinter.Label(root,text="target symbol:")
# target_entry_label.grid(row=3,column=0)

# target_entry = tkinter.Entry(root)
# target_entry.grid(row=3,column=1)

# target_var = tkinter.StringVar()
# target_entry_label_combo = ttk.Combobox(root,values=[],textvariable=target_var,state="readonly",width=17)
# target_entry_label_combo.grid(row=3,column=1)

calc_button = tkinter.Button(root,text="calc",command=solve_truth_formula)
calc_button.grid(row=3,column=0,sticky=tkinter.NSEW)

answer_copy_button = tkinter.Button(root,text="copy",command=copy_answer)
answer_copy_button.grid(row=4,column=2)

result_label = tkinter.Label(root,text="result:")
result_label.grid(row=4,column=0)

result_display = tkinter.Entry(root)
result_display.grid(row=4,column=1)



#辞書初期化
truth_table_dict = {}



root.mainloop() 