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

# Fonction qui sera appelée chaque fois qu'une sélection change
def update(*args):
    # Récupère l'élément sélectionné
    selectedtypeNfertivar= typeNfertivar.get()
    print(selectedtypeNfertivar)


def Managementpracticesinterface(functioncount,file_path):
    global typeNfertivar
    global Nfertiplacement
    infopracticeroot=Tk()
    #Nom de la fenêtre
    infopracticeroot.title("Management practice input")
    #Définition de la taille de la fenêtre
    widthscreen = infopracticeroot.winfo_screenwidth()
    heightscreen = infopracticeroot.winfo_screenheight()
    infopracticeroot.geometry(f"{widthscreen}x{heightscreen}")

    #Message titre
    label=(tkinter.Label(infopracticeroot,
                         text="Management practice",font=("Ariel",30,'bold')))
    label.pack()
    #Intégration message de confirmation sauvegarde données
    if functioncount==1:
        saveok=(tkinter.Label(infopracticeroot,
                              text=f"Data was been save on{file_path}",font=("Ariel",12,'italic'),
                              fg="blue"))
        saveok.place(relx=0.3,rely=0.07)

    #Intégration années
    year1=(tkinter.Label(infopracticeroot,
                         text="First year", font=("Ariel",20,'underline')))
    year1.place(relx=0.025, rely=0.1)

    #Listes de sélection

    Nfertiplacement=["*Choice*","In the circle","Evenly distributed"]
    Nfertiplacementinthecircle=["buried","not buried","windrow"]
    Orgafertitype=["EFB","Compost"]
    Orgafertiplacement=["In the circle","In the harvesting path","Spread (anti erosion)"]
    understoreybiomass=["Very high","High","Medium","Low","No"]
    understoreylegumefraction=["Very high","High","Medium","Low","No"]
    Prunedfronds=["Exported","In heaps","In windows","Spread (anti erosion"]

    #Intégration data mineral Nfertilizer


    #Nommage encadré
    frame = tkinter.Frame(infopracticeroot, bd=2, relief="solid", padx=10, pady=10)
    frame.place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.7)
    MineralNfertilizer=(tkinter.Label(frame,
                                      text="Mineral Nitrogen fertilizer",justify="center",
                                      font=("Ariel",13,"bold","underline")))
    MineralNfertilizer.place(rely=0.15,relx=0.15)
    #Intégration des mois
    January=(tkinter.Label(frame,
                           text="January",
                           font=("Ariel",9),fg="blue"))
    January.place(relx=0.04,rely=0.18)
    #Création du type
    type=(tkinter.Label(frame,
                        text="Type",
                        fg="blue",font=("Ariel",12,"bold")))
    type.place(relx=0.005,rely=0.205)

    #Liste déroulante
    typeNferti = ["*Choice*", "Ammonium Sulfate", "Urea", "Ammonicum Chloride", "Ammonium Nitrate", "Sodium Nitrate"]
    # Créer une variable Tkinter pour stocker l'élément sélectionné
    typeNfertivar = tkinter.StringVar()
    typeNfertivar.set(typeNferti[0])  # Sélection initiale (par défaut "Choice")

    # Lier la variable StringVar avec la fonction `update` à chaque changement
    typeNfertivar.trace("w", update)

    # Créer le widget OptionMenu
    option_menu = tkinter.OptionMenu(frame, typeNfertivar, *typeNferti)
    option_menu.place(relx=0.03, rely=0.20)

    # Création d'un encadré

    infopracticeroot.mainloop()



def savecsv(table,town,country):
    # Ouverture d'une boîte de dialogue pour choisir le dossier
    folder_path = filedialog.askdirectory(title="Please choose your directory save")

    #Dossier choisi
    if folder_path:
        # Définir le chemin complet du fichier CSV (nom de fichier prédéfini)
        file_path = os.path.join(folder_path, f"{town}_{country}_cumulmonthly_rainfall.csv")

        # Ouverture du fichier CSV en mode écriture
        with open(file_path, mode="w", newline="") as file:
            writer = csv.writer(file)

            # Création de l'en-tête du fichier CSV
            writer.writerow(["Year", "Month", "Rainfall(mm)","Rain frequency"])

            # Report de chaque ligne dans le csv
            for row in table.get_children():
                values = table.item(row)["values"]
                writer.writerow(values)
            Managementpracticesinterface(1,file_path)

def closeinfodicosave(infodico):
    infodico.destroy()

#Fonction données les infos csv et réécriture d'un fichier excel
def infodicosave(dictionnary, town, country) :
    #Création fenêtre de résumé:
    infodico=Tk()

    #Nom de la fenêtre
    infodico.title("Summary information and calculate information")

    infodico.geometry("1000x800")

    #Information localisation
    label=(tkinter.Label(infodico,text=f"Monthly cumulative rainy statement\n"
                                       f"Country:{country}\n"
                                       f"Town:{town}",
                         font=("Ariel",15)))
    label.pack(pady=20)

    #Création du tableau résumé
    table=ttk.Treeview(infodico,columns=("Year","Month","Rainfall","Frequency"),show="headings")
    #Insertion des entêtes
    table.heading("Year",text="Year")
    table.heading("Month",text="Month")
    table.heading("Rainfall",text="Rainfall(in mm)")
    table.heading("Frequency",text="Rain frequency (number of rainy days)")
    #Insertion des valeurs
    for (years, months) in dictionnary.items():
        for monthdata, data in months.items():
            table.insert("","end",values=(years,monthdata,data['Rainfall'], data['Rain frequency']))


    #Barre de défilement
    scrollbar=tkinter.Scrollbar(infodico,orient="vertical",command=table.yview)
    #Liaison de la barre à la table
    table.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(fill='y', side="right")
    table.pack(fill="both", expand=True)



    savebutton=tkinter.Button(infodico,text="Save data on csv file",
                              bg="blue",fg="white", font=("Ariel",12,"bold"),
                              width=15, height=2,command=lambda :savecsv(table, town, country))
    savebutton.place(relx=0.8,rely=0.04)

    #Bouton continuer l'analyse
    analysecontinue=tkinter.Button(infodico,text="Continue analyse",
                                   bg="blue",fg="white",font=("Ariel",12,"bold"),
                                   width=15,height=2)#Rajouter une command d'appel au parent weatherdata()
    analysecontinue.place(relx=0.1,rely=0.04)





#Fonction lecture données sur csv données météo
def weatherdata():
    file=filedialog.askopenfilename(title="Please select your file")

    #Cas ou il n'y a aucune sélection
    if not file:
        return

    #Contrôle que le fichier donné soit un fichier csv
    csvfile=file.split(".")
    if csvfile[-1]!="csv":
        # Création de la fenêtre
        csverror = Toplevel()
        # Nom de l'onglet de fenêtre
        csverror.title("Error message")
        # Définition de la taille de la fenêtre
        csverror.geometry("400x100")
        # Nom de la fenêtre
        message = (tkinter.Label(csverror,
                             text="please give an csv file",
                             justify="center",
                             font=("Aptos",15,"bold"),fg='red'))  # parfaire le message
        message.place(relx=0.5,rely=0.2, anchor="center")

        #Réouverture du dialogue
        def reopen_filedialog():
            csverror.destroy()
            weatherdata()
            #Evite erreur coupure programme
            return
        #Bouton retour
        return_button = tkinter.Button(csverror, text="Return",
                                       bg="lightblue",command=reopen_filedialog)
        return_button.place(relx=0.5,rely=0.7,anchor="center")
        #Permet de garder la fenêtre d'erreur ouverte
        csverror.mainloop()
        #Arret fonction évitant de continuer le programme
        return
    else:

        # Lecture du fichier CSV
        with open(file, mode='r',newline='', encoding='utf-8') as file:
            reader=csv.reader(file)
            # Lecture de la première ligne du fichier
            firstrow = next(reader)

            #Contrôle que les noms de colonnes soient bien identique à l'exemple
            firstrowsep=firstrow[0].split(";")
            if (firstrowsep[0] not in ("date","Date")) or (firstrowsep[1] not in("Rain (mm)","rain (mm)","Rain(mm)","rain(mm)")) or (firstrowsep[2] not in ("Country","country")) or (firstrowsep[3] not in ("Town","town")):
                # Création bouton erreur fichier
                # Création de la fenêtre
                errorfileheader = Toplevel()
                # Nom de l'onglet de fenêtre
                errorfileheader.title("Error message")
                # Définition de la taille de la fenêtre
                errorfileheader.geometry("400x150")
                # Nom de la fenêtre
                messagefileheader = (tkinter.Label(errorfileheader,
                                             text="Please use the same format as example\n"
                                                  "Please modify your file and reselect it",
                                             justify="center",
                                             font=("Aptos", 15, "bold"), fg='red'))
                messagefileheader.place(relx=0.5, rely=0.2, anchor="center")
                # Réouverture du dialogue
                def reopen_filedialog():
                    errorfileheader.destroy()
                    weatherdata()
                    #Evite erreur coupure programme
                    return
                # Bouton retour
                return_button = tkinter.Button(errorfileheader, text="Return",
                                               bg="lightblue", command=reopen_filedialog)
                return_button.place(relx=0.5, rely=0.7, anchor="center")
                # Permet de garder la fenêtre d'erreur ouverte
                errorfileheader.mainloop()
                #Arrêt fonction évitant de continuer le programme
                return

            else:

                #Initialisation de l'année précédente
                prevyear=99999


                #Création d'un dictionnaire mensuel pour stockage données années
                Jandict= {}
                Febdict= {}
                Mardict= {}
                Aprdict= {}
                Maydict = {}
                Jundict = {}
                Juldict = {}
                Augdict = {}
                Sepdict = {}
                Octdict = {}
                Novdict = {}
                Decdict = {}

                #Boucle de lecture
                for i in reader:

                    #Définition de chaque élément
                    element=i[0].split(";")

                    #Contrôle que les chiffre rain soient bien au bon format 0.13 et non 0,13
                    if len(element)<3:
                        # Création bouton erreur fichier virgule
                        # Création de la fenêtre
                        errorfilecomma = Toplevel()
                        # Nom de l'onglet de fenêtre
                        errorfilecomma.title("Error message")
                        # Définition de la taille de la fenêtre
                        errorfilecomma.geometry("500x150")
                        # Nom de la fenêtre
                        messagefilecomma = (tkinter.Label(errorfilecomma,
                                                          text="Please control your rain format: \n"
                                                          "numbers must be separated by points (0.13) \nand not commas (0,13)\n"
                                                          "Please modify your file and reselect it",
                                                          justify="center",
                                                          font=("Aptos", 12, "bold"), fg='red'))
                        messagefilecomma.place(relx=0.5, rely=0.3, anchor="center")
                        # Réouverture du dialogue
                        def reopen_filedialog():
                            errorfilecomma.destroy()
                            weatherdata()
                            #Evite erreurs lors coupure programme
                            return
                        # Bouton retour
                        return_button = tkinter.Button(errorfilecomma, text="Return",
                                                       bg="lightblue", command=reopen_filedialog)
                        return_button.place(relx=0.5, rely=0.7, anchor="center")
                        errorfilecomma.mainloop()
                        return

                    #Défintion des éléments de la date
                    date=element[0].split("/")
                    year=date[-1]
                    month = date[0]

                    #Définition de l'élément pluie
                    rain=element[1]

                    #Récupération du nom du pays
                    country=element[2]
                    town=element[3]

                    #Conversion en integer
                    intyear=int(year)
                    intmonth=int(month)

                    #Conversion en reel
                    floatrain=float(rain)

                    #Contrôle qu'il y ait bien 12 mois
                    if intmonth>12:
                        # Création bouton erreur mois incorrect
                        # Création de la fenêtre
                        errormonth = Toplevel()
                        # Nom de l'onglet de fenêtre
                        errormonth.title("Error message")
                        # Définition de la taille de la fenêtre
                        errormonth.geometry("400x100")
                        # Nom de la fenêtre
                        messagemonth = (tkinter.Label(errormonth,
                                                      text="Month must be between 1 and 12.\n"
                                                           "Please convert your date in month/date/year\n"
                                                           "Please modify your file and reselect it",
                                                      justify="center",
                                                      font=("Aptos", 12, "bold"), fg='red'))
                        messagemonth.place(relx=0.5, rely=0.3, anchor="center")
                        # Réouverture du dialogue
                        def reopen_filedialog():
                            errormonth.destroy()
                            weatherdata()
                            # Evite erreurs lors coupure programme
                            return
                        # Bouton retour
                        return_button = tkinter.Button(errormonth, text="Return",
                                                       bg="lightblue", command=reopen_filedialog)
                        return_button.place(relx=0.5, rely=0.8, anchor="center")
                        errormonth.mainloop()
                        return

                    else:

                        #Contrôle des années cumulatives
                        if intyear == prevyear or intyear == prevyear+1 or prevyear==99999 :

                            #Stockage des données du mois de Janvier dans un dictionnaire
                            if intmonth==1:
                                if year in Jandict:
                                    #Conversion si rain est négatif
                                    if floatrain < 0:
                                        floatrain = 0
                                        Jandict[year].append(floatrain)
                                    else:
                                        Jandict[year].append(floatrain)
                                else:
                                    # Si l'année n'est pas encore dans le dictionnaire, on crée une nouvelle liste avec la précipitation
                                    Jandict[year] = [floatrain]

                            # Stockage des données du mois de Février dans un dictionnaire
                            if intmonth == 2:
                                if year in Febdict:
                                    # Conversion si rain est négatif
                                    if floatrain < 0:
                                        floatrain = 0
                                        Febdict[year].append(floatrain)
                                    else:
                                        Febdict[year].append(floatrain)
                                else:
                                    # Si l'année n'est pas encore dans le dictionnaire, on crée une nouvelle liste avec la précipitation
                                    Febdict[year] = [floatrain]

                            # Stockage des données du mois de Mars dans un dictionnaire
                            if intmonth == 3:
                                if year in Mardict:
                                    # Conversion si rain est négatif
                                    if floatrain < 0:
                                        floatrain = 0
                                        Mardict[year].append(floatrain)
                                    else:
                                        Mardict[year].append(floatrain)
                                else:
                                    # Si l'année n'est pas encore dans le dictionnaire, on crée une nouvelle liste avec la précipitation
                                    Mardict[year] = [floatrain]

                            # Stockage des données du mois d'Avril dans un dictionnaire
                            if intmonth == 4:
                                if year in Aprdict:
                                    # Conversion si rain est négatif
                                    if floatrain < 0:
                                        floatrain = 0
                                        Aprdict[year].append(floatrain)
                                    else:
                                        Aprdict[year].append(floatrain)
                                else:
                                            # Si l'année n'est pas encore dans le dictionnaire, on crée une nouvelle liste avec la précipitation
                                    Aprdict[year] = [floatrain]

                            # Stockage des données du mois de mai dans un dictionnaire
                            if intmonth == 5:
                                if year in Maydict:
                                    # Conversion si rain est négatif
                                    if floatrain < 0:
                                        floatrain = 0
                                        Maydict[year].append(floatrain)
                                    else:
                                        Maydict[year].append(floatrain)
                                else:
                                    # Si l'année n'est pas encore dans le dictionnaire, on crée une nouvelle liste avec la précipitation
                                    Maydict[year] = [floatrain]

                            # Stockage des données du mois de juin dans un dictionnaire
                            if intmonth == 6:
                                if year in Jundict:
                                    # Conversion si rain est négatif
                                    if floatrain < 0:
                                        floatrain = 0
                                        Jundict[year].append(floatrain)
                                    else:
                                        Jundict[year].append(floatrain)
                                else:
                                    # Si l'année n'est pas encore dans le dictionnaire, on crée une nouvelle liste avec la précipitation
                                    Jundict[year] = [floatrain]

                            # Stockage des données du mois de juillet dans un dictionnaire
                            if intmonth == 7:
                                if year in Juldict:
                                    # Conversion si rain est négatif
                                    if floatrain < 0:
                                        floatrain = 0
                                        Juldict[year].append(floatrain)
                                    else:
                                        Juldict[year].append(floatrain)
                                else:
                                    # Si l'année n'est pas encore dans le dictionnaire, on crée une nouvelle liste avec la précipitation
                                    Juldict[year] = [floatrain]

                            # Stockage des données du mois de aout dans un dictionnaire
                            if intmonth == 8:
                                if year in Augdict:
                                    # Conversion si rain est négatif
                                    if floatrain < 0:
                                        floatrain = 0
                                        Augdict[year].append(floatrain)
                                    else:
                                        Augdict[year].append(floatrain)
                                else:
                                    # Si l'année n'est pas encore dans le dictionnaire, on crée une nouvelle liste avec la précipitation
                                    Augdict[year] = [floatrain]

                            # Stockage des données du mois de Septembre dans un dictionnaire
                            if intmonth == 9:
                                if year in Sepdict:
                                    # Conversion si rain est négatif
                                    if floatrain < 0:
                                        floatrain = 0
                                        Sepdict[year].append(floatrain)
                                    else:
                                        Sepdict[year].append(floatrain)
                                else:
                                    # Si l'année n'est pas encore dans le dictionnaire, on crée une nouvelle liste avec la précipitation
                                    Sepdict[year] = [floatrain]

                            # Stockage des données du mois de octobre dans un dictionnaire
                            if intmonth == 10:
                                if year in Octdict:
                                    # Conversion si rain est négatif
                                    if floatrain < 0:
                                        floatrain = 0
                                        Octdict[year].append(floatrain)
                                    else:
                                        Octdict[year].append(floatrain)
                                else:
                                    # Si l'année n'est pas encore dans le dictionnaire, on crée une nouvelle liste avec la précipitation
                                    Octdict[year] = [floatrain]

                            # Stockage des données du mois de novembre dans un dictionnaire
                            if intmonth == 11:
                                if year in Novdict:
                                    # Conversion si rain est négatif
                                    if floatrain < 0:
                                        floatrain = 0
                                        Novdict[year].append(floatrain)
                                    else:
                                        Novdict[year].append(floatrain)
                                else:
                                    # Si l'année n'est pas encore dans le dictionnaire, on crée une nouvelle liste avec la précipitation
                                    Novdict[year] = [floatrain]

                            # Stockage des données du mois de juillet dans un dictionnaire
                            if intmonth == 12:
                                if year in Decdict:
                                    # Conversion si rain est négatif
                                    if floatrain < 0:
                                        floatrain = 0
                                        Decdict[year].append(floatrain)
                                    else:
                                        Decdict[year].append(floatrain)
                                else:
                                    # Si l'année n'est pas encore dans le dictionnaire, on crée une nouvelle liste avec la précipitation
                                    Decdict[year] = [floatrain]
                        #Code erreur si pas années pas cumulative
                        else:
                            #Création bouton
                            #Création fenêtre
                            errorfileyear=Toplevel()
                            #Nom de la fenêtre
                            errorfileyear.title("Error message")
                            #Taille de la fenêtre
                            errorfileyear.geometry("400x150")
                            #Message fenêtre
                            messagefileyear=(tkinter.Label(errorfileyear,
                                                           text="Your years must be cumulative\n"
                                                                "Please modify your file and reselect if",
                                                           justify='center',font=('Ariel',12,"bold"),fg="red"))
                            messagefileyear.place(relx=0.5, rely=0.3, anchor="center")
                            # Réouverture du dialogue
                            def reopen_filedialog():
                                errorfileyear.destroy()
                                weatherdata()
                                # Evite erreurs lors coupure programme
                                return
                            # Bouton retour
                            return_button = tkinter.Button(errorfileyear, text="Return",
                                                           bg="lightblue", command=reopen_filedialog)
                            return_button.place(relx=0.5, rely=0.7, anchor="center")
                            errorfileyear.mainloop()
                            return

                    prevyear = intyear


        #Stockage des données d'intérêt dans un dictionnaire années
        # Initialisation de liste de stockage avant envoie dans le dictionnaire
        listv=[]
        listcumul=[]
        listcount=[]

        #Création d'un dictionnaire vide qui contiendra l'ensemble des infos
        dictionnary={}

        # Création d'une liste contenant l'ensemble des années du tableau
        for key in Jandict:
            listv.append(key)
        # Mise des années dans un dictionnaire globale contenant des sous-dictionnaire avec l'ensemble des informations
        for years in listv:
            dictionnary[years] = {}


        #Intégration janvier
        #Calcule du cumul précipitation et comptage jour pluie puis stockage dans une liste
        for j in Jandict :
            cumulrain=sum(Jandict[j])
            listcumul.append(cumulrain)
            count = len([x for x in Jandict[j] if x > 0])
            listcount.append(count)
        # Attribution des cumuls pluie à january
        for (years, months), valuecumul,valuecount in zip(dictionnary.items(), listcumul,listcount):
            months['January'] = {'Rainfall':valuecumul,'Rain frequency':valuecount}
        #Destruction dictionnaire Jandict
        del Jandict
        #Réinitialisation des listes
        listcumul = []
        listcount = []

        #Intégration février
        #Calcule du cumul précipitation et comptage jour pluie puis stockage dans une liste
        for j in Febdict :
            cumulrain=sum(Febdict[j])
            listcumul.append(cumulrain)
            count = len([x for x in Febdict[j] if x > 0])
            listcount.append(count)
        # Attribution des cumuls pluie à février
        for (years, months), valuecumul,valuecount in zip(dictionnary.items(), listcumul,listcount):
            months['February'] = {'Rainfall':valuecumul,'Rain frequency':valuecount}
        #Destruction dictionnaire Febdict
        del Febdict
        #Réinitialisation des listes
        listcumul = []
        listcount = []

        # Intégration mars
        # Calcule du cumul précipitation et comptage jour pluie puis stockage dans une liste
        for j in Mardict:
            cumulrain = sum(Mardict[j])
            listcumul.append(cumulrain)
            count = len([x for x in Mardict[j] if x > 0])
            listcount.append(count)
        # Attribution des cumuls pluie à march
        for (years, months), valuecumul, valuecount in zip(dictionnary.items(), listcumul, listcount):
            months['March'] = {'Rainfall': valuecumul, 'Rain frequency': valuecount}
        # Destruction dictionnaire Mardict
        del Mardict
        # Réinitialisation des listes
        listcumul = []
        listcount = []

        # Intégration avril
        # Calcule du cumul précipitation et comptage jour pluie puis stockage dans une liste
        for j in Aprdict:
            cumulrain = sum(Aprdict[j])
            listcumul.append(cumulrain)
            count = len([x for x in Aprdict[j] if x > 0])
            listcount.append(count)
        # Attribution des cumuls pluie à april
        for (years, months), valuecumul, valuecount in zip(dictionnary.items(), listcumul, listcount):
            months['April'] = {'Rainfall': valuecumul, 'Rain frequency': valuecount}
        # Destruction dictionnaire Aprdict
        del Aprdict
        # Réinitialisation des listes
        listcumul = []
        listcount = []

        # Intégration mai
        # Calcule du cumul précipitation et comptage jour pluie puis stockage dans une liste
        for j in Maydict:
            cumulrain = sum(Maydict[j])
            listcumul.append(cumulrain)
            count = len([x for x in Maydict[j] if x > 0])
            listcount.append(count)
        # Attribution des cumuls pluie à may
        for (years, months), valuecumul, valuecount in zip(dictionnary.items(), listcumul, listcount):
            months['May'] = {'Rainfall': valuecumul, 'Rain frequency': valuecount}
        # Destruction dictionnaire Maydict
        del Maydict
        # Réinitialisation des listes
        listcumul = []
        listcount = []

        # Intégration june
        # Calcule du cumul précipitation et comptage jour pluie puis stockage dans une liste
        for j in Jundict:
            cumulrain = sum(Jundict[j])
            listcumul.append(cumulrain)
            count = len([x for x in Jundict[j] if x > 0])
            listcount.append(count)
        # Attribution des cumuls pluie à june
        for (years, months), valuecumul, valuecount in zip(dictionnary.items(), listcumul, listcount):
            months['June'] = {'Rainfall': valuecumul, 'Rain frequency': valuecount}
        # Destruction dictionnaire June
        del Jundict
        # Réinitialisation des listes
        listcumul = []
        listcount = []

        # Intégration july
        # Calcule du cumul précipitation et comptage jour pluie puis stockage dans une liste
        for j in Juldict:
            cumulrain = sum(Juldict[j])
            listcumul.append(cumulrain)
            count = len([x for x in Juldict[j] if x > 0])
            listcount.append(count)
        # Attribution des cumuls pluie à july
        for (years, months), valuecumul, valuecount in zip(dictionnary.items(), listcumul, listcount):
            months['July'] = {'Rainfall': valuecumul, 'Rain frequency': valuecount}
        # Destruction dictionnaire June
        del Juldict
        # Réinitialisation des listes
        listcumul = []
        listcount = []

        # Intégration august
        # Calcule du cumul précipitation et comptage jour pluie puis stockage dans une liste
        for j in Augdict:
            cumulrain = sum(Augdict[j])
            listcumul.append(cumulrain)
            count = len([x for x in Augdict[j] if x > 0])
            listcount.append(count)
        # Attribution des cumuls pluie à august
        for (years, months), valuecumul, valuecount in zip(dictionnary.items(), listcumul, listcount):
            months['August'] = {'Rainfall': valuecumul, 'Rain frequency': valuecount}
        # Destruction dictionnaire Augdict
        del Augdict
        # Réinitialisation des listes
        listcumul = []
        listcount = []

        # Intégration september
        # Calcule du cumul précipitation et comptage jour pluie puis stockage dans une liste
        for j in Sepdict:
            cumulrain = sum(Sepdict[j])
            listcumul.append(cumulrain)
            count = len([x for x in Sepdict[j] if x > 0])
            listcount.append(count)
        # Attribution des cumuls pluie à september
        for (years, months), valuecumul, valuecount in zip(dictionnary.items(), listcumul, listcount):
            months['September'] = {'Rainfall': valuecumul, 'Rain frequency': valuecount}
        # Destruction dictionnaire Septdict
        del Sepdict
        # Réinitialisation des listes
        listcumul = []
        listcount = []

        # Intégration october
        # Calcule du cumul précipitation et comptage jour pluie puis stockage dans une liste
        for j in Octdict:
            cumulrain = sum(Octdict[j])
            listcumul.append(cumulrain)
            count = len([x for x in Octdict[j] if x > 0])
            listcount.append(count)
        # Attribution des cumuls pluie à october
        for (years, months), valuecumul, valuecount in zip(dictionnary.items(), listcumul, listcount):
            months['October'] = {'Rainfall': valuecumul, 'Rain frequency': valuecount}
        # Destruction dictionnaire Octdict
        del Octdict
        # Réinitialisation des listes
        listcumul = []
        listcount = []

        # Intégration november
        # Calcule du cumul précipitation et comptage jour pluie puis stockage dans une liste
        for j in Novdict:
            cumulrain = sum(Novdict[j])
            listcumul.append(cumulrain)
            count = len([x for x in Novdict[j] if x > 0])
            listcount.append(count)
        # Attribution des cumuls pluie à november
        for (years, months), valuecumul, valuecount in zip(dictionnary.items(), listcumul, listcount):
            months['November'] = {'Rainfall': valuecumul, 'Rain frequency': valuecount}
        # Destruction dictionnaire Novdict
        del Novdict
        # Réinitialisation des listes
        listcumul = []
        listcount = []

        # Intégration december
        # Calcule du cumul précipitation et comptage jour pluie puis stockage dans une liste
        for j in Decdict:
            cumulrain = sum(Decdict[j])
            listcumul.append(cumulrain)
            count = len([x for x in Decdict[j] if x > 0])
            listcount.append(count)
        # Attribution des cumuls pluie à december
        for (years, months), valuecumul, valuecount in zip(dictionnary.items(), listcumul, listcount):
            months['December'] = {'Rainfall': valuecumul, 'Rain frequency': valuecount}
        # Destruction dictionnaire Decdict
        del Decdict

        infodicosave(dictionnary,town,country)













#Fonction fenêtre pour rentrer les données climatiques pluie cumulées
def cumuldataroot(weatherroot):
    #Fermeture fenêtre précédente
    weatherroot.destroy()
    #Création de la fenêtre
    cumuldata=Tk()

    #Nom de la fenêtre
    cumuldata.title("IN-Palm indicator: planting \u2264 10 years Input data")
    #Définition de la taille de la fenêtre
    cumuldata.geometry("800x600")

#Fonction fermeture de la fenêtre weatherroot
def closeweatherroot(weatherroot):
    weatherroot.destroy()

#Fonction pour plantation inférieur ou égale à 10 ans
def weatherlower10 (root):
    #Fermeture fenêtre précédente
    root.destroy()
    #Création de la fenêtre
    weatherroot= Tk()

    #Nom de l'onglet de fenêtre
    weatherroot.title("IN-Palm indicator: planting \u2264 10 years Input data")
    #Définition de la taille de la fenêtre
    weatherroot.geometry("800x200")

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
    cumulativedata.place(relx=0.2, rely=0.4, anchor="center")

    dailydata=(ttk.Label(weatherroot,text="You have daily data in csv format like ",
                         justify="center",
                         font=("Ariel", 12)))#parfaire le message
    dailydata.place(relx=0.7, rely=0.4, anchor="center")

    #Création des boutons
    #Bouton pour données climatiques cumulées
    buttoncumuldata = tkinter.Button(weatherroot, text="Click here",
                                 font=("Ariel",12,"bold"), anchor="center",
                                 bg="blue",fg="white",activebackground = "lightgreen",
                                 command=lambda: cumuldataroot(weatherroot))
    buttoncumuldata.place(relx=0.2, rely=0.7, anchor="center")

    #Bouton exemple
    example=tkinter.Button(weatherroot, text="Example",
                           font=("Ariel",12,"bold"), anchor="center",
                           bg="blue",fg="white",activebackground = "lightgreen",
                           command=openexample)
    example.place(relx=0.92, rely=0.4, anchor="center")


    # Bouton pour données climatiques journalière
    dailydata = tkinter.Button(weatherroot, text="Click here",
                             font=("Ariel", 12, "bold"), anchor="center",
                             bg="blue", fg="white", activebackground="lightgreen",
                             command=lambda :[weatherdata(),closeweatherroot(weatherroot)])
    dailydata.place(relx=0.7, rely=0.7, anchor="center")

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



