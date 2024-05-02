import tkinter as tk

def get_frame_size():
    width = frame.winfo_width()
    height = frame.winfo_height()
    print("Frameの幅:", width)
    print("Frameの高さ:", height)

root = tk.Tk()

frame = tk.Frame(root,bg="lightblue")
frame.pack()



button = tk.Button(frame, text="Frameの大きさを取得", command=get_frame_size)
button.pack()

root.mainloop()
