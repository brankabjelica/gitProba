import tkinter as tk
from tkinter import messagebox

glavni=tk.Tk()
glavni.title("Digitron")
prviFramee=tk.Frame(glavni)
drugiFramee=tk.Frame(glavni)
prviFramee.pack()
drugiFramee.pack()

def nula():
    v=str(rez.get())
    rez.set(v+"0")
def jedan():
    v=str(rez.get())
    rez.set(v+"1")
def dva():
    v=str(rez.get())
    rez.set(v+"2")
def tri():
    v = str(rez.get())
    rez.set(v + "3")
def cetiri():
    v = str(rez.get())
    rez.set(v + "4")
def pet():
    v = str(rez.get())
    rez.set(v + "5")
def sest():
    v=str(rez.get())
    rez.set(v+"6")
def sedam():
    v=str(rez.get())
    rez.set(v+"7")
def osam():
    v=str(rez.get())
    rez.set(v+"8")
def devet():
    v=str(rez.get())
    rez.set(v+"9")
def plus():
    v=str(rez.get())
    rez.set(v+"+")
def minus():
    v=str(rez.get())
    rez.set(v+"-")
def puta():
    v=str(rez.get())
    rez.set(v+"*")
def podeljeno():
    v=str(rez.get())
    rez.set(v+"/")
def obrisi():
    rez.set("")
def jednako():
    try:
        v=str(rez.get())
        y=eval(v)
        rez.set(y)
    except SyntaxError:
        rez.set("")
        messagebox.showerror("Greska","Broj ne moze pocinjati nulom!")
    except ZeroDivisionError:
        rez.set("")
        messagebox.showerror("Greska", "Zabranjeno je deljenje nulom!")

rez=tk.StringVar()

rezultat=tk.Label(prviFramee,text="",textvariable=rez).pack()

jedinica=tk.Button(drugiFramee, text='  1  ', command=jedan)
jedinica.grid(row=0,column=0)

dvojka=tk.Button(drugiFramee, text='  2  ', command=dva)
dvojka.grid(row=0,column=1)

trojka=tk.Button(drugiFramee, text='  3  ', command=tri)
trojka.grid(row=0,column=2)

pluss=tk.Button(drugiFramee, text='  +  ', command=plus)
pluss.grid(row=0,column=3)

cetvorka=tk.Button(drugiFramee, text='  4  ', command=cetiri)
cetvorka.grid(row=1,column=0)

petica=tk.Button(drugiFramee, text='  5  ', command=pet)
petica.grid(row=1,column=1)

sestica=tk.Button(drugiFramee, text='  6  ', command=sest)
sestica.grid(row=1,column=2)

minuss=tk.Button(drugiFramee, text='  -  ', command=minus)
minuss.grid(row=1,column=3)

sedmica=tk.Button(drugiFramee, text='  7  ', command=sedam)
sedmica.grid(row=2,column=0)

osmica=tk.Button(drugiFramee, text='  8  ', command=osam)
osmica.grid(row=2,column=1)

devetka=tk.Button(drugiFramee, text='  9  ', command=devet)
devetka.grid(row=2,column=2)

putaa=tk.Button(drugiFramee, text='  *  ', command=puta)
putaa.grid(row=2,column=3)

null=tk.Button(drugiFramee, text='  0  ', command=nula)
null.grid(row=3,column=0)

c=tk.Button(drugiFramee, text='  C  ', command=obrisi)
c.grid(row=3,column=1)

jednakoo=tk.Button(drugiFramee, text='  =  ', command=jednako)
jednakoo.grid(row=3,column=2)

deljenje=tk.Button(drugiFramee, text='  /  ', command=podeljeno)
deljenje.grid(row=3,column=3)

glavni.mainloop()