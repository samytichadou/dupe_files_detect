import tkinter as tk
from tkinter.ttk import Button, Label

def change_window(self):
    self.destroy()
    root = tk.Tk()
    Then(root)
    root.mainloop()

# first window frame startpage
class Start(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        parent.title("title")
        parent.geometry("800x500")

        a = Button(text="Click This", command=lambda: change_window(self))
        a.pack()

# first window frame startpage
class Then(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        # self.parent = parent

        Label(self, text="Bye Bye").pack()

# Start.mainloop()

root = tk.Tk()
Start(root)
# Zouip_main_settings_parent(root)
# Zouip_receive_from_settings_parent(root)
# Zouip_send_to_settings_parent(root)
root.mainloop()
