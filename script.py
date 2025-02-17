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


# Fonctions qui sera appelée chaque fois qu'une sélection change pour chacun des mois
def y1_Jan(*y1Jan):
    return y1Jan[0].get()
def y1_Feb(*y1Feb):
    return y1Feb[0].get()
def y1_Mar(*y1Mar):
    return y1Mar[0].get()
def y1_Apr(*y1Apr):
    return y1Apr[0].get()
def y1_Maymonth(*y1Maymonth):
    return y1Maymonth[0].get()
def y1_Jun(*y1Jun):
    return y1Jun[0].get()
def y1_Jul(*y1Jul):
    return y1Jul[0].get()
def y1_Aug(*y1Aug):
    return y1Aug[0].get()
def y1_Sep(*y1Sep):
    return y1Sep[0].get()
def y1_Oct(*y1Oct):
    return y1Oct[0].get()
def y1_Nov(*y1Nov):
    return y1Nov[0].get()
def y1_Dec(*y1Dec):
    return y1Dec[0].get()


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

    # Création scrollbar
    # Créer un Canvas pour le contenu défilant
    canvas = tkinter.Canvas(infopracticeroot)
    canvas.pack(side="left", fill="both", expand=True)
    # Créer la barre de défilement verticale
    scrollbar_vertical = tkinter.Scrollbar(infopracticeroot, orient="vertical", command=canvas.yview)
    scrollbar_vertical.pack(side="right", fill="y")
    # Configurer le Canvas pour scrollbar
    canvas.config(yscrollcommand=scrollbar_vertical.set)
    # Créer un Frame à l'intérieur du Canvas pour contenir tous les widgets
    main_frame = tkinter.Frame(canvas)
    # Ajouter le Frame au Canvas avec la méthode create_window
    canvas.create_window((0, 0), window=main_frame, anchor="nw")
    # Mettre à jour la taille du canvas pour qu'il s'ajuste à la taille du contenu
    def on_frame_configure(event):
        canvas.config(scrollregion=canvas.bbox("all"))
    # Lier l'événement de redimensionnement du Frame pour mettre à jour la zone de défilement
    main_frame.bind("<Configure>", on_frame_configure)

    # Listes de sélection
    typeNferti = ["Ammo Sulf", "Urea", "Ammo Chlo", "Ammo Nit", "Sod Nit"]
    Nfertiplacement = ["In the circle", "Evenly distributed"]
    Nfertiplacementinthecircle = ["buried", "not buried", "windrow"]
    Orgafertitype = ["EFB", "Compost"]
    Orgafertiplacement = ["In the circle", "In the harvesting path", "Spread (anti erosion)"]
    understoreybiomass = ["Very high", "High", "Medium", "Low", "No"]
    understoreylegumefraction = ["Very high", "High", "Medium", "Low", "No"]
    Prunedfronds = ["Exported", "In heaps", "In windows", "Spread (anti erosion"]

    #Message titre fenêtre
    label=(tkinter.Label(main_frame,
                         text="Management practice",font=("Ariel",25,'bold')))
    label.pack(anchor="center")

    #Intégration message de confirmation sauvegarde données
    if functioncount==1:
        saveok=(tkinter.Label(main_frame,
                              text=f"Data was been save on{file_path}",font=("Ariel",12,'italic'),
                              fg="blue"))
        saveok.pack(anchor="center")

    #Intégration de chaque années dans la fenêtre
    year1=(tkinter.Label(main_frame,
                             text="First year", font=("Ariel",20,'underline')))
    year1.pack(anchor="w",pady=5)

    #Intégration des instructions de remplissage
    # Intégration des instruction
    # Création encadré
    instructionframe = tkinter.Frame(main_frame,
                                     bd=2, relief="solid",
                                     width=400, height=1000)
    instructionframe.pack(side="right", anchor="n", fill="none")
    #Titre
    instructions=(tkinter.Label(instructionframe,
                                text="Data filling instructions",
                                font=("Ariel",15, "bold")))
    instructions.place(relx=0.2)
    #Définition et message
    message=(tkinter.Label(instructionframe,
                           text="*Sod Nit*: Sodium Nitrate\n"
                                "*Ammo Nit*: Ammonium Nitrate\n"
                                "*Ammo Chlo*: Ammonium Chloride\n"
                                "*Ammo Sulf*: Ammonium Sulfate"))



    #Intégration du bloc data mineral Nfertilizer
    #Création encadré
    frame = tkinter.Frame(main_frame, bd=2, relief="solid", width=1450, height=400, padx=5, pady=2)
    frame.pack(anchor="w",padx=15, pady=5,fill="none")
    #Mise de titre Mineral N ferti
    y1_MineralNfertilizer=(tkinter.Label(frame,
                                      text="Mineral Nitrogen fertilizer",justify="center",
                                      font=("Ariel",13,"bold","underline")))
    y1_MineralNfertilizer.place(relx=0.01)

    #Intégration des mois
    y1_January=(tkinter.Label(frame,text="January",font=("Ariel",9),fg="blue"))
    y1_January.place(relx=0.06,rely=0.08)
    y1_February = (tkinter.Label(frame, text="February", font=("Ariel", 9), fg="blue"))
    y1_February.place(relx=0.14, rely=0.08)
    y1_March = (tkinter.Label(frame, text="March", font=("Ariel", 9), fg="blue"))
    y1_March.place(relx=0.22, rely=0.08)
    y1_April = (tkinter.Label(frame, text="April", font=("Ariel", 9), fg="blue"))
    y1_April.place(relx=0.295, rely=0.08)
    y1_May = (tkinter.Label(frame, text="May", font=("Ariel", 9), fg="blue"))
    y1_May.place(relx=0.377, rely=0.08)
    y1_June = (tkinter.Label(frame, text="June", font=("Ariel", 9), fg="blue"))
    y1_June.place(relx=0.46, rely=0.08)
    y1_July = (tkinter.Label(frame, text="July", font=("Ariel", 9), fg="blue"))
    y1_July.place(relx=0.54, rely=0.08)
    y1_August = (tkinter.Label(frame, text="August", font=("Ariel", 9), fg="blue"))
    y1_August.place(relx=0.62, rely=0.08)
    y1_September = (tkinter.Label(frame, text="September", font=("Ariel", 9), fg="blue"))
    y1_September.place(relx=0.69, rely=0.08)
    y1_October = (tkinter.Label(frame, text="October", font=("Ariel", 9), fg="blue"))
    y1_October.place(relx=0.78, rely=0.08)
    y1_November = (tkinter.Label(frame, text="November", font=("Ariel", 9), fg="blue"))
    y1_November.place(relx=0.85, rely=0.08)
    y1_December = (tkinter.Label(frame, text="December", font=("Ariel", 9), fg="blue"))
    y1_December.place(relx=0.93, rely=0.08)

    #Création du type
    y1_type=(tkinter.Label(frame,text="Type",fg="blue",font=("Ariel",12,"bold")))
    y1_type.place(relx=0,rely=0.14)

    # Création data rate
    y1_rate = (tkinter.Label(frame, text="Rate \n(kg/ha)", fg="blue", font=("Ariel", 11, "bold")))
    y1_rate.place(relx=0, rely=0.21)

    #Création placement
    y1_placement=(tkinter.Label(frame, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y1_placement.place(relx=0, rely=0.47)


    # Fonction pour récupérer toutes les valeurs des mois pour Type N ferti
    def get_all_month_valuestypeNfertiy1():
        month_valuestypeNfertiy1 = [
            y1_Jan(y1_Jan_typeNfertivar),
            y1_Feb(y1_Feb_typeNfertivar),
            y1_Mar(y1_Mar_typeNfertivar),
            y1_Apr(y1_Apr_typeNfertivar),
            y1_Maymonth(y1_Maymonth_typeNfertivar),
            y1_Jun(y1_Jun_typeNfertivar),
            y1_Jul(y1_Jul_typeNfertivar),
            y1_Aug(y1_Aug_typeNfertivar),
            y1_Sep(y1_Sep_typeNfertivar),
            y1_Oct(y1_Oct_typeNfertivar),
            y1_Nov(y1_Nov_typeNfertivar),
            y1_Dec(y1_Dec_typeNfertivar)
        ]

        return month_valuestypeNfertiy1

    # Créer une variable Tkinter pour stocker l'élément sélectionné Nfertitype
    #Création combobox
    #Janvier
    y1_Jan_typeNfertivar = ttk.Combobox(frame,values=typeNferti,
                                        width=10)
    y1_Jan_typeNfertivar.set("*None")
    y1_Jan_typeNfertivar.place(relx=0.04, rely=0.14)
    # Février
    y1_Feb_typeNfertivar = ttk.Combobox(frame, values=typeNferti,
                                        width=10)
    y1_Feb_typeNfertivar.set("*None")
    y1_Feb_typeNfertivar.place(relx=0.12, rely=0.14)
    # Mars
    y1_Mar_typeNfertivar = ttk.Combobox(frame, values=typeNferti,
                                        width=10)
    y1_Mar_typeNfertivar.set("*None")
    y1_Mar_typeNfertivar.place(relx=0.2, rely=0.14)
    # Avril
    y1_Apr_typeNfertivar = ttk.Combobox(frame, values=typeNferti,
                                        width=10)
    y1_Apr_typeNfertivar.set("*None")
    y1_Apr_typeNfertivar.place(relx=0.28, rely=0.14)
    # May
    y1_Maymonth_typeNfertivar = ttk.Combobox(frame, values=typeNferti,
                                        width=10)
    y1_Maymonth_typeNfertivar.set("*None")
    y1_Maymonth_typeNfertivar.place(relx=0.36, rely=0.14)
    # Juin
    y1_Jun_typeNfertivar = ttk.Combobox(frame, values=typeNferti,
                                             width=10)
    y1_Jun_typeNfertivar.set("*None")
    y1_Jun_typeNfertivar.place(relx=0.44, rely=0.14)
    # July
    y1_Jul_typeNfertivar = ttk.Combobox(frame, values=typeNferti,
                                        width=10)
    y1_Jul_typeNfertivar.set("*None")
    y1_Jul_typeNfertivar.place(relx=0.52, rely=0.14)
    # Aout
    y1_Aug_typeNfertivar = ttk.Combobox(frame, values=typeNferti,
                                        width=10)
    y1_Aug_typeNfertivar.set("*None")
    y1_Aug_typeNfertivar.place(relx=0.6, rely=0.14)
    # Septembre
    y1_Sep_typeNfertivar = ttk.Combobox(frame, values=typeNferti,
                                        width=10)
    y1_Sep_typeNfertivar.set("*None")
    y1_Sep_typeNfertivar.place(relx=0.68, rely=0.14)
    # Octobre
    y1_Oct_typeNfertivar = ttk.Combobox(frame, values=typeNferti,
                                        width=10)
    y1_Oct_typeNfertivar.set("*None")
    y1_Oct_typeNfertivar.place(relx=0.76, rely=0.14)
    # Novembre
    y1_Nov_typeNfertivar = ttk.Combobox(frame, values=typeNferti,
                                        width=10)
    y1_Nov_typeNfertivar.set("*None")
    y1_Nov_typeNfertivar.place(relx=0.84, rely=0.14)
    # Décembre
    y1_Dec_typeNfertivar = ttk.Combobox(frame, values=typeNferti,
                                        width=10)
    y1_Dec_typeNfertivar.set("*None")
    y1_Dec_typeNfertivar.place(relx=0.92, rely=0.14)


    # Fonction pour récupérer toutes les valeurs des mois pour rate N ferti
    def get_all_month_valuesrateNfertiy1():
        month_valuesrateNfertiy1 = [
            y1_Jan(y1_Jan_rateNfertivar),
            y1_Feb(y1_Feb_rateNfertivar),
            y1_Mar(y1_Mar_rateNfertivar),
            y1_Apr(y1_Apr_rateNfertivar),
            y1_Maymonth(y1_Maymonth_rateNfertivar),
            y1_Jun(y1_Jun_rateNfertivar),
            y1_Jul(y1_Jul_rateNfertivar),
            y1_Aug(y1_Aug_rateNfertivar),
            y1_Sep(y1_Sep_rateNfertivar),
            y1_Oct(y1_Oct_rateNfertivar),
            y1_Nov(y1_Nov_rateNfertivar),
            y1_Dec(y1_Dec_rateNfertivar)
        ]
        return month_valuesrateNfertiy1

    # Créer une variable Tkinter pour stocker l'élément sélectionné NfertiRate
    # Création combobox
    # Janvier
    y1_Jan_rateNfertivar = tkinter.Entry(frame,
                                         width=13,
                                         justify="right")
    y1_Jan_rateNfertivar.insert(tkinter.END,"0")
    y1_Jan_rateNfertivar.place(relx=0.04, rely=0.22)
    # Février
    y1_Feb_rateNfertivar = tkinter.Entry(frame,
                                         width=13,
                                         justify="right")
    y1_Feb_rateNfertivar.insert(tkinter.END, "0")
    y1_Feb_rateNfertivar.place(relx=0.12, rely=0.22)
    # Mars
    y1_Mar_rateNfertivar = tkinter.Entry(frame,
                                         width=13,
                                         justify="right")
    y1_Mar_rateNfertivar.insert(tkinter.END, "0")
    y1_Mar_rateNfertivar.place(relx=0.2, rely=0.22)
    # Avril
    y1_Apr_rateNfertivar = tkinter.Entry(frame,
                                         width=13,
                                         justify="right")
    y1_Apr_rateNfertivar.insert(tkinter.END, "0")
    y1_Apr_rateNfertivar.place(relx=0.28, rely=0.22)
    # May
    y1_Maymonth_rateNfertivar = tkinter.Entry(frame,
                                              width=13,
                                              justify="right")
    y1_Maymonth_rateNfertivar.insert(tkinter.END, "0")
    y1_Maymonth_rateNfertivar.place(relx=0.36, rely=0.22)
    # Juin
    y1_Jun_rateNfertivar = tkinter.Entry(frame,
                                         width=13,
                                         justify="right")
    y1_Jun_rateNfertivar.insert(tkinter.END, "0")
    y1_Jun_rateNfertivar.place(relx=0.44, rely=0.22)
    # July
    y1_Jul_rateNfertivar = tkinter.Entry(frame,
                                         width=13,
                                         justify="right")
    y1_Jul_rateNfertivar.insert(tkinter.END, "0")
    y1_Jul_rateNfertivar.place(relx=0.52, rely=0.22)
    # Aout
    y1_Aug_rateNfertivar = tkinter.Entry(frame,
                                         width=13,
                                         justify="right")
    y1_Aug_rateNfertivar.insert(tkinter.END, "0")
    y1_Aug_rateNfertivar.place(relx=0.6, rely=0.22)
    # Septembre
    y1_Sep_rateNfertivar = tkinter.Entry(frame,
                                         width=13,
                                         justify="right")
    y1_Sep_rateNfertivar.insert(tkinter.END, "0")
    y1_Sep_rateNfertivar.place(relx=0.68, rely=0.22)
    # Octobre
    y1_Oct_rateNfertivar = tkinter.Entry(frame,
                                         width=13,
                                         justify="right")
    y1_Oct_rateNfertivar.insert(tkinter.END, "0")
    y1_Oct_rateNfertivar.place(relx=0.76, rely=0.22)
    # Novembre
    y1_Nov_rateNfertivar = tkinter.Entry(frame,
                                         width=13,
                                         justify="right")
    y1_Nov_rateNfertivar.insert(tkinter.END, "0")
    y1_Nov_rateNfertivar.place(relx=0.84, rely=0.22)
    # Décembre
    y1_Dec_rateNfertivar = tkinter.Entry(frame,
                                         width=13,
                                         justify="right")
    y1_Dec_rateNfertivar.insert(tkinter.END, "0")
    y1_Dec_rateNfertivar.place(relx=0.92, rely=0.22)

    #Calcule taux d'N en fonction du type d'engrais


    # Fonction d'appel pour affichage liste Type Nferti


    #Calcule du taux d'N en kg/ha en fonction de l'apport et du type ferti
    def calculate_kgN():
        #Mise des return list dans des listes spécifiques
        listferti=printlist()
        y1rateferti_str=listferti[1]
        y1typeferti=listferti[0]
        #Création d'une liste vide convertissant les rate str en float
        y1rateferti_float=[]
        #Création d'une liste pour les résultats des calcules
        resultlist=[]
        #Vérification que chaque élément de cette liste puisse être convertie + conversion

        try:
            for i in y1rateferti_str:
                y1rateferti_float.append(float(i))
        except ValueError:
            errorlabel=tkinter.Label(frame,
                                     text="Error! Please check you rate data. Some data are not float",
                                     font=("Ariel",12,"bold"))
            errorlabel.place(relx=0.36, rely=0.28)
            return
        #Calcule taux N en fonction type ferti
        for i in range(12):  # Pour janvier (0) et février (1)
            if y1typeferti[i] == "*None" and y1rateferti_float[i]==0:
                resultlist.append(0)
            elif y1typeferti[i] == "Ammo Chlo" and y1rateferti_float[i]>0:
                resammochlo=round(0.25 * y1rateferti_float[i],1)
                resultlist.append(resammochlo)
            elif y1typeferti[i] == "Ammo Nit" and y1rateferti_float[i]>0:
                resammonit=round(0.34 * y1rateferti_float[i],1)
                resultlist.append(resammonit)
            elif y1typeferti[i] == "Ammo Sulf" and y1rateferti_float[i]>0:
                resammosulf=round(0.21 * y1rateferti_float[i],1)
                resultlist.append(resammosulf)
            elif y1typeferti[i] == "Sod Nit" and y1rateferti_float[i]>0:
                ressodnit=round(0.16 * y1rateferti_float[i],1)
                resultlist.append(ressodnit)
            elif y1typeferti[i] == "Urea" and y1rateferti_float[i]>0:
                resurea=round(0.46 * y1rateferti_float[i],1)
                resultlist.append(resurea)
            elif y1typeferti[i] == "*None" and y1rateferti_float[i]>0:
                resultlist.append("Error!")
            elif y1typeferti[i] != "*None" and y1typeferti[i] !="Ammo Chlo" and y1typeferti[i] !="Ammo Nit" and y1typeferti[i] !="Ammo Sulf" and y1typeferti[i] !="Sod Nit" and y1typeferti[i] !="Urea":
                resultlist.append ("Error!")
            else:
                resultlist.append("Error!")

        #Information résultats
            #Janvier
        equnitrogenjan=tkinter.Label(frame,
                                     text=resultlist[0],font=("Ariel",9,"bold"),
                                     bg="white",fg="blue",justify="right",
                                     width=10,
                                     relief="groove",borderwidth=5)
        equnitrogenjan.place(relx=0.04, rely=0.28)
        # Fevrier
        equnitrogenfev = tkinter.Label(frame,
                                       text=resultlist[1], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenfev.place(relx=0.12, rely=0.28)
        # Mars
        equnitrogenmar = tkinter.Label(frame,
                                       text=resultlist[2], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenmar.place(relx=0.2, rely=0.28)
        # Avril
        equnitrogenapr = tkinter.Label(frame,
                                       text=resultlist[3], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenapr.place(relx=0.28, rely=0.28)
        # Mai
        equnitrogenmay = tkinter.Label(frame,
                                       text=resultlist[4], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenmay.place(relx=0.36, rely=0.28)
        # Juin
        equnitrogenjun = tkinter.Label(frame,
                                       text=resultlist[5], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjun.place(relx=0.44, rely=0.28)
        # Juillet
        equnitrogenjul = tkinter.Label(frame,
                                       text=resultlist[6], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjul.place(relx=0.52, rely=0.28)
        # Aout
        equnitrogenaug = tkinter.Label(frame,
                                       text=resultlist[7], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenaug.place(relx=0.6, rely=0.28)
        # September
        equnitrogensep = tkinter.Label(frame,
                                       text=resultlist[8], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogensep.place(relx=0.68, rely=0.28)
        # Octobre
        equnitrogenoct = tkinter.Label(frame,
                                       text=resultlist[9], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenoct.place(relx=0.76, rely=0.28)
        # Novembre
        equnitrogennov = tkinter.Label(frame,
                                       text=resultlist[10], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogennov.place(relx=0.84, rely=0.28)
        # Decembre
        equnitrogendec = tkinter.Label(frame,
                                       text=resultlist[11], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogendec.place(relx=0.92, rely=0.28)

        #Calcule total annuelle
        yearcumul=0
        resultlist_float=[]
        try:
            for i in resultlist:
                resultlist_float.append(float(i))
        except ValueError:
            return
        for i in resultlist_float:
            if isinstance(i,float):
                yearcumul=i+yearcumul
        #label cacule annuel
        Nfertianuel=tkinter.Label(frame,text=f"Cumulative nitrogen for year: {yearcumul}")
        Nfertianuel.place(relx=0.04,rely=0.35)

    #Création bouton calcul équivalent azote
    button = tkinter.Button(frame, text="Nitrogen equivalent (in kg/ha)",
                            width=100,
                            font=("Ariel",10,"bold"),bg="lightblue",
                            command=calculate_kgN)
    button.place(relx=0.2, rely=0.4)

    # Fonction pour récupérer toutes les infos placement
    def get_placement1():
        placementfertiy1 = [
            y1_Jan(y1_placementferti)]
        return placementfertiy1

    #Création combobox placement
    y1_placementferti = ttk.Combobox(frame, values=Nfertiplacement,
                                     width=16)
    y1_placementferti.set("*Choice*")
    y1_placementferti.place(relx=0.06, rely=0.47)




    def printlist():
        y1Nfertitype = get_all_month_valuestypeNfertiy1()
        print (y1Nfertitype)
        y1Nfertirate=get_all_month_valuesrateNfertiy1()
        print(y1Nfertirate)
        y1placement=get_placement1()
        print(y1placement)
        return y1Nfertitype,y1Nfertirate,y1_placement



    button = tkinter.Button(frame, text="confirmation", command=printlist)
    button.place(relx=0.6, rely=0.9)

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



