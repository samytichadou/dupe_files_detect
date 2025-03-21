import os
import tkinter as tk
from tkinter import ttk, filedialog

datas = {
    'identifier_0':{
        'name':'filename0',
        'size':0,
        'occurences':[
            'filepath0_01',
            'filepath0_02'
        ]
    },
    'identifier_1':{
        'name':'filename1',
        'size':0,
        'occurences':[
            'filepath1_01',
            'filepath1_02'
        ]
    }
}


class Application(tk.Tk):
    file_count = 0
    total = len(datas)

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Main")
        self.create_widget()

    def delete_file(self, filepath):
        print(filepath)
        # Delete filepath
        # for fp in filepath_list:
        #     if os.path.isfile(fp):
        #         print(f"Deleting {fp}")
        #     else:
        #         print(f"Invalid filpath - {fp}")

        # Increment
        self.file_count += 1

        # Quit when finished
        if self.file_count>=self.total:
            print("End of dupe files, exiting")
            exit()

        # Reload
        self.destroy()
        self.__init__()

    def create_widget(self):
        tk.Label(
            text = "Choose a file to keep :",
        ).grid(
            row = 0,
        )

        occurences = datas[list(datas)[self.file_count]]['occurences']
        row = 1
        for fp in occurences:
            tk.Button(
                self,
                text = fp,
                command = lambda fp=fp: self.delete_file(fp)
            ).grid(
                row=row,
            )
            row += 1

        tk.Button(
            self,
            text = "Quit",
            command = exit,
        ).grid(
            row=row,
        )


if __name__ == "__main__":
    app = Application()
    app.mainloop()
