import tkinter as tk
from tkinter import ttk, filedialog

root = tk.Tk()
root.title("Main Window")
root.geometry('750x150')

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

def select(option):
    print(option)

ttk.Button(root, text='Filepath 1', command=lambda: select('Rock')).grid(
    row=0,
    column=0,
)
ttk.Button(root, text='Filepath 2',command=lambda: select('Paper')).grid(
    row=1,
    column=0,
)

root.directory = None
browse = ttk.Button(root, text='Directory')

def askopenfile():
    root.directory = filedialog.askdirectory()
    browse.config(text = root.directory)
    return root.directory

browse.configure(command = askopenfile)
browse.grid(
    row=2,
    column=0,
)

def button_clicked():
    print(root.directory)

button = ttk.Button(root, text='Click Me', command=button_clicked)
button.grid(row=3)


root.mainloop()
