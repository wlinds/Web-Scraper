import tkinter as tk
from tkinter import ttk

def option_selected(*args):
    # Function to call when an option is selected
    selected_value = selected_option.get()
    print("Option selected:", selected_value)

    # Update the menu options
    option_menu['menu'].delete(0, 'end')
    for option in options:
        option_menu['menu'].add_command(label=option, command=tk._setit(selected_option, option))

    # Set the selected value
    selected_option.set("selected_value")

    # After updating the options, wait for a short delay and then open the menu
    root.after(1, open_menu)

def open_menu():
    option_menu['state'] = 'readonly'
    option_menu.event_generate('<Button-1>')

root = tk.Tk()

# Create a StringVar to hold the selected value
selected_option = tk.StringVar()

# Define the options
options = ["Option 1", "Option 2", "Option 3"]

# Create the OptionMenu widget
option_menu = ttk.OptionMenu(root, selected_option, "", *options)

# Add a trace to the StringVar to call the option_selected function
selected_option.trace("w", option_selected)

option_menu.pack()

root.mainloop()
