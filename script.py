#!/usr/bin/env python3

#essai tkinter: tkinter._test()

#Importation des bibliothèques
#tkinter
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
#Système
import os
#Lecture csv
import csv


#Fonction lecture fichier
def openexample():
    file=".\\example.csv"
    os.startfile(file)

#Fonction lecture données sur csv données météo
def weatherdata():
    file=filedialog.askopenfilename(title="Please select your file")
    print (file)






#Fonction fenêtre pour rentrer les données climatiques pluie cumulées
def cumuldata(weatherroot):
    #Fermeture fenêtre précédente
    weatherroot.destroy()
    #Création de la fenêtre
    cumuldata=Tk()

    #Nom de la fenêtre
    cumuldata.title("IN-Palm indicator: planting \u2264 10 years Input data")
    #Définition de la taille de la fenêtre
    cumuldata.geometry("800x600")


#Fonction pour plantation inférieur ou égale à 10 ans
def weatherlower10 (root):
    #Fermeture fenêtre précédente
    root.destroy()
    #Création de la fenêtre
    weatherroot= Tk()

    #Nom de l'onglet de fenêtre
    weatherroot.title("IN-Palm indicator: planting \u2264 10 years Input data")
    #Définition de la taille de la fenêtre
    weatherroot.geometry("800x600")

    #Nom de la fenêtre
    introduction = (ttk.Label(weatherroot,
                                text="Input weather data",
                                justify="center",
                                font=("Aptos", 20)))  # parfaire le message
    introduction.pack(pady=5)

    #Texte d'indication type donnée de départ
    cumulativedata=(ttk.Label(weatherroot,text="You have cumulative monthly climate data \n(quantity (mm) and number of rainy days)",
                           justify="center",
                           font=("Ariel", 12)))#parfaire le message
    cumulativedata.place(relx=0.2, rely=0.2, anchor="center")

    dailydata=(ttk.Label(weatherroot,text="You have daily data in csv format like ",
                         justify="center",
                         font=("Ariel", 12)))#parfaire le message
    dailydata.place(relx=0.7, rely=0.2, anchor="center")

    #Création des boutons
    #Bouton pour données climatiques cumulées
    buttoncumuldata = tkinter.Button(weatherroot, text="Click here",
                                 font=("Ariel",12,"bold"), anchor="center",
                                 bg="blue",fg="white",activebackground = "lightgreen",
                                 command=lambda: cumuldata(weatherroot))
    buttoncumuldata.place(relx=0.2, rely=0.3, anchor="center")

    #Bouton exemple
    example=tkinter.Button(weatherroot, text="Example",
                           font=("Ariel",12,"bold"), anchor="center",
                           bg="blue",fg="white",activebackground = "lightgreen",
                           command=openexample)
    example.place(relx=0.92, rely=0.2, anchor="center")


    # Bouton pour données climatiques journalière
    dailydata = tkinter.Button(weatherroot, text="Click here",
                             font=("Ariel", 12, "bold"), anchor="center",
                             bg="blue", fg="white", activebackground="lightgreen",
                             command=weatherdata)
    dailydata.place(relx=0.7, rely=0.3, anchor="center")

    weatherroot.mainloop()


#Fonction page d'accueil et choix age plantation
def ageplantation():
    root=Tk()
    #Définition du titre
    root.title("IN-Palm indicator")#Voir pour changement couleur de la bordure
    #Définition de la taille de l'écran
    widthroot=root.winfo_screenwidth()
    heightroot=root.winfo_screenheight()
    root.geometry(f"{widthroot}x{heightroot}")
    #Texte de bienvenue
    welcometext=(ttk.Label(root, text="Welcome to IN-Palm indicator\n Here explication\n Now entry data",
                           font=("Aptos",28), justify="center" )) #parfaire le message d'accueil
    welcometext.place(relx=0.5, rely=0.3, anchor="center")

    #Insertion des boutons choix age plantation
    #Bouton plantation =<10 ans
    buttonloweregal10years = tkinter.Button(root, text='Planting \u2264 10 years',
                                            font=("Ariel",12,"bold"),anchor='center',
                                            bg="#33ff61",activebackground="lightblue",
                                            command=lambda: weatherlower10(root))
    buttonloweregal10years.place(relx=0.3, rely=0.8, anchor="center", width=150, height=100)
    # Bouton plantation >10 ans
    buttonhigher10years = tkinter.Button(root, text='Planting > 10 years',
                                         font=("Ariel",12, "bold"),anchor="center",
                                         bg="#33ff61", activebackground="lightblue",
                                         command=ageplantation)
    buttonhigher10years.place(relx=0.7, rely=0.8, anchor="center",width=150, height=100)


    root.mainloop()


ageplantation()




