import tkinter as tk
from tkinter import ttk, filedialog

class DupeFilesDetectApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # Them
        self.title("Dupe Files Detect")
        self.geometry('750x150')

        # Datas
        self.directory = None

        # creating a container
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row = 0, column = 0)#, sticky ="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage
class StartPage(tk.Frame):

    def askopenfile(self):
        self.directory = filedialog.askdirectory()
        self.browse.config(text = self.directory)
        # return root.directory

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.browse = ttk.Button(
            self,
            text='No Directory',
            command = self.askopenfile,
        )
        self.browse.grid(
            row = 0,
            column = 0,
        )

        startbutton = ttk.Button(
            self,
            text ="Start Dupe Files Detection",
            command = lambda : controller.show_frame(Page1),
        )
        startbutton.grid(
            row = 1,
            column = 0,
        )


# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Page 1")
        label.grid(
            row = 0,
            column = 4,
            padx = 10,
            pady = 10,
        )

        button1 = ttk.Button(
            self,
            text ="StartPage",
            command = lambda : controller.show_frame(StartPage),
        )
        button1.grid(
            row = 1,
            column = 1,
            padx = 10,
            pady = 10,
        )


# Driver Code
app = DupeFilesDetectApp()
app.mainloop()
