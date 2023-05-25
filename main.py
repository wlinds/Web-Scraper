import tkinter as tk
from tkinter import ttk
import sv_ttk

root = tk.Tk()
root.geometry("800x500")

settings_frame = ttk.Frame(root, relief="solid", borderwidth=1, width= 300, height= 480, style='danger.TFrame')
settings_frame.grid(row=0, column=0, padx=10, pady=10)
settings_frame.grid_propagate(0)

settings_frame_name = ttk.LabelFrame(settings_frame, text="Settings")
settings_frame_name.grid(row=0, column=0)

test_entry = ttk.Entry(settings_frame)
test_entry.grid(row= 0, column= 0, sticky="ew")

sv_ttk.set_theme("dark")
root.mainloop()
