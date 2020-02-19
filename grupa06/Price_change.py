from tkinter import *
import tkinter.ttk as ttk


def check(a, b, c, d):
    if a.isnumeric() and b.isnumeric():
        first_res = f'{a}.{b}'
    elif a.isnumeric() and b == '':
        first_res = f'{a}.00'
    elif a == '' and b.isnumeric():
        first_res = f'0.{b}'
    else:
        first_res = 'incorrect'

    if c.isnumeric() and d.isnumeric():
        second_res = f'{c}.{d}'
    elif c.isnumeric() and d == '':
        second_res = f'{c}.00'
    elif c == '' and d.isnumeric():
        second_res = f'0.{d}'
    else:
        second_res = 'incorrect'
    result.set(f'Old price is {first_res},\nnew price is {second_res}')


def clean():
    oldPriceFirst.delete(0, END)
    oldPriceSecond.delete(0, END)
    newPriceFirst.delete(0, END)
    newPriceSecond.delete(0, END)
    result.set('Please, click button')
    oldPriceFirst.focus()


root = Tk()
root.title('Price check')

priceFrame = ttk.LabelFrame(root, text='Price')

ttk.Label(priceFrame, text='Old Price').grid(row=0, column=0)
oldPriceFirst = Entry(priceFrame, justify=RIGHT)
oldPriceFirst.focus()
oldPriceFirst.grid(row=0, column=1)
ttk.Label(priceFrame, text='.').grid(row=0, column=2)
oldPriceSecond = Entry(priceFrame, width=2)
oldPriceSecond.grid(row=0, column=3)

ttk.Label(priceFrame, text='New Price').grid(row=1, column=0)
newPriceFirst = Entry(priceFrame, justify=RIGHT)
newPriceFirst.grid(row=1, column=1)
ttk.Label(priceFrame, text='.').grid(row=1, column=2)
newPriceSecond = Entry(priceFrame, width=2)
newPriceSecond.grid(row=1, column=3)

buttFrame = Frame(root)
ttk.Button(buttFrame, text='Check', command=lambda: check(oldPriceFirst.get(), oldPriceSecond.get(),
                                                          newPriceFirst.get(), newPriceSecond.get())).pack(fill=X)
ttk.Button(buttFrame, text='Clean', command=clean).pack(fill=X)

resultFrame = ttk.LabelFrame(root, text='Result')
result = StringVar()
result.set('Please, click button')
resultLabel = ttk.Label(resultFrame, textvariable=result, justify=CENTER, wraplength=250)
resultLabel.pack()

priceFrame.pack()
buttFrame.pack(fill=X)
resultFrame.pack(fill=X)


root.mainloop()

