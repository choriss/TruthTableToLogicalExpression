import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

class ExcelViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("Excel Viewer")

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.btn_open = tk.Button(self.frame, text="Open Excel File", command=self.open_excel_file)
        self.btn_open.pack()

        self.cells = []

    def open_excel_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if file_path:
            try:
                df = pd.read_excel(file_path)
                self.display_excel_content(df)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

    def display_excel_content(self, df):
        # Clear existing cells
        for cell in self.cells:
            cell.destroy()
        self.cells.clear()

        # Display column headers
        for col_idx, col_name in enumerate(df.columns):
            header_label = tk.Label(self.frame, text=col_name, relief=tk.RIDGE, padx=5, pady=5)
            header_label.grid(row=0, column=col_idx, sticky="nsew")
            self.cells.append(header_label)

        # Display data cells
        for row_idx, row in df.iterrows():
            for col_idx, value in enumerate(row):
                data_label = tk.Label(self.frame, text=str(value), relief=tk.RIDGE, padx=5, pady=5)
                data_label.grid(row=row_idx+1, column=col_idx, sticky="nsew")
                self.cells.append(data_label)

def main():
    root = tk.Tk()
    app = ExcelViewer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
