import tkinter as tk
from tkinter import ttk
import sv_ttk
from window import Window

root = tk.Tk()
root.geometry("800x500")

win = Window(root)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

output_frame = ttk.LabelFrame(root, relief="solid", borderwidth=1, width=530, height= 480, text="Output")
output_frame.grid(row=0, column=0, padx=10, pady=10)
output_frame.grid_propagate(0)

settings_frame = ttk.LabelFrame(root, relief="solid", borderwidth=1, width= 250, height= 480, text="settings")
settings_frame.grid(row=0, column=1, padx=10, pady=10)
settings_frame.grid_propagate(0)


sv_ttk.set_theme("dark")
root.resizable(False, False)
root.mainloop()

