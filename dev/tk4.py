import tkinter as tk
from tkinter.ttk import Button, Label


# first window frame startpage
class Start(tk.Frame):

    def refresh(self):
        self.destroy()
        self.__init__(self.parent)

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        parent.title("title")
        parent.geometry("800x500")

        a = Button(text="Click This", command=self.refresh)
        a.pack()

root = tk.Tk()
Start(root)
root.mainloop()
