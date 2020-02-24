import tkinter as tk
import tkinter.scrolledtext as tkst
import tkinter.font as tkfont
from tkinter import messagebox
from tkinter import filedialog
import os


class AppText:
    def __init__(self, file_path=None):
        self.root = tk.Tk()
        self.root.title('Text')
        self.root.protocol('WM_DELETE_WINDOW', self.exit)
        self.origin_font = tkfont.Font(family='Courier', size=12)
        self.file_path = file_path
        first_frame = tk.Frame(master=self.root)
        first_frame.pack(fill='both', expand='yes')
        self.text_area = tkst.ScrolledText(master=first_frame, wrap=tk.WORD, font=self.origin_font)
        self.text_area.pack(fill='both', expand='yes')

        main_menu = tk.Menu(self.root)

        file_menu = tk.Menu(main_menu, tearoff=0)
        file_menu.add_command(label='Open', command=self.open)
        file_menu.add_command(label='Save', command=self.save)

        change_menu = tk.Menu(main_menu, tearoff=1)

        change_font = tk.Menu(change_menu, tearoff=0)
        change_font.add_command(label='Times', command=lambda: self.ch_font('Times'))
        change_font.add_command(label='Helvetica', command=lambda: self.ch_font('Helvetica'))
        change_font.add_command(label='Origin (Courier)', command=lambda: self.ch_font('Courier'))

        change_back = tk.Menu(change_menu, tearoff=0)
        change_back.add_command(label='Red', command=lambda: self.ch_back('red'))
        change_back.add_command(label='Yellow', command=lambda: self.ch_back('yellow'))
        change_back.add_command(label='Blue', command=lambda: self.ch_back('blue'))
        change_back.add_command(label='Origin (White)', command=lambda: self.ch_back('white'))

        change_menu.add_cascade(label='Change font', menu=change_font)
        change_menu.add_cascade(label='Change background', menu=change_back)

        count_menu = tk.Menu(main_menu, tearoff=0)
        count_menu.add_command(label='With spaces', command=self.spaces)
        count_menu.add_command(label='Without spaces', command=self.no_spaces)

        main_menu.add_cascade(label='File', menu=file_menu)
        main_menu.add_cascade(label='Change', menu=change_menu)
        main_menu.add_cascade(label='Amount of symbols', menu=count_menu)

        self.root.config(menu=main_menu)
        self.use_config()
        self.root.mainloop()

    def open(self):
        folder_path = os.getcwd()
        self.file_path = filedialog.askopenfilename(initialdir=folder_path, title='Select file',
                                                    filetypes=(('txt files', '*.txt'), ('all files', '*.*')))
        if not self.file_path:
            return
        self.text_area.delete('1.0', 'end')
        with open(self.file_path, mode='r') as f:
            self.text_area.insert('1.0', f.read())

    def save(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if f is None:
            return
        with f:
            saved_text = str(self.text_area.get(1.0, 'end'))
            f.write(saved_text)
            folder_path = os.getcwd()
            config_path = os.path.join(folder_path, 'config.txt')
            try:
                with open(config_path, mode='w') as c:
                    c.write(f.name)
            except FileNotFoundError:
                return

    def exit(self):
        result = messagebox.askyesnocancel(title='Saving', message='Would you like to save the data?')
        if result:
            self.save()
            self.root.destroy()
        elif result is None:
            pass
        else:
            self.root.destroy()

    def ch_font(self, fontname):
        self.origin_font.configure(family=fontname)

    def ch_back(self, color):
        self.text_area.configure(background=color)

    def spaces(self):
        self.new_win = tk.Toplevel()
        self.new_win.title('Amount of symbols')
        self.new_win.geometry('300x50')
        line = str(self.text_area.get(1.0, 'end'))
        invis = line.count('\f') + line.count('\n') + line.count('\r') + line.count('\t') + line.count('\v')
        amount = len(line) - invis
        tk.Label(self.new_win, text=f'There are {amount} symbols in text\n(with spaces)', justify='center').pack()

    def no_spaces(self):
        self.new_win = tk.Toplevel()
        self.new_win.title('Amount of symbols')
        self.new_win.geometry('300x50')
        line = str(self.text_area.get(1.0, 'end'))
        invis = line.count('\f') + line.count('\n') + line.count('\r') + line.count('\t') + line.count('\v')
        amount = len(line) - line.count(' ') - invis
        tk.Label(self.new_win, text=f'There are {amount} symbols in text\n(without spaces)', justify='center').pack()

    def use_config(self):
        folder_path = os.getcwd()
        config_path = os.path.join(folder_path, 'config.txt')
        try:
            with open(config_path, mode='r') as c:
                self.file_path = c.read()
        except FileNotFoundError:
            open(config_path, mode='x').close()
        try:
            with open(self.file_path, mode='r') as f:
                self.text_area.insert('1.0', f.read())
        except:
            pass


AppText()





