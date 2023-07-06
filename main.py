import tkinter as tk
from tkinter import ttk
import sv_ttk
from tkinter import filedialog
from bs4 import BeautifulSoup
import requests
import preferences as pref

root = tk.Tk()
root.geometry("800x500")
root.title("Web Scraper")

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

    global entry_focused
    entry_focused = True
    
    if url_entry.get() == "Enter URL" or url_entry.get() == "Invalid URL!":  # if text == Enter URL
        url_entry.delete(0, tk.END)  # Clear the entry widget
        url_entry.configure(foreground=entry_foreground)  # Change the text color

# if not focused.
def on_focusout(event):

    if url_entry.get() == "" or "Invalid URL!":  # if text is none
        url_entry.insert(0, "Enter URL")  # Set the placeholder text
        url_entry.configure(foreground="gray")  # Change the text color

def on_entry_focus_out(event):

    global entry_focused
    
    if event.widget != url_entry and entry_focused == True:
        entry_focused = False
        input_text = url_entry.get()
        print("Input:", input_text)
        root.focus_set()

        retrive_website(input_text)
        

def on_entry_return(event):

    global entry_focused

    input_text = url_entry.get()
    print("Input:", input_text)
    entry_focused = False
    root.focus_set()

    retrive_website(input_text)

entry_focused = False
entry_error = False

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
url_entry.bind("<FocusOut>", on_entry_focus_out)
url_entry.bind("<Return>", on_entry_return)
root.bind("<Button-1>", on_entry_focus_out)

def retrive_website(URL):

    global options
    global entry_focused

    try:
        response = requests.get(URL)
    except:
        url_entry.delete(0, tk.END)
        url_entry.insert(0, "Invalid URL!")
        url_entry.configure(foreground="gray")

    page = BeautifulSoup(response.content, "html.parser")

    elements = page.find_all()

    new_options = []

    for element in elements:
        print(f"{element.name} {element.get('class')}")
        new_options.append(f"{element.name}, {element.get('class')}".replace("[", "").replace("]", ""))
    
    new_options = list(set(new_options))

    options = new_options
    
    update_menu()

# seperator for settings frame.
divider = ttk.Separator(settings_frame, orient="horizontal")
divider.grid(row=1, column=0, padx=0, pady=10, sticky="ew")

# list of selected option from element dropdown.
selected_list = []

# fuction for handeling selection of elements.
def on_option_selected(*args):
    # removes the place holder index in option list.
    if "" in options:
        options.remove("")

    # gets the value of the selected option.
    selected_item = var.get()

    # checks if the selected item is in the selected list.
    if selected_item not in selected_list:
        # if not appends.
        selected_list.append(selected_item)

    else:
        # if is removes.
        selected_list.remove(selected_item)

    # resets the dropdown menu.
    dropdown["menu"].delete(0, "end")

    # adds back all the options to the menu.
    for option in options:
        dropdown["menu"].add_command(label=option, command=tk._setit(var, option))

    # edits the selected options with a checkmark.
    for option in options:
        if option in selected_list:
            dropdown["menu"].entryconfigure(option, label="\u2713 " + option)

    # resets the displayed option to "Select elements".
    var.set("Select elements")
    # run open_menu() after 1 millisecond.
    root.after(1, open_menu)

    print(selected_list)


# opens the option menu.
def open_menu():
    dropdown["state"] = "readonly"
    dropdown.event_generate("<Button-1>")

# update menu.
def update_menu():

    # resets the dropdown menu.
    dropdown["menu"].delete(0, "end")

    # adds back all the options to the menu.
    for option in options:
        dropdown["menu"].add_command(label=option, command=tk._setit(var, option))


# var for the selected option.
var = tk.StringVar()
options = ["", "None"]  # list of options.

# creats the dropdown and position it.
dropdown = ttk.OptionMenu(settings_frame, var, *(options), command=on_option_selected)
dropdown.config(width=18)
dropdown.grid(row=3, column=0, padx=0, pady=10)

def toggle_theme():
    """Swap between dark and light theme"""
    current_theme = sv_ttk.get_theme()
    if current_theme == "dark":
        new_theme = "light"
    else:
        new_theme = "dark"
    sv_ttk.set_theme(new_theme)
    config = pref.load_config()
    config["THEME"] = new_theme
    pref.save_config(config)

# Add menu (Works on macOS, have not checked Windows yet)
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Toggle light mode", command=toggle_theme)
menubar.add_cascade(label="Preferences", menu=filemenu)
editmenu = tk.Menu(menubar, tearoff=0)

# sets the display option.
var.set("Select elements")
# runs the on_option_selected() fuction if a option is selected.
var.trace("w", on_option_selected)

root.config(menu=menubar)

current_theme = pref.get_theme()
sv_ttk.set_theme(current_theme)

root.resizable(False, False)
root.mainloop()
