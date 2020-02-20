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
        self.query = tk.StringVar()
        self.query2 = tk.StringVar()
        frame1 = tk.Frame(
            master=self.win,
             background = 'green'
        )
        frame1.pack(fill='both', expand='yes')
        self.editArea = tkst.ScrolledText(
            master=frame1,
            wrap=tk.WORD,
            font=self.customFont,
        )

        self.editArea.pack(padx=1, pady=1, fill=tk.BOTH, expand=True)
        self.editArea.focus_set()

        menubar = tk.Menu(self.win)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="?", command=self.Help)

        # create a pulldown menu, and add it to the menu bar
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.Open)
        filemenu.add_command(label="Save", command=self.Save)

        #filemenu.add_command(label="Rename", command=self.Rename)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.Exit)
        menubar.add_cascade(label="File",  menu=filemenu)
        fontMenu=tk.Menu(menubar, tearoff=1)
        fontMenu.add_command(label="IncreaseFont", command=self.IncreaseFont)
        fontMenu.add_command(label="DecreaseFont", command=self.DecreaseFont)
        menubar.add_cascade(label="Font", menu=fontMenu)
        searchMenu= tk.Menu(menubar, tearoff= 0)
        searchMenu.add_command(label="Count", command = self.count)
        searchMenu.add_command(label="Replace", command=self.replace)
        menubar.add_cascade(label="Search", menu=searchMenu )
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.win.config(menu=menubar)
        self.InitConfig()
        self.win.mainloop()


    def IncreaseFont(self):
        size = self.customFont['size']
        self.customFont.configure(size=size + 2)

    def DecreaseFont(self):
        size = self.customFont['size']
        if size-2>0:
            self.customFont.configure(size=size - 2)

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
        print(f.name)
        print(type(f))
        with f:
            text2save = str(self.editArea.get(1.0, "end"))  # starts from `1.0`, not `0.0`
            f.write(text2save)
            cwd = os.getcwd()
            configFilePath = os.path.join(cwd, "config.txt")
            try:
                with open(configFilePath, mode='w') as cf:
                    cf.write(f.name)
            except FileNotFoundError:
                return


    def Exit(self):
        result = messagebox.askyesnocancel(title="Python",message="Would you like to save the data?")
        print(result)
        if result:
            self.Save()
            self.win.destroy()
        elif result==None:
            pass
        else:
            self.win.destroy()

    def count(self):
        self.result = tk.Toplevel()
        self.result.title('Count')
        self.result.geometry('400x150')
        tk.Label(self.result, text="Unesite izraz za pretragu").pack()
        tk.Entry(self.result, textvariable=self.query).pack()
        tk.Button(self.result, text="OK", command=self.DestroyResult).pack()

    def DestroyResult(self):
        self.result.destroy()
        unetiTekst=self.query.get()
        messageResult=tk.Toplevel()
        textInArea = str(self.editArea.get(1.0, "end"))
        c = textInArea.count(unetiTekst)
        messageResult.title("Rezultat")
        tk.Label(messageResult, text="U tekstu se nalazi {} puta {}".format(c,unetiTekst)).pack()
        tk.Button(messageResult, text="OK", command=messageResult.destroy).pack()

    def replace(self):
        self.replaceWindow = tk.Toplevel()
        tk.Label(self.replaceWindow,text="Unesite izraz koji se menja: ").grid(row=0, column=0)
        tk.Entry(self.replaceWindow, textvariable = self.query).grid(row=0, column=1)
        tk.Label(self.replaceWindow,text="Unesite izraz kojim se menja: ").grid(row=1, column=0)
        tk.Entry(self.replaceWindow, textvariable = self.query2).grid(row=1, column=1)
        tk.Button(self.replaceWindow,text="REPLACE", command = self.DestroyReplace).grid(row=1, column=2)


    def DestroyReplace(self):
        self.replaceWindow.destroy()
        textInArea = str(self.editArea.get(1.0, "end"))
        textInArea = textInArea.replace(self.query.get(),self.query2.get())
        self.editArea.delete(1.0,"end")
        self.editArea.insert(tk.END,textInArea)
        self.query.set("")
        self.query2.set("")

    def Help(self):
        messagebox.showinfo("Help","Ovo je aplikacija koju je radila cetvrta grupa")

    def InitConfig(self):
        cwd = os.getcwd()
        configFilePath = os.path.join(cwd,"config.txt")
        try:
            with open(configFilePath,mode='r') as f:
                self.filename = f.read()
        except FileNotFoundError:
            #TO-DO za domaci uradite da ako nema config.txt fajla da se napravi
            return
        try:
            with open(self.filename, mode='r') as f:
                self.editArea.insert('1.0', f.read())

        except:
            pass



app=App()