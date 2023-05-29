import tkinter as tk

class Window:

    def __init__(self, root) -> None:

        self.root = root

    def width(self, ratio):

        return self.root.winfo_screenwidth() * (ratio / 100)
    
    def height(self, ratio):

        return self.root.winfo_screenheight() * (ratio / 100)
        