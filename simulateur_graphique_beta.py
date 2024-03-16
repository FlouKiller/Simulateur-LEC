from objets import *
from random import randint
from tkinter import *

main = Tk()
main.resizable(width=False, height=False)
main.geometry("1080x608")

def clear():
    for item in main.winfo_children():
            item.destroy()


def menuprincipal():
    clear()
    main.title("Tah le projet de NSI - Menu principal")
    
    simul_button = Button(text="Simulation", font=("Helvetica", 25), width=15, command=simulation)
    equipes_button = Button(text="Équipes", font=("Helvetica", 25), width=15, command=equipes)
    
    simul_button.place(x=400, y=200)
    equipes_button.place(x=400, y=300)
    
    
def simulation():
    clear()
    main.title("Tah le projet de NSI - Simulation")
    
    
    
    retour_button = Button(text="Retour", font=("Helvetica", 20), command=menuprincipal)
    retour_button.place(x=960, y=540)
  
  
def equipes():
    clear()
    main.title("Tah le projet de NSI - Équipes")
    
    logo_astralis = PhotoImage(file="assets/astralis.png")
    logo_excel = PhotoImage(file="assets/excel.png")
    logo_fnatic = PhotoImage(file="assets/fnatic.png")
    logo_g2 = PhotoImage(file="assets/g2esport.png")
    logo_mad = PhotoImage(file="assets/madlions.png")
    logo_msf = PhotoImage(file="assets/misfitsgaming.png")
    logo_rogue = PhotoImage(file="assets/rogue.png")
    logo_shalke = PhotoImage(file="assets/shalke04.png")
    logo_skgaming = PhotoImage(file="assets/skgaming.png")
    logo_vitality = PhotoImage(file="assets/vitality.png")
    logo_astralis.photo = logo_astralis
    logo_excel.photo = logo_excel
    logo_fnatic.photo = logo_fnatic
    logo_g2.photo = logo_g2
    logo_mad.photo = logo_mad
    logo_msf.photo = logo_msf
    logo_rogue.photo = logo_rogue
    logo_shalke.photo = logo_shalke
    logo_skgaming.photo = logo_skgaming
    logo_vitality.photo = logo_vitality
    
    label_logo_astralis = Label(image=logo_astralis)
    label_logo_astralis.bind("<Button-1>", lambda:menuprincipal)
    label_logo_excel = Label(image=logo_excel)
    label_logo_fnatic = Label(image=logo_fnatic)
    label_logo_g2 = Label(image=logo_g2)
    label_logo_mad = Label(image=logo_mad)
    label_logo_msf = Label(image=logo_msf)
    label_logo_rogue = Label(image=logo_rogue)
    label_logo_shalke = Label(image=logo_shalke)
    label_logo_skgaming = Label(image=logo_skgaming)
    label_logo_vitality = Label(image=logo_vitality)
    
    label_logo_astralis.place(x=100, y=0)
    label_logo_excel.place(x=100, y=100)
    label_logo_fnatic.place(x=100, y=200)
    label_logo_g2.place(x=100, y=300)
    label_logo_mad.place(x=100, y=400)
    label_logo_msf.place(x=880, y=0)
    label_logo_rogue.place(x=880, y=100)
    label_logo_shalke.place(x=880, y=200)
    label_logo_skgaming.place(x=880, y=300)
    label_logo_vitality.place(x=880, y=400)
   
    retour_button = Button(text="Retour", font=("Helvetica", 20), command=menuprincipal)
    retour_button.place(x=960, y=540)


menuprincipal()
main.mainloop()