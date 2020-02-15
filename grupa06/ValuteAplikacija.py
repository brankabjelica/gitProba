import tkinter as tk

valute=[]

def snimi():
    name=ime.get().upper()
    value=iznos.get().upper()
    valute.append((name, value))
    ime.set("")
    iznos.set("")
    ent1.focus()

def vidiListu():
    string=""
    for ime,iznos in valute:
        p="\n"+ime+" - "+iznos+" dinara"
        string+=p
    if string=="":
        label4.config(text="Lista je prazna.")
    else:
        label4.config(text=string)

def konvertuj():
    lista2 = [k for k, v in valute]
    ime2=ime.get().upper()
    iznos2=iznos.get()
    if ime2 in lista2:
        for ime1, iznos1 in valute:
            if ime1 == ime2:
                rez = iznos2 + " " + ime2 + " je: " + str(float(iznos2)*float(iznos1)) + " dinara."
                label4.config(text=rez)
    else:
        rez1 = "Valuta " + ime2 + " nije uneta u listu valuta."
        label4.config(text = rez1)
    ime.set("")
    iznos.set("")
    ent1.focus()

def ocistiListu():
    valute.clear()
    label4.config(text="Lista valuta je sada prazna.")

glavni=tk.Tk()
glavni.title("Konverzija valuta")

obavestenje=tk.Frame(glavni)
unos=tk.Frame(glavni)
dugmici=tk.Frame(glavni)
rezultat=tk.Frame(glavni)

obavestenje.pack()
unos.pack()
dugmici.pack()
rezultat.pack()

textObavestenja='OBAVESTENJE:\nPre konverzije, morate uneti u listu valute i njihov kurs izrazen u dinarima.\nDa unesete valute u listu popunite odgovarajuca polja i kliknite na dugme "Snimi".\nMoguca je samo konverzija u dinare.\nDa biste izvrsili konverziju, unesite valutu i iznos koji zelite da konvertujete u dinare u odgovarajuca polja i kliknite na dugme "Konvertuj".'
msg = tk.Message(obavestenje, text = textObavestenja)
msg.config(font=('times',10))
msg.pack()

label1=tk.Label(unos, text="Ime valute: ").grid(row=0,column=0)
label2=tk.Label(unos, text="Iznos valute u dinarima: ").grid(row=1,column=0)

ime = tk.StringVar()
iznos = tk.StringVar()

ent1=tk.Entry(unos, textvariable = ime)
ent1.grid(row=0,column=1)
ent2=tk.Entry(unos, textvariable = iznos)
ent2.grid(row=1,column=1)

b1 = tk.Button(dugmici, text=' Snimi ', command=snimi)
b1.pack(side=tk.LEFT)
b2 = tk.Button(dugmici, text=' Konvertuj ', command=konvertuj)
b2.pack(side=tk.LEFT)
b4 = tk.Button(dugmici, text=' Ocisti listu ', command=ocistiListu)
b4.pack(side=tk.LEFT)
b5 = tk.Button(dugmici, text=' Vidi listu ', command=vidiListu)
b5.pack(side=tk.LEFT)

label3=tk.Label(rezultat, text="\nODGOVOR:").pack()
label4=tk.Label(rezultat, text="")
label4.pack()

ent1.focus()

glavni.mainloop()
