import tkinter as tk
import tkinter.scrolledtext as tkst
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog
import os
import shutil

class App:
    def __init__(self,filename=None):
        self.win = tk.Tk()
        self.win.protocol("WM_DELETE_WINDOW", self.Exit)
        self.customFont = tkFont.Font(
            family="Helvetica", size=14
        )
        self.filename=filename

        frame1 = tk.Frame(
            master=self.win,
            # background = 'maroon'
        )
        frame1.pack(fill='both', expand='yes')
        self.editArea = tkst.ScrolledText(
            master=frame1,
            wrap=tk.WORD,
            font=self.customFont,
        )

        self.editArea.pack(padx=3, pady=3, fill=tk.BOTH, expand=True)
        self.editArea.focus_set()

        menubar = tk.Menu(self.win)
        # create a pulldown menu, and add it to the menu bar
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.Open)
        filemenu.add_command(label="Save", command=self.Save)

        filemenu.add_command(label="Rename", command=self.Rename)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.Exit)
        menubar.add_cascade(label="File",  menu=filemenu)
        fontMenu=tk.Menu(menubar, tearoff=1)
        fontMenu.add_command(label="IncreaseFont", command=self.IncreaseFont)
        fontMenu.add_command(label="DecreaseFont", command=self.DecreaseFont)
        menubar.add_cascade(label="Font", menu=fontMenu)
        self.win.config(menu=menubar)


        self.win.mainloop()

    def IncreaseFont(self):
        size = self.customFont['size']
        self.customFont.configure(size=size + 2)

    def DecreaseFont(self):
        size = self.customFont['size']
        if size-2>0:
            self.customFont.configure(size=size - 2)

    def Exit(self):
        result = messagebox.askyesnocancel(title="Python",message="Would you like to save the data?")
        if result:
            self.Save()
            self.win.destroy()
        else:
            pass

    def Open(self):
        cwd = os.getcwd()
        self.filename=filedialog.askopenfilename(initialdir=cwd, title="Select file",
                                   filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        print(self.filename)
        if not self.filename:
            return
        with open(self.filename,mode='r') as f:
            self.editArea.insert('1.0', f.read())

    def Save(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return
        with f:
            text2save = str(self.editArea.get(1.0, "end"))  # starts from `1.0`, not `0.0`
            f.write(text2save)

    def Rename(self):
        if self.filename:
            pathToDir=os.path.dirname(self.filename)
            f = filedialog.asksaveasfile(mode='w', defaultextension=".txt", initialdir=pathToDir)
            if f:
                print(f)
                shutil.move(self.filename, f.name)
                self.filename=f.name
        else:
            self.Save()


app=App()