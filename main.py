import tkinter as tk
from tkinter import ttk
import sv_ttk
from window import Window

root = tk.Tk()
root.geometry("800x500")

win = Window(root)

url = tk.StringVar()

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

output_frame = ttk.LabelFrame(
    root, relief="solid", borderwidth=1, width=530, height=480, text="Output"
)
output_frame.grid(row=0, column=0, padx=10, pady=10)
output_frame.grid_propagate(0)

settings_frame = ttk.LabelFrame(
    root, relief="solid", borderwidth=1, width=250, height=480, text="settings"
)
settings_frame.grid(row=0, column=1, padx=10, pady=10)
settings_frame.grid_propagate(0)
settings_frame.columnconfigure(0, weight=1)


# if entry url is clicked.
def on_entry_click(event):
    if url_entry.get() == "Enter URL":  # if text == Enter URL
        url_entry.delete(0, tk.END)  # Clear the entry widget
        url_entry.configure(foreground=entry_foreground)  # Change the text color


# if not focused.
def on_focusout(event):
    if url_entry.get() == "":  # if text is none
        url_entry.insert(0, "Enter URL")  # Set the placeholder text
        url_entry.configure(foreground="gray")  # Change the text color

# adding the entry to layout.
url_entry = ttk.Entry(settings_frame, textvariable=url)
url_entry.grid(row=0, column=0, padx=5, pady=10)
url_entry.grid_propagate(0)

# gets the def color of forground.
entry_foreground = url_entry.cget("foreground")

# addes placeholder text.
url_entry.insert(0, "Enter URL")
url_entry.configure(foreground="gray")

# event checkers.
url_entry.bind("<FocusIn>", on_entry_click)
url_entry.bind("<FocusOut>", on_focusout)


sv_ttk.set_theme("dark")
root.resizable(False, False)
root.mainloop()
