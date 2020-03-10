import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import os
from tkinter import messagebox


class Phone:
    def __init__(self):
        root = tk.Tk()
        root.title('Phonebook')
        self.df_path = os.path.join(os.getcwd(), 'book'
                                                 '.xls')
        self.book = pd.DataFrame(columns=['name', 'last', 'num'])
        self.book['name'].astype('str')
        self.book['last'].astype('str')
        self.book['num'].astype('str')
        self.work_book = pd.DataFrame(columns=['name', 'last', 'num'])
        self.work_book['num'].astype('str')
        self.search_book = pd.DataFrame(columns=['name', 'last', 'num'])
        info_frame = ttk.Labelframe(root, text='Info')
        name_label = tk.Label(info_frame, text='Name')
        self.nameEntry = tk.Entry(info_frame)
        name_label.grid(row=0, column=0)
        self.nameEntry.grid(row=0, column=1)

        lastname_label = tk.Label(info_frame, text='Last Name')
        self.lastnameEntry = tk.Entry(info_frame)
        lastname_label.grid(row=1, column=0)
        self.lastnameEntry.grid(row=1, column=1)

        number_label = tk.Label(info_frame, text='Number')
        self.numberEntry = tk.Entry(info_frame)
        self.numberEntry.insert(0, '+')
        number_label.grid(row=2, column=0)
        self.numberEntry.grid(row=2, column=1)
        ttk.Button(info_frame, text='Add', command=self.add).grid(row=0, column=2, rowspan=3, columnspan=3)

        info_frame.grid(row=0, column=0)

        tools_frame = ttk.Labelframe(root, text='Tools')

        ttk.Button(tools_frame, text='Delete all', command=self.delete_all).grid(row=0, column=0)
        ttk.Button(tools_frame, text='Delete part', command=self.delete).grid(row=1, column=0)
        ttk.Button(tools_frame, text='Edit', command=self.edit).grid(row=0, column=1)
        ttk.Button(tools_frame, text='Save', command=self.save_data).grid(row=1, column=1)
        ttk.Button(tools_frame, text='Import data', command=self.import_data).grid(row=2, column=0, rowspan=1,
                                                                                   columnspan=2)

        tools_frame.grid(row=0, column=1)

        treeview_frame = tk.Frame(root)
        self.tree = ttk.Treeview(treeview_frame, columns=('Name', 'Lastname', 'Number'), show='headings')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Lastname', text='Last Name')
        self.tree.heading('Number', text='Number')

        self.tree.grid(row=0, column=0)
        treeview_frame.grid(row=1, column=0, columnspan=2)

        search_frame = ttk.Labelframe(root, text='Search')
        self.search_text = ttk.Entry(search_frame)
        self.search_text.grid(row=0, column=0)
        self.r_var = tk.IntVar()
        ttk.Button(search_frame, text='Search', command=self.search).grid(row=0, column=1, padx=5)
        ttk.Radiobutton(search_frame, text='Name', variable=self.r_var, value=1).grid(row=0, column=2, padx=5)
        ttk.Radiobutton(search_frame, text='Last Name', variable=self.r_var, value=2).grid(row=0, column=3, padx=5)
        ttk.Radiobutton(search_frame, text='Number', variable=self.r_var, value=3).grid(row=0, column=4, padx=5)
        ttk.Button(search_frame, text='Clean', command=self.clean_search).grid(row=0, column=5, padx=5)
        search_frame.grid(row=2, column=0, columnspan=2)

        self.numbers = []

        root.mainloop()

    def add(self):
        if self.validation(self.nameEntry.get(), self.lastnameEntry.get(), self.numberEntry.get(), False):
            self.work_book.loc[len(self.work_book)] = [self.nameEntry.get(),
                                                       self.lastnameEntry.get(),
                                                       (self.numberEntry.get())]
            self.tree.insert('', tk.END, value=(self.nameEntry.get(), self.lastnameEntry.get(), self.numberEntry.get()))
            self.nameEntry.delete(0, tk.END)
            self.lastnameEntry.delete(0, tk.END)
            self.numberEntry.delete(0, tk.END)
            self.numberEntry.insert(0, '+')

    def delete_all(self):
        self.tree.delete(*self.tree.get_children())
        self.work_book.drop(['name', 'last', 'num'], axis=1, inplace=True)
        self.work_book = pd.DataFrame(columns=['name', 'last', 'num'])

    def delete(self):
        for selected_item in self.tree.selection():
            number = '+' + str(list(self.tree.item(selected_item).values())[2][2])
            self.numbers.append(number)
            self.tree.delete(selected_item)
        for item in self.numbers:
            self.work_book = self.work_book[self.work_book['num'] != item].reset_index(drop=True)
            self.numbers = []

    def save_data(self):
        self.book = self.work_book.drop_duplicates()
        self.book.to_excel(self.df_path, index=False)
        tk.messagebox.showinfo("Save", "Saved successfully")
        # print(self.book)

    def import_data(self):
        self.tree.delete(*self.tree.get_children())
        try:
            self.book = pd.read_excel(self.df_path, dtype=str)
        except:
            self.book = pd.DataFrame(columns=['name', 'last', 'num'])
        frames = [self.book, self.work_book]
        self.work_book = pd.concat(frames).reset_index(drop=True)
        self.work_book = self.work_book.drop_duplicates()
        self.work_book = self.work_book.reset_index(drop=True)
        for i in range(0, len(self.work_book)):
            self.tree.insert('', tk.END,
                             value=(self.work_book.loc[i, 'name'], self.work_book.loc[i, 'last'], self.work_book.loc[i, 'num']))

    def search(self):
        self.tree.delete(*self.tree.get_children())
        self.search_book = pd.read_excel(self.df_path, dtype=str)

        if self.r_var.get() == 1:
            self.search_book = self.book[self.book['name'] == self.search_text.get()].reset_index(drop=True)
            for i in range(0, len(self.search_book)):
                self.tree.insert('', tk.END, value=(self.search_book.loc[i, 'name'], self.search_book.loc[i, 'last'],
                                                    self.search_book.loc[i, 'num']))
        elif self.r_var.get() == 2:
            self.search_book = self.book[self.book['last'] == self.search_text.get()].reset_index(drop=True)
            for i in range(0, len(self.search_book)):
                self.tree.insert('', tk.END, value=(self.search_book.loc[i, 'name'], self.search_book.loc[i, 'last'],
                                                    self.search_book.loc[i, 'num']))
        if self.r_var.get() == 3:
            if self.search_text.get()[0] == '+':
                self.search_book = self.book[self.book['num'] == self.search_text.get()].reset_index(drop=True)
                for i in range(0, len(self.search_book)):
                    self.tree.insert('', tk.END, value=(self.search_book.loc[i, 'name'],
                                                        self.search_book.loc[i, 'last'],
                                                        self.search_book.loc[i, 'num']))
            elif self.search_text.get().isnumeric:
                self.search_book = self.book[self.book['num'] == '+' + self.search_text.get()].reset_index(drop=True)
                for i in range(0, len(self.search_book)):
                    self.tree.insert('', tk.END, value=(self.search_book.loc[i, 'name'],
                                                        self.search_book.loc[i, 'last'],
                                                        self.search_book.loc[i, 'num']))

        self.search_text.delete(0, tk.END)

    def clean_search(self):
        self.search_text.delete(0, tk.END)
        self.tree.delete(*self.tree.get_children())
        self.r_var.set(0)

    def edit(self):
        if len(self.tree.selection()) > 0:
            self.edit_win = tk.Toplevel()
            self.edit_win.title('Edit')
            self.edit_item = self.tree.selection()[0]
            self.edit_item_list = list(self.tree.item(self.edit_item).values())[2]

            tk.Label(self.edit_win, text='Change name').grid(row=0, column=0)
            tk.Label(self.edit_win, text='Change last name').grid(row=1, column=0)
            tk.Label(self.edit_win, text='Change number').grid(row=2, column=0)

            self.new_name = tk.Entry(self.edit_win)
            self.new_lastname = tk.Entry(self.edit_win)
            self.new_num = tk.Entry(self.edit_win)

            self.new_name.grid(row=0, column=1)
            self.new_lastname.grid(row=1, column=1)
            self.new_num.grid(row=2, column=1)

            tk.Button(self.edit_win, text='Ok', command=self.ok).grid(row=3, column=0, columnspan=2)

            self.new_name.insert(0, self.edit_item_list[0])
            self.new_lastname.insert(0, self.edit_item_list[1])
            self.new_num.insert(0, '+' + str(self.edit_item_list[2]))
        else:
            tk.messagebox.showerror('Error', 'Please, select the line you want to change')

    def ok(self):
        changed_name = self.new_name.get()
        changed_last = self.new_lastname.get()
        changed_num = self.new_num.get()

        if self.validation(changed_name, changed_last, changed_num, True):
            num = '+' + str(self.edit_item_list[2])
            self.work_book = self.work_book[self.work_book['num'] != num].reset_index(drop=True)
            self.tree.delete(self.edit_item)
            self.work_book.loc[len(self.work_book)] = [changed_name, changed_last, str(changed_num)]
            self.tree.insert('', tk.END, value=(changed_name, changed_last, changed_num))
            self.edit_win.destroy()

    def validation(self, name, last, number, edit=False):
        if len(name) == 0:
            tk.messagebox.showerror('Error', 'Write name')
            return False

        if len(last) == 0:
            tk.messagebox.showerror('Error', "Write last name")
            return False

        if number == '+':
            tk.messagebox.showerror('Error', "Write number")
            return False

        if len(number) == 0 or number[0] != '+' or not number[1:].isnumeric() or number[1] == '0':
            tk.messagebox.showerror('Error', 'The number must begin with +, the first digit must not be 0')
            if edit:
                self.new_num.delete(0, tk.END)
                self.new_num.insert(0, '+')
            else:
                self.numberEntry.delete(0, tk.END)
                self.numberEntry.insert(0, '+')
            return False

        return True


Phone()
