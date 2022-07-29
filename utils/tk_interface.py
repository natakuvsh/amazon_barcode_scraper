import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


def tk_interface():
    # create the root window
    root = tk.Tk()
    root.title('Tkinter Open File Dialog')
    root.resizable(False, False)
    root.geometry('300x150')

    def select_file():
        global filename
        filetypes = (
            ("Excel files", "*.xlsx"),
            ("CSV Files", "*.csv")
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        showinfo(
            title='Selected File',
            message=filename
        )
        root.destroy()
        return filename

    # open button

    open_button = ttk.Button(
        root,
        text='Open a File',
        command=select_file
    )

    open_button.pack(expand=True)

    # run the application
    root.mainloop()
    return filename

