import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime as dt
import Marari as mr
import Controle as ct
import Fenetre as fn
import DateInvalide as di


def inscri():
    anarana = valeurnom.get()
    daty = valeurdaty.get()
    temperature = valtemperature.get()
    o2 = valeuro2.get()
    malade = mr.Marary()
    malade.insertMarary(anarana)
    malade2 = ct.Controle()
    malade2.insertControle(anarana, daty, temperature, o2)
    messagebox.showinfo("Succès", "Données insérer avec succès")


def insertDonnees():
    anarana = valeurnom.get()
    daty = valeurdaty.get()
    temperature = valtemperature.get()
    o2 = valeuro2.get()
    control = ct.Controle()
    valiny = control.getDaty(anarana)
    for i in range(len(valiny)):
        for j in range(len(valiny[i])):
            valiny = valiny[i][j]
    datyvrai = dt.datetime.strptime(daty, '%Y-%m-%d').date()
    print(datyvrai)
    print(valiny)
    if valiny > datyvrai:
        messagebox.showerror("Erreur", "Date invalide: Date inferieur au dernier controle du patient")
        raise di.DateInvalide(datyvrai, valiny)
    else:
        print("mety")
        malade2 = ct.Controle()
        malade2.insertControle(anarana, daty, temperature, o2)
        messagebox.showinfo("Succès", "Données insérer avec succès")


def showGraph():
    anarana = typeanarana.get()
    fn.showGraphMaro1(anarana)


def fillTabel():
    valeur = ct.Controle().getDonnees()
    for row in tabel.get_children():
        tabel.delete(row)
    for row in valeur:
        tabel.insert("", tk.END, text=row[0], values=(row[1], row[2], row[3]))


def showGraphFillTabel():
    showGraph()
    fillTabel()


def makaanarana():
    anaranas = []
    check = c.get()
    check1 = c1.get()
    check2 = c2.get()
    check3 = c3.get()
    check4 = c4.get()
    check5 = c5.get()
    check6 = c6.get()
    check7 = c7.get()
    check8 = c8.get()
    check9 = c9.get()
    if check == "Jean":
        anaranas.append("Jean")
    if check1 == "Lucas":
        anaranas.append("Lucas")
    if check2 == "Charo":
        anaranas.append("Charo")
    fn.showGraphMaro(anaranas)
    print(anaranas)


graph = tk.Tk()
graph.title("Fomulaire d'inscription et de details")
graph.geometry("850x480")

# frame inscription
inscription = tk.LabelFrame(graph, text="Inscription", width=300, height=300, borderwidth=1, padx=5)
# widget inscription
nom = tk.Label(inscription, text="Nom: ")
valeurnom = tk.StringVar()
valnom = tk.Entry(inscription, textvariable=valeurnom)

daty = tk.Label(inscription, text="Jour: ")
valeurdaty = tk.StringVar()
datynidirana = tk.Entry(inscription, textvariable=valeurdaty)

temperature = tk.Label(inscription, text="Temperature (°C): ")
valeurtemperature = tk.DoubleVar()
valtemperature = tk.Entry(inscription, textvariable=valeurtemperature)

tauxO2 = tk.Label(inscription, text="Taux d'O2 (en %): ")
valeuro2 = tk.DoubleVar()
valo2 = tk.Entry(inscription, textvariable=valeuro2)

validerInscription = tk.Button(inscription, text="S'inscrire", command=inscri)
validerDonnees = tk.Button(inscription, text="Donnees", command=insertDonnees)
# inscription -> widget
nom.grid(row=0, column=0, padx=5, pady=5)
valnom.grid(row=0, column=2, pady=5)

daty.grid(row=1, column=0, padx=5, pady=5)
datynidirana.grid(row=1, column=2, pady=5)

temperature.grid(row=2, column=0, pady=5)
valtemperature.grid(row=2, column=2, pady=5)

tauxO2.grid(row=3, column=0, pady=5)
valo2.grid(row=3, column=2, pady=5)
validerInscription.grid(row=4, column=1, pady=5)
validerDonnees.grid(row=4, column=2, pady=5)

# frame details
details = tk.LabelFrame(graph, text="Details", width=350, height=300, borderwidth=1, padx=5)
# details widget
anarana = tk.Label(details, text="Patient à détailler: ")
typeanarana = tk.StringVar()
anaranavaleur = tk.Entry(details, textvariable=typeanarana)

detailler = tk.Button(details, text="Detailler", command=showGraphFillTabel)

# details -> widget
anarana.grid(row=0, column=0, padx=5, pady=5)
anaranavaleur.grid(row=0, column=2, pady=5, padx=5)

detailler.grid(row=1, column=2, padx=5, pady=5)

# frame donnees
donnees = tk.LabelFrame(graph, text="Donnees", width=800, height=900, borderwidth=1, padx=5)

# donnees widget
tabel = ttk.Treeview(donnees, columns=('Nom', 'Date', 'Temperature', 'Oxygene'))
tabel.heading('#0', text='Nom')
tabel.heading('Nom', text='Date')
tabel.heading('Date', text='Temperature (en °C)')
tabel.heading('Temperature', text='Oxygene (en %)')

# donnees -> widget
tabel.place(x=0, y=0, width=800, height=300)

name = tk.LabelFrame(graph, text="Anarana", padx=5)

c = tk.StringVar()
c1 = tk.StringVar()
c2 = tk.StringVar()
c3 = tk.StringVar()
c4 = tk.StringVar()
c5 = tk.StringVar()
c6 = tk.StringVar()
c7 = tk.StringVar()
c8 = tk.StringVar()
c9 = tk.StringVar()

checkbox = tk.Checkbutton(name, text="Jean", variable=c, onvalue="Jean")
checkbox1 = tk.Checkbutton(name, text="Lucas", variable=c1, onvalue="Lucas")
checkbox2 = tk.Checkbutton(name, text="Charo", variable=c2, onvalue="Charo")
checkbox3 = tk.Checkbutton(name, text="Solofo", variable=c3, onvalue="Solofo")
checkbox4 = tk.Checkbutton(name, text="Aina", variable=c4, onvalue="Aina")
checkbox5 = tk.Checkbutton(name, text="Rabe", variable=c5, onvalue="Rabe")
checkbox6 = tk.Checkbutton(name, text="Rakoto", variable=c6, onvalue="Rakoto")
checkbox7 = tk.Checkbutton(name, text="Niaina", variable=c7, onvalue="Rakoto")
checkbox8 = tk.Checkbutton(name, text="Rajo", variable=c8, onvalue="Niaina")
checkbox9 = tk.Checkbutton(name, text="Jhon", variable=c9, onvalue="Jhon")

btn = tk.Button(name, text="show", command=makaanarana)

checkbox.grid(row=0, column=0, padx=5)
checkbox1.grid(row=0, column=1, padx=5)
checkbox2.grid(row=0, column=2, padx=5)
checkbox3.grid(row=0, column=3, padx=5)
checkbox4.grid(row=0, column=4, padx=5)
checkbox5.grid(row=1, column=0, padx=5)
checkbox6.grid(row=1, column=1, padx=5)
checkbox7.grid(row=1, column=2, padx=5)
checkbox8.grid(row=1, column=3, padx=5)
checkbox9.grid(row=1, column=4, padx=5)

btn.grid(row=2, column=4, padx=5)

# Frame -> Graph
inscription.grid(row=0, column=0, padx=5)
details.place(x=450, y=2)
donnees.place(x=5, y=200)
name.place(x=450, y=100)

graph.mainloop()
