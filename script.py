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

#Fonction permettant de rentrer les données des pratiques agronomiques
def Managementpracticesinterface(functioncount,file_path):
    global typeNfertivar
    global Nfertiplacement
    global Orgafertitype
    global Orgafertiplacement
    global understoreybiomass
    global understoreylegumefraction
    global Prunedfronds
    global Soiltexture
    global Landterraces
    global LandPrevpalm

    # Création de la fenêtre
    infopracticeroot = Tk()
    # Nom de la fenêtre
    infopracticeroot.title("Management practice input")
    # Définition de la taille de la fenêtre
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
    Nfertiplacement = ["In the circle, buried", "In the circle, not buried", "In the circle + windrow",
                       "Evenly distributed"]
    Orgafertitype = ["EFB", "Compost"]
    Orgafertiplacement = ["In the circle", "In the harvesting path", "Spread (anti erosion)"]
    understoreybiomass = ["Very high", "High", "Medium", "Low", "No"]
    understoreylegumefraction = ["Very high", "High", "Medium", "Low", "No"]
    Prunedfronds = ["Exported", "In heaps", "In windows", "Spread (anti erosion)"]
    Soiltexture = ["Clay", "Clay loam", "Loam", "Loamy sand", "Sand", "Sandy clay", "Sandy clay loam", "Sandy loam",
                   "Silt", "Silt clay", "Silt clay loam", "Silt loam"]
    Landterraces = ["No", "Yes"]
    LandPrevpalm = ["Exported", "No (first cycle)", "Shredded left"]

    # Message titre fenêtre
    label = (tkinter.Label(main_frame,
                           text="Management practice", font=("Ariel", 25, 'bold')))
    label.pack(anchor="center")

    # Intégration message de confirmation sauvegarde données
    if functioncount == 1:
        saveok = (tkinter.Label(main_frame,
                                text=f"Data was been save on{file_path}", font=("Ariel", 12, 'italic'),
                                fg="blue"))
        saveok.pack(anchor="center")

    # Intégration des instructions de remplissage
    # Intégration des instructions
    # Création encadré
    instructionframe = tkinter.Frame(main_frame,
                                     bd=2, relief="solid",
                                     width=400, height=800)
    instructionframe.pack(side="right", anchor="n", fill="none", pady=55)

    # Création instruction
    instructions = (tkinter.Label(instructionframe,
                                  text="Data filling instructions",
                                  font=("Ariel", 15, "bold", "underline"),
                                  fg="blue"))
    instructions.place(relx=0.2)

    # Définition et message
    message1 = (tkinter.Label(instructionframe,
                              text="\n\n"
                                   "You have this information in csv format like :\n",
                              font=("Ariel", 11, "bold"), justify="left"))
    message1.place(rely=0.07)

    Examplebutton = tkinter.Button(instructionframe,
                                   text="Example",
                                   fg="white", bg="blue",
                                   font=("Ariel", 12, "bold"),
                                   width=6)
    Examplebutton.place(relx=0.81, rely=0.1)

    Databutton = tkinter.Button(instructionframe,
                                text="Please click here",
                                fg="white", bg="blue",
                                font=("Ariel", 12, "bold"))
    Databutton.place(relx=0.3, rely=0.15)

    message2 = (tkinter.Label(instructionframe,
                              text="You don't have this information on csv file.\n\n",
                              font=("Ariel", 12, "bold"), justify="left"))
    message2.place(rely=0.22)

    message3 = (tkinter.Label(instructionframe,
                              text="Please complete all informations requested for \neach year.\n\n\n"
                                   "For Previous palm in general field preparation:\n"
                                   "\t*No* : zero residue\n"
                                   "\t*Exported* : below-ground residue\n"
                                   "\t*Shredded* : above- and below-ground\n"
                                   "\tresidue\n"
                                   "For fertilizer type in Mineral Nitrogen fertilizer:\n"
                                   "\t*Ammo Sulf* : Ammonium Sulfate\n"
                                   "\t*Ammo chlo* : Ammonium Chloride\n"
                                   "\t*Ammo Nit* : Ammonium Nitrate\n"
                                   "\t*Sod Nit* : Sodium Nitrate\n\n\n"
                                   "Equivalent to bare-soil for:\n\n"
                                   "\t Understorey biomass (of standing biomass):\n"
                                   "\t\tNo : 0 tDM/ha\n"
                                   "\t\tLow : 3 tDM/ha\n"
                                   "\t\tMedium : 6 tDM/ha\n"
                                   "\t\tHigh : 9 tDM/ha\n"
                                   "\t\tVery high : 12tDM/ha\n\n"
                                   "\tLegume fraction :\n"
                                   "\t\tNo : 0%\n"
                                   "\t\tLow : 25% \n"
                                   "\t\tMedium : 50%\n"
                                   "\t\tHigh : 75%\n"
                                   "\t\tVery high : 100%\n\n"
                                   "For atmospheric deposition the default value (18 \nkg/ha/year) can be modyfied",
                              font=("Ariel", 12), justify="left"))
    message3.place(rely=0.25)

    # Création data general
    generaldata = (tkinter.Label(main_frame,
                                 text="General field preparation and soil caracteristic",
                                 font=("Ariel", 20, 'underline')))
    generaldata.pack(anchor="w", pady=5)

    # Intégration du bloc data pour chaque type
    # Création encadré
    genframe = tkinter.Frame(main_frame, bd=2, relief="solid", width=1450, height=400, padx=5, pady=2)
    genframe.pack(anchor="w", padx=15, pady=5, fill="none")

    # Création soil caracteristic
    soilcarac = (tkinter.Label(genframe,
                               text="Soil Caracteristic",
                               font=("Ariel", 13, "bold", "underline")))
    soilcarac.place(relx=0.01)

    # Création Land preparation
    Landprep = (tkinter.Label(genframe,
                              text="Land preparation",
                              font=("Ariel", 13, "bold", "underline")))
    Landprep.place(relx=0.01, rely=0.5)

    # Création organic carbon
    OrgaC = (tkinter.Label(genframe, text="Organic Carbon (in %)", fg="blue", font=("Ariel", 11, "bold")))
    OrgaC.place(relx=0, rely=0.1)

    # Création texture
    Texture = (tkinter.Label(genframe, text="Texture", fg="blue", font=("Ariel", 11, "bold")))
    Texture.place(relx=0, rely=0.2)

    # Création Slope
    Slope = (tkinter.Label(genframe, text="Slope (in %)", fg="blue", font=("Ariel", 11, "bold")))
    Slope.place(relx=0, rely=0.3)

    # Création Terraces
    Terraces = (tkinter.Label(genframe, text="Terraces", fg="blue", font=("Ariel", 11, "bold")))
    Terraces.place(relx=0, rely=0.6)

    # Création Previous palm
    Previous = (tkinter.Label(genframe, text="Previous palms", fg="blue", font=("Ariel", 11, "bold")))
    Previous.place(relx=0, rely=0.7)

    # Fonction pour récupérer toute la valeur de Corga
    def get_orgaC():
        orgaCvar = [
            y1_Jan(organicC)]
        return orgaCvar

    # Création quantité fertilisation organique
    organicC = tkinter.Entry(genframe,
                             width=8,
                             justify="right")
    organicC.insert(tkinter.END, "0")
    organicC.place(relx=0.13, rely=0.1)

    # Fonction pour récupérer toutes les infos Texture
    def get_Texturesoil():
        Texturevar = [
            y1_Jan(Text)]
        return Texturevar

    # Création combobox
    # Texture
    Text = ttk.Combobox(genframe, values=Soiltexture,
                        width=20)
    Text.set("*Choice*")
    Text.place(relx=0.05, rely=0.2)

    # Fonction pour récupérer toute la valeur de pente
    def get_slope():
        Slopevar = [
            y1_Jan(slope)]
        return Slopevar

    # Création quantité fertilisation organique
    slope = tkinter.Entry(genframe,
                          width=8,
                          justify="right")
    slope.insert(tkinter.END, "0")
    slope.place(relx=0.08, rely=0.3)

    # Fonction pour récupérer toutes les infos Terracex
    def get_Terraces():
        Terracesvar = [
            y1_Jan(Terr)]
        return Terracesvar

    # Création combobox
    # Terraces
    Terr = ttk.Combobox(genframe, values=Landterraces,
                        width=10)
    Terr.set("*Choice*")
    Terr.place(relx=0.05, rely=0.6)

    # Fonction pour récupérer toutes les infos Terracex
    def get_Prevpalm():
        Prevpalmvar = [
            y1_Jan(Ppalm)]
        return Prevpalmvar

    # Création combobox
    # Previous palm
    Ppalm = ttk.Combobox(genframe, values=LandPrevpalm,
                         width=20)
    Ppalm.set("*Choice*")
    Ppalm.place(relx=0.05, rely=0.7)

    ################################################################################################################
    ###################################Year 1#######################################################################
    ################################################################################################################
    # Intégration de first years dans la fenêtre
    year1 = (tkinter.Label(main_frame,
                           text="First year", font=("Ariel", 20, 'underline')))
    year1.pack(anchor="w", pady=5)

    #Intégration du bloc data pour chaque type
    #Création encadré
    frame = tkinter.Frame(main_frame, bd=2, relief="solid", width=1450, height=400, padx=5, pady=2)
    frame.pack(anchor="w",padx=15, pady=5,fill="none")

    #Mise de titre Mineral N ferti
    y1_MineralNfertilizer=(tkinter.Label(frame,
                                      text="Mineral Nitrogen fertilizer",justify="center",
                                      font=("Ariel",13,"bold","underline")))
    y1_MineralNfertilizer.place(relx=0.01)

    #Mise de titre organic fertilizer
    y1_Organicfertilizer = (tkinter.Label(frame,
                                           text="Organic fertilizer", justify="center",
                                           font=("Ariel", 13, "bold", "underline")))
    y1_Organicfertilizer.place(relx=0.01, rely=0.55)

    #Mise de titre understorey
    y1_Understorey = (tkinter.Label(frame,
                                          text="Understorey", justify="center",
                                          font=("Ariel", 13, "bold", "underline")))
    y1_Understorey.place(relx=0.01, rely=0.7)

    #Mise de titre Pruned fronds
    y1_Prunedfronds = (tkinter.Label(frame,
                                    text="Pruned fronds", justify="center",
                                    font=("Ariel", 13, "bold", "underline")))
    y1_Prunedfronds.place(relx=0.01, rely=0.85)

    #Mise titre atmospheric depositions
    y1_atmodepo = (tkinter.Label(frame,
                                 text="Atmospheric depositions", justify="center",
                                 font=("Ariel", 13, "bold", "underline")))
    y1_atmodepo.place(relx=0.55, rely=0.75)


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
    y1_type=(tkinter.Label(frame,text="Type",fg="blue",font=("Ariel",11,"bold")))
    y1_type.place(relx=0,rely=0.14)

    # Création data rate
    y1_rate = (tkinter.Label(frame, text="Rate \n(kg/ha)", fg="blue", font=("Ariel", 11, "bold")))
    y1_rate.place(relx=0, rely=0.21)

    #Création placement
    y1_placementferti=(tkinter.Label(frame, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y1_placementferti.place(relx=0, rely=0.47)

    #Création quantity ferti orga
    y1_quantityorga = (tkinter.Label(frame, text="Quantity (in tFM)", fg="blue", font=("Ariel", 11, "bold")))
    y1_quantityorga.place(relx=0, rely=0.63)

    #Création type ferti orga
    y1_typeorga=(tkinter.Label(frame, text="Type", fg="blue", font=("Ariel", 11, "bold")))
    y1_typeorga.place(relx=0.15, rely=0.63)

    #Création placement ferti orga
    y1_placementorga = (tkinter.Label(frame, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y1_placementorga.place(relx=0.25, rely=0.63)

    # Création biomasse understorey
    y1_biomass = (tkinter.Label(frame, text="Biomass", fg="blue", font=("Ariel", 11, "bold")))
    y1_biomass.place(relx=0, rely=0.78)

    # Création legume fraction
    y1_legumefrac = (tkinter.Label(frame, text="Legume fraction", fg="blue", font=("Ariel", 11, "bold")))
    y1_legumefrac.place(relx=0.15, rely=0.78)

    # Création pruned fronts placement
    y1_prunedfr = (tkinter.Label(frame, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y1_prunedfr.place(relx=0, rely=0.92)

    # Création atmospheric depositions
    y1_quantityNatmo = (tkinter.Label(frame, text="Quantity of nitrogen\n (in kg/ha/yr)", fg="blue", font=("Ariel", 11, "bold")))
    y1_quantityNatmo.place(relx=0.55, rely=0.82)




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

    #Calcule du taux d'N en kg/ha en fonction de l'apport et du type ferti
    def calculate_kgN1():
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
            print("Error! Please check you rate data. Some data are not float")

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
                yearcumul=round(i+yearcumul,1)
        #label cacule annuel
        Nfertianuel=tkinter.Label(frame,text=f"Cumulative nitrogen for year: {yearcumul}")
        Nfertianuel.place(relx=0.04,rely=0.35)


    #Création bouton calcul équivalent azote N ferti
    button = tkinter.Button(frame, text="Nitrogen equivalent (in kg/ha)",
                            width=100,
                            font=("Ariel",10,"bold"),bg="lightblue",
                            command=lambda:[calculate_kgN1(),calculate_kgNorga1()])
    button.place(relx=0.2, rely=0.4)

    # Fonction pour récupérer toutes les infos placement
    def get_placement1():
        placementfertiy1 = [
            y1_Jan(y1_placementferti)]
        return placementfertiy1
    #Création combobox placement N ferti
    y1_placementferti = ttk.Combobox(frame, values=Nfertiplacement,
                                     width=21)
    y1_placementferti.set("*Choice*")
    y1_placementferti.place(relx=0.06, rely=0.47)
    # Fonction pour récupérer toute la valeur de quantity organic
    def get_quantityorgafertiy1():
        quantityorgafertiy1list = [
            y1_Jan(y1_quantityorgavar)]
        return quantityorgafertiy1list
    #Création quantité fertilisation organique
    y1_quantityorgavar = tkinter.Entry(frame,
                                       width=8,
                                       justify="right")
    y1_quantityorgavar.insert(tkinter.END, "0")
    y1_quantityorgavar.place(relx=0.1, rely=0.63)

    # Fonction pour récupérer la valeur de type organic
    def get_typeorgafertiy1():
        typeorgafertiy1list = [
            y1_Jan(y1_typeorgavar)]
        return typeorgafertiy1list
    #Création quantité fertilisation organique
    y1_typeorgavar = ttk.Combobox(frame, values=Orgafertitype,
                                     width=10)
    y1_typeorgavar.set("*Choice*")
    y1_typeorgavar.place(relx=0.185, rely=0.63)

    #Calcule équivalent N ferti orga
    def calculate_kgNorga1():
        # Mise des return list dans des listes spécifiques
        listferti = printlist()
        y1_typefertiorga = listferti[4]
        y1_quantityfertiorga = listferti[3]
        # Création d'une liste vide permettant conversion liste en float
        y1_quantityfertiorga_float=[]
        #Création liste pour valeurs
        Nfertiorga=[]
        # Vérification que chaque élément de cette liste puisse être convertie + conversion
        try:
            for i in y1_quantityfertiorga:
                y1_quantityfertiorga_float.append(float(i))
        except ValueError:
            print("Error! Please check you rate data. Some data are not float")

        # Calcule taux N en fonction type ferti orga si plusieurs valeurs
        for i in range(1):
            if y1_typefertiorga[i] == "*Choice*" and y1_quantityfertiorga_float[i] == 0:
                Nfertiorga.append(0)
            elif y1_typefertiorga[i] == "EFB" and y1_quantityfertiorga_float[i] > 0:
                #0.90% N in DM * 0.36tDM/tFM (cf pg Pardon)
                Nfertiorgacal = round(3.24*y1_quantityfertiorga_float[i], 1)
                Nfertiorga.append(Nfertiorgacal )
            elif y1_typefertiorga[i] == "Compost" and y1_quantityfertiorga_float[i] > 0:
                # 2.05% N in DM * 0.41tDM/tFM (cf pg Pardon)
                Nfertiorgacal = round(8.405* y1_quantityfertiorga_float[i], 1)
                Nfertiorga.append(Nfertiorgacal)
            elif y1_typefertiorga[i] == "*Choice*" and y1_quantityfertiorga_float[i] > 0:
                Nfertiorga.append("Error!")
            elif y1_typefertiorga[i] != "*Choice*" and y1_typefertiorga[i] != "EFB" and y1_typefertiorga[i] != "Compost":
                Nfertiorga.append("Error!")
            else:
                Nfertiorga.append("Error!")


            # Information résultats
        equilabelnitroorgaferti=tkinter.Label(frame,
                                              text="Nitrogen equivalent organic fertilization (in kgN/ha/yr) :")
        equilabelnitroorgaferti.place(relx=0.45, rely=0.63)
        equnitrogenorgaferti = tkinter.Label(frame,
                                             text=Nfertiorga[0], font=("Ariel", 9, "bold"),
                                             bg="white", fg="blue", justify="right",
                                             width=10,
                                             relief="groove", borderwidth=5)
        equnitrogenorgaferti.place(relx=0.68, rely=0.63)

    # Fonction pour récupérer la valeur de placement organic
    def get_placementorgafertiy1():
        placementorgafertiy1list = [
            y1_Jan(y1_placementorgavar)]
        return placementorgafertiy1list
    # Création placement ferti organique
    y1_placementorgavar = ttk.Combobox(frame, values=Orgafertiplacement,
                                  width=20)
    y1_placementorgavar.set("*Choice*")
    y1_placementorgavar.place(relx=0.31, rely=0.63)

    # Fonction pour récupérer la valeur de biomasse understorey
    def get_understoreybiomassy1():
        understoreybiomassy1list = [
            y1_Jan(y1_understoreybiomass)]
        return understoreybiomassy1list
    # Création biomasse understorey
    y1_understoreybiomass = ttk.Combobox(frame, values=understoreybiomass,
                                       width=10)
    y1_understoreybiomass.set("*Choice*")
    y1_understoreybiomass.place(relx=0.05, rely=0.78)

    # Fonction pour récupérer la valeur de biomasse understorey
    def get_legumefractiony1():
        legumefractiony1list = [
            y1_Jan(y1_legumefraction)]
        return legumefractiony1list
    # Création legume fraction
    y1_legumefraction = ttk.Combobox(frame, values=understoreylegumefraction,
                                         width=10)
    y1_legumefraction.set("*Choice*")
    y1_legumefraction.place(relx=0.24, rely=0.78)

    # Fonction pour récupérer la valeur pruned fronds
    def get_prunedy1():
        prunedy1list = [
            y1_Jan(y1_pruned)]
        return prunedy1list
    # Création combobox pruned fronds
    y1_pruned = ttk.Combobox(frame, values=Prunedfronds,
                                     width=20)
    y1_pruned.set("*Choice*")
    y1_pruned.place(relx=0.07, rely=0.92)

    # Fonction pour récupérer toute la valeur Natmo
    def get_Natmodepoy1():
        Natmoy1list = [
            y1_Jan(y1_Natmodepo)]
        return Natmoy1list
    # Création quantité Natmo
    y1_Natmodepo = tkinter.Entry(frame,
                                 width=8,
                                 justify="right")
    y1_Natmodepo.insert(tkinter.END, "18")
    y1_Natmodepo.place(relx=0.66, rely=0.84)

    ################################################################################################################
    ###################################Year 2#######################################################################
    ################################################################################################################
    # Intégration de Second year dans la fenêtre
    year2 = (tkinter.Label(main_frame,
                           text="Second year", font=("Ariel", 20, 'underline')))
    year2.pack(anchor="w", pady=5)

    # Intégration du bloc data pour chaque type
    # Création encadré
    frame2 = tkinter.Frame(main_frame, bd=2, relief="solid", width=1450, height=400, padx=5, pady=2)
    frame2.pack(anchor="w", padx=15, pady=5, fill="none")

    # Mise de titre Mineral N ferti
    y2_MineralNfertilizer = (tkinter.Label(frame2,
                                           text="Mineral Nitrogen fertilizer", justify="center",
                                           font=("Ariel", 13, "bold", "underline")))
    y2_MineralNfertilizer.place(relx=0.01)

    # Mise de titre organic fertilizer
    y2_Organicfertilizer = (tkinter.Label(frame2,
                                          text="Organic fertilizer", justify="center",
                                          font=("Ariel", 13, "bold", "underline")))
    y2_Organicfertilizer.place(relx=0.01, rely=0.55)

    # Mise de titre understorey
    y2_Understorey = (tkinter.Label(frame2,
                                    text="Understorey", justify="center",
                                    font=("Ariel", 13, "bold", "underline")))
    y2_Understorey.place(relx=0.01, rely=0.7)

    # Mise de titre Pruned fronds
    y2_Prunedfronds = (tkinter.Label(frame2,
                                     text="Pruned fronds", justify="center",
                                     font=("Ariel", 13, "bold", "underline")))
    y2_Prunedfronds.place(relx=0.01, rely=0.85)

    # Mise titre atmospheric depositions
    y2_atmodepo = (tkinter.Label(frame2,
                                 text="Atmospheric depositions", justify="center",
                                 font=("Ariel", 13, "bold", "underline")))
    y2_atmodepo.place(relx=0.55, rely=0.75)

    # Intégration des mois
    y2_January = (tkinter.Label(frame2, text="January", font=("Ariel", 9), fg="blue"))
    y2_January.place(relx=0.06, rely=0.08)
    y2_February = (tkinter.Label(frame2, text="February", font=("Ariel", 9), fg="blue"))
    y2_February.place(relx=0.14, rely=0.08)
    y2_March = (tkinter.Label(frame2, text="March", font=("Ariel", 9), fg="blue"))
    y2_March.place(relx=0.22, rely=0.08)
    y2_April = (tkinter.Label(frame2, text="April", font=("Ariel", 9), fg="blue"))
    y2_April.place(relx=0.295, rely=0.08)
    y2_May = (tkinter.Label(frame2, text="May", font=("Ariel", 9), fg="blue"))
    y2_May.place(relx=0.377, rely=0.08)
    y2_June = (tkinter.Label(frame2, text="June", font=("Ariel", 9), fg="blue"))
    y2_June.place(relx=0.46, rely=0.08)
    y2_July = (tkinter.Label(frame2, text="July", font=("Ariel", 9), fg="blue"))
    y2_July.place(relx=0.54, rely=0.08)
    y2_August = (tkinter.Label(frame2, text="August", font=("Ariel", 9), fg="blue"))
    y2_August.place(relx=0.62, rely=0.08)
    y2_September = (tkinter.Label(frame2, text="September", font=("Ariel", 9), fg="blue"))
    y2_September.place(relx=0.69, rely=0.08)
    y2_October = (tkinter.Label(frame2, text="October", font=("Ariel", 9), fg="blue"))
    y2_October.place(relx=0.78, rely=0.08)
    y2_November = (tkinter.Label(frame2, text="November", font=("Ariel", 9), fg="blue"))
    y2_November.place(relx=0.85, rely=0.08)
    y2_December = (tkinter.Label(frame2, text="December", font=("Ariel", 9), fg="blue"))
    y2_December.place(relx=0.93, rely=0.08)

    # Création du type
    y2_type = (tkinter.Label(frame2, text="Type", fg="blue", font=("Ariel", 11, "bold")))
    y2_type.place(relx=0, rely=0.14)

    # Création data rate
    y2_rate = (tkinter.Label(frame2, text="Rate \n(kg/ha)", fg="blue", font=("Ariel", 11, "bold")))
    y2_rate.place(relx=0, rely=0.21)

    # Création placement
    y2_placementferti = (tkinter.Label(frame2, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y2_placementferti.place(relx=0, rely=0.47)

    # Création quantity ferti orga
    y2_quantityorga = (tkinter.Label(frame2, text="Quantity (in tFM)", fg="blue", font=("Ariel", 11, "bold")))
    y2_quantityorga.place(relx=0, rely=0.63)

    # Création type ferti orga
    y2_typeorga = (tkinter.Label(frame2, text="Type", fg="blue", font=("Ariel", 11, "bold")))
    y2_typeorga.place(relx=0.15, rely=0.63)

    # Création placement ferti orga
    y2_placementorga = (tkinter.Label(frame2, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y2_placementorga.place(relx=0.25, rely=0.63)

    # Création biomasse understorey
    y2_biomass = (tkinter.Label(frame2, text="Biomass", fg="blue", font=("Ariel", 11, "bold")))
    y2_biomass.place(relx=0, rely=0.78)

    # Création legume fraction
    y2_legumefrac = (tkinter.Label(frame2, text="Legume fraction", fg="blue", font=("Ariel", 11, "bold")))
    y2_legumefrac.place(relx=0.15, rely=0.78)

    # Création pruned fronts placement
    y2_prunedfr = (tkinter.Label(frame2, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y2_prunedfr.place(relx=0, rely=0.92)

    # Création atmospheric depositions
    y2_quantityNatmo = (
        tkinter.Label(frame2, text="Quantity of nitrogen\n (in kg/ha/yr)", fg="blue", font=("Ariel", 11, "bold")))
    y2_quantityNatmo.place(relx=0.55, rely=0.82)

    # Fonction pour récupérer toutes les valeurs des mois pour Type N ferti
    def get_all_month_valuestypeNfertiy2():
        month_valuestypeNfertiy2 = [
            y1_Jan(y2_Jan_typeNfertivar),
            y1_Feb(y2_Feb_typeNfertivar),
            y1_Mar(y2_Mar_typeNfertivar),
            y1_Apr(y2_Apr_typeNfertivar),
            y1_Maymonth(y2_Maymonth_typeNfertivar),
            y1_Jun(y2_Jun_typeNfertivar),
            y1_Jul(y2_Jul_typeNfertivar),
            y1_Aug(y2_Aug_typeNfertivar),
            y1_Sep(y2_Sep_typeNfertivar),
            y1_Oct(y2_Oct_typeNfertivar),
            y1_Nov(y2_Nov_typeNfertivar),
            y1_Dec(y2_Dec_typeNfertivar)
        ]

        return month_valuestypeNfertiy2

    # Créer une variable Tkinter pour stocker l'élément sélectionné Nfertitype
    # Création combobox
    # Janvier
    y2_Jan_typeNfertivar = ttk.Combobox(frame2, values=typeNferti,
                                        width=10)
    y2_Jan_typeNfertivar.set("*None")
    y2_Jan_typeNfertivar.place(relx=0.04, rely=0.14)
    # Février
    y2_Feb_typeNfertivar = ttk.Combobox(frame2, values=typeNferti,
                                        width=10)
    y2_Feb_typeNfertivar.set("*None")
    y2_Feb_typeNfertivar.place(relx=0.12, rely=0.14)
    # Mars
    y2_Mar_typeNfertivar = ttk.Combobox(frame2, values=typeNferti,
                                        width=10)
    y2_Mar_typeNfertivar.set("*None")
    y2_Mar_typeNfertivar.place(relx=0.2, rely=0.14)
    # Avril
    y2_Apr_typeNfertivar = ttk.Combobox(frame2, values=typeNferti,
                                        width=10)
    y2_Apr_typeNfertivar.set("*None")
    y2_Apr_typeNfertivar.place(relx=0.28, rely=0.14)
    # May
    y2_Maymonth_typeNfertivar = ttk.Combobox(frame2, values=typeNferti,
                                             width=10)
    y2_Maymonth_typeNfertivar.set("*None")
    y2_Maymonth_typeNfertivar.place(relx=0.36, rely=0.14)
    # Juin
    y2_Jun_typeNfertivar = ttk.Combobox(frame2, values=typeNferti,
                                        width=10)
    y2_Jun_typeNfertivar.set("*None")
    y2_Jun_typeNfertivar.place(relx=0.44, rely=0.14)
    # July
    y2_Jul_typeNfertivar = ttk.Combobox(frame2, values=typeNferti,
                                        width=10)
    y2_Jul_typeNfertivar.set("*None")
    y2_Jul_typeNfertivar.place(relx=0.52, rely=0.14)
    # Aout
    y2_Aug_typeNfertivar = ttk.Combobox(frame2, values=typeNferti,
                                        width=10)
    y2_Aug_typeNfertivar.set("*None")
    y2_Aug_typeNfertivar.place(relx=0.6, rely=0.14)
    # Septembre
    y2_Sep_typeNfertivar = ttk.Combobox(frame2, values=typeNferti,
                                        width=10)
    y2_Sep_typeNfertivar.set("*None")
    y2_Sep_typeNfertivar.place(relx=0.68, rely=0.14)
    # Octobre
    y2_Oct_typeNfertivar = ttk.Combobox(frame2, values=typeNferti,
                                        width=10)
    y2_Oct_typeNfertivar.set("*None")
    y2_Oct_typeNfertivar.place(relx=0.76, rely=0.14)
    # Novembre
    y2_Nov_typeNfertivar = ttk.Combobox(frame2, values=typeNferti,
                                        width=10)
    y2_Nov_typeNfertivar.set("*None")
    y2_Nov_typeNfertivar.place(relx=0.84, rely=0.14)
    # Décembre
    y2_Dec_typeNfertivar = ttk.Combobox(frame2, values=typeNferti,
                                        width=10)
    y2_Dec_typeNfertivar.set("*None")
    y2_Dec_typeNfertivar.place(relx=0.92, rely=0.14)

    # Fonction pour récupérer toutes les valeurs des mois pour rate N ferti
    def get_all_month_valuesrateNfertiy2():
        month_valuesrateNfertiy2 = [
            y1_Jan(y2_Jan_rateNfertivar),
            y1_Feb(y2_Feb_rateNfertivar),
            y1_Mar(y2_Mar_rateNfertivar),
            y1_Apr(y2_Apr_rateNfertivar),
            y1_Maymonth(y2_Maymonth_rateNfertivar),
            y1_Jun(y2_Jun_rateNfertivar),
            y1_Jul(y2_Jul_rateNfertivar),
            y1_Aug(y2_Aug_rateNfertivar),
            y1_Sep(y2_Sep_rateNfertivar),
            y1_Oct(y2_Oct_rateNfertivar),
            y1_Nov(y2_Nov_rateNfertivar),
            y1_Dec(y2_Dec_rateNfertivar)
        ]
        return month_valuesrateNfertiy2

    # Créer une variable Tkinter pour stocker l'élément sélectionné NfertiRate
    # Création combobox
    # Janvier
    y2_Jan_rateNfertivar = tkinter.Entry(frame2,
                                         width=13,
                                         justify="right")
    y2_Jan_rateNfertivar.insert(tkinter.END, "0")
    y2_Jan_rateNfertivar.place(relx=0.04, rely=0.22)
    # Février
    y2_Feb_rateNfertivar = tkinter.Entry(frame2,
                                         width=13,
                                         justify="right")
    y2_Feb_rateNfertivar.insert(tkinter.END, "0")
    y2_Feb_rateNfertivar.place(relx=0.12, rely=0.22)
    # Mars
    y2_Mar_rateNfertivar = tkinter.Entry(frame2,
                                         width=13,
                                         justify="right")
    y2_Mar_rateNfertivar.insert(tkinter.END, "0")
    y2_Mar_rateNfertivar.place(relx=0.2, rely=0.22)
    # Avril
    y2_Apr_rateNfertivar = tkinter.Entry(frame2,
                                         width=13,
                                         justify="right")
    y2_Apr_rateNfertivar.insert(tkinter.END, "0")
    y2_Apr_rateNfertivar.place(relx=0.28, rely=0.22)
    # May
    y2_Maymonth_rateNfertivar = tkinter.Entry(frame2,
                                              width=13,
                                              justify="right")
    y2_Maymonth_rateNfertivar.insert(tkinter.END, "0")
    y2_Maymonth_rateNfertivar.place(relx=0.36, rely=0.22)
    # Juin
    y2_Jun_rateNfertivar = tkinter.Entry(frame2,
                                         width=13,
                                         justify="right")
    y2_Jun_rateNfertivar.insert(tkinter.END, "0")
    y2_Jun_rateNfertivar.place(relx=0.44, rely=0.22)
    # July
    y2_Jul_rateNfertivar = tkinter.Entry(frame2,
                                         width=13,
                                         justify="right")
    y2_Jul_rateNfertivar.insert(tkinter.END, "0")
    y2_Jul_rateNfertivar.place(relx=0.52, rely=0.22)
    # Aout
    y2_Aug_rateNfertivar = tkinter.Entry(frame2,
                                         width=13,
                                         justify="right")
    y2_Aug_rateNfertivar.insert(tkinter.END, "0")
    y2_Aug_rateNfertivar.place(relx=0.6, rely=0.22)
    # Septembre
    y2_Sep_rateNfertivar = tkinter.Entry(frame2,
                                         width=13,
                                         justify="right")
    y2_Sep_rateNfertivar.insert(tkinter.END, "0")
    y2_Sep_rateNfertivar.place(relx=0.68, rely=0.22)
    # Octobre
    y2_Oct_rateNfertivar = tkinter.Entry(frame2,
                                         width=13,
                                         justify="right")
    y2_Oct_rateNfertivar.insert(tkinter.END, "0")
    y2_Oct_rateNfertivar.place(relx=0.76, rely=0.22)
    # Novembre
    y2_Nov_rateNfertivar = tkinter.Entry(frame2,
                                         width=13,
                                         justify="right")
    y2_Nov_rateNfertivar.insert(tkinter.END, "0")
    y2_Nov_rateNfertivar.place(relx=0.84, rely=0.22)
    # Décembre
    y2_Dec_rateNfertivar = tkinter.Entry(frame2,
                                         width=13,
                                         justify="right")
    y2_Dec_rateNfertivar.insert(tkinter.END, "0")
    y2_Dec_rateNfertivar.place(relx=0.92, rely=0.22)

    # Calcule du taux d'N en kg/ha en fonction de l'apport et du type ferti
    def calculate_kgN2():
        # Mise des return list dans des listes spécifiques
        listferti = printlist()
        y2rateferti_str = listferti[11]
        y2typeferti = listferti[10]
        # Création d'une liste vide convertissant les rate str en float
        y2rateferti_float = []
        # Création d'une liste pour les résultats des calcules
        resultlist = []
        # Vérification que chaque élément de cette liste puisse être convertie + conversion

        try:
            for i in y2rateferti_str:
                y2rateferti_float.append(float(i))
        except ValueError:
            print("Error! Please check you rate data. Some data are not float")

        # Calcule taux N en fonction type ferti
        for i in range(12):  # Pour janvier (0) et février (1)
            if y2typeferti[i] == "*None" and y2rateferti_float[i] == 0:
                resultlist.append(0)
            elif y2typeferti[i] == "Ammo Chlo" and y2rateferti_float[i] > 0:
                resammochlo = round(0.25 * y2rateferti_float[i], 1)
                resultlist.append(resammochlo)
            elif y2typeferti[i] == "Ammo Nit" and y2rateferti_float[i] > 0:
                resammonit = round(0.34 * y2rateferti_float[i], 1)
                resultlist.append(resammonit)
            elif y2typeferti[i] == "Ammo Sulf" and y2rateferti_float[i] > 0:
                resammosulf = round(0.21 * y2rateferti_float[i], 1)
                resultlist.append(resammosulf)
            elif y2typeferti[i] == "Sod Nit" and y2rateferti_float[i] > 0:
                ressodnit = round(0.16 * y2rateferti_float[i], 1)
                resultlist.append(ressodnit)
            elif y2typeferti[i] == "Urea" and y2rateferti_float[i] > 0:
                resurea = round(0.46 * y2rateferti_float[i], 1)
                resultlist.append(resurea)
            elif y2typeferti[i] == "*None" and y2rateferti_float[i] > 0:
                resultlist.append("Error!")
            elif y2typeferti[i] != "*None" and y2typeferti[i] != "Ammo Chlo" and y2typeferti[i] != "Ammo Nit" and \
                    y2typeferti[i] != "Ammo Sulf" and y2typeferti[i] != "Sod Nit" and y2typeferti[i] != "Urea":
                resultlist.append("Error!")
            else:
                resultlist.append("Error!")

        # Information résultats
        # Janvier
        equnitrogenjan = tkinter.Label(frame2,
                                       text=resultlist[0], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjan.place(relx=0.04, rely=0.28)
        # Fevrier
        equnitrogenfev = tkinter.Label(frame2,
                                       text=resultlist[1], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenfev.place(relx=0.12, rely=0.28)
        # Mars
        equnitrogenmar = tkinter.Label(frame2,
                                       text=resultlist[2], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenmar.place(relx=0.2, rely=0.28)
        # Avril
        equnitrogenapr = tkinter.Label(frame2,
                                       text=resultlist[3], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenapr.place(relx=0.28, rely=0.28)
        # Mai
        equnitrogenmay = tkinter.Label(frame2,
                                       text=resultlist[4], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenmay.place(relx=0.36, rely=0.28)
        # Juin
        equnitrogenjun = tkinter.Label(frame2,
                                       text=resultlist[5], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjun.place(relx=0.44, rely=0.28)
        # Juillet
        equnitrogenjul = tkinter.Label(frame2,
                                       text=resultlist[6], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjul.place(relx=0.52, rely=0.28)
        # Aout
        equnitrogenaug = tkinter.Label(frame2,
                                       text=resultlist[7], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenaug.place(relx=0.6, rely=0.28)
        # September
        equnitrogensep = tkinter.Label(frame2,
                                       text=resultlist[8], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogensep.place(relx=0.68, rely=0.28)
        # Octobre
        equnitrogenoct = tkinter.Label(frame2,
                                       text=resultlist[9], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenoct.place(relx=0.76, rely=0.28)
        # Novembre
        equnitrogennov = tkinter.Label(frame2,
                                       text=resultlist[10], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogennov.place(relx=0.84, rely=0.28)
        # Decembre
        equnitrogendec = tkinter.Label(frame2,
                                       text=resultlist[11], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogendec.place(relx=0.92, rely=0.28)

        # Calcule total annuelle
        yearcumul = 0
        resultlist_float = []
        try:
            for i in resultlist:
                resultlist_float.append(float(i))
        except ValueError:
            return
        for i in resultlist_float:
            if isinstance(i, float):
                yearcumul = round(i + yearcumul,1)
        # label cacule annuel
        Nfertianuel = tkinter.Label(frame2, text=f"Cumulative nitrogen for year: {yearcumul}")
        Nfertianuel.place(relx=0.04, rely=0.35)

    # Création bouton calcul équivalent azote N ferti
    button = tkinter.Button(frame2, text="Nitrogen equivalent (in kg/ha)",
                            width=100,
                            font=("Ariel", 10, "bold"), bg="lightblue",
                            command=lambda: [calculate_kgN2(), calculate_kgNorga2()])
    button.place(relx=0.2, rely=0.4)

    # Fonction pour récupérer toutes les infos placement
    def get_placement2():
        placementfertiy2 = [
            y1_Jan(y2_placementferti)]
        return placementfertiy2

    # Création combobox placement N ferti
    y2_placementferti = ttk.Combobox(frame2, values=Nfertiplacement,
                                     width=21)
    y2_placementferti.set("*Choice*")
    y2_placementferti.place(relx=0.06, rely=0.47)

    # Fonction pour récupérer toute la valeur de quantity organic
    def get_quantityorgafertiy2():
        quantityorgafertiy2list = [
            y1_Jan(y2_quantityorgavar)]
        return quantityorgafertiy2list

    # Création quantité fertilisation organique
    y2_quantityorgavar = tkinter.Entry(frame2,
                                       width=8,
                                       justify="right")
    y2_quantityorgavar.insert(tkinter.END, "0")
    y2_quantityorgavar.place(relx=0.1, rely=0.63)

    # Fonction pour récupérer la valeur de type organic
    def get_typeorgafertiy2():
        typeorgafertiy2list = [
            y1_Jan(y2_typeorgavar)]
        return typeorgafertiy2list

    # Création quantité fertilisation organique
    y2_typeorgavar = ttk.Combobox(frame2, values=Orgafertitype,
                                  width=10)
    y2_typeorgavar.set("*Choice*")
    y2_typeorgavar.place(relx=0.185, rely=0.63)

    # Calcule équivalent N ferti orga
    def calculate_kgNorga2():
        # Mise des return list dans des listes spécifiques
        listferti = printlist()
        y2_typefertiorga = listferti[14]
        y2_quantityfertiorga = listferti[13]
        print(y2_typefertiorga)
        # Création d'une liste vide permettant conversion liste en float
        y2_quantityfertiorga_float = []
        # Création liste pour valeurs
        Nfertiorga = []
        # Vérification que chaque élément de cette liste puisse être convertie + conversion
        try:
            for i in y2_quantityfertiorga:
                y2_quantityfertiorga_float.append(float(i))
        except ValueError:
            print("Error! Please check you rate data. Some data are not float")
            return
        # Calcule taux N en fonction type ferti orga si plusieurs valeurs
        for i in range(1):
            if y2_typefertiorga[i] == "*Choice*" and y2_quantityfertiorga_float[i] == 0:
                Nfertiorga.append(0)
            elif y2_typefertiorga[i] == "EFB" and y2_quantityfertiorga_float[i] > 0:
                # 0.90% N in DM * 0.36tDM/tFM (cf pg Pardon)
                Nfertiorgacal = round(3.24 * y2_quantityfertiorga_float[i], 1)
                Nfertiorga.append(Nfertiorgacal)
            elif y2_typefertiorga[i] == "Compost" and y2_quantityfertiorga_float[i] > 0:
                # 2.05% N in DM * 0.41tDM/tFM (cf pg Pardon)
                Nfertiorgacal = round(8.405 * y2_quantityfertiorga_float[i], 1)
                Nfertiorga.append(Nfertiorgacal)
            elif y2_typefertiorga[i] == "*Choice*" and y2_quantityfertiorga_float[i] > 0:
                Nfertiorga.append("Error!")
            elif y2_typefertiorga[i] != "*Choice*" and y2_typefertiorga[i] != "EFB" and y2_typefertiorga[i] != "Compost":
                Nfertiorga.append("Error!")
            else:
                Nfertiorga.append("Error!")

            # Information résultats
        equilabelnitroorgaferti = tkinter.Label(frame2,
                                                text="Nitrogen equivalent organic fertilization (in kgN/ha/yr) :")
        equilabelnitroorgaferti.place(relx=0.45, rely=0.63)
        equnitrogenorgaferti = tkinter.Label(frame2,
                                             text=Nfertiorga[0], font=("Ariel", 9, "bold"),
                                             bg="white", fg="blue", justify="right",
                                             width=10,
                                             relief="groove", borderwidth=5)
        equnitrogenorgaferti.place(relx=0.68, rely=0.63)

    # Fonction pour récupérer la valeur de placement organic
    def get_placementorgafertiy2():
        placementorgafertiy2list = [
            y1_Jan(y2_placementorgavar)]
        return placementorgafertiy2list

    # Création placement ferti organique
    y2_placementorgavar = ttk.Combobox(frame2, values=Orgafertiplacement,
                                       width=20)
    y2_placementorgavar.set("*Choice*")
    y2_placementorgavar.place(relx=0.31, rely=0.63)

    # Fonction pour récupérer la valeur de biomasse understorey
    def get_understoreybiomassy2():
        understoreybiomassy2list = [
            y1_Jan(y2_understoreybiomass)]
        return understoreybiomassy2list

    # Création biomasse understorey
    y2_understoreybiomass = ttk.Combobox(frame2, values=understoreybiomass,
                                         width=10)
    y2_understoreybiomass.set("*Choice*")
    y2_understoreybiomass.place(relx=0.05, rely=0.78)

    # Fonction pour récupérer la valeur de biomasse understorey
    def get_legumefractiony2():
        legumefractiony2list = [
            y1_Jan(y2_legumefraction)]
        return legumefractiony2list

    # Création legume fraction
    y2_legumefraction = ttk.Combobox(frame2, values=understoreylegumefraction,
                                     width=10)
    y2_legumefraction.set("*Choice*")
    y2_legumefraction.place(relx=0.24, rely=0.78)

    # Fonction pour récupérer la valeur pruned fronds
    def get_prunedy2():
        prunedy2list = [
            y1_Jan(y2_pruned)]
        return prunedy2list

    # Création combobox pruned fronds
    y2_pruned = ttk.Combobox(frame2, values=Prunedfronds,
                             width=20)
    y2_pruned.set("*Choice*")
    y2_pruned.place(relx=0.07, rely=0.92)

    # Fonction pour récupérer toute la valeur Natmo
    def get_Natmodepoy2():
        Natmoy2list = [
            y1_Jan(y2_Natmodepo)]
        return Natmoy2list

    # Création quantité Natmo
    y2_Natmodepo = tkinter.Entry(frame2,
                                 width=8,
                                 justify="right")
    y2_Natmodepo.insert(tkinter.END, "18")
    y2_Natmodepo.place(relx=0.66, rely=0.84)


    ################################################################################################################
    ###################################Year 3#######################################################################
    ################################################################################################################
    # Intégration de Second year dans la fenêtre
    year3 = (tkinter.Label(main_frame,
                           text="Third year", font=("Ariel", 20, 'underline')))
    year3.pack(anchor="w", pady=5)

    # Intégration du bloc data pour chaque type
    # Création encadré
    frame3 = tkinter.Frame(main_frame, bd=2, relief="solid", width=1450, height=400, padx=5, pady=2)
    frame3.pack(anchor="w", padx=15, pady=5, fill="none")

    # Mise de titre Mineral N ferti
    y3_MineralNfertilizer = (tkinter.Label(frame3,
                                           text="Mineral Nitrogen fertilizer", justify="center",
                                           font=("Ariel", 13, "bold", "underline")))
    y3_MineralNfertilizer.place(relx=0.01)

    # Mise de titre organic fertilizer
    y3_Organicfertilizer = (tkinter.Label(frame3,
                                          text="Organic fertilizer", justify="center",
                                          font=("Ariel", 13, "bold", "underline")))
    y3_Organicfertilizer.place(relx=0.01, rely=0.55)

    # Mise de titre understorey
    y3_Understorey = (tkinter.Label(frame3,
                                    text="Understorey", justify="center",
                                    font=("Ariel", 13, "bold", "underline")))
    y3_Understorey.place(relx=0.01, rely=0.7)

    # Mise de titre Pruned fronds
    y3_Prunedfronds = (tkinter.Label(frame3,
                                     text="Pruned fronds", justify="center",
                                     font=("Ariel", 13, "bold", "underline")))
    y3_Prunedfronds.place(relx=0.01, rely=0.85)

    # Mise titre atmospheric depositions
    y3_atmodepo = (tkinter.Label(frame3,
                                 text="Atmospheric depositions", justify="center",
                                 font=("Ariel", 13, "bold", "underline")))
    y3_atmodepo.place(relx=0.55, rely=0.75)

    # Intégration des mois
    y3_January = (tkinter.Label(frame3, text="January", font=("Ariel", 9), fg="blue"))
    y3_January.place(relx=0.06, rely=0.08)
    y3_February = (tkinter.Label(frame3, text="February", font=("Ariel", 9), fg="blue"))
    y3_February.place(relx=0.14, rely=0.08)
    y3_March = (tkinter.Label(frame3, text="March", font=("Ariel", 9), fg="blue"))
    y3_March.place(relx=0.22, rely=0.08)
    y3_April = (tkinter.Label(frame3, text="April", font=("Ariel", 9), fg="blue"))
    y3_April.place(relx=0.295, rely=0.08)
    y3_May = (tkinter.Label(frame3, text="May", font=("Ariel", 9), fg="blue"))
    y3_May.place(relx=0.377, rely=0.08)
    y3_June = (tkinter.Label(frame3, text="June", font=("Ariel", 9), fg="blue"))
    y3_June.place(relx=0.46, rely=0.08)
    y3_July = (tkinter.Label(frame3, text="July", font=("Ariel", 9), fg="blue"))
    y3_July.place(relx=0.54, rely=0.08)
    y3_August = (tkinter.Label(frame3, text="August", font=("Ariel", 9), fg="blue"))
    y3_August.place(relx=0.62, rely=0.08)
    y3_September = (tkinter.Label(frame3, text="September", font=("Ariel", 9), fg="blue"))
    y3_September.place(relx=0.69, rely=0.08)
    y3_October = (tkinter.Label(frame3, text="October", font=("Ariel", 9), fg="blue"))
    y3_October.place(relx=0.78, rely=0.08)
    y3_November = (tkinter.Label(frame3, text="November", font=("Ariel", 9), fg="blue"))
    y3_November.place(relx=0.85, rely=0.08)
    y3_December = (tkinter.Label(frame3, text="December", font=("Ariel", 9), fg="blue"))
    y3_December.place(relx=0.93, rely=0.08)

    # Création du type
    y3_type = (tkinter.Label(frame3, text="Type", fg="blue", font=("Ariel", 11, "bold")))
    y3_type.place(relx=0, rely=0.14)

    # Création data rate
    y3_rate = (tkinter.Label(frame3, text="Rate \n(kg/ha)", fg="blue", font=("Ariel", 11, "bold")))
    y3_rate.place(relx=0, rely=0.21)

    # Création placement
    y3_placementferti = (tkinter.Label(frame3, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y3_placementferti.place(relx=0, rely=0.47)

    # Création quantity ferti orga
    y3_quantityorga = (tkinter.Label(frame3, text="Quantity (in tFM)", fg="blue", font=("Ariel", 11, "bold")))
    y3_quantityorga.place(relx=0, rely=0.63)

    # Création type ferti orga
    y3_typeorga = (tkinter.Label(frame3, text="Type", fg="blue", font=("Ariel", 11, "bold")))
    y3_typeorga.place(relx=0.15, rely=0.63)

    # Création placement ferti orga
    y3_placementorga = (tkinter.Label(frame3, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y3_placementorga.place(relx=0.25, rely=0.63)

    # Création biomasse understorey
    y3_biomass = (tkinter.Label(frame3, text="Biomass", fg="blue", font=("Ariel", 11, "bold")))
    y3_biomass.place(relx=0, rely=0.78)

    # Création legume fraction
    y3_legumefrac = (tkinter.Label(frame3, text="Legume fraction", fg="blue", font=("Ariel", 11, "bold")))
    y3_legumefrac.place(relx=0.15, rely=0.78)

    # Création pruned fronts placement
    y3_prunedfr = (tkinter.Label(frame3, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y3_prunedfr.place(relx=0, rely=0.92)

    # Création atmospheric depositions
    y3_quantityNatmo = (
        tkinter.Label(frame3, text="Quantity of nitrogen\n (in kg/ha/yr)", fg="blue", font=("Ariel", 11, "bold")))
    y3_quantityNatmo.place(relx=0.55, rely=0.82)

    # Fonction pour récupérer toutes les valeurs des mois pour Type N ferti
    def get_all_month_valuestypeNfertiy3():
        month_valuestypeNfertiy3 = [
            y1_Jan(y3_Jan_typeNfertivar),
            y1_Feb(y3_Feb_typeNfertivar),
            y1_Mar(y3_Mar_typeNfertivar),
            y1_Apr(y3_Apr_typeNfertivar),
            y1_Maymonth(y3_Maymonth_typeNfertivar),
            y1_Jun(y3_Jun_typeNfertivar),
            y1_Jul(y3_Jul_typeNfertivar),
            y1_Aug(y3_Aug_typeNfertivar),
            y1_Sep(y3_Sep_typeNfertivar),
            y1_Oct(y3_Oct_typeNfertivar),
            y1_Nov(y3_Nov_typeNfertivar),
            y1_Dec(y3_Dec_typeNfertivar)
        ]

        return month_valuestypeNfertiy3

    # Créer une variable Tkinter pour stocker l'élément sélectionné Nfertitype
    # Création combobox
    # Janvier
    y3_Jan_typeNfertivar = ttk.Combobox(frame3, values=typeNferti,
                                        width=10)
    y3_Jan_typeNfertivar.set("*None")
    y3_Jan_typeNfertivar.place(relx=0.04, rely=0.14)
    # Février
    y3_Feb_typeNfertivar = ttk.Combobox(frame3, values=typeNferti,
                                        width=10)
    y3_Feb_typeNfertivar.set("*None")
    y3_Feb_typeNfertivar.place(relx=0.12, rely=0.14)
    # Mars
    y3_Mar_typeNfertivar = ttk.Combobox(frame3, values=typeNferti,
                                        width=10)
    y3_Mar_typeNfertivar.set("*None")
    y3_Mar_typeNfertivar.place(relx=0.2, rely=0.14)
    # Avril
    y3_Apr_typeNfertivar = ttk.Combobox(frame3, values=typeNferti,
                                        width=10)
    y3_Apr_typeNfertivar.set("*None")
    y3_Apr_typeNfertivar.place(relx=0.28, rely=0.14)
    # May
    y3_Maymonth_typeNfertivar = ttk.Combobox(frame3, values=typeNferti,
                                             width=10)
    y3_Maymonth_typeNfertivar.set("*None")
    y3_Maymonth_typeNfertivar.place(relx=0.36, rely=0.14)
    # Juin
    y3_Jun_typeNfertivar = ttk.Combobox(frame3, values=typeNferti,
                                        width=10)
    y3_Jun_typeNfertivar.set("*None")
    y3_Jun_typeNfertivar.place(relx=0.44, rely=0.14)
    # July
    y3_Jul_typeNfertivar = ttk.Combobox(frame3, values=typeNferti,
                                        width=10)
    y3_Jul_typeNfertivar.set("*None")
    y3_Jul_typeNfertivar.place(relx=0.52, rely=0.14)
    # Aout
    y3_Aug_typeNfertivar = ttk.Combobox(frame3, values=typeNferti,
                                        width=10)
    y3_Aug_typeNfertivar.set("*None")
    y3_Aug_typeNfertivar.place(relx=0.6, rely=0.14)
    # Septembre
    y3_Sep_typeNfertivar = ttk.Combobox(frame3, values=typeNferti,
                                        width=10)
    y3_Sep_typeNfertivar.set("*None")
    y3_Sep_typeNfertivar.place(relx=0.68, rely=0.14)
    # Octobre
    y3_Oct_typeNfertivar = ttk.Combobox(frame3, values=typeNferti,
                                        width=10)
    y3_Oct_typeNfertivar.set("*None")
    y3_Oct_typeNfertivar.place(relx=0.76, rely=0.14)
    # Novembre
    y3_Nov_typeNfertivar = ttk.Combobox(frame3, values=typeNferti,
                                        width=10)
    y3_Nov_typeNfertivar.set("*None")
    y3_Nov_typeNfertivar.place(relx=0.84, rely=0.14)
    # Décembre
    y3_Dec_typeNfertivar = ttk.Combobox(frame3, values=typeNferti,
                                        width=10)
    y3_Dec_typeNfertivar.set("*None")
    y3_Dec_typeNfertivar.place(relx=0.92, rely=0.14)

    # Fonction pour récupérer toutes les valeurs des mois pour rate N ferti
    def get_all_month_valuesrateNfertiy3():
        month_valuesrateNfertiy3 = [
            y1_Jan(y3_Jan_rateNfertivar),
            y1_Feb(y3_Feb_rateNfertivar),
            y1_Mar(y3_Mar_rateNfertivar),
            y1_Apr(y3_Apr_rateNfertivar),
            y1_Maymonth(y3_Maymonth_rateNfertivar),
            y1_Jun(y3_Jun_rateNfertivar),
            y1_Jul(y3_Jul_rateNfertivar),
            y1_Aug(y3_Aug_rateNfertivar),
            y1_Sep(y3_Sep_rateNfertivar),
            y1_Oct(y3_Oct_rateNfertivar),
            y1_Nov(y3_Nov_rateNfertivar),
            y1_Dec(y3_Dec_rateNfertivar)
        ]
        return month_valuesrateNfertiy3

    # Créer une variable Tkinter pour stocker l'élément sélectionné NfertiRate
    # Création combobox
    # Janvier
    y3_Jan_rateNfertivar = tkinter.Entry(frame3,
                                         width=13,
                                         justify="right")
    y3_Jan_rateNfertivar.insert(tkinter.END, "0")
    y3_Jan_rateNfertivar.place(relx=0.04, rely=0.22)
    # Février
    y3_Feb_rateNfertivar = tkinter.Entry(frame3,
                                         width=13,
                                         justify="right")
    y3_Feb_rateNfertivar.insert(tkinter.END, "0")
    y3_Feb_rateNfertivar.place(relx=0.12, rely=0.22)
    # Mars
    y3_Mar_rateNfertivar = tkinter.Entry(frame3,
                                         width=13,
                                         justify="right")
    y3_Mar_rateNfertivar.insert(tkinter.END, "0")
    y3_Mar_rateNfertivar.place(relx=0.2, rely=0.22)
    # Avril
    y3_Apr_rateNfertivar = tkinter.Entry(frame3,
                                         width=13,
                                         justify="right")
    y3_Apr_rateNfertivar.insert(tkinter.END, "0")
    y3_Apr_rateNfertivar.place(relx=0.28, rely=0.22)
    # May
    y3_Maymonth_rateNfertivar = tkinter.Entry(frame3,
                                              width=13,
                                              justify="right")
    y3_Maymonth_rateNfertivar.insert(tkinter.END, "0")
    y3_Maymonth_rateNfertivar.place(relx=0.36, rely=0.22)
    # Juin
    y3_Jun_rateNfertivar = tkinter.Entry(frame3,
                                         width=13,
                                         justify="right")
    y3_Jun_rateNfertivar.insert(tkinter.END, "0")
    y3_Jun_rateNfertivar.place(relx=0.44, rely=0.22)
    # July
    y3_Jul_rateNfertivar = tkinter.Entry(frame3,
                                         width=13,
                                         justify="right")
    y3_Jul_rateNfertivar.insert(tkinter.END, "0")
    y3_Jul_rateNfertivar.place(relx=0.52, rely=0.22)
    # Aout
    y3_Aug_rateNfertivar = tkinter.Entry(frame3,
                                         width=13,
                                         justify="right")
    y3_Aug_rateNfertivar.insert(tkinter.END, "0")
    y3_Aug_rateNfertivar.place(relx=0.6, rely=0.22)
    # Septembre
    y3_Sep_rateNfertivar = tkinter.Entry(frame3,
                                         width=13,
                                         justify="right")
    y3_Sep_rateNfertivar.insert(tkinter.END, "0")
    y3_Sep_rateNfertivar.place(relx=0.68, rely=0.22)
    # Octobre
    y3_Oct_rateNfertivar = tkinter.Entry(frame3,
                                         width=13,
                                         justify="right")
    y3_Oct_rateNfertivar.insert(tkinter.END, "0")
    y3_Oct_rateNfertivar.place(relx=0.76, rely=0.22)
    # Novembre
    y3_Nov_rateNfertivar = tkinter.Entry(frame3,
                                         width=13,
                                         justify="right")
    y3_Nov_rateNfertivar.insert(tkinter.END, "0")
    y3_Nov_rateNfertivar.place(relx=0.84, rely=0.22)
    # Décembre
    y3_Dec_rateNfertivar = tkinter.Entry(frame3,
                                         width=13,
                                         justify="right")
    y3_Dec_rateNfertivar.insert(tkinter.END, "0")
    y3_Dec_rateNfertivar.place(relx=0.92, rely=0.22)

    # Calcule du taux d'N en kg/ha en fonction de l'apport et du type ferti
    def calculate_kgN3():
        # Mise des return list dans des listes spécifiques
        listferti = printlist()
        y3rateferti_str = listferti[21]
        y3typeferti = listferti[20]
        # Création d'une liste vide convertissant les rate str en float
        y3rateferti_float = []
        # Création d'une liste pour les résultats des calcules
        resultlist = []
        # Vérification que chaque élément de cette liste puisse être convertie + conversion

        try:
            for i in y3rateferti_str:
                y3rateferti_float.append(float(i))
        except ValueError:
            print("Error! Please check you rate data. Some data are not float")

        # Calcule taux N en fonction type ferti
        for i in range(12):  # Pour janvier (0) et février (1)
            if y3typeferti[i] == "*None" and y3rateferti_float[i] == 0:
                resultlist.append(0)
            elif y3typeferti[i] == "Ammo Chlo" and y3rateferti_float[i] > 0:
                resammochlo = round(0.25 * y3rateferti_float[i], 1)
                resultlist.append(resammochlo)
            elif y3typeferti[i] == "Ammo Nit" and y3rateferti_float[i] > 0:
                resammonit = round(0.34 * y3rateferti_float[i], 1)
                resultlist.append(resammonit)
            elif y3typeferti[i] == "Ammo Sulf" and y3rateferti_float[i] > 0:
                resammosulf = round(0.21 * y3rateferti_float[i], 1)
                resultlist.append(resammosulf)
            elif y3typeferti[i] == "Sod Nit" and y3rateferti_float[i] > 0:
                ressodnit = round(0.16 * y3rateferti_float[i], 1)
                resultlist.append(ressodnit)
            elif y3typeferti[i] == "Urea" and y3rateferti_float[i] > 0:
                resurea = round(0.46 * y3rateferti_float[i], 1)
                resultlist.append(resurea)
            elif y3typeferti[i] == "*None" and y3rateferti_float[i] > 0:
                resultlist.append("Error!")
            elif y3typeferti[i] != "*None" and y3typeferti[i] != "Ammo Chlo" and y3typeferti[i] != "Ammo Nit" and \
                    y3typeferti[i] != "Ammo Sulf" and y3typeferti[i] != "Sod Nit" and y3typeferti[i] != "Urea":
                resultlist.append("Error!")
            else:
                resultlist.append("Error!")

        # Information résultats
        # Janvier
        equnitrogenjan = tkinter.Label(frame3,
                                       text=resultlist[0], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjan.place(relx=0.04, rely=0.28)
        # Fevrier
        equnitrogenfev = tkinter.Label(frame3,
                                       text=resultlist[1], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenfev.place(relx=0.12, rely=0.28)
        # Mars
        equnitrogenmar = tkinter.Label(frame3,
                                       text=resultlist[2], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenmar.place(relx=0.2, rely=0.28)
        # Avril
        equnitrogenapr = tkinter.Label(frame3,
                                       text=resultlist[3], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenapr.place(relx=0.28, rely=0.28)
        # Mai
        equnitrogenmay = tkinter.Label(frame3,
                                       text=resultlist[4], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenmay.place(relx=0.36, rely=0.28)
        # Juin
        equnitrogenjun = tkinter.Label(frame3,
                                       text=resultlist[5], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjun.place(relx=0.44, rely=0.28)
        # Juillet
        equnitrogenjul = tkinter.Label(frame3,
                                       text=resultlist[6], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjul.place(relx=0.52, rely=0.28)
        # Aout
        equnitrogenaug = tkinter.Label(frame3,
                                       text=resultlist[7], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenaug.place(relx=0.6, rely=0.28)
        # September
        equnitrogensep = tkinter.Label(frame3,
                                       text=resultlist[8], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogensep.place(relx=0.68, rely=0.28)
        # Octobre
        equnitrogenoct = tkinter.Label(frame3,
                                       text=resultlist[9], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenoct.place(relx=0.76, rely=0.28)
        # Novembre
        equnitrogennov = tkinter.Label(frame3,
                                       text=resultlist[10], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogennov.place(relx=0.84, rely=0.28)
        # Decembre
        equnitrogendec = tkinter.Label(frame3,
                                       text=resultlist[11], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogendec.place(relx=0.92, rely=0.28)

        # Calcule total annuelle
        yearcumul = 0
        resultlist_float = []
        try:
            for i in resultlist:
                resultlist_float.append(float(i))
        except ValueError:
            return
        for i in resultlist_float:
            if isinstance(i, float):
                yearcumul = round(i + yearcumul,1)
        # label cacule annuel
        Nfertianuel = tkinter.Label(frame3, text=f"Cumulative nitrogen for year: {yearcumul}")
        Nfertianuel.place(relx=0.04, rely=0.35)

    # Création bouton calcul équivalent azote N ferti
    button = tkinter.Button(frame3, text="Nitrogen equivalent (in kg/ha)",
                            width=100,
                            font=("Ariel", 10, "bold"), bg="lightblue",
                            command=lambda: [calculate_kgN3(), calculate_kgNorga3()])
    button.place(relx=0.2, rely=0.4)

    # Fonction pour récupérer toutes les infos placement
    def get_placement3():
        placementfertiy3 = [
            y1_Jan(y3_placementferti)]
        return placementfertiy3

    # Création combobox placement N ferti
    y3_placementferti = ttk.Combobox(frame3, values=Nfertiplacement,
                                     width=21)
    y3_placementferti.set("*Choice*")
    y3_placementferti.place(relx=0.06, rely=0.47)

    # Fonction pour récupérer toute la valeur de quantity organic
    def get_quantityorgafertiy3():
        quantityorgafertiy3list = [
            y1_Jan(y3_quantityorgavar)]
        return quantityorgafertiy3list

    # Création quantité fertilisation organique
    y3_quantityorgavar = tkinter.Entry(frame3,
                                       width=8,
                                       justify="right")
    y3_quantityorgavar.insert(tkinter.END, "0")
    y3_quantityorgavar.place(relx=0.1, rely=0.63)

    # Fonction pour récupérer la valeur de type organic
    def get_typeorgafertiy3():
        typeorgafertiy3list = [
            y1_Jan(y3_typeorgavar)]
        return typeorgafertiy3list

    # Création quantité fertilisation organique
    y3_typeorgavar = ttk.Combobox(frame3, values=Orgafertitype,
                                  width=10)
    y3_typeorgavar.set("*Choice*")
    y3_typeorgavar.place(relx=0.185, rely=0.63)

    # Calcule équivalent N ferti orga
    def calculate_kgNorga3():
        # Mise des return list dans des listes spécifiques
        listferti = printlist()
        y3_typefertiorga = listferti[24]
        y3_quantityfertiorga = listferti[23]
        print (y3_typefertiorga)
        print (y3_quantityfertiorga)
        # Création d'une liste vide permettant conversion liste en float
        y3_quantityfertiorga_float = []
        # Création liste pour valeurs
        Nfertiorga = []
        # Vérification que chaque élément de cette liste puisse être convertie + conversion
        try:
            for i in y3_quantityfertiorga:
                y3_quantityfertiorga_float.append(float(i))
        except ValueError:
            print("Error! Please check you rate data. Some data are not float")
            return
        # Calcule taux N en fonction type ferti orga si plusieurs valeurs
        for i in range(1):
            if y3_typefertiorga[i] == "*Choice*" and y3_quantityfertiorga_float[i] == 0:
                Nfertiorga.append(0)
            elif y3_typefertiorga[i] == "EFB" and y3_quantityfertiorga_float[i] > 0:
                # 0.90% N in DM * 0.36tDM/tFM (cf pg Pardon)
                Nfertiorgacal = round(3.24 * y3_quantityfertiorga_float[i], 1)
                Nfertiorga.append(Nfertiorgacal)
            elif y3_typefertiorga[i] == "Compost" and y3_quantityfertiorga_float[i] > 0:
                # 2.05% N in DM * 0.41tDM/tFM (cf pg Pardon)
                Nfertiorgacal = round(8.405 * y3_quantityfertiorga_float[i], 1)
                Nfertiorga.append(Nfertiorgacal)
            elif y3_typefertiorga[i] == "*Choice*" and y3_quantityfertiorga_float[i] > 0:
                Nfertiorga.append("Error!")
            elif y3_typefertiorga[i] != "*Choice*" and y3_typefertiorga[i] != "EFB" and y3_typefertiorga[i] != "Compost":
                Nfertiorga.append("Error!")
            else:
                Nfertiorga.append("Error!")

            # Information résultats
        equilabelnitroorgaferti = tkinter.Label(frame3,
                                                text="Nitrogen equivalent organic fertilization (in kgN/ha/yr) :")
        equilabelnitroorgaferti.place(relx=0.45, rely=0.63)
        equnitrogenorgaferti = tkinter.Label(frame3,
                                             text=Nfertiorga[0], font=("Ariel", 9, "bold"),
                                             bg="white", fg="blue", justify="right",
                                             width=10,
                                             relief="groove", borderwidth=5)
        equnitrogenorgaferti.place(relx=0.68, rely=0.63)

    # Fonction pour récupérer la valeur de placement organic
    def get_placementorgafertiy3():
        placementorgafertiy3list = [
            y1_Jan(y3_placementorgavar)]
        return placementorgafertiy3list

    # Création placement ferti organique
    y3_placementorgavar = ttk.Combobox(frame3, values=Orgafertiplacement,
                                       width=20)
    y3_placementorgavar.set("*Choice*")
    y3_placementorgavar.place(relx=0.31, rely=0.63)

    # Fonction pour récupérer la valeur de biomasse understorey
    def get_understoreybiomassy3():
        understoreybiomassy3list = [
            y1_Jan(y3_understoreybiomass)]
        return understoreybiomassy3list

    # Création biomasse understorey
    y3_understoreybiomass = ttk.Combobox(frame3, values=understoreybiomass,
                                         width=10)
    y3_understoreybiomass.set("*Choice*")
    y3_understoreybiomass.place(relx=0.05, rely=0.78)

    # Fonction pour récupérer la valeur de biomasse understorey
    def get_legumefractiony3():
        legumefractiony3list = [
            y1_Jan(y3_legumefraction)]
        return legumefractiony3list

    # Création legume fraction
    y3_legumefraction = ttk.Combobox(frame3, values=understoreylegumefraction,
                                     width=10)
    y3_legumefraction.set("*Choice*")
    y3_legumefraction.place(relx=0.24, rely=0.78)

    # Fonction pour récupérer la valeur pruned fronds
    def get_prunedy3():
        prunedy3list = [
            y1_Jan(y3_pruned)]
        return prunedy3list

    # Création combobox pruned fronds
    y3_pruned = ttk.Combobox(frame3, values=Prunedfronds,
                             width=20)
    y3_pruned.set("*Choice*")
    y3_pruned.place(relx=0.07, rely=0.92)

    # Fonction pour récupérer toute la valeur Natmo
    def get_Natmodepoy3():
        Natmoy3list = [
            y1_Jan(y3_Natmodepo)]
        return Natmoy3list

    # Création quantité Natmo
    y3_Natmodepo = tkinter.Entry(frame3,
                                 width=8,
                                 justify="right")
    y3_Natmodepo.insert(tkinter.END, "18")
    y3_Natmodepo.place(relx=0.66, rely=0.84)


    ################################################################################################################
    ###################################Year 4#######################################################################
    ################################################################################################################
    # Intégration de Second year dans la fenêtre
    year4 = (tkinter.Label(main_frame,
                           text="Fourth year", font=("Ariel", 20, 'underline')))
    year4.pack(anchor="w", pady=5)

    # Intégration du bloc data pour chaque type
    # Création encadré
    frame4 = tkinter.Frame(main_frame, bd=2, relief="solid", width=1450, height=400, padx=5, pady=2)
    frame4.pack(anchor="w", padx=15, pady=5, fill="none")

    # Mise de titre Mineral N ferti
    y4_MineralNfertilizer = (tkinter.Label(frame4,
                                           text="Mineral Nitrogen fertilizer", justify="center",
                                           font=("Ariel", 13, "bold", "underline")))
    y4_MineralNfertilizer.place(relx=0.01)

    # Mise de titre organic fertilizer
    y4_Organicfertilizer = (tkinter.Label(frame4,
                                          text="Organic fertilizer", justify="center",
                                          font=("Ariel", 13, "bold", "underline")))
    y4_Organicfertilizer.place(relx=0.01, rely=0.55)

    # Mise de titre understorey
    y4_Understorey = (tkinter.Label(frame4,
                                    text="Understorey", justify="center",
                                    font=("Ariel", 13, "bold", "underline")))
    y4_Understorey.place(relx=0.01, rely=0.7)

    # Mise de titre Pruned fronds
    y4_Prunedfronds = (tkinter.Label(frame4,
                                     text="Pruned fronds", justify="center",
                                     font=("Ariel", 13, "bold", "underline")))
    y4_Prunedfronds.place(relx=0.01, rely=0.85)

    # Mise titre atmospheric depositions
    y4_atmodepo = (tkinter.Label(frame4,
                                 text="Atmospheric depositions", justify="center",
                                 font=("Ariel", 13, "bold", "underline")))
    y4_atmodepo.place(relx=0.55, rely=0.75)

    # Intégration des mois
    y4_January = (tkinter.Label(frame4, text="January", font=("Ariel", 9), fg="blue"))
    y4_January.place(relx=0.06, rely=0.08)
    y4_February = (tkinter.Label(frame4, text="February", font=("Ariel", 9), fg="blue"))
    y4_February.place(relx=0.14, rely=0.08)
    y4_March = (tkinter.Label(frame4, text="March", font=("Ariel", 9), fg="blue"))
    y4_March.place(relx=0.22, rely=0.08)
    y4_April = (tkinter.Label(frame4, text="April", font=("Ariel", 9), fg="blue"))
    y4_April.place(relx=0.295, rely=0.08)
    y4_May = (tkinter.Label(frame4, text="May", font=("Ariel", 9), fg="blue"))
    y4_May.place(relx=0.377, rely=0.08)
    y4_June = (tkinter.Label(frame4, text="June", font=("Ariel", 9), fg="blue"))
    y4_June.place(relx=0.46, rely=0.08)
    y4_July = (tkinter.Label(frame4, text="July", font=("Ariel", 9), fg="blue"))
    y4_July.place(relx=0.54, rely=0.08)
    y4_August = (tkinter.Label(frame4, text="August", font=("Ariel", 9), fg="blue"))
    y4_August.place(relx=0.62, rely=0.08)
    y4_September = (tkinter.Label(frame4, text="September", font=("Ariel", 9), fg="blue"))
    y4_September.place(relx=0.69, rely=0.08)
    y4_October = (tkinter.Label(frame4, text="October", font=("Ariel", 9), fg="blue"))
    y4_October.place(relx=0.78, rely=0.08)
    y4_November = (tkinter.Label(frame4, text="November", font=("Ariel", 9), fg="blue"))
    y4_November.place(relx=0.85, rely=0.08)
    y4_December = (tkinter.Label(frame4, text="December", font=("Ariel", 9), fg="blue"))
    y4_December.place(relx=0.93, rely=0.08)

    # Création du type
    y4_type = (tkinter.Label(frame4, text="Type", fg="blue", font=("Ariel", 11, "bold")))
    y4_type.place(relx=0, rely=0.14)

    # Création data rate
    y4_rate = (tkinter.Label(frame4, text="Rate \n(kg/ha)", fg="blue", font=("Ariel", 11, "bold")))
    y4_rate.place(relx=0, rely=0.21)

    # Création placement
    y4_placementferti = (tkinter.Label(frame4, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y4_placementferti.place(relx=0, rely=0.47)

    # Création quantity ferti orga
    y4_quantityorga = (tkinter.Label(frame4, text="Quantity (in tFM)", fg="blue", font=("Ariel", 11, "bold")))
    y4_quantityorga.place(relx=0, rely=0.63)

    # Création type ferti orga
    y4_typeorga = (tkinter.Label(frame4, text="Type", fg="blue", font=("Ariel", 11, "bold")))
    y4_typeorga.place(relx=0.15, rely=0.63)

    # Création placement ferti orga
    y4_placementorga = (tkinter.Label(frame4, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y4_placementorga.place(relx=0.25, rely=0.63)

    # Création biomasse understorey
    y4_biomass = (tkinter.Label(frame4, text="Biomass", fg="blue", font=("Ariel", 11, "bold")))
    y4_biomass.place(relx=0, rely=0.78)

    # Création legume fraction
    y4_legumefrac = (tkinter.Label(frame4, text="Legume fraction", fg="blue", font=("Ariel", 11, "bold")))
    y4_legumefrac.place(relx=0.15, rely=0.78)

    # Création pruned fronts placement
    y4_prunedfr = (tkinter.Label(frame4, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y4_prunedfr.place(relx=0, rely=0.92)

    # Création atmospheric depositions
    y4_quantityNatmo = (
        tkinter.Label(frame4, text="Quantity of nitrogen\n (in kg/ha/yr)", fg="blue", font=("Ariel", 11, "bold")))
    y4_quantityNatmo.place(relx=0.55, rely=0.82)

    # Fonction pour récupérer toutes les valeurs des mois pour Type N ferti
    def get_all_month_valuestypeNfertiy4():
        month_valuestypeNfertiy4 = [
            y1_Jan(y4_Jan_typeNfertivar),
            y1_Feb(y4_Feb_typeNfertivar),
            y1_Mar(y4_Mar_typeNfertivar),
            y1_Apr(y4_Apr_typeNfertivar),
            y1_Maymonth(y4_Maymonth_typeNfertivar),
            y1_Jun(y4_Jun_typeNfertivar),
            y1_Jul(y4_Jul_typeNfertivar),
            y1_Aug(y4_Aug_typeNfertivar),
            y1_Sep(y4_Sep_typeNfertivar),
            y1_Oct(y4_Oct_typeNfertivar),
            y1_Nov(y4_Nov_typeNfertivar),
            y1_Dec(y4_Dec_typeNfertivar)
        ]

        return month_valuestypeNfertiy4

    # Créer une variable Tkinter pour stocker l'élément sélectionné Nfertitype
    # Création combobox
    # Janvier
    y4_Jan_typeNfertivar = ttk.Combobox(frame4, values=typeNferti,
                                        width=10)
    y4_Jan_typeNfertivar.set("*None")
    y4_Jan_typeNfertivar.place(relx=0.04, rely=0.14)
    # Février
    y4_Feb_typeNfertivar = ttk.Combobox(frame4, values=typeNferti,
                                        width=10)
    y4_Feb_typeNfertivar.set("*None")
    y4_Feb_typeNfertivar.place(relx=0.12, rely=0.14)
    # Mars
    y4_Mar_typeNfertivar = ttk.Combobox(frame4, values=typeNferti,
                                        width=10)
    y4_Mar_typeNfertivar.set("*None")
    y4_Mar_typeNfertivar.place(relx=0.2, rely=0.14)
    # Avril
    y4_Apr_typeNfertivar = ttk.Combobox(frame4, values=typeNferti,
                                        width=10)
    y4_Apr_typeNfertivar.set("*None")
    y4_Apr_typeNfertivar.place(relx=0.28, rely=0.14)
    # May
    y4_Maymonth_typeNfertivar = ttk.Combobox(frame4, values=typeNferti,
                                             width=10)
    y4_Maymonth_typeNfertivar.set("*None")
    y4_Maymonth_typeNfertivar.place(relx=0.36, rely=0.14)
    # Juin
    y4_Jun_typeNfertivar = ttk.Combobox(frame4, values=typeNferti,
                                        width=10)
    y4_Jun_typeNfertivar.set("*None")
    y4_Jun_typeNfertivar.place(relx=0.44, rely=0.14)
    # July
    y4_Jul_typeNfertivar = ttk.Combobox(frame4, values=typeNferti,
                                        width=10)
    y4_Jul_typeNfertivar.set("*None")
    y4_Jul_typeNfertivar.place(relx=0.52, rely=0.14)
    # Aout
    y4_Aug_typeNfertivar = ttk.Combobox(frame4, values=typeNferti,
                                        width=10)
    y4_Aug_typeNfertivar.set("*None")
    y4_Aug_typeNfertivar.place(relx=0.6, rely=0.14)
    # Septembre
    y4_Sep_typeNfertivar = ttk.Combobox(frame4, values=typeNferti,
                                        width=10)
    y4_Sep_typeNfertivar.set("*None")
    y4_Sep_typeNfertivar.place(relx=0.68, rely=0.14)
    # Octobre
    y4_Oct_typeNfertivar = ttk.Combobox(frame4, values=typeNferti,
                                        width=10)
    y4_Oct_typeNfertivar.set("*None")
    y4_Oct_typeNfertivar.place(relx=0.76, rely=0.14)
    # Novembre
    y4_Nov_typeNfertivar = ttk.Combobox(frame4, values=typeNferti,
                                        width=10)
    y4_Nov_typeNfertivar.set("*None")
    y4_Nov_typeNfertivar.place(relx=0.84, rely=0.14)
    # Décembre
    y4_Dec_typeNfertivar = ttk.Combobox(frame4, values=typeNferti,
                                        width=10)
    y4_Dec_typeNfertivar.set("*None")
    y4_Dec_typeNfertivar.place(relx=0.92, rely=0.14)

    # Fonction pour récupérer toutes les valeurs des mois pour rate N ferti
    def get_all_month_valuesrateNfertiy4():
        month_valuesrateNfertiy4 = [
            y1_Jan(y4_Jan_rateNfertivar),
            y1_Feb(y4_Feb_rateNfertivar),
            y1_Mar(y4_Mar_rateNfertivar),
            y1_Apr(y4_Apr_rateNfertivar),
            y1_Maymonth(y4_Maymonth_rateNfertivar),
            y1_Jun(y4_Jun_rateNfertivar),
            y1_Jul(y4_Jul_rateNfertivar),
            y1_Aug(y4_Aug_rateNfertivar),
            y1_Sep(y4_Sep_rateNfertivar),
            y1_Oct(y4_Oct_rateNfertivar),
            y1_Nov(y4_Nov_rateNfertivar),
            y1_Dec(y4_Dec_rateNfertivar)
        ]
        return month_valuesrateNfertiy4

    # Créer une variable Tkinter pour stocker l'élément sélectionné NfertiRate
    # Création combobox
    # Janvier
    y4_Jan_rateNfertivar = tkinter.Entry(frame4,
                                         width=13,
                                         justify="right")
    y4_Jan_rateNfertivar.insert(tkinter.END, "0")
    y4_Jan_rateNfertivar.place(relx=0.04, rely=0.22)
    # Février
    y4_Feb_rateNfertivar = tkinter.Entry(frame4,
                                         width=13,
                                         justify="right")
    y4_Feb_rateNfertivar.insert(tkinter.END, "0")
    y4_Feb_rateNfertivar.place(relx=0.12, rely=0.22)
    # Mars
    y4_Mar_rateNfertivar = tkinter.Entry(frame4,
                                         width=13,
                                         justify="right")
    y4_Mar_rateNfertivar.insert(tkinter.END, "0")
    y4_Mar_rateNfertivar.place(relx=0.2, rely=0.22)
    # Avril
    y4_Apr_rateNfertivar = tkinter.Entry(frame4,
                                         width=13,
                                         justify="right")
    y4_Apr_rateNfertivar.insert(tkinter.END, "0")
    y4_Apr_rateNfertivar.place(relx=0.28, rely=0.22)
    # May
    y4_Maymonth_rateNfertivar = tkinter.Entry(frame4,
                                              width=13,
                                              justify="right")
    y4_Maymonth_rateNfertivar.insert(tkinter.END, "0")
    y4_Maymonth_rateNfertivar.place(relx=0.36, rely=0.22)
    # Juin
    y4_Jun_rateNfertivar = tkinter.Entry(frame4,
                                         width=13,
                                         justify="right")
    y4_Jun_rateNfertivar.insert(tkinter.END, "0")
    y4_Jun_rateNfertivar.place(relx=0.44, rely=0.22)
    # July
    y4_Jul_rateNfertivar = tkinter.Entry(frame4,
                                         width=13,
                                         justify="right")
    y4_Jul_rateNfertivar.insert(tkinter.END, "0")
    y4_Jul_rateNfertivar.place(relx=0.52, rely=0.22)
    # Aout
    y4_Aug_rateNfertivar = tkinter.Entry(frame4,
                                         width=13,
                                         justify="right")
    y4_Aug_rateNfertivar.insert(tkinter.END, "0")
    y4_Aug_rateNfertivar.place(relx=0.6, rely=0.22)
    # Septembre
    y4_Sep_rateNfertivar = tkinter.Entry(frame4,
                                         width=13,
                                         justify="right")
    y4_Sep_rateNfertivar.insert(tkinter.END, "0")
    y4_Sep_rateNfertivar.place(relx=0.68, rely=0.22)
    # Octobre
    y4_Oct_rateNfertivar = tkinter.Entry(frame4,
                                         width=13,
                                         justify="right")
    y4_Oct_rateNfertivar.insert(tkinter.END, "0")
    y4_Oct_rateNfertivar.place(relx=0.76, rely=0.22)
    # Novembre
    y4_Nov_rateNfertivar = tkinter.Entry(frame4,
                                         width=13,
                                         justify="right")
    y4_Nov_rateNfertivar.insert(tkinter.END, "0")
    y4_Nov_rateNfertivar.place(relx=0.84, rely=0.22)
    # Décembre
    y4_Dec_rateNfertivar = tkinter.Entry(frame4,
                                         width=13,
                                         justify="right")
    y4_Dec_rateNfertivar.insert(tkinter.END, "0")
    y4_Dec_rateNfertivar.place(relx=0.92, rely=0.22)

    # Calcule du taux d'N en kg/ha en fonction de l'apport et du type ferti
    def calculate_kgN4():
        # Mise des return list dans des listes spécifiques
        listferti = printlist()
        y4rateferti_str = listferti[31]
        y4typeferti = listferti[30]
        # Création d'une liste vide convertissant les rate str en float
        y4rateferti_float = []
        # Création d'une liste pour les résultats des calcules
        resultlist = []
        # Vérification que chaque élément de cette liste puisse être convertie + conversion

        try:
            for i in y4rateferti_str:
                y4rateferti_float.append(float(i))
        except ValueError:
            print("Error! Please check you rate data. Some data are not float")

        # Calcule taux N en fonction type ferti
        for i in range(12):  # Pour janvier (0) et février (1)
            if y4typeferti[i] == "*None" and y4rateferti_float[i] == 0:
                resultlist.append(0)
            elif y4typeferti[i] == "Ammo Chlo" and y4rateferti_float[i] > 0:
                resammochlo = round(0.25 * y4rateferti_float[i], 1)
                resultlist.append(resammochlo)
            elif y4typeferti[i] == "Ammo Nit" and y4rateferti_float[i] > 0:
                resammonit = round(0.34 * y4rateferti_float[i], 1)
                resultlist.append(resammonit)
            elif y4typeferti[i] == "Ammo Sulf" and y4rateferti_float[i] > 0:
                resammosulf = round(0.21 * y4rateferti_float[i], 1)
                resultlist.append(resammosulf)
            elif y4typeferti[i] == "Sod Nit" and y4rateferti_float[i] > 0:
                ressodnit = round(0.16 * y4rateferti_float[i], 1)
                resultlist.append(ressodnit)
            elif y4typeferti[i] == "Urea" and y4rateferti_float[i] > 0:
                resurea = round(0.46 * y4rateferti_float[i], 1)
                resultlist.append(resurea)
            elif y4typeferti[i] == "*None" and y4rateferti_float[i] > 0:
                resultlist.append("Error!")
            elif y4typeferti[i] != "*None" and y4typeferti[i] != "Ammo Chlo" and y4typeferti[i] != "Ammo Nit" and \
                    y4typeferti[i] != "Ammo Sulf" and y4typeferti[i] != "Sod Nit" and y4typeferti[i] != "Urea":
                resultlist.append("Error!")
            else:
                resultlist.append("Error!")

        # Information résultats
        # Janvier
        equnitrogenjan = tkinter.Label(frame4,
                                       text=resultlist[0], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjan.place(relx=0.04, rely=0.28)
        # Fevrier
        equnitrogenfev = tkinter.Label(frame4,
                                       text=resultlist[1], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenfev.place(relx=0.12, rely=0.28)
        # Mars
        equnitrogenmar = tkinter.Label(frame4,
                                       text=resultlist[2], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenmar.place(relx=0.2, rely=0.28)
        # Avril
        equnitrogenapr = tkinter.Label(frame4,
                                       text=resultlist[3], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenapr.place(relx=0.28, rely=0.28)
        # Mai
        equnitrogenmay = tkinter.Label(frame4,
                                       text=resultlist[4], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenmay.place(relx=0.36, rely=0.28)
        # Juin
        equnitrogenjun = tkinter.Label(frame4,
                                       text=resultlist[5], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjun.place(relx=0.44, rely=0.28)
        # Juillet
        equnitrogenjul = tkinter.Label(frame4,
                                       text=resultlist[6], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjul.place(relx=0.52, rely=0.28)
        # Aout
        equnitrogenaug = tkinter.Label(frame4,
                                       text=resultlist[7], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenaug.place(relx=0.6, rely=0.28)
        # September
        equnitrogensep = tkinter.Label(frame4,
                                       text=resultlist[8], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogensep.place(relx=0.68, rely=0.28)
        # Octobre
        equnitrogenoct = tkinter.Label(frame4,
                                       text=resultlist[9], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenoct.place(relx=0.76, rely=0.28)
        # Novembre
        equnitrogennov = tkinter.Label(frame4,
                                       text=resultlist[10], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogennov.place(relx=0.84, rely=0.28)
        # Decembre
        equnitrogendec = tkinter.Label(frame4,
                                       text=resultlist[11], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogendec.place(relx=0.92, rely=0.28)

        # Calcule total annuelle
        yearcumul = 0
        resultlist_float = []
        try:
            for i in resultlist:
                resultlist_float.append(float(i))
        except ValueError:
            return
        for i in resultlist_float:
            if isinstance(i, float):
                yearcumul = round(i + yearcumul,1)
        # label cacule annuel
        Nfertianuel = tkinter.Label(frame4, text=f"Cumulative nitrogen for year: {yearcumul}")
        Nfertianuel.place(relx=0.04, rely=0.35)

    # Création bouton calcul équivalent azote N ferti
    button = tkinter.Button(frame4, text="Nitrogen equivalent (in kg/ha)",
                            width=100,
                            font=("Ariel", 10, "bold"), bg="lightblue",
                            command=lambda: [calculate_kgN4(), calculate_kgNorga4()])
    button.place(relx=0.2, rely=0.4)

    # Fonction pour récupérer toutes les infos placement
    def get_placement4():
        placementfertiy4 = [
            y1_Jan(y4_placementferti)]
        return placementfertiy4

    # Création combobox placement N ferti
    y4_placementferti = ttk.Combobox(frame4, values=Nfertiplacement,
                                     width=21)
    y4_placementferti.set("*Choice*")
    y4_placementferti.place(relx=0.06, rely=0.47)

    # Fonction pour récupérer toute la valeur de quantity organic
    def get_quantityorgafertiy4():
        quantityorgafertiy4list = [
            y1_Jan(y4_quantityorgavar)]
        return quantityorgafertiy4list

    # Création quantité fertilisation organique
    y4_quantityorgavar = tkinter.Entry(frame4,
                                       width=8,
                                       justify="right")
    y4_quantityorgavar.insert(tkinter.END, "0")
    y4_quantityorgavar.place(relx=0.1, rely=0.63)

    # Fonction pour récupérer la valeur de type organic
    def get_typeorgafertiy4():
        typeorgafertiy4list = [
            y1_Jan(y4_typeorgavar)]
        return typeorgafertiy4list

    # Création quantité fertilisation organique
    y4_typeorgavar = ttk.Combobox(frame4, values=Orgafertitype,
                                  width=10)
    y4_typeorgavar.set("*Choice*")
    y4_typeorgavar.place(relx=0.185, rely=0.63)

    # Calcule équivalent N ferti orga
    def calculate_kgNorga4():
        # Mise des return list dans des listes spécifiques
        listferti = printlist()
        y4_typefertiorga = listferti[34]
        y4_quantityfertiorga = listferti[33]
        # Création d'une liste vide permettant conversion liste en float
        y4_quantityfertiorga_float = []
        # Création liste pour valeurs
        Nfertiorga = []
        # Vérification que chaque élément de cette liste puisse être convertie + conversion
        try:
            for i in y4_quantityfertiorga:
                y4_quantityfertiorga_float.append(float(i))
        except ValueError:
            print("Error! Please check you rate data. Some data are not float")
            return
        # Calcule taux N en fonction type ferti orga si plusieurs valeurs
        for i in range(1):
            if y4_typefertiorga[i] == "*Choice*" and y4_quantityfertiorga_float[i] == 0:
                Nfertiorga.append(0)
            elif y4_typefertiorga[i] == "EFB" and y4_quantityfertiorga_float[i] > 0:
                # 0.90% N in DM * 0.36tDM/tFM (cf pg Pardon)
                Nfertiorgacal = round(3.24 * y4_quantityfertiorga_float[i], 1)
                Nfertiorga.append(Nfertiorgacal)
            elif y4_typefertiorga[i] == "Compost" and y4_quantityfertiorga_float[i] > 0:
                # 2.05% N in DM * 0.41tDM/tFM (cf pg Pardon)
                Nfertiorgacal = round(8.405 * y4_quantityfertiorga_float[i], 1)
                Nfertiorga.append(Nfertiorgacal)
            elif y4_typefertiorga[i] == "*Choice*" and y4_quantityfertiorga_float[i] > 0:
                Nfertiorga.append("Error!")
            elif y4_typefertiorga[i] != "*Choice*" and y4_typefertiorga[i] != "EFB" and y4_typefertiorga[i] != "Compost":
                Nfertiorga.append("Error!")
            else:
                Nfertiorga.append("Error!")

            # Information résultats
        equilabelnitroorgaferti = tkinter.Label(frame4,
                                                text="Nitrogen equivalent organic fertilization (in kgN/ha/yr) :")
        equilabelnitroorgaferti.place(relx=0.45, rely=0.63)
        equnitrogenorgaferti = tkinter.Label(frame4,
                                             text=Nfertiorga[0], font=("Ariel", 9, "bold"),
                                             bg="white", fg="blue", justify="right",
                                             width=10,
                                             relief="groove", borderwidth=5)
        equnitrogenorgaferti.place(relx=0.68, rely=0.63)

    # Fonction pour récupérer la valeur de placement organic
    def get_placementorgafertiy4():
        placementorgafertiy4list = [
            y1_Jan(y4_placementorgavar)]
        return placementorgafertiy4list

    # Création placement ferti organique
    y4_placementorgavar = ttk.Combobox(frame4, values=Orgafertiplacement,
                                       width=20)
    y4_placementorgavar.set("*Choice*")
    y4_placementorgavar.place(relx=0.31, rely=0.63)

    # Fonction pour récupérer la valeur de biomasse understorey
    def get_understoreybiomassy4():
        understoreybiomassy4list = [
            y1_Jan(y4_understoreybiomass)]
        return understoreybiomassy4list

    # Création biomasse understorey
    y4_understoreybiomass = ttk.Combobox(frame4, values=understoreybiomass,
                                         width=10)
    y4_understoreybiomass.set("*Choice*")
    y4_understoreybiomass.place(relx=0.05, rely=0.78)

    # Fonction pour récupérer la valeur de biomasse understorey
    def get_legumefractiony4():
        legumefractiony4list = [
            y1_Jan(y4_legumefraction)]
        return legumefractiony4list

    # Création legume fraction
    y4_legumefraction = ttk.Combobox(frame4, values=understoreylegumefraction,
                                     width=10)
    y4_legumefraction.set("*Choice*")
    y4_legumefraction.place(relx=0.24, rely=0.78)

    # Fonction pour récupérer la valeur pruned fronds
    def get_prunedy4():
        prunedy4list = [
            y1_Jan(y4_pruned)]
        return prunedy4list

    # Création combobox pruned fronds
    y4_pruned = ttk.Combobox(frame4, values=Prunedfronds,
                             width=20)
    y4_pruned.set("*Choice*")
    y4_pruned.place(relx=0.07, rely=0.92)

    # Fonction pour récupérer toute la valeur Natmo
    def get_Natmodepoy4():
        Natmoy4list = [
            y1_Jan(y4_Natmodepo)]
        return Natmoy4list

    # Création quantité Natmo
    y4_Natmodepo = tkinter.Entry(frame4,
                                 width=8,
                                 justify="right")
    y4_Natmodepo.insert(tkinter.END, "18")
    y4_Natmodepo.place(relx=0.66, rely=0.84)


    ################################################################################################################
    ###################################Year 5#######################################################################
    ################################################################################################################
    # Intégration de Second year dans la fenêtre
    year5 = (tkinter.Label(main_frame,
                           text="Fifth year", font=("Ariel", 20, 'underline')))
    year5.pack(anchor="w", pady=5)

    # Intégration du bloc data pour chaque type
    # Création encadré
    frame5 = tkinter.Frame(main_frame, bd=2, relief="solid", width=1450, height=400, padx=5, pady=2)
    frame5.pack(anchor="w", padx=15, pady=5, fill="none")

    # Mise de titre Mineral N ferti
    y5_MineralNfertilizer = (tkinter.Label(frame5,
                                           text="Mineral Nitrogen fertilizer", justify="center",
                                           font=("Ariel", 13, "bold", "underline")))
    y5_MineralNfertilizer.place(relx=0.01)

    # Mise de titre organic fertilizer
    y5_Organicfertilizer = (tkinter.Label(frame5,
                                          text="Organic fertilizer", justify="center",
                                          font=("Ariel", 13, "bold", "underline")))
    y5_Organicfertilizer.place(relx=0.01, rely=0.55)

    # Mise de titre understorey
    y5_Understorey = (tkinter.Label(frame5,
                                    text="Understorey", justify="center",
                                    font=("Ariel", 13, "bold", "underline")))
    y5_Understorey.place(relx=0.01, rely=0.7)

    # Mise de titre Pruned fronds
    y5_Prunedfronds = (tkinter.Label(frame5,
                                     text="Pruned fronds", justify="center",
                                     font=("Ariel", 13, "bold", "underline")))
    y5_Prunedfronds.place(relx=0.01, rely=0.85)

    # Mise titre atmospheric depositions
    y5_atmodepo = (tkinter.Label(frame5,
                                 text="Atmospheric depositions", justify="center",
                                 font=("Ariel", 13, "bold", "underline")))
    y5_atmodepo.place(relx=0.55, rely=0.75)

    # Intégration des mois
    y5_January = (tkinter.Label(frame5, text="January", font=("Ariel", 9), fg="blue"))
    y5_January.place(relx=0.06, rely=0.08)
    y5_February = (tkinter.Label(frame5, text="February", font=("Ariel", 9), fg="blue"))
    y5_February.place(relx=0.14, rely=0.08)
    y5_March = (tkinter.Label(frame5, text="March", font=("Ariel", 9), fg="blue"))
    y5_March.place(relx=0.22, rely=0.08)
    y5_April = (tkinter.Label(frame5, text="April", font=("Ariel", 9), fg="blue"))
    y5_April.place(relx=0.295, rely=0.08)
    y5_May = (tkinter.Label(frame5, text="May", font=("Ariel", 9), fg="blue"))
    y5_May.place(relx=0.377, rely=0.08)
    y5_June = (tkinter.Label(frame5, text="June", font=("Ariel", 9), fg="blue"))
    y5_June.place(relx=0.46, rely=0.08)
    y5_July = (tkinter.Label(frame5, text="July", font=("Ariel", 9), fg="blue"))
    y5_July.place(relx=0.54, rely=0.08)
    y5_August = (tkinter.Label(frame5, text="August", font=("Ariel", 9), fg="blue"))
    y5_August.place(relx=0.62, rely=0.08)
    y5_September = (tkinter.Label(frame5, text="September", font=("Ariel", 9), fg="blue"))
    y5_September.place(relx=0.69, rely=0.08)
    y5_October = (tkinter.Label(frame5, text="October", font=("Ariel", 9), fg="blue"))
    y5_October.place(relx=0.78, rely=0.08)
    y5_November = (tkinter.Label(frame5, text="November", font=("Ariel", 9), fg="blue"))
    y5_November.place(relx=0.85, rely=0.08)
    y5_December = (tkinter.Label(frame5, text="December", font=("Ariel", 9), fg="blue"))
    y5_December.place(relx=0.93, rely=0.08)

    # Création du type
    y5_type = (tkinter.Label(frame5, text="Type", fg="blue", font=("Ariel", 11, "bold")))
    y5_type.place(relx=0, rely=0.14)

    # Création data rate
    y5_rate = (tkinter.Label(frame5, text="Rate \n(kg/ha)", fg="blue", font=("Ariel", 11, "bold")))
    y5_rate.place(relx=0, rely=0.21)

    # Création placement
    y5_placementferti = (tkinter.Label(frame5, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y5_placementferti.place(relx=0, rely=0.47)

    # Création quantity ferti orga
    y5_quantityorga = (tkinter.Label(frame5, text="Quantity (in tFM)", fg="blue", font=("Ariel", 11, "bold")))
    y5_quantityorga.place(relx=0, rely=0.63)

    # Création type ferti orga
    y5_typeorga = (tkinter.Label(frame5, text="Type", fg="blue", font=("Ariel", 11, "bold")))
    y5_typeorga.place(relx=0.15, rely=0.63)

    # Création placement ferti orga
    y5_placementorga = (tkinter.Label(frame5, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y5_placementorga.place(relx=0.25, rely=0.63)

    # Création biomasse understorey
    y5_biomass = (tkinter.Label(frame5, text="Biomass", fg="blue", font=("Ariel", 11, "bold")))
    y5_biomass.place(relx=0, rely=0.78)

    # Création legume fraction
    y5_legumefrac = (tkinter.Label(frame5, text="Legume fraction", fg="blue", font=("Ariel", 11, "bold")))
    y5_legumefrac.place(relx=0.15, rely=0.78)

    # Création pruned fronts placement
    y5_prunedfr = (tkinter.Label(frame5, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y5_prunedfr.place(relx=0, rely=0.92)

    # Création atmospheric depositions
    y5_quantityNatmo = ( tkinter.Label(frame5, text="Quantity of nitrogen\n (in kg/ha/yr)", fg="blue", font=("Ariel", 11, "bold")))
    y5_quantityNatmo.place(relx=0.55, rely=0.82)

    # Fonction pour récupérer toutes les valeurs des mois pour Type N ferti
    def get_all_month_valuestypeNfertiy5():
        month_valuestypeNfertiy5 = [
            y1_Jan(y5_Jan_typeNfertivar),
            y1_Feb(y5_Feb_typeNfertivar),
            y1_Mar(y5_Mar_typeNfertivar),
            y1_Apr(y5_Apr_typeNfertivar),
            y1_Maymonth(y5_Maymonth_typeNfertivar),
            y1_Jun(y5_Jun_typeNfertivar),
            y1_Jul(y5_Jul_typeNfertivar),
            y1_Aug(y5_Aug_typeNfertivar),
            y1_Sep(y5_Sep_typeNfertivar),
            y1_Oct(y5_Oct_typeNfertivar),
            y1_Nov(y5_Nov_typeNfertivar),
            y1_Dec(y5_Dec_typeNfertivar)
        ]

        return month_valuestypeNfertiy5

    # Créer une variable Tkinter pour stocker l'élément sélectionné Nfertitype
    # Création combobox
    # Janvier
    y5_Jan_typeNfertivar = ttk.Combobox(frame5, values=typeNferti,
                                        width=10)
    y5_Jan_typeNfertivar.set("*None")
    y5_Jan_typeNfertivar.place(relx=0.04, rely=0.14)
    # Février
    y5_Feb_typeNfertivar = ttk.Combobox(frame5, values=typeNferti,
                                        width=10)
    y5_Feb_typeNfertivar.set("*None")
    y5_Feb_typeNfertivar.place(relx=0.12, rely=0.14)
    # Mars
    y5_Mar_typeNfertivar = ttk.Combobox(frame5, values=typeNferti,
                                        width=10)
    y5_Mar_typeNfertivar.set("*None")
    y5_Mar_typeNfertivar.place(relx=0.2, rely=0.14)
    # Avril
    y5_Apr_typeNfertivar = ttk.Combobox(frame5, values=typeNferti,
                                        width=10)
    y5_Apr_typeNfertivar.set("*None")
    y5_Apr_typeNfertivar.place(relx=0.28, rely=0.14)
    # May
    y5_Maymonth_typeNfertivar = ttk.Combobox(frame5, values=typeNferti,
                                             width=10)
    y5_Maymonth_typeNfertivar.set("*None")
    y5_Maymonth_typeNfertivar.place(relx=0.36, rely=0.14)
    # Juin
    y5_Jun_typeNfertivar = ttk.Combobox(frame5, values=typeNferti,
                                        width=10)
    y5_Jun_typeNfertivar.set("*None")
    y5_Jun_typeNfertivar.place(relx=0.44, rely=0.14)
    # July
    y5_Jul_typeNfertivar = ttk.Combobox(frame5, values=typeNferti,
                                        width=10)
    y5_Jul_typeNfertivar.set("*None")
    y5_Jul_typeNfertivar.place(relx=0.52, rely=0.14)
    # Aout
    y5_Aug_typeNfertivar = ttk.Combobox(frame5, values=typeNferti,
                                        width=10)
    y5_Aug_typeNfertivar.set("*None")
    y5_Aug_typeNfertivar.place(relx=0.6, rely=0.14)
    # Septembre
    y5_Sep_typeNfertivar = ttk.Combobox(frame5, values=typeNferti,
                                        width=10)
    y5_Sep_typeNfertivar.set("*None")
    y5_Sep_typeNfertivar.place(relx=0.68, rely=0.14)
    # Octobre
    y5_Oct_typeNfertivar = ttk.Combobox(frame5, values=typeNferti,
                                        width=10)
    y5_Oct_typeNfertivar.set("*None")
    y5_Oct_typeNfertivar.place(relx=0.76, rely=0.14)
    # Novembre
    y5_Nov_typeNfertivar = ttk.Combobox(frame5, values=typeNferti,
                                        width=10)
    y5_Nov_typeNfertivar.set("*None")
    y5_Nov_typeNfertivar.place(relx=0.84, rely=0.14)
    # Décembre
    y5_Dec_typeNfertivar = ttk.Combobox(frame5, values=typeNferti,
                                        width=10)
    y5_Dec_typeNfertivar.set("*None")
    y5_Dec_typeNfertivar.place(relx=0.92, rely=0.14)

    # Fonction pour récupérer toutes les valeurs des mois pour rate N ferti
    def get_all_month_valuesrateNfertiy5():
        month_valuesrateNfertiy5 = [
            y1_Jan(y5_Jan_rateNfertivar),
            y1_Feb(y5_Feb_rateNfertivar),
            y1_Mar(y5_Mar_rateNfertivar),
            y1_Apr(y5_Apr_rateNfertivar),
            y1_Maymonth(y5_Maymonth_rateNfertivar),
            y1_Jun(y5_Jun_rateNfertivar),
            y1_Jul(y5_Jul_rateNfertivar),
            y1_Aug(y5_Aug_rateNfertivar),
            y1_Sep(y5_Sep_rateNfertivar),
            y1_Oct(y5_Oct_rateNfertivar),
            y1_Nov(y5_Nov_rateNfertivar),
            y1_Dec(y5_Dec_rateNfertivar)
        ]
        return month_valuesrateNfertiy5

    # Créer une variable Tkinter pour stocker l'élément sélectionné NfertiRate
    # Création combobox
    # Janvier
    y5_Jan_rateNfertivar = tkinter.Entry(frame5,
                                         width=13,
                                         justify="right")
    y5_Jan_rateNfertivar.insert(tkinter.END, "0")
    y5_Jan_rateNfertivar.place(relx=0.04, rely=0.22)
    # Février
    y5_Feb_rateNfertivar = tkinter.Entry(frame5,
                                         width=13,
                                         justify="right")
    y5_Feb_rateNfertivar.insert(tkinter.END, "0")
    y5_Feb_rateNfertivar.place(relx=0.12, rely=0.22)
    # Mars
    y5_Mar_rateNfertivar = tkinter.Entry(frame5,
                                         width=13,
                                         justify="right")
    y5_Mar_rateNfertivar.insert(tkinter.END, "0")
    y5_Mar_rateNfertivar.place(relx=0.2, rely=0.22)
    # Avril
    y5_Apr_rateNfertivar = tkinter.Entry(frame5,
                                         width=13,
                                         justify="right")
    y5_Apr_rateNfertivar.insert(tkinter.END, "0")
    y5_Apr_rateNfertivar.place(relx=0.28, rely=0.22)
    # May
    y5_Maymonth_rateNfertivar = tkinter.Entry(frame5,
                                              width=13,
                                              justify="right")
    y5_Maymonth_rateNfertivar.insert(tkinter.END, "0")
    y5_Maymonth_rateNfertivar.place(relx=0.36, rely=0.22)
    # Juin
    y5_Jun_rateNfertivar = tkinter.Entry(frame5,
                                         width=13,
                                         justify="right")
    y5_Jun_rateNfertivar.insert(tkinter.END, "0")
    y5_Jun_rateNfertivar.place(relx=0.44, rely=0.22)
    # July
    y5_Jul_rateNfertivar = tkinter.Entry(frame5,
                                         width=13,
                                         justify="right")
    y5_Jul_rateNfertivar.insert(tkinter.END, "0")
    y5_Jul_rateNfertivar.place(relx=0.52, rely=0.22)
    # Aout
    y5_Aug_rateNfertivar = tkinter.Entry(frame5,
                                         width=13,
                                         justify="right")
    y5_Aug_rateNfertivar.insert(tkinter.END, "0")
    y5_Aug_rateNfertivar.place(relx=0.6, rely=0.22)
    # Septembre
    y5_Sep_rateNfertivar = tkinter.Entry(frame5,
                                         width=13,
                                         justify="right")
    y5_Sep_rateNfertivar.insert(tkinter.END, "0")
    y5_Sep_rateNfertivar.place(relx=0.68, rely=0.22)
    # Octobre
    y5_Oct_rateNfertivar = tkinter.Entry(frame5,
                                         width=13,
                                         justify="right")
    y5_Oct_rateNfertivar.insert(tkinter.END, "0")
    y5_Oct_rateNfertivar.place(relx=0.76, rely=0.22)
    # Novembre
    y5_Nov_rateNfertivar = tkinter.Entry(frame5,
                                         width=13,
                                         justify="right")
    y5_Nov_rateNfertivar.insert(tkinter.END, "0")
    y5_Nov_rateNfertivar.place(relx=0.84, rely=0.22)
    # Décembre
    y5_Dec_rateNfertivar = tkinter.Entry(frame5,
                                         width=13,
                                         justify="right")
    y5_Dec_rateNfertivar.insert(tkinter.END, "0")
    y5_Dec_rateNfertivar.place(relx=0.92, rely=0.22)

    # Calcule du taux d'N en kg/ha en fonction de l'apport et du type ferti
    def calculate_kgN5():
        # Mise des return list dans des listes spécifiques
        listferti = printlist()
        y5rateferti_str = listferti[41]
        y5typeferti = listferti[40]
        # Création d'une liste vide convertissant les rate str en float
        y5rateferti_float = []
        # Création d'une liste pour les résultats des calcules
        resultlist = []
        # Vérification que chaque élément de cette liste puisse être convertie + conversion

        try:
            for i in y5rateferti_str:
                y5rateferti_float.append(float(i))
        except ValueError:
            print("Error! Please check you rate data. Some data are not float")

        # Calcule taux N en fonction type ferti
        for i in range(12):  # Pour janvier (0) et février (1)
            if y5typeferti[i] == "*None" and y5rateferti_float[i] == 0:
                resultlist.append(0)
            elif y5typeferti[i] == "Ammo Chlo" and y5rateferti_float[i] > 0:
                resammochlo = round(0.25 * y5rateferti_float[i], 1)
                resultlist.append(resammochlo)
            elif y5typeferti[i] == "Ammo Nit" and y5rateferti_float[i] > 0:
                resammonit = round(0.34 * y5rateferti_float[i], 1)
                resultlist.append(resammonit)
            elif y5typeferti[i] == "Ammo Sulf" and y5rateferti_float[i] > 0:
                resammosulf = round(0.21 * y5rateferti_float[i], 1)
                resultlist.append(resammosulf)
            elif y5typeferti[i] == "Sod Nit" and y5rateferti_float[i] > 0:
                ressodnit = round(0.16 * y5rateferti_float[i], 1)
                resultlist.append(ressodnit)
            elif y5typeferti[i] == "Urea" and y5rateferti_float[i] > 0:
                resurea = round(0.46 * y5rateferti_float[i], 1)
                resultlist.append(resurea)
            elif y5typeferti[i] == "*None" and y5rateferti_float[i] > 0:
                resultlist.append("Error!")
            elif y5typeferti[i] != "*None" and y5typeferti[i] != "Ammo Chlo" and y5typeferti[i] != "Ammo Nit" and \
                    y5typeferti[i] != "Ammo Sulf" and y5typeferti[i] != "Sod Nit" and y5typeferti[i] != "Urea":
                resultlist.append("Error!")
            else:
                resultlist.append("Error!")

        # Information résultats
        # Janvier
        equnitrogenjan = tkinter.Label(frame5,
                                       text=resultlist[0], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjan.place(relx=0.04, rely=0.28)
        # Fevrier
        equnitrogenfev = tkinter.Label(frame5,
                                       text=resultlist[1], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenfev.place(relx=0.12, rely=0.28)
        # Mars
        equnitrogenmar = tkinter.Label(frame5,
                                       text=resultlist[2], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenmar.place(relx=0.2, rely=0.28)
        # Avril
        equnitrogenapr = tkinter.Label(frame5,
                                       text=resultlist[3], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenapr.place(relx=0.28, rely=0.28)
        # Mai
        equnitrogenmay = tkinter.Label(frame5,
                                       text=resultlist[4], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenmay.place(relx=0.36, rely=0.28)
        # Juin
        equnitrogenjun = tkinter.Label(frame5,
                                       text=resultlist[5], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjun.place(relx=0.44, rely=0.28)
        # Juillet
        equnitrogenjul = tkinter.Label(frame5,
                                       text=resultlist[6], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjul.place(relx=0.52, rely=0.28)
        # Aout
        equnitrogenaug = tkinter.Label(frame5,
                                       text=resultlist[7], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenaug.place(relx=0.6, rely=0.28)
        # September
        equnitrogensep = tkinter.Label(frame5,
                                       text=resultlist[8], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogensep.place(relx=0.68, rely=0.28)
        # Octobre
        equnitrogenoct = tkinter.Label(frame5,
                                       text=resultlist[9], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenoct.place(relx=0.76, rely=0.28)
        # Novembre
        equnitrogennov = tkinter.Label(frame5,
                                       text=resultlist[10], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogennov.place(relx=0.84, rely=0.28)
        # Decembre
        equnitrogendec = tkinter.Label(frame5,
                                       text=resultlist[11], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogendec.place(relx=0.92, rely=0.28)

        # Calcule total annuelle
        yearcumul = 0
        resultlist_float = []
        try:
            for i in resultlist:
                resultlist_float.append(float(i))
        except ValueError:
            return
        for i in resultlist_float:
            if isinstance(i, float):
                yearcumul = round(i + yearcumul,1)
        # label cacule annuel
        Nfertianuel = tkinter.Label(frame5, text=f"Cumulative nitrogen for year: {yearcumul}")
        Nfertianuel.place(relx=0.04, rely=0.35)

    # Création bouton calcul équivalent azote N ferti
    button = tkinter.Button(frame5, text="Nitrogen equivalent (in kg/ha)",
                            width=100,
                            font=("Ariel", 10, "bold"), bg="lightblue",
                            command=lambda: [calculate_kgN5(), calculate_kgNorga5()])
    button.place(relx=0.2, rely=0.4)

    # Fonction pour récupérer toutes les infos placement
    def get_placement5():
        placementfertiy5 = [
            y1_Jan(y5_placementferti)]
        return placementfertiy5

    # Création combobox placement N ferti
    y5_placementferti = ttk.Combobox(frame5, values=Nfertiplacement,
                                     width=21)
    y5_placementferti.set("*Choice*")
    y5_placementferti.place(relx=0.06, rely=0.47)

    # Fonction pour récupérer toute la valeur de quantity organic
    def get_quantityorgafertiy5():
        quantityorgafertiy5list = [
            y1_Jan(y5_quantityorgavar)]
        return quantityorgafertiy5list

    # Création quantité fertilisation organique
    y5_quantityorgavar = tkinter.Entry(frame5,
                                       width=8,
                                       justify="right")
    y5_quantityorgavar.insert(tkinter.END, "0")
    y5_quantityorgavar.place(relx=0.1, rely=0.63)

    # Fonction pour récupérer la valeur de type organic
    def get_typeorgafertiy5():
        typeorgafertiy5list = [
            y1_Jan(y5_typeorgavar)]
        return typeorgafertiy5list

    # Création quantité fertilisation organique
    y5_typeorgavar = ttk.Combobox(frame5, values=Orgafertitype,
                                  width=10)
    y5_typeorgavar.set("*Choice*")
    y5_typeorgavar.place(relx=0.185, rely=0.63)

    # Calcule équivalent N ferti orga
    def calculate_kgNorga5():
        # Mise des return list dans des listes spécifiques
        listferti = printlist()
        y5_typefertiorga = listferti[44]
        y5_quantityfertiorga = listferti[43]
        # Création d'une liste vide permettant conversion liste en float
        y5_quantityfertiorga_float = []
        # Création liste pour valeurs
        Nfertiorga = []
        # Vérification que chaque élément de cette liste puisse être convertie + conversion
        try:
            for i in y5_quantityfertiorga:
                y5_quantityfertiorga_float.append(float(i))
        except ValueError:
            print("Error! Please check you rate data. Some data are not float")
            return
        # Calcule taux N en fonction type ferti orga si plusieurs valeurs
        for i in range(1):
            if y5_typefertiorga[i] == "*Choice*" and y5_quantityfertiorga_float[i] == 0:
                Nfertiorga.append(0)
            elif y5_typefertiorga[i] == "EFB" and y5_quantityfertiorga_float[i] > 0:
                # 0.90% N in DM * 0.36tDM/tFM (cf pg Pardon)
                Nfertiorgacal = round(3.24 * y5_quantityfertiorga_float[i], 1)
                Nfertiorga.append(Nfertiorgacal)
            elif y5_typefertiorga[i] == "Compost" and y5_quantityfertiorga_float[i] > 0:
                # 2.05% N in DM * 0.41tDM/tFM (cf pg Pardon)
                Nfertiorgacal = round(8.405 * y5_quantityfertiorga_float[i], 1)
                Nfertiorga.append(Nfertiorgacal)
            elif y5_typefertiorga[i] == "*Choice*" and y5_quantityfertiorga_float[i] > 0:
                Nfertiorga.append("Error!")
            elif y5_typefertiorga[i] != "*Choice*" and y5_typefertiorga[i] != "EFB" and y5_typefertiorga[i] != "Compost":
                Nfertiorga.append("Error!")
            else:
                Nfertiorga.append("Error!")

            # Information résultats
        equilabelnitroorgaferti = tkinter.Label(frame5,
                                                text="Nitrogen equivalent organic fertilization (in kgN/ha/yr) :")
        equilabelnitroorgaferti.place(relx=0.45, rely=0.63)
        equnitrogenorgaferti = tkinter.Label(frame5,
                                             text=Nfertiorga[0], font=("Ariel", 9, "bold"),
                                             bg="white", fg="blue", justify="right",
                                             width=10,
                                             relief="groove", borderwidth=5)
        equnitrogenorgaferti.place(relx=0.68, rely=0.63)

    # Fonction pour récupérer la valeur de placement organic
    def get_placementorgafertiy5():
        placementorgafertiy5list = [
            y1_Jan(y5_placementorgavar)]
        return placementorgafertiy5list

    # Création placement ferti organique
    y5_placementorgavar = ttk.Combobox(frame5, values=Orgafertiplacement,
                                       width=20)
    y5_placementorgavar.set("*Choice*")
    y5_placementorgavar.place(relx=0.31, rely=0.63)

    # Fonction pour récupérer la valeur de biomasse understorey
    def get_understoreybiomassy5():
        understoreybiomassy5list = [
            y1_Jan(y5_understoreybiomass)]
        return understoreybiomassy5list

    # Création biomasse understorey
    y5_understoreybiomass = ttk.Combobox(frame5, values=understoreybiomass,
                                         width=10)
    y5_understoreybiomass.set("*Choice*")
    y5_understoreybiomass.place(relx=0.05, rely=0.78)

    # Fonction pour récupérer la valeur de biomasse understorey
    def get_legumefractiony5():
        legumefractiony5list = [
            y1_Jan(y5_legumefraction)]
        return legumefractiony5list

    # Création legume fraction
    y5_legumefraction = ttk.Combobox(frame5, values=understoreylegumefraction,
                                     width=10)
    y5_legumefraction.set("*Choice*")
    y5_legumefraction.place(relx=0.24, rely=0.78)

    # Fonction pour récupérer la valeur pruned fronds
    def get_prunedy5():
        prunedy5list = [
            y1_Jan(y5_pruned)]
        return prunedy5list

    # Création combobox pruned fronds
    y5_pruned = ttk.Combobox(frame5, values=Prunedfronds,
                             width=20)
    y5_pruned.set("*Choice*")
    y5_pruned.place(relx=0.07, rely=0.92)

    # Fonction pour récupérer toute la valeur Natmo
    def get_Natmodepoy5():
        Natmoy5list = [
            y1_Jan(y5_Natmodepo)]
        return Natmoy5list

    # Création quantité Natmo
    y5_Natmodepo = tkinter.Entry(frame5,
                                 width=8,
                                 justify="right")
    y5_Natmodepo.insert(tkinter.END, "18")
    y5_Natmodepo.place(relx=0.66, rely=0.84)


    ################################################################################################################
    ###################################Year 6#######################################################################
    ################################################################################################################
    # Intégration de Second year dans la fenêtre
    year6 = (tkinter.Label(main_frame,
                           text="Sixth year", font=("Ariel", 20, 'underline')))
    year6.pack(anchor="w", pady=5)

    # Intégration du bloc data pour chaque type
    # Création encadré
    frame6 = tkinter.Frame(main_frame, bd=2, relief="solid", width=1450, height=400, padx=5, pady=2)
    frame6.pack(anchor="w", padx=15, pady=5, fill="none")

    # Mise de titre Mineral N ferti
    y6_MineralNfertilizer = (tkinter.Label(frame6,
                                           text="Mineral Nitrogen fertilizer", justify="center",
                                           font=("Ariel", 13, "bold", "underline")))
    y6_MineralNfertilizer.place(relx=0.01)

    # Mise de titre organic fertilizer
    y6_Organicfertilizer = (tkinter.Label(frame6,
                                          text="Organic fertilizer", justify="center",
                                          font=("Ariel", 13, "bold", "underline")))
    y6_Organicfertilizer.place(relx=0.01, rely=0.55)

    # Mise de titre understorey
    y6_Understorey = (tkinter.Label(frame6,
                                    text="Understorey", justify="center",
                                    font=("Ariel", 13, "bold", "underline")))
    y6_Understorey.place(relx=0.01, rely=0.7)

    # Mise de titre Pruned fronds
    y6_Prunedfronds = (tkinter.Label(frame6,
                                     text="Pruned fronds", justify="center",
                                     font=("Ariel", 13, "bold", "underline")))
    y6_Prunedfronds.place(relx=0.01, rely=0.85)

    # Mise titre atmospheric depositions
    y6_atmodepo = (tkinter.Label(frame6,
                                 text="Atmospheric depositions", justify="center",
                                 font=("Ariel", 13, "bold", "underline")))
    y6_atmodepo.place(relx=0.55, rely=0.75)

    # Intégration des mois
    y6_January = (tkinter.Label(frame6, text="January", font=("Ariel", 9), fg="blue"))
    y6_January.place(relx=0.06, rely=0.08)
    y6_February = (tkinter.Label(frame6, text="February", font=("Ariel", 9), fg="blue"))
    y6_February.place(relx=0.14, rely=0.08)
    y6_March = (tkinter.Label(frame6, text="March", font=("Ariel", 9), fg="blue"))
    y6_March.place(relx=0.22, rely=0.08)
    y6_April = (tkinter.Label(frame6, text="April", font=("Ariel", 9), fg="blue"))
    y6_April.place(relx=0.295, rely=0.08)
    y6_May = (tkinter.Label(frame6, text="May", font=("Ariel", 9), fg="blue"))
    y6_May.place(relx=0.377, rely=0.08)
    y6_June = (tkinter.Label(frame6, text="June", font=("Ariel", 9), fg="blue"))
    y6_June.place(relx=0.46, rely=0.08)
    y6_July = (tkinter.Label(frame6, text="July", font=("Ariel", 9), fg="blue"))
    y6_July.place(relx=0.54, rely=0.08)
    y6_August = (tkinter.Label(frame6, text="August", font=("Ariel", 9), fg="blue"))
    y6_August.place(relx=0.62, rely=0.08)
    y6_September = (tkinter.Label(frame6, text="September", font=("Ariel", 9), fg="blue"))
    y6_September.place(relx=0.69, rely=0.08)
    y6_October = (tkinter.Label(frame6, text="October", font=("Ariel", 9), fg="blue"))
    y6_October.place(relx=0.78, rely=0.08)
    y6_November = (tkinter.Label(frame6, text="November", font=("Ariel", 9), fg="blue"))
    y6_November.place(relx=0.85, rely=0.08)
    y6_December = (tkinter.Label(frame6, text="December", font=("Ariel", 9), fg="blue"))
    y6_December.place(relx=0.93, rely=0.08)

    # Création du type
    y6_type = (tkinter.Label(frame6, text="Type", fg="blue", font=("Ariel", 11, "bold")))
    y6_type.place(relx=0, rely=0.14)

    # Création data rate
    y6_rate = (tkinter.Label(frame6, text="Rate \n(kg/ha)", fg="blue", font=("Ariel", 11, "bold")))
    y6_rate.place(relx=0, rely=0.21)

    # Création placement
    y6_placementferti = (tkinter.Label(frame6, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y6_placementferti.place(relx=0, rely=0.47)

    # Création quantity ferti orga
    y6_quantityorga = (tkinter.Label(frame6, text="Quantity (in tFM)", fg="blue", font=("Ariel", 11, "bold")))
    y6_quantityorga.place(relx=0, rely=0.63)

    # Création type ferti orga
    y6_typeorga = (tkinter.Label(frame6, text="Type", fg="blue", font=("Ariel", 11, "bold")))
    y6_typeorga.place(relx=0.15, rely=0.63)

    # Création placement ferti orga
    y6_placementorga = (tkinter.Label(frame6, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y6_placementorga.place(relx=0.25, rely=0.63)

    # Création biomasse understorey
    y6_biomass = (tkinter.Label(frame6, text="Biomass", fg="blue", font=("Ariel", 11, "bold")))
    y6_biomass.place(relx=0, rely=0.78)

    # Création legume fraction
    y6_legumefrac = (tkinter.Label(frame6, text="Legume fraction", fg="blue", font=("Ariel", 11, "bold")))
    y6_legumefrac.place(relx=0.15, rely=0.78)

    # Création pruned fronts placement
    y6_prunedfr = (tkinter.Label(frame6, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y6_prunedfr.place(relx=0, rely=0.92)

    # Création atmospheric depositions
    y6_quantityNatmo = ( tkinter.Label(frame6, text="Quantity of nitrogen\n (in kg/ha/yr)", fg="blue", font=("Ariel", 11, "bold")))
    y6_quantityNatmo.place(relx=0.55, rely=0.82)

    # Fonction pour récupérer toutes les valeurs des mois pour Type N ferti
    def get_all_month_valuestypeNfertiy6():
        month_valuestypeNfertiy6 = [
            y1_Jan(y6_Jan_typeNfertivar),
            y1_Feb(y6_Feb_typeNfertivar),
            y1_Mar(y6_Mar_typeNfertivar),
            y1_Apr(y6_Apr_typeNfertivar),
            y1_Maymonth(y6_Maymonth_typeNfertivar),
            y1_Jun(y6_Jun_typeNfertivar),
            y1_Jul(y6_Jul_typeNfertivar),
            y1_Aug(y6_Aug_typeNfertivar),
            y1_Sep(y6_Sep_typeNfertivar),
            y1_Oct(y6_Oct_typeNfertivar),
            y1_Nov(y6_Nov_typeNfertivar),
            y1_Dec(y6_Dec_typeNfertivar)
        ]

        return month_valuestypeNfertiy6

    # Créer une variable Tkinter pour stocker l'élément sélectionné Nfertitype
    # Création combobox
    # Janvier
    y6_Jan_typeNfertivar = ttk.Combobox(frame6, values=typeNferti,
                                        width=10)
    y6_Jan_typeNfertivar.set("*None")
    y6_Jan_typeNfertivar.place(relx=0.04, rely=0.14)
    # Février
    y6_Feb_typeNfertivar = ttk.Combobox(frame6, values=typeNferti,
                                        width=10)
    y6_Feb_typeNfertivar.set("*None")
    y6_Feb_typeNfertivar.place(relx=0.12, rely=0.14)
    # Mars
    y6_Mar_typeNfertivar = ttk.Combobox(frame6, values=typeNferti,
                                        width=10)
    y6_Mar_typeNfertivar.set("*None")
    y6_Mar_typeNfertivar.place(relx=0.2, rely=0.14)
    # Avril
    y6_Apr_typeNfertivar = ttk.Combobox(frame6, values=typeNferti,
                                        width=10)
    y6_Apr_typeNfertivar.set("*None")
    y6_Apr_typeNfertivar.place(relx=0.28, rely=0.14)
    # May
    y6_Maymonth_typeNfertivar = ttk.Combobox(frame6, values=typeNferti,
                                             width=10)
    y6_Maymonth_typeNfertivar.set("*None")
    y6_Maymonth_typeNfertivar.place(relx=0.36, rely=0.14)
    # Juin
    y6_Jun_typeNfertivar = ttk.Combobox(frame6, values=typeNferti,
                                        width=10)
    y6_Jun_typeNfertivar.set("*None")
    y6_Jun_typeNfertivar.place(relx=0.44, rely=0.14)
    # July
    y6_Jul_typeNfertivar = ttk.Combobox(frame6, values=typeNferti,
                                        width=10)
    y6_Jul_typeNfertivar.set("*None")
    y6_Jul_typeNfertivar.place(relx=0.52, rely=0.14)
    # Aout
    y6_Aug_typeNfertivar = ttk.Combobox(frame6, values=typeNferti,
                                        width=10)
    y6_Aug_typeNfertivar.set("*None")
    y6_Aug_typeNfertivar.place(relx=0.6, rely=0.14)
    # Septembre
    y6_Sep_typeNfertivar = ttk.Combobox(frame6, values=typeNferti,
                                        width=10)
    y6_Sep_typeNfertivar.set("*None")
    y6_Sep_typeNfertivar.place(relx=0.68, rely=0.14)
    # Octobre
    y6_Oct_typeNfertivar = ttk.Combobox(frame6, values=typeNferti,
                                        width=10)
    y6_Oct_typeNfertivar.set("*None")
    y6_Oct_typeNfertivar.place(relx=0.76, rely=0.14)
    # Novembre
    y6_Nov_typeNfertivar = ttk.Combobox(frame6, values=typeNferti,
                                        width=10)
    y6_Nov_typeNfertivar.set("*None")
    y6_Nov_typeNfertivar.place(relx=0.84, rely=0.14)
    # Décembre
    y6_Dec_typeNfertivar = ttk.Combobox(frame6, values=typeNferti,
                                        width=10)
    y6_Dec_typeNfertivar.set("*None")
    y6_Dec_typeNfertivar.place(relx=0.92, rely=0.14)

    # Fonction pour récupérer toutes les valeurs des mois pour rate N ferti
    def get_all_month_valuesrateNfertiy6():
        month_valuesrateNfertiy6 = [
            y1_Jan(y6_Jan_rateNfertivar),
            y1_Feb(y6_Feb_rateNfertivar),
            y1_Mar(y6_Mar_rateNfertivar),
            y1_Apr(y6_Apr_rateNfertivar),
            y1_Maymonth(y6_Maymonth_rateNfertivar),
            y1_Jun(y6_Jun_rateNfertivar),
            y1_Jul(y6_Jul_rateNfertivar),
            y1_Aug(y6_Aug_rateNfertivar),
            y1_Sep(y6_Sep_rateNfertivar),
            y1_Oct(y6_Oct_rateNfertivar),
            y1_Nov(y6_Nov_rateNfertivar),
            y1_Dec(y6_Dec_rateNfertivar)
        ]
        return month_valuesrateNfertiy6

    # Créer une variable Tkinter pour stocker l'élément sélectionné NfertiRate
    # Création combobox
    # Janvier
    y6_Jan_rateNfertivar = tkinter.Entry(frame6,
                                         width=13,
                                         justify="right")
    y6_Jan_rateNfertivar.insert(tkinter.END, "0")
    y6_Jan_rateNfertivar.place(relx=0.04, rely=0.22)
    # Février
    y6_Feb_rateNfertivar = tkinter.Entry(frame6,
                                         width=13,
                                         justify="right")
    y6_Feb_rateNfertivar.insert(tkinter.END, "0")
    y6_Feb_rateNfertivar.place(relx=0.12, rely=0.22)
    # Mars
    y6_Mar_rateNfertivar = tkinter.Entry(frame6,
                                         width=13,
                                         justify="right")
    y6_Mar_rateNfertivar.insert(tkinter.END, "0")
    y6_Mar_rateNfertivar.place(relx=0.2, rely=0.22)
    # Avril
    y6_Apr_rateNfertivar = tkinter.Entry(frame6,
                                         width=13,
                                         justify="right")
    y6_Apr_rateNfertivar.insert(tkinter.END, "0")
    y6_Apr_rateNfertivar.place(relx=0.28, rely=0.22)
    # May
    y6_Maymonth_rateNfertivar = tkinter.Entry(frame6,
                                              width=13,
                                              justify="right")
    y6_Maymonth_rateNfertivar.insert(tkinter.END, "0")
    y6_Maymonth_rateNfertivar.place(relx=0.36, rely=0.22)
    # Juin
    y6_Jun_rateNfertivar = tkinter.Entry(frame6,
                                         width=13,
                                         justify="right")
    y6_Jun_rateNfertivar.insert(tkinter.END, "0")
    y6_Jun_rateNfertivar.place(relx=0.44, rely=0.22)
    # July
    y6_Jul_rateNfertivar = tkinter.Entry(frame6,
                                         width=13,
                                         justify="right")
    y6_Jul_rateNfertivar.insert(tkinter.END, "0")
    y6_Jul_rateNfertivar.place(relx=0.52, rely=0.22)
    # Aout
    y6_Aug_rateNfertivar = tkinter.Entry(frame6,
                                         width=13,
                                         justify="right")
    y6_Aug_rateNfertivar.insert(tkinter.END, "0")
    y6_Aug_rateNfertivar.place(relx=0.6, rely=0.22)
    # Septembre
    y6_Sep_rateNfertivar = tkinter.Entry(frame6,
                                         width=13,
                                         justify="right")
    y6_Sep_rateNfertivar.insert(tkinter.END, "0")
    y6_Sep_rateNfertivar.place(relx=0.68, rely=0.22)
    # Octobre
    y6_Oct_rateNfertivar = tkinter.Entry(frame6,
                                         width=13,
                                         justify="right")
    y6_Oct_rateNfertivar.insert(tkinter.END, "0")
    y6_Oct_rateNfertivar.place(relx=0.76, rely=0.22)
    # Novembre
    y6_Nov_rateNfertivar = tkinter.Entry(frame6,
                                         width=13,
                                         justify="right")
    y6_Nov_rateNfertivar.insert(tkinter.END, "0")
    y6_Nov_rateNfertivar.place(relx=0.84, rely=0.22)
    # Décembre
    y6_Dec_rateNfertivar = tkinter.Entry(frame6,
                                         width=13,
                                         justify="right")
    y6_Dec_rateNfertivar.insert(tkinter.END, "0")
    y6_Dec_rateNfertivar.place(relx=0.92, rely=0.22)

    # Calcule du taux d'N en kg/ha en fonction de l'apport et du type ferti
    def calculate_kgN6():
        # Mise des return list dans des listes spécifiques
        listferti = printlist()
        y6rateferti_str = listferti[51]
        y6typeferti = listferti[50]
        # Création d'une liste vide convertissant les rate str en float
        y6rateferti_float = []
        # Création d'une liste pour les résultats des calcules
        resultlist = []
        # Vérification que chaque élément de cette liste puisse être convertie + conversion

        try:
            for i in y6rateferti_str:
                y6rateferti_float.append(float(i))
        except ValueError:
            print("Error! Please check you rate data. Some data are not float")

        # Calcule taux N en fonction type ferti
        for i in range(12):  # Pour janvier (0) et février (1)
            if y6typeferti[i] == "*None" and y6rateferti_float[i] == 0:
                resultlist.append(0)
            elif y6typeferti[i] == "Ammo Chlo" and y6rateferti_float[i] > 0:
                resammochlo = round(0.25 * y6rateferti_float[i], 1)
                resultlist.append(resammochlo)
            elif y6typeferti[i] == "Ammo Nit" and y6rateferti_float[i] > 0:
                resammonit = round(0.34 * y6rateferti_float[i], 1)
                resultlist.append(resammonit)
            elif y6typeferti[i] == "Ammo Sulf" and y6rateferti_float[i] > 0:
                resammosulf = round(0.21 * y6rateferti_float[i], 1)
                resultlist.append(resammosulf)
            elif y6typeferti[i] == "Sod Nit" and y6rateferti_float[i] > 0:
                ressodnit = round(0.16 * y6rateferti_float[i], 1)
                resultlist.append(ressodnit)
            elif y6typeferti[i] == "Urea" and y6rateferti_float[i] > 0:
                resurea = round(0.46 * y6rateferti_float[i], 1)
                resultlist.append(resurea)
            elif y6typeferti[i] == "*None" and y6rateferti_float[i] > 0:
                resultlist.append("Error!")
            elif y6typeferti[i] != "*None" and y6typeferti[i] != "Ammo Chlo" and y6typeferti[i] != "Ammo Nit" and \
                    y6typeferti[i] != "Ammo Sulf" and y6typeferti[i] != "Sod Nit" and y6typeferti[i] != "Urea":
                resultlist.append("Error!")
            else:
                resultlist.append("Error!")

        # Information résultats
        # Janvier
        equnitrogenjan = tkinter.Label(frame6,
                                       text=resultlist[0], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjan.place(relx=0.04, rely=0.28)
        # Fevrier
        equnitrogenfev = tkinter.Label(frame6,
                                       text=resultlist[1], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenfev.place(relx=0.12, rely=0.28)
        # Mars
        equnitrogenmar = tkinter.Label(frame6,
                                       text=resultlist[2], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenmar.place(relx=0.2, rely=0.28)
        # Avril
        equnitrogenapr = tkinter.Label(frame6,
                                       text=resultlist[3], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenapr.place(relx=0.28, rely=0.28)
        # Mai
        equnitrogenmay = tkinter.Label(frame6,
                                       text=resultlist[4], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenmay.place(relx=0.36, rely=0.28)
        # Juin
        equnitrogenjun = tkinter.Label(frame6,
                                       text=resultlist[5], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjun.place(relx=0.44, rely=0.28)
        # Juillet
        equnitrogenjul = tkinter.Label(frame6,
                                       text=resultlist[6], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjul.place(relx=0.52, rely=0.28)
        # Aout
        equnitrogenaug = tkinter.Label(frame6,
                                       text=resultlist[7], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenaug.place(relx=0.6, rely=0.28)
        # September
        equnitrogensep = tkinter.Label(frame6,
                                       text=resultlist[8], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogensep.place(relx=0.68, rely=0.28)
        # Octobre
        equnitrogenoct = tkinter.Label(frame6,
                                       text=resultlist[9], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenoct.place(relx=0.76, rely=0.28)
        # Novembre
        equnitrogennov = tkinter.Label(frame6,
                                       text=resultlist[10], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogennov.place(relx=0.84, rely=0.28)
        # Decembre
        equnitrogendec = tkinter.Label(frame6,
                                       text=resultlist[11], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogendec.place(relx=0.92, rely=0.28)

        # Calcule total annuelle
        yearcumul = 0
        resultlist_float = []
        try:
            for i in resultlist:
                resultlist_float.append(float(i))
        except ValueError:
            return
        for i in resultlist_float:
            if isinstance(i, float):
                yearcumul = round(i + yearcumul,1)
        # label cacule annuel
        Nfertianuel = tkinter.Label(frame6, text=f"Cumulative nitrogen for year: {yearcumul}")
        Nfertianuel.place(relx=0.04, rely=0.35)

    # Création bouton calcul équivalent azote N ferti
    button = tkinter.Button(frame6, text="Nitrogen equivalent (in kg/ha)",
                            width=100,
                            font=("Ariel", 10, "bold"), bg="lightblue",
                            command=lambda: [calculate_kgN6(), calculate_kgNorga6()])
    button.place(relx=0.2, rely=0.4)

    # Fonction pour récupérer toutes les infos placement
    def get_placement6():
        placementfertiy6 = [
            y1_Jan(y6_placementferti)]
        return placementfertiy6

    # Création combobox placement N ferti
    y6_placementferti = ttk.Combobox(frame6, values=Nfertiplacement,
                                     width=21)
    y6_placementferti.set("*Choice*")
    y6_placementferti.place(relx=0.06, rely=0.47)

    # Fonction pour récupérer toute la valeur de quantity organic
    def get_quantityorgafertiy6():
        quantityorgafertiy6list = [
            y1_Jan(y6_quantityorgavar)]
        return quantityorgafertiy6list

    # Création quantité fertilisation organique
    y6_quantityorgavar = tkinter.Entry(frame6,
                                       width=8,
                                       justify="right")
    y6_quantityorgavar.insert(tkinter.END, "0")
    y6_quantityorgavar.place(relx=0.1, rely=0.63)

    # Fonction pour récupérer la valeur de type organic
    def get_typeorgafertiy6():
        typeorgafertiy6list = [
            y1_Jan(y6_typeorgavar)]
        return typeorgafertiy6list

    # Création quantité fertilisation organique
    y6_typeorgavar = ttk.Combobox(frame6, values=Orgafertitype,
                                  width=10)
    y6_typeorgavar.set("*Choice*")
    y6_typeorgavar.place(relx=0.185, rely=0.63)

    # Calcule équivalent N ferti orga
    def calculate_kgNorga6():
        # Mise des return list dans des listes spécifiques
        listferti = printlist()
        y6_typefertiorga = listferti[54]
        y6_quantityfertiorga = listferti[53]
        # Création d'une liste vide permettant conversion liste en float
        y6_quantityfertiorga_float = []
        # Création liste pour valeurs
        Nfertiorga = []
        # Vérification que chaque élément de cette liste puisse être convertie + conversion
        try:
            for i in y6_quantityfertiorga:
                y6_quantityfertiorga_float.append(float(i))
        except ValueError:
            print("Error! Please check you rate data. Some data are not float")
            return
        # Calcule taux N en fonction type ferti orga si plusieurs valeurs
        for i in range(1):
            if y6_typefertiorga[i] == "*Choice*" and y6_quantityfertiorga_float[i] == 0:
                Nfertiorga.append(0)
            elif y6_typefertiorga[i] == "EFB" and y6_quantityfertiorga_float[i] > 0:
                # 0.90% N in DM * 0.36tDM/tFM (cf pg Pardon)
                Nfertiorgacal = round(3.24 * y6_quantityfertiorga_float[i], 1)
                Nfertiorga.append(Nfertiorgacal)
            elif y6_typefertiorga[i] == "Compost" and y6_quantityfertiorga_float[i] > 0:
                # 2.05% N in DM * 0.41tDM/tFM (cf pg Pardon)
                Nfertiorgacal = round(8.405 * y6_quantityfertiorga_float[i], 1)
                Nfertiorga.append(Nfertiorgacal)
            elif y6_typefertiorga[i] == "*Choice*" and y6_quantityfertiorga_float[i] > 0:
                Nfertiorga.append("Error!")
            elif y6_typefertiorga[i] != "*Choice*" and y6_typefertiorga[i] != "EFB" and y6_typefertiorga[i] != "Compost":
                Nfertiorga.append("Error!")
            else:
                Nfertiorga.append("Error!")

            # Information résultats
        equilabelnitroorgaferti = tkinter.Label(frame6,
                                                text="Nitrogen equivalent organic fertilization (in kgN/ha/yr) :")
        equilabelnitroorgaferti.place(relx=0.45, rely=0.63)
        equnitrogenorgaferti = tkinter.Label(frame6,
                                             text=Nfertiorga[0], font=("Ariel", 9, "bold"),
                                             bg="white", fg="blue", justify="right",
                                             width=10,
                                             relief="groove", borderwidth=5)
        equnitrogenorgaferti.place(relx=0.68, rely=0.63)

    # Fonction pour récupérer la valeur de placement organic
    def get_placementorgafertiy6():
        placementorgafertiy6list = [
            y1_Jan(y6_placementorgavar)]
        return placementorgafertiy6list

    # Création placement ferti organique
    y6_placementorgavar = ttk.Combobox(frame6, values=Orgafertiplacement,
                                       width=20)
    y6_placementorgavar.set("*Choice*")
    y6_placementorgavar.place(relx=0.31, rely=0.63)

    # Fonction pour récupérer la valeur de biomasse understorey
    def get_understoreybiomassy6():
        understoreybiomassy6list = [
            y1_Jan(y6_understoreybiomass)]
        return understoreybiomassy6list

    # Création biomasse understorey
    y6_understoreybiomass = ttk.Combobox(frame6, values=understoreybiomass,
                                         width=10)
    y6_understoreybiomass.set("*Choice*")
    y6_understoreybiomass.place(relx=0.05, rely=0.78)

    # Fonction pour récupérer la valeur de biomasse understorey
    def get_legumefractiony6():
        legumefractiony6list = [
            y1_Jan(y6_legumefraction)]
        return legumefractiony6list

    # Création legume fraction
    y6_legumefraction = ttk.Combobox(frame6, values=understoreylegumefraction,
                                     width=10)
    y6_legumefraction.set("*Choice*")
    y6_legumefraction.place(relx=0.24, rely=0.78)

    # Fonction pour récupérer la valeur pruned fronds
    def get_prunedy6():
        prunedy6list = [
            y1_Jan(y6_pruned)]
        return prunedy6list

    # Création combobox pruned fronds
    y6_pruned = ttk.Combobox(frame6, values=Prunedfronds,
                             width=20)
    y6_pruned.set("*Choice*")
    y6_pruned.place(relx=0.07, rely=0.92)

    # Fonction pour récupérer toute la valeur Natmo
    def get_Natmodepoy6():
        Natmoy6list = [
            y1_Jan(y6_Natmodepo)]
        return Natmoy6list

    # Création quantité Natmo
    y6_Natmodepo = tkinter.Entry(frame6,
                                 width=8,
                                 justify="right")
    y6_Natmodepo.insert(tkinter.END, "18")
    y6_Natmodepo.place(relx=0.66, rely=0.84)

    ################################################################################################################
    ###################################Year 7#######################################################################
    ################################################################################################################
    # Intégration de Second year dans la fenêtre
    year7 = (tkinter.Label(main_frame,
                           text="Seventh year", font=("Ariel", 20, 'underline')))
    year7.pack(anchor="w", pady=5)

    # Intégration du bloc data pour chaque type
    # Création encadré
    frame7 = tkinter.Frame(main_frame, bd=2, relief="solid", width=1450, height=400, padx=5, pady=2)
    frame7.pack(anchor="w", padx=15, pady=5, fill="none")

    # Mise de titre Mineral N ferti
    y7_MineralNfertilizer = (tkinter.Label(frame7,
                                           text="Mineral Nitrogen fertilizer", justify="center",
                                           font=("Ariel", 13, "bold", "underline")))
    y7_MineralNfertilizer.place(relx=0.01)

    # Mise de titre organic fertilizer
    y7_Organicfertilizer = (tkinter.Label(frame7,
                                          text="Organic fertilizer", justify="center",
                                          font=("Ariel", 13, "bold", "underline")))
    y7_Organicfertilizer.place(relx=0.01, rely=0.55)

    # Mise de titre understorey
    y7_Understorey = (tkinter.Label(frame7,
                                    text="Understorey", justify="center",
                                    font=("Ariel", 13, "bold", "underline")))
    y7_Understorey.place(relx=0.01, rely=0.7)

    # Mise de titre Pruned fronds
    y7_Prunedfronds = (tkinter.Label(frame7,
                                     text="Pruned fronds", justify="center",
                                     font=("Ariel", 13, "bold", "underline")))
    y7_Prunedfronds.place(relx=0.01, rely=0.85)

    # Mise titre atmospheric depositions
    y7_atmodepo = (tkinter.Label(frame7,
                                 text="Atmospheric depositions", justify="center",
                                 font=("Ariel", 13, "bold", "underline")))
    y7_atmodepo.place(relx=0.55, rely=0.75)

    # Intégration des mois
    y7_January = (tkinter.Label(frame7, text="January", font=("Ariel", 9), fg="blue"))
    y7_January.place(relx=0.06, rely=0.08)
    y7_February = (tkinter.Label(frame7, text="February", font=("Ariel", 9), fg="blue"))
    y7_February.place(relx=0.14, rely=0.08)
    y7_March = (tkinter.Label(frame7, text="March", font=("Ariel", 9), fg="blue"))
    y7_March.place(relx=0.22, rely=0.08)
    y7_April = (tkinter.Label(frame7, text="April", font=("Ariel", 9), fg="blue"))
    y7_April.place(relx=0.295, rely=0.08)
    y7_May = (tkinter.Label(frame7, text="May", font=("Ariel", 9), fg="blue"))
    y7_May.place(relx=0.377, rely=0.08)
    y7_June = (tkinter.Label(frame7, text="June", font=("Ariel", 9), fg="blue"))
    y7_June.place(relx=0.46, rely=0.08)
    y7_July = (tkinter.Label(frame7, text="July", font=("Ariel", 9), fg="blue"))
    y7_July.place(relx=0.54, rely=0.08)
    y7_August = (tkinter.Label(frame7, text="August", font=("Ariel", 9), fg="blue"))
    y7_August.place(relx=0.62, rely=0.08)
    y7_September = (tkinter.Label(frame7, text="September", font=("Ariel", 9), fg="blue"))
    y7_September.place(relx=0.69, rely=0.08)
    y7_October = (tkinter.Label(frame7, text="October", font=("Ariel", 9), fg="blue"))
    y7_October.place(relx=0.78, rely=0.08)
    y7_November = (tkinter.Label(frame7, text="November", font=("Ariel", 9), fg="blue"))
    y7_November.place(relx=0.85, rely=0.08)
    y7_December = (tkinter.Label(frame7, text="December", font=("Ariel", 9), fg="blue"))
    y7_December.place(relx=0.93, rely=0.08)

    # Création du type
    y7_type = (tkinter.Label(frame7, text="Type", fg="blue", font=("Ariel", 11, "bold")))
    y7_type.place(relx=0, rely=0.14)

    # Création data rate
    y7_rate = (tkinter.Label(frame7, text="Rate \n(kg/ha)", fg="blue", font=("Ariel", 11, "bold")))
    y7_rate.place(relx=0, rely=0.21)

    # Création placement
    y7_placementferti = (tkinter.Label(frame7, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y7_placementferti.place(relx=0, rely=0.47)

    # Création quantity ferti orga
    y7_quantityorga = (tkinter.Label(frame7, text="Quantity (in tFM)", fg="blue", font=("Ariel", 11, "bold")))
    y7_quantityorga.place(relx=0, rely=0.63)

    # Création type ferti orga
    y7_typeorga = (tkinter.Label(frame7, text="Type", fg="blue", font=("Ariel", 11, "bold")))
    y7_typeorga.place(relx=0.15, rely=0.63)

    # Création placement ferti orga
    y7_placementorga = (tkinter.Label(frame7, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y7_placementorga.place(relx=0.25, rely=0.63)

    # Création biomasse understorey
    y7_biomass = (tkinter.Label(frame7, text="Biomass", fg="blue", font=("Ariel", 11, "bold")))
    y7_biomass.place(relx=0, rely=0.78)

    # Création legume fraction
    y7_legumefrac = (tkinter.Label(frame7, text="Legume fraction", fg="blue", font=("Ariel", 11, "bold")))
    y7_legumefrac.place(relx=0.15, rely=0.78)

    # Création pruned fronts placement
    y7_prunedfr = (tkinter.Label(frame7, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y7_prunedfr.place(relx=0, rely=0.92)

    # Création atmospheric depositions
    y7_quantityNatmo = (tkinter.Label(frame7, text="Quantity of nitrogen\n (in kg/ha/yr)", fg="blue", font=("Ariel", 11, "bold")))
    y7_quantityNatmo.place(relx=0.55, rely=0.82)

    # Fonction pour récupérer toutes les valeurs des mois pour Type N ferti
    def get_all_month_valuestypeNfertiy7():
        month_valuestypeNfertiy7 = [
            y1_Jan(y7_Jan_typeNfertivar),
            y1_Feb(y7_Feb_typeNfertivar),
            y1_Mar(y7_Mar_typeNfertivar),
            y1_Apr(y7_Apr_typeNfertivar),
            y1_Maymonth(y7_Maymonth_typeNfertivar),
            y1_Jun(y7_Jun_typeNfertivar),
            y1_Jul(y7_Jul_typeNfertivar),
            y1_Aug(y7_Aug_typeNfertivar),
            y1_Sep(y7_Sep_typeNfertivar),
            y1_Oct(y7_Oct_typeNfertivar),
            y1_Nov(y7_Nov_typeNfertivar),
            y1_Dec(y7_Dec_typeNfertivar)
        ]

        return month_valuestypeNfertiy7

    # Créer une variable Tkinter pour stocker l'élément sélectionné Nfertitype
    # Création combobox
    # Janvier
    y7_Jan_typeNfertivar = ttk.Combobox(frame7, values=typeNferti,
                                        width=10)
    y7_Jan_typeNfertivar.set("*None")
    y7_Jan_typeNfertivar.place(relx=0.04, rely=0.14)
    # Février
    y7_Feb_typeNfertivar = ttk.Combobox(frame7, values=typeNferti,
                                        width=10)
    y7_Feb_typeNfertivar.set("*None")
    y7_Feb_typeNfertivar.place(relx=0.12, rely=0.14)
    # Mars
    y7_Mar_typeNfertivar = ttk.Combobox(frame7, values=typeNferti,
                                        width=10)
    y7_Mar_typeNfertivar.set("*None")
    y7_Mar_typeNfertivar.place(relx=0.2, rely=0.14)
    # Avril
    y7_Apr_typeNfertivar = ttk.Combobox(frame7, values=typeNferti,
                                        width=10)
    y7_Apr_typeNfertivar.set("*None")
    y7_Apr_typeNfertivar.place(relx=0.28, rely=0.14)
    # May
    y7_Maymonth_typeNfertivar = ttk.Combobox(frame7, values=typeNferti,
                                             width=10)
    y7_Maymonth_typeNfertivar.set("*None")
    y7_Maymonth_typeNfertivar.place(relx=0.36, rely=0.14)
    # Juin
    y7_Jun_typeNfertivar = ttk.Combobox(frame7, values=typeNferti,
                                        width=10)
    y7_Jun_typeNfertivar.set("*None")
    y7_Jun_typeNfertivar.place(relx=0.44, rely=0.14)
    # July
    y7_Jul_typeNfertivar = ttk.Combobox(frame7, values=typeNferti,
                                        width=10)
    y7_Jul_typeNfertivar.set("*None")
    y7_Jul_typeNfertivar.place(relx=0.52, rely=0.14)
    # Aout
    y7_Aug_typeNfertivar = ttk.Combobox(frame7, values=typeNferti,
                                        width=10)
    y7_Aug_typeNfertivar.set("*None")
    y7_Aug_typeNfertivar.place(relx=0.6, rely=0.14)
    # Septembre
    y7_Sep_typeNfertivar = ttk.Combobox(frame7, values=typeNferti,
                                        width=10)
    y7_Sep_typeNfertivar.set("*None")
    y7_Sep_typeNfertivar.place(relx=0.68, rely=0.14)
    # Octobre
    y7_Oct_typeNfertivar = ttk.Combobox(frame7, values=typeNferti,
                                        width=10)
    y7_Oct_typeNfertivar.set("*None")
    y7_Oct_typeNfertivar.place(relx=0.76, rely=0.14)
    # Novembre
    y7_Nov_typeNfertivar = ttk.Combobox(frame7, values=typeNferti,
                                        width=10)
    y7_Nov_typeNfertivar.set("*None")
    y7_Nov_typeNfertivar.place(relx=0.84, rely=0.14)
    # Décembre
    y7_Dec_typeNfertivar = ttk.Combobox(frame7, values=typeNferti,
                                        width=10)
    y7_Dec_typeNfertivar.set("*None")
    y7_Dec_typeNfertivar.place(relx=0.92, rely=0.14)

    # Fonction pour récupérer toutes les valeurs des mois pour rate N ferti
    def get_all_month_valuesrateNfertiy7():
        month_valuesrateNfertiy7 = [
            y1_Jan(y7_Jan_rateNfertivar),
            y1_Feb(y7_Feb_rateNfertivar),
            y1_Mar(y7_Mar_rateNfertivar),
            y1_Apr(y7_Apr_rateNfertivar),
            y1_Maymonth(y7_Maymonth_rateNfertivar),
            y1_Jun(y7_Jun_rateNfertivar),
            y1_Jul(y7_Jul_rateNfertivar),
            y1_Aug(y7_Aug_rateNfertivar),
            y1_Sep(y7_Sep_rateNfertivar),
            y1_Oct(y7_Oct_rateNfertivar),
            y1_Nov(y7_Nov_rateNfertivar),
            y1_Dec(y7_Dec_rateNfertivar)
        ]
        return month_valuesrateNfertiy7

    # Créer une variable Tkinter pour stocker l'élément sélectionné NfertiRate
    # Création combobox
    # Janvier
    y7_Jan_rateNfertivar = tkinter.Entry(frame7,
                                         width=13,
                                         justify="right")
    y7_Jan_rateNfertivar.insert(tkinter.END, "0")
    y7_Jan_rateNfertivar.place(relx=0.04, rely=0.22)
    # Février
    y7_Feb_rateNfertivar = tkinter.Entry(frame7,
                                         width=13,
                                         justify="right")
    y7_Feb_rateNfertivar.insert(tkinter.END, "0")
    y7_Feb_rateNfertivar.place(relx=0.12, rely=0.22)
    # Mars
    y7_Mar_rateNfertivar = tkinter.Entry(frame7,
                                         width=13,
                                         justify="right")
    y7_Mar_rateNfertivar.insert(tkinter.END, "0")
    y7_Mar_rateNfertivar.place(relx=0.2, rely=0.22)
    # Avril
    y7_Apr_rateNfertivar = tkinter.Entry(frame7,
                                         width=13,
                                         justify="right")
    y7_Apr_rateNfertivar.insert(tkinter.END, "0")
    y7_Apr_rateNfertivar.place(relx=0.28, rely=0.22)
    # May
    y7_Maymonth_rateNfertivar = tkinter.Entry(frame7,
                                              width=13,
                                              justify="right")
    y7_Maymonth_rateNfertivar.insert(tkinter.END, "0")
    y7_Maymonth_rateNfertivar.place(relx=0.36, rely=0.22)
    # Juin
    y7_Jun_rateNfertivar = tkinter.Entry(frame7,
                                         width=13,
                                         justify="right")
    y7_Jun_rateNfertivar.insert(tkinter.END, "0")
    y7_Jun_rateNfertivar.place(relx=0.44, rely=0.22)
    # July
    y7_Jul_rateNfertivar = tkinter.Entry(frame7,
                                         width=13,
                                         justify="right")
    y7_Jul_rateNfertivar.insert(tkinter.END, "0")
    y7_Jul_rateNfertivar.place(relx=0.52, rely=0.22)
    # Aout
    y7_Aug_rateNfertivar = tkinter.Entry(frame7,
                                         width=13,
                                         justify="right")
    y7_Aug_rateNfertivar.insert(tkinter.END, "0")
    y7_Aug_rateNfertivar.place(relx=0.6, rely=0.22)
    # Septembre
    y7_Sep_rateNfertivar = tkinter.Entry(frame7,
                                         width=13,
                                         justify="right")
    y7_Sep_rateNfertivar.insert(tkinter.END, "0")
    y7_Sep_rateNfertivar.place(relx=0.68, rely=0.22)
    # Octobre
    y7_Oct_rateNfertivar = tkinter.Entry(frame7,
                                         width=13,
                                         justify="right")
    y7_Oct_rateNfertivar.insert(tkinter.END, "0")
    y7_Oct_rateNfertivar.place(relx=0.76, rely=0.22)
    # Novembre
    y7_Nov_rateNfertivar = tkinter.Entry(frame7,
                                         width=13,
                                         justify="right")
    y7_Nov_rateNfertivar.insert(tkinter.END, "0")
    y7_Nov_rateNfertivar.place(relx=0.84, rely=0.22)
    # Décembre
    y7_Dec_rateNfertivar = tkinter.Entry(frame7,
                                         width=13,
                                         justify="right")
    y7_Dec_rateNfertivar.insert(tkinter.END, "0")
    y7_Dec_rateNfertivar.place(relx=0.92, rely=0.22)

    # Calcule du taux d'N en kg/ha en fonction de l'apport et du type ferti
    def calculate_kgN7():
        # Mise des return list dans des listes spécifiques
        listferti = printlist()
        y7rateferti_str = listferti[61]
        y7typeferti = listferti[60]
        # Création d'une liste vide convertissant les rate str en float
        y7rateferti_float = []
        # Création d'une liste pour les résultats des calcules
        resultlist = []
        # Vérification que chaque élément de cette liste puisse être convertie + conversion

        try:
            for i in y7rateferti_str:
                y7rateferti_float.append(float(i))
        except ValueError:
            print("Error! Please check you rate data. Some data are not float")

        # Calcule taux N en fonction type ferti
        for i in range(12):  # Pour janvier (0) et février (1)
            if y7typeferti[i] == "*None" and y7rateferti_float[i] == 0:
                resultlist.append(0)
            elif y7typeferti[i] == "Ammo Chlo" and y7rateferti_float[i] > 0:
                resammochlo = round(0.25 * y7rateferti_float[i], 1)
                resultlist.append(resammochlo)
            elif y7typeferti[i] == "Ammo Nit" and y7rateferti_float[i] > 0:
                resammonit = round(0.34 * y7rateferti_float[i], 1)
                resultlist.append(resammonit)
            elif y7typeferti[i] == "Ammo Sulf" and y7rateferti_float[i] > 0:
                resammosulf = round(0.21 * y7rateferti_float[i], 1)
                resultlist.append(resammosulf)
            elif y7typeferti[i] == "Sod Nit" and y7rateferti_float[i] > 0:
                ressodnit = round(0.16 * y7rateferti_float[i], 1)
                resultlist.append(ressodnit)
            elif y7typeferti[i] == "Urea" and y7rateferti_float[i] > 0:
                resurea = round(0.46 * y7rateferti_float[i], 1)
                resultlist.append(resurea)
            elif y7typeferti[i] == "*None" and y7rateferti_float[i] > 0:
                resultlist.append("Error!")
            elif y7typeferti[i] != "*None" and y7typeferti[i] != "Ammo Chlo" and y7typeferti[i] != "Ammo Nit" and \
                    y7typeferti[i] != "Ammo Sulf" and y7typeferti[i] != "Sod Nit" and y7typeferti[i] != "Urea":
                resultlist.append("Error!")
            else:
                resultlist.append("Error!")

        # Information résultats
        # Janvier
        equnitrogenjan = tkinter.Label(frame7,
                                       text=resultlist[0], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjan.place(relx=0.04, rely=0.28)
        # Fevrier
        equnitrogenfev = tkinter.Label(frame7,
                                       text=resultlist[1], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenfev.place(relx=0.12, rely=0.28)
        # Mars
        equnitrogenmar = tkinter.Label(frame7,
                                       text=resultlist[2], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenmar.place(relx=0.2, rely=0.28)
        # Avril
        equnitrogenapr = tkinter.Label(frame7,
                                       text=resultlist[3], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenapr.place(relx=0.28, rely=0.28)
        # Mai
        equnitrogenmay = tkinter.Label(frame7,
                                       text=resultlist[4], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenmay.place(relx=0.36, rely=0.28)
        # Juin
        equnitrogenjun = tkinter.Label(frame7,
                                       text=resultlist[5], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjun.place(relx=0.44, rely=0.28)
        # Juillet
        equnitrogenjul = tkinter.Label(frame7,
                                       text=resultlist[6], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjul.place(relx=0.52, rely=0.28)
        # Aout
        equnitrogenaug = tkinter.Label(frame7,
                                       text=resultlist[7], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenaug.place(relx=0.6, rely=0.28)
        # September
        equnitrogensep = tkinter.Label(frame7,
                                       text=resultlist[8], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogensep.place(relx=0.68, rely=0.28)
        # Octobre
        equnitrogenoct = tkinter.Label(frame7,
                                       text=resultlist[9], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenoct.place(relx=0.76, rely=0.28)
        # Novembre
        equnitrogennov = tkinter.Label(frame7,
                                       text=resultlist[10], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogennov.place(relx=0.84, rely=0.28)
        # Decembre
        equnitrogendec = tkinter.Label(frame7,
                                       text=resultlist[11], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogendec.place(relx=0.92, rely=0.28)

        # Calcule total annuelle
        yearcumul = 0
        resultlist_float = []
        try:
            for i in resultlist:
                resultlist_float.append(float(i))
        except ValueError:
            return
        for i in resultlist_float:
            if isinstance(i, float):
                yearcumul = round(i + yearcumul,1)
        # label cacule annuel
        Nfertianuel = tkinter.Label(frame7, text=f"Cumulative nitrogen for year: {yearcumul}")
        Nfertianuel.place(relx=0.04, rely=0.35)

    # Création bouton calcul équivalent azote N ferti
    button = tkinter.Button(frame7, text="Nitrogen equivalent (in kg/ha)",
                            width=100,
                            font=("Ariel", 10, "bold"), bg="lightblue",
                            command=lambda: [calculate_kgN7(), calculate_kgNorga7()])
    button.place(relx=0.2, rely=0.4)

    # Fonction pour récupérer toutes les infos placement
    def get_placement7():
        placementfertiy7 = [
            y1_Jan(y7_placementferti)]
        return placementfertiy7

    # Création combobox placement N ferti
    y7_placementferti = ttk.Combobox(frame7, values=Nfertiplacement,
                                     width=21)
    y7_placementferti.set("*Choice*")
    y7_placementferti.place(relx=0.06, rely=0.47)

    # Fonction pour récupérer toute la valeur de quantity organic
    def get_quantityorgafertiy7():
        quantityorgafertiy7list = [
            y1_Jan(y7_quantityorgavar)]
        return quantityorgafertiy7list

    # Création quantité fertilisation organique
    y7_quantityorgavar = tkinter.Entry(frame7,
                                       width=8,
                                       justify="right")
    y7_quantityorgavar.insert(tkinter.END, "0")
    y7_quantityorgavar.place(relx=0.1, rely=0.63)

    # Fonction pour récupérer la valeur de type organic
    def get_typeorgafertiy7():
        typeorgafertiy7list = [
            y1_Jan(y7_typeorgavar)]
        return typeorgafertiy7list

    # Création quantité fertilisation organique
    y7_typeorgavar = ttk.Combobox(frame7, values=Orgafertitype,
                                  width=10)
    y7_typeorgavar.set("*Choice*")
    y7_typeorgavar.place(relx=0.185, rely=0.63)

    # Calcule équivalent N ferti orga
    def calculate_kgNorga7():
        # Mise des return list dans des listes spécifiques
        listferti = printlist()
        y7_typefertiorga = listferti[64]
        y7_quantityfertiorga = listferti[63]
        # Création d'une liste vide permettant conversion liste en float
        y7_quantityfertiorga_float = []
        # Création liste pour valeurs
        Nfertiorga = []
        # Vérification que chaque élément de cette liste puisse être convertie + conversion
        try:
            for i in y7_quantityfertiorga:
                y7_quantityfertiorga_float.append(float(i))
        except ValueError:
            print("Error! Please check you rate data. Some data are not float")
            return
        # Calcule taux N en fonction type ferti orga si plusieurs valeurs
        for i in range(1):
            if y7_typefertiorga[i] == "*Choice*" and y7_quantityfertiorga_float[i] == 0:
                Nfertiorga.append(0)
            elif y7_typefertiorga[i] == "EFB" and y7_quantityfertiorga_float[i] > 0:
                # 0.90% N in DM * 0.36tDM/tFM (cf pg Pardon)
                Nfertiorgacal = round(3.24 * y7_quantityfertiorga_float[i], 1)
                Nfertiorga.append(Nfertiorgacal)
            elif y7_typefertiorga[i] == "Compost" and y7_quantityfertiorga_float[i] > 0:
                # 2.05% N in DM * 0.41tDM/tFM (cf pg Pardon)
                Nfertiorgacal = round(8.405 * y7_quantityfertiorga_float[i], 1)
                Nfertiorga.append(Nfertiorgacal)
            elif y7_typefertiorga[i] == "*Choice*" and y7_quantityfertiorga_float[i] > 0:
                Nfertiorga.append("Error!")
            elif y7_typefertiorga[i] != "*Choice*" and y7_typefertiorga[i] != "EFB" and y7_typefertiorga[
                i] != "Compost":
                Nfertiorga.append("Error!")
            else:
                Nfertiorga.append("Error!")

            # Information résultats
        equilabelnitroorgaferti = tkinter.Label(frame7,
                                                text="Nitrogen equivalent organic fertilization (in kgN/ha/yr) :")
        equilabelnitroorgaferti.place(relx=0.45, rely=0.63)
        equnitrogenorgaferti = tkinter.Label(frame7,
                                             text=Nfertiorga[0], font=("Ariel", 9, "bold"),
                                             bg="white", fg="blue", justify="right",
                                             width=10,
                                             relief="groove", borderwidth=5)
        equnitrogenorgaferti.place(relx=0.68, rely=0.63)

    # Fonction pour récupérer la valeur de placement organic
    def get_placementorgafertiy7():
        placementorgafertiy7list = [
            y1_Jan(y7_placementorgavar)]
        return placementorgafertiy7list

    # Création placement ferti organique
    y7_placementorgavar = ttk.Combobox(frame7, values=Orgafertiplacement,
                                       width=20)
    y7_placementorgavar.set("*Choice*")
    y7_placementorgavar.place(relx=0.31, rely=0.63)

    # Fonction pour récupérer la valeur de biomasse understorey
    def get_understoreybiomassy7():
        understoreybiomassy7list = [
            y1_Jan(y7_understoreybiomass)]
        return understoreybiomassy7list

    # Création biomasse understorey
    y7_understoreybiomass = ttk.Combobox(frame7, values=understoreybiomass,
                                         width=10)
    y7_understoreybiomass.set("*Choice*")
    y7_understoreybiomass.place(relx=0.05, rely=0.78)

    # Fonction pour récupérer la valeur de biomasse understorey
    def get_legumefractiony7():
        legumefractiony7list = [
            y1_Jan(y7_legumefraction)]
        return legumefractiony7list

    # Création legume fraction
    y7_legumefraction = ttk.Combobox(frame7, values=understoreylegumefraction,
                                     width=10)
    y7_legumefraction.set("*Choice*")
    y7_legumefraction.place(relx=0.24, rely=0.78)

    # Fonction pour récupérer la valeur pruned fronds
    def get_prunedy7():
        prunedy7list = [
            y1_Jan(y7_pruned)]
        return prunedy7list

    # Création combobox pruned fronds
    y7_pruned = ttk.Combobox(frame7, values=Prunedfronds,
                             width=20)
    y7_pruned.set("*Choice*")
    y7_pruned.place(relx=0.07, rely=0.92)

    # Fonction pour récupérer toute la valeur Natmo
    def get_Natmodepoy7():
        Natmoy7list = [
            y1_Jan(y7_Natmodepo)]
        return Natmoy7list

    # Création quantité Natmo
    y7_Natmodepo = tkinter.Entry(frame7,
                                 width=8,
                                 justify="right")
    y7_Natmodepo.insert(tkinter.END, "18")
    y7_Natmodepo.place(relx=0.66, rely=0.84)


    ################################################################################################################
    ###################################Year 8#######################################################################
    ################################################################################################################
    # Intégration de Second year dans la fenêtre
    year8 = (tkinter.Label(main_frame,
                           text="Eigth year", font=("Ariel", 20, 'underline')))
    year8.pack(anchor="w", pady=5)

    # Intégration du bloc data pour chaque type
    # Création encadré
    frame8 = tkinter.Frame(main_frame, bd=2, relief="solid", width=1450, height=400, padx=5, pady=2)
    frame8.pack(anchor="w", padx=15, pady=5, fill="none")

    # Mise de titre Mineral N ferti
    y8_MineralNfertilizer = (tkinter.Label(frame8,
                                           text="Mineral Nitrogen fertilizer", justify="center",
                                           font=("Ariel", 13, "bold", "underline")))
    y8_MineralNfertilizer.place(relx=0.01)

    # Mise de titre organic fertilizer
    y8_Organicfertilizer = (tkinter.Label(frame8,
                                          text="Organic fertilizer", justify="center",
                                          font=("Ariel", 13, "bold", "underline")))
    y8_Organicfertilizer.place(relx=0.01, rely=0.55)

    # Mise de titre understorey
    y8_Understorey = (tkinter.Label(frame8,
                                    text="Understorey", justify="center",
                                    font=("Ariel", 13, "bold", "underline")))
    y8_Understorey.place(relx=0.01, rely=0.7)

    # Mise de titre Pruned fronds
    y8_Prunedfronds = (tkinter.Label(frame8,
                                     text="Pruned fronds", justify="center",
                                     font=("Ariel", 13, "bold", "underline")))
    y8_Prunedfronds.place(relx=0.01, rely=0.85)

    # Mise titre atmospheric depositions
    y8_atmodepo = (tkinter.Label(frame8,
                                 text="Atmospheric depositions", justify="center",
                                 font=("Ariel", 13, "bold", "underline")))
    y8_atmodepo.place(relx=0.55, rely=0.75)

    # Intégration des mois
    y8_January = (tkinter.Label(frame8, text="January", font=("Ariel", 9), fg="blue"))
    y8_January.place(relx=0.06, rely=0.08)
    y8_February = (tkinter.Label(frame8, text="February", font=("Ariel", 9), fg="blue"))
    y8_February.place(relx=0.14, rely=0.08)
    y8_March = (tkinter.Label(frame8, text="March", font=("Ariel", 9), fg="blue"))
    y8_March.place(relx=0.22, rely=0.08)
    y8_April = (tkinter.Label(frame8, text="April", font=("Ariel", 9), fg="blue"))
    y8_April.place(relx=0.295, rely=0.08)
    y8_May = (tkinter.Label(frame8, text="May", font=("Ariel", 9), fg="blue"))
    y8_May.place(relx=0.377, rely=0.08)
    y8_June = (tkinter.Label(frame8, text="June", font=("Ariel", 9), fg="blue"))
    y8_June.place(relx=0.46, rely=0.08)
    y8_July = (tkinter.Label(frame8, text="July", font=("Ariel", 9), fg="blue"))
    y8_July.place(relx=0.54, rely=0.08)
    y8_August = (tkinter.Label(frame8, text="August", font=("Ariel", 9), fg="blue"))
    y8_August.place(relx=0.62, rely=0.08)
    y8_September = (tkinter.Label(frame8, text="September", font=("Ariel", 9), fg="blue"))
    y8_September.place(relx=0.69, rely=0.08)
    y8_October = (tkinter.Label(frame8, text="October", font=("Ariel", 9), fg="blue"))
    y8_October.place(relx=0.78, rely=0.08)
    y8_November = (tkinter.Label(frame8, text="November", font=("Ariel", 9), fg="blue"))
    y8_November.place(relx=0.85, rely=0.08)
    y8_December = (tkinter.Label(frame8, text="December", font=("Ariel", 9), fg="blue"))
    y8_December.place(relx=0.93, rely=0.08)

    # Création du type
    y8_type = (tkinter.Label(frame8, text="Type", fg="blue", font=("Ariel", 11, "bold")))
    y8_type.place(relx=0, rely=0.14)

    # Création data rate
    y8_rate = (tkinter.Label(frame8, text="Rate \n(kg/ha)", fg="blue", font=("Ariel", 11, "bold")))
    y8_rate.place(relx=0, rely=0.21)

    # Création placement
    y8_placementferti = (tkinter.Label(frame8, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y8_placementferti.place(relx=0, rely=0.47)

    # Création quantity ferti orga
    y8_quantityorga = (tkinter.Label(frame8, text="Quantity (in tFM)", fg="blue", font=("Ariel", 11, "bold")))
    y8_quantityorga.place(relx=0, rely=0.63)

    # Création type ferti orga
    y8_typeorga = (tkinter.Label(frame8, text="Type", fg="blue", font=("Ariel", 11, "bold")))
    y8_typeorga.place(relx=0.15, rely=0.63)

    # Création placement ferti orga
    y8_placementorga = (tkinter.Label(frame8, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y8_placementorga.place(relx=0.25, rely=0.63)

    # Création biomasse understorey
    y8_biomass = (tkinter.Label(frame8, text="Biomass", fg="blue", font=("Ariel", 11, "bold")))
    y8_biomass.place(relx=0, rely=0.78)

    # Création legume fraction
    y8_legumefrac = (tkinter.Label(frame8, text="Legume fraction", fg="blue", font=("Ariel", 11, "bold")))
    y8_legumefrac.place(relx=0.15, rely=0.78)

    # Création pruned fronts placement
    y8_prunedfr = (tkinter.Label(frame8, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y8_prunedfr.place(relx=0, rely=0.92)

    # Création atmospheric depositions
    y8_quantityNatmo = (tkinter.Label(frame8, text="Quantity of nitrogen\n (in kg/ha/yr)", fg="blue", font=("Ariel", 11, "bold")))
    y8_quantityNatmo.place(relx=0.55, rely=0.82)

    # Fonction pour récupérer toutes les valeurs des mois pour Type N ferti
    def get_all_month_valuestypeNfertiy8():
        month_valuestypeNfertiy8 = [
            y1_Jan(y8_Jan_typeNfertivar),
            y1_Feb(y8_Feb_typeNfertivar),
            y1_Mar(y8_Mar_typeNfertivar),
            y1_Apr(y8_Apr_typeNfertivar),
            y1_Maymonth(y8_Maymonth_typeNfertivar),
            y1_Jun(y8_Jun_typeNfertivar),
            y1_Jul(y8_Jul_typeNfertivar),
            y1_Aug(y8_Aug_typeNfertivar),
            y1_Sep(y8_Sep_typeNfertivar),
            y1_Oct(y8_Oct_typeNfertivar),
            y1_Nov(y8_Nov_typeNfertivar),
            y1_Dec(y8_Dec_typeNfertivar)
        ]

        return month_valuestypeNfertiy8

    # Créer une variable Tkinter pour stocker l'élément sélectionné Nfertitype
    # Création combobox
    # Janvier
    y8_Jan_typeNfertivar = ttk.Combobox(frame8, values=typeNferti,
                                        width=10)
    y8_Jan_typeNfertivar.set("*None")
    y8_Jan_typeNfertivar.place(relx=0.04, rely=0.14)
    # Février
    y8_Feb_typeNfertivar = ttk.Combobox(frame8, values=typeNferti,
                                        width=10)
    y8_Feb_typeNfertivar.set("*None")
    y8_Feb_typeNfertivar.place(relx=0.12, rely=0.14)
    # Mars
    y8_Mar_typeNfertivar = ttk.Combobox(frame8, values=typeNferti,
                                        width=10)
    y8_Mar_typeNfertivar.set("*None")
    y8_Mar_typeNfertivar.place(relx=0.2, rely=0.14)
    # Avril
    y8_Apr_typeNfertivar = ttk.Combobox(frame8, values=typeNferti,
                                        width=10)
    y8_Apr_typeNfertivar.set("*None")
    y8_Apr_typeNfertivar.place(relx=0.28, rely=0.14)
    # May
    y8_Maymonth_typeNfertivar = ttk.Combobox(frame8, values=typeNferti,
                                             width=10)
    y8_Maymonth_typeNfertivar.set("*None")
    y8_Maymonth_typeNfertivar.place(relx=0.36, rely=0.14)
    # Juin
    y8_Jun_typeNfertivar = ttk.Combobox(frame8, values=typeNferti,
                                        width=10)
    y8_Jun_typeNfertivar.set("*None")
    y8_Jun_typeNfertivar.place(relx=0.44, rely=0.14)
    # July
    y8_Jul_typeNfertivar = ttk.Combobox(frame8, values=typeNferti,
                                        width=10)
    y8_Jul_typeNfertivar.set("*None")
    y8_Jul_typeNfertivar.place(relx=0.52, rely=0.14)
    # Aout
    y8_Aug_typeNfertivar = ttk.Combobox(frame8, values=typeNferti,
                                        width=10)
    y8_Aug_typeNfertivar.set("*None")
    y8_Aug_typeNfertivar.place(relx=0.6, rely=0.14)
    # Septembre
    y8_Sep_typeNfertivar = ttk.Combobox(frame8, values=typeNferti,
                                        width=10)
    y8_Sep_typeNfertivar.set("*None")
    y8_Sep_typeNfertivar.place(relx=0.68, rely=0.14)
    # Octobre
    y8_Oct_typeNfertivar = ttk.Combobox(frame8, values=typeNferti,
                                        width=10)
    y8_Oct_typeNfertivar.set("*None")
    y8_Oct_typeNfertivar.place(relx=0.76, rely=0.14)
    # Novembre
    y8_Nov_typeNfertivar = ttk.Combobox(frame8, values=typeNferti,
                                        width=10)
    y8_Nov_typeNfertivar.set("*None")
    y8_Nov_typeNfertivar.place(relx=0.84, rely=0.14)
    # Décembre
    y8_Dec_typeNfertivar = ttk.Combobox(frame8, values=typeNferti,
                                        width=10)
    y8_Dec_typeNfertivar.set("*None")
    y8_Dec_typeNfertivar.place(relx=0.92, rely=0.14)

    # Fonction pour récupérer toutes les valeurs des mois pour rate N ferti
    def get_all_month_valuesrateNfertiy8():
        month_valuesrateNfertiy8 = [
            y1_Jan(y8_Jan_rateNfertivar),
            y1_Feb(y8_Feb_rateNfertivar),
            y1_Mar(y8_Mar_rateNfertivar),
            y1_Apr(y8_Apr_rateNfertivar),
            y1_Maymonth(y8_Maymonth_rateNfertivar),
            y1_Jun(y8_Jun_rateNfertivar),
            y1_Jul(y8_Jul_rateNfertivar),
            y1_Aug(y8_Aug_rateNfertivar),
            y1_Sep(y8_Sep_rateNfertivar),
            y1_Oct(y8_Oct_rateNfertivar),
            y1_Nov(y8_Nov_rateNfertivar),
            y1_Dec(y8_Dec_rateNfertivar)
        ]
        return month_valuesrateNfertiy8

    # Créer une variable Tkinter pour stocker l'élément sélectionné NfertiRate
    # Création combobox
    # Janvier
    y8_Jan_rateNfertivar = tkinter.Entry(frame8,
                                         width=13,
                                         justify="right")
    y8_Jan_rateNfertivar.insert(tkinter.END, "0")
    y8_Jan_rateNfertivar.place(relx=0.04, rely=0.22)
    # Février
    y8_Feb_rateNfertivar = tkinter.Entry(frame8,
                                         width=13,
                                         justify="right")
    y8_Feb_rateNfertivar.insert(tkinter.END, "0")
    y8_Feb_rateNfertivar.place(relx=0.12, rely=0.22)
    # Mars
    y8_Mar_rateNfertivar = tkinter.Entry(frame8,
                                         width=13,
                                         justify="right")
    y8_Mar_rateNfertivar.insert(tkinter.END, "0")
    y8_Mar_rateNfertivar.place(relx=0.2, rely=0.22)
    # Avril
    y8_Apr_rateNfertivar = tkinter.Entry(frame8,
                                         width=13,
                                         justify="right")
    y8_Apr_rateNfertivar.insert(tkinter.END, "0")
    y8_Apr_rateNfertivar.place(relx=0.28, rely=0.22)
    # May
    y8_Maymonth_rateNfertivar = tkinter.Entry(frame8,
                                              width=13,
                                              justify="right")
    y8_Maymonth_rateNfertivar.insert(tkinter.END, "0")
    y8_Maymonth_rateNfertivar.place(relx=0.36, rely=0.22)
    # Juin
    y8_Jun_rateNfertivar = tkinter.Entry(frame8,
                                         width=13,
                                         justify="right")
    y8_Jun_rateNfertivar.insert(tkinter.END, "0")
    y8_Jun_rateNfertivar.place(relx=0.44, rely=0.22)
    # July
    y8_Jul_rateNfertivar = tkinter.Entry(frame8,
                                         width=13,
                                         justify="right")
    y8_Jul_rateNfertivar.insert(tkinter.END, "0")
    y8_Jul_rateNfertivar.place(relx=0.52, rely=0.22)
    # Aout
    y8_Aug_rateNfertivar = tkinter.Entry(frame8,
                                         width=13,
                                         justify="right")
    y8_Aug_rateNfertivar.insert(tkinter.END, "0")
    y8_Aug_rateNfertivar.place(relx=0.6, rely=0.22)
    # Septembre
    y8_Sep_rateNfertivar = tkinter.Entry(frame8,
                                         width=13,
                                         justify="right")
    y8_Sep_rateNfertivar.insert(tkinter.END, "0")
    y8_Sep_rateNfertivar.place(relx=0.68, rely=0.22)
    # Octobre
    y8_Oct_rateNfertivar = tkinter.Entry(frame8,
                                         width=13,
                                         justify="right")
    y8_Oct_rateNfertivar.insert(tkinter.END, "0")
    y8_Oct_rateNfertivar.place(relx=0.76, rely=0.22)
    # Novembre
    y8_Nov_rateNfertivar = tkinter.Entry(frame8,
                                         width=13,
                                         justify="right")
    y8_Nov_rateNfertivar.insert(tkinter.END, "0")
    y8_Nov_rateNfertivar.place(relx=0.84, rely=0.22)
    # Décembre
    y8_Dec_rateNfertivar = tkinter.Entry(frame8,
                                         width=13,
                                         justify="right")
    y8_Dec_rateNfertivar.insert(tkinter.END, "0")
    y8_Dec_rateNfertivar.place(relx=0.92, rely=0.22)

    # Calcule du taux d'N en kg/ha en fonction de l'apport et du type ferti
    def calculate_kgN8():
        # Mise des return list dans des listes spécifiques
        listferti = printlist()
        y8rateferti_str = listferti[71]
        y8typeferti = listferti[70]
        # Création d'une liste vide convertissant les rate str en float
        y8rateferti_float = []
        # Création d'une liste pour les résultats des calcules
        resultlist = []
        # Vérification que chaque élément de cette liste puisse être convertie + conversion

        try:
            for i in y8rateferti_str:
                y8rateferti_float.append(float(i))
        except ValueError:
            print("Error! Please check you rate data. Some data are not float")

        # Calcule taux N en fonction type ferti
        for i in range(12):  # Pour janvier (0) et février (1)
            if y8typeferti[i] == "*None" and y8rateferti_float[i] == 0:
                resultlist.append(0)
            elif y8typeferti[i] == "Ammo Chlo" and y8rateferti_float[i] > 0:
                resammochlo = round(0.25 * y8rateferti_float[i], 1)
                resultlist.append(resammochlo)
            elif y8typeferti[i] == "Ammo Nit" and y8rateferti_float[i] > 0:
                resammonit = round(0.34 * y8rateferti_float[i], 1)
                resultlist.append(resammonit)
            elif y8typeferti[i] == "Ammo Sulf" and y8rateferti_float[i] > 0:
                resammosulf = round(0.21 * y8rateferti_float[i], 1)
                resultlist.append(resammosulf)
            elif y8typeferti[i] == "Sod Nit" and y8rateferti_float[i] > 0:
                ressodnit = round(0.16 * y8rateferti_float[i], 1)
                resultlist.append(ressodnit)
            elif y8typeferti[i] == "Urea" and y8rateferti_float[i] > 0:
                resurea = round(0.46 * y8rateferti_float[i], 1)
                resultlist.append(resurea)
            elif y8typeferti[i] == "*None" and y8rateferti_float[i] > 0:
                resultlist.append("Error!")
            elif y8typeferti[i] != "*None" and y8typeferti[i] != "Ammo Chlo" and y8typeferti[i] != "Ammo Nit" and \
                    y8typeferti[i] != "Ammo Sulf" and y8typeferti[i] != "Sod Nit" and y8typeferti[i] != "Urea":
                resultlist.append("Error!")
            else:
                resultlist.append("Error!")

        # Information résultats
        # Janvier
        equnitrogenjan = tkinter.Label(frame8,
                                       text=resultlist[0], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjan.place(relx=0.04, rely=0.28)
        # Fevrier
        equnitrogenfev = tkinter.Label(frame8,
                                       text=resultlist[1], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenfev.place(relx=0.12, rely=0.28)
        # Mars
        equnitrogenmar = tkinter.Label(frame8,
                                       text=resultlist[2], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenmar.place(relx=0.2, rely=0.28)
        # Avril
        equnitrogenapr = tkinter.Label(frame8,
                                       text=resultlist[3], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenapr.place(relx=0.28, rely=0.28)
        # Mai
        equnitrogenmay = tkinter.Label(frame8,
                                       text=resultlist[4], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenmay.place(relx=0.36, rely=0.28)
        # Juin
        equnitrogenjun = tkinter.Label(frame8,
                                       text=resultlist[5], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjun.place(relx=0.44, rely=0.28)
        # Juillet
        equnitrogenjul = tkinter.Label(frame8,
                                       text=resultlist[6], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjul.place(relx=0.52, rely=0.28)
        # Aout
        equnitrogenaug = tkinter.Label(frame8,
                                       text=resultlist[7], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenaug.place(relx=0.6, rely=0.28)
        # September
        equnitrogensep = tkinter.Label(frame8,
                                       text=resultlist[8], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogensep.place(relx=0.68, rely=0.28)
        # Octobre
        equnitrogenoct = tkinter.Label(frame8,
                                       text=resultlist[9], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenoct.place(relx=0.76, rely=0.28)
        # Novembre
        equnitrogennov = tkinter.Label(frame8,
                                       text=resultlist[10], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogennov.place(relx=0.84, rely=0.28)
        # Decembre
        equnitrogendec = tkinter.Label(frame8,
                                       text=resultlist[11], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogendec.place(relx=0.92, rely=0.28)

        # Calcule total annuelle
        yearcumul = 0
        resultlist_float = []
        try:
            for i in resultlist:
                resultlist_float.append(float(i))
        except ValueError:
            return
        for i in resultlist_float:
            if isinstance(i, float):
                yearcumul = round(i + yearcumul)
        # label cacule annuel
        Nfertianuel = tkinter.Label(frame8, text=f"Cumulative nitrogen for year: {yearcumul}")
        Nfertianuel.place(relx=0.04, rely=0.35)

    # Création bouton calcul équivalent azote N ferti
    button = tkinter.Button(frame8, text="Nitrogen equivalent (in kg/ha)",
                            width=100,
                            font=("Ariel", 10, "bold"), bg="lightblue",
                            command=lambda: [calculate_kgN8(), calculate_kgNorga8()])
    button.place(relx=0.2, rely=0.4)

    # Fonction pour récupérer toutes les infos placement
    def get_placement8():
        placementfertiy8 = [
            y1_Jan(y8_placementferti)]
        return placementfertiy8

    # Création combobox placement N ferti
    y8_placementferti = ttk.Combobox(frame8, values=Nfertiplacement,
                                     width=21)
    y8_placementferti.set("*Choice*")
    y8_placementferti.place(relx=0.06, rely=0.47)

    # Fonction pour récupérer toute la valeur de quantity organic
    def get_quantityorgafertiy8():
        quantityorgafertiy8list = [
            y1_Jan(y8_quantityorgavar)]
        return quantityorgafertiy8list

    # Création quantité fertilisation organique
    y8_quantityorgavar = tkinter.Entry(frame8,
                                       width=8,
                                       justify="right")
    y8_quantityorgavar.insert(tkinter.END, "0")
    y8_quantityorgavar.place(relx=0.1, rely=0.63)

    # Fonction pour récupérer la valeur de type organic
    def get_typeorgafertiy8():
        typeorgafertiy8list = [
            y1_Jan(y8_typeorgavar)]
        return typeorgafertiy8list

    # Création quantité fertilisation organique
    y8_typeorgavar = ttk.Combobox(frame8, values=Orgafertitype,
                                  width=10)
    y8_typeorgavar.set("*Choice*")
    y8_typeorgavar.place(relx=0.185, rely=0.63)

    # Calcule équivalent N ferti orga
    def calculate_kgNorga8():
        # Mise des return list dans des listes spécifiques
        listferti = printlist()
        y8_typefertiorga = listferti[74]
        y8_quantityfertiorga = listferti[73]
        # Création d'une liste vide permettant conversion liste en float
        y8_quantityfertiorga_float = []
        # Création liste pour valeurs
        Nfertiorga = []
        # Vérification que chaque élément de cette liste puisse être convertie + conversion
        try:
            for i in y8_quantityfertiorga:
                y8_quantityfertiorga_float.append(float(i))
        except ValueError:
            print("Error! Please check you rate data. Some data are not float")
            return
        # Calcule taux N en fonction type ferti orga si plusieurs valeurs
        for i in range(1):
            if y8_typefertiorga[i] == "*Choice*" and y8_quantityfertiorga_float[i] == 0:
                Nfertiorga.append(0)
            elif y8_typefertiorga[i] == "EFB" and y8_quantityfertiorga_float[i] > 0:
                # 0.90% N in DM * 0.36tDM/tFM (cf pg Pardon)
                Nfertiorgacal = round(3.24 * y8_quantityfertiorga_float[i], 1)
                Nfertiorga.append(Nfertiorgacal)
            elif y8_typefertiorga[i] == "Compost" and y8_quantityfertiorga_float[i] > 0:
                # 2.05% N in DM * 0.41tDM/tFM (cf pg Pardon)
                Nfertiorgacal = round(8.405 * y8_quantityfertiorga_float[i], 1)
                Nfertiorga.append(Nfertiorgacal)
            elif y8_typefertiorga[i] == "*Choice*" and y8_quantityfertiorga_float[i] > 0:
                Nfertiorga.append("Error!")
            elif y8_typefertiorga[i] != "*Choice*" and y8_typefertiorga[i] != "EFB" and y8_typefertiorga[
                i] != "Compost":
                Nfertiorga.append("Error!")
            else:
                Nfertiorga.append("Error!")

            # Information résultats
        equilabelnitroorgaferti = tkinter.Label(frame8,
                                                text="Nitrogen equivalent organic fertilization (in kgN/ha/yr) :")
        equilabelnitroorgaferti.place(relx=0.45, rely=0.63)
        equnitrogenorgaferti = tkinter.Label(frame8,
                                             text=Nfertiorga[0], font=("Ariel", 9, "bold"),
                                             bg="white", fg="blue", justify="right",
                                             width=10,
                                             relief="groove", borderwidth=5)
        equnitrogenorgaferti.place(relx=0.68, rely=0.63)

    # Fonction pour récupérer la valeur de placement organic
    def get_placementorgafertiy8():
        placementorgafertiy8list = [
            y1_Jan(y8_placementorgavar)]
        return placementorgafertiy8list

    # Création placement ferti organique
    y8_placementorgavar = ttk.Combobox(frame8, values=Orgafertiplacement,
                                       width=20)
    y8_placementorgavar.set("*Choice*")
    y8_placementorgavar.place(relx=0.31, rely=0.63)

    # Fonction pour récupérer la valeur de biomasse understorey
    def get_understoreybiomassy8():
        understoreybiomassy8list = [
            y1_Jan(y8_understoreybiomass)]
        return understoreybiomassy8list

    # Création biomasse understorey
    y8_understoreybiomass = ttk.Combobox(frame8, values=understoreybiomass,
                                         width=10)
    y8_understoreybiomass.set("*Choice*")
    y8_understoreybiomass.place(relx=0.05, rely=0.78)

    # Fonction pour récupérer la valeur de biomasse understorey
    def get_legumefractiony8():
        legumefractiony8list = [
            y1_Jan(y8_legumefraction)]
        return legumefractiony8list

    # Création legume fraction
    y8_legumefraction = ttk.Combobox(frame8, values=understoreylegumefraction,
                                     width=10)
    y8_legumefraction.set("*Choice*")
    y8_legumefraction.place(relx=0.24, rely=0.78)

    # Fonction pour récupérer la valeur pruned fronds
    def get_prunedy8():
        prunedy8list = [
            y1_Jan(y8_pruned)]
        return prunedy8list

    # Création combobox pruned fronds
    y8_pruned = ttk.Combobox(frame8, values=Prunedfronds,
                             width=20)
    y8_pruned.set("*Choice*")
    y8_pruned.place(relx=0.07, rely=0.92)

    # Fonction pour récupérer toute la valeur Natmo
    def get_Natmodepoy8():
        Natmoy8list = [
            y1_Jan(y8_Natmodepo)]
        return Natmoy8list

    # Création quantité Natmo
    y8_Natmodepo = tkinter.Entry(frame8,
                                 width=8,
                                 justify="right")
    y8_Natmodepo.insert(tkinter.END, "18")
    y8_Natmodepo.place(relx=0.66, rely=0.84)

    ################################################################################################################
    ###################################Year 9#######################################################################
    ################################################################################################################
    # Intégration de Second year dans la fenêtre
    year9 = (tkinter.Label(main_frame,
                           text="Nineth year", font=("Ariel", 20, 'underline')))
    year9.pack(anchor="w", pady=5)

    # Intégration du bloc data pour chaque type
    # Création encadré
    frame9 = tkinter.Frame(main_frame, bd=2, relief="solid", width=1450, height=400, padx=5, pady=2)
    frame9.pack(anchor="w", padx=15, pady=5, fill="none")

    # Mise de titre Mineral N ferti
    y9_MineralNfertilizer = (tkinter.Label(frame9,
                                           text="Mineral Nitrogen fertilizer", justify="center",
                                           font=("Ariel", 13, "bold", "underline")))
    y9_MineralNfertilizer.place(relx=0.01)

    # Mise de titre organic fertilizer
    y9_Organicfertilizer = (tkinter.Label(frame9,
                                          text="Organic fertilizer", justify="center",
                                          font=("Ariel", 13, "bold", "underline")))
    y9_Organicfertilizer.place(relx=0.01, rely=0.55)

    # Mise de titre understorey
    y9_Understorey = (tkinter.Label(frame9,
                                    text="Understorey", justify="center",
                                    font=("Ariel", 13, "bold", "underline")))
    y9_Understorey.place(relx=0.01, rely=0.7)

    # Mise de titre Pruned fronds
    y9_Prunedfronds = (tkinter.Label(frame9,
                                     text="Pruned fronds", justify="center",
                                     font=("Ariel", 13, "bold", "underline")))
    y9_Prunedfronds.place(relx=0.01, rely=0.85)

    # Mise titre atmospheric depositions
    y9_atmodepo = (tkinter.Label(frame9,
                                 text="Atmospheric depositions", justify="center",
                                 font=("Ariel", 13, "bold", "underline")))
    y9_atmodepo.place(relx=0.55, rely=0.75)

    # Intégration des mois
    y9_January = (tkinter.Label(frame9, text="January", font=("Ariel", 9), fg="blue"))
    y9_January.place(relx=0.06, rely=0.08)
    y9_February = (tkinter.Label(frame9, text="February", font=("Ariel", 9), fg="blue"))
    y9_February.place(relx=0.14, rely=0.08)
    y9_March = (tkinter.Label(frame9, text="March", font=("Ariel", 9), fg="blue"))
    y9_March.place(relx=0.22, rely=0.08)
    y9_April = (tkinter.Label(frame9, text="April", font=("Ariel", 9), fg="blue"))
    y9_April.place(relx=0.295, rely=0.08)
    y9_May = (tkinter.Label(frame9, text="May", font=("Ariel", 9), fg="blue"))
    y9_May.place(relx=0.377, rely=0.08)
    y9_June = (tkinter.Label(frame9, text="June", font=("Ariel", 9), fg="blue"))
    y9_June.place(relx=0.46, rely=0.08)
    y9_July = (tkinter.Label(frame9, text="July", font=("Ariel", 9), fg="blue"))
    y9_July.place(relx=0.54, rely=0.08)
    y9_August = (tkinter.Label(frame9, text="August", font=("Ariel", 9), fg="blue"))
    y9_August.place(relx=0.62, rely=0.08)
    y9_September = (tkinter.Label(frame9, text="September", font=("Ariel", 9), fg="blue"))
    y9_September.place(relx=0.69, rely=0.08)
    y9_October = (tkinter.Label(frame9, text="October", font=("Ariel", 9), fg="blue"))
    y9_October.place(relx=0.78, rely=0.08)
    y9_November = (tkinter.Label(frame9, text="November", font=("Ariel", 9), fg="blue"))
    y9_November.place(relx=0.85, rely=0.08)
    y9_December = (tkinter.Label(frame9, text="December", font=("Ariel", 9), fg="blue"))
    y9_December.place(relx=0.93, rely=0.08)

    # Création du type
    y9_type = (tkinter.Label(frame9, text="Type", fg="blue", font=("Ariel", 11, "bold")))
    y9_type.place(relx=0, rely=0.14)

    # Création data rate
    y9_rate = (tkinter.Label(frame9, text="Rate \n(kg/ha)", fg="blue", font=("Ariel", 11, "bold")))
    y9_rate.place(relx=0, rely=0.21)

    # Création placement
    y9_placementferti = (tkinter.Label(frame9, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y9_placementferti.place(relx=0, rely=0.47)

    # Création quantity ferti orga
    y9_quantityorga = (tkinter.Label(frame9, text="Quantity (in tFM)", fg="blue", font=("Ariel", 11, "bold")))
    y9_quantityorga.place(relx=0, rely=0.63)

    # Création type ferti orga
    y9_typeorga = (tkinter.Label(frame9, text="Type", fg="blue", font=("Ariel", 11, "bold")))
    y9_typeorga.place(relx=0.15, rely=0.63)

    # Création placement ferti orga
    y9_placementorga = (tkinter.Label(frame9, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y9_placementorga.place(relx=0.25, rely=0.63)

    # Création biomasse understorey
    y9_biomass = (tkinter.Label(frame9, text="Biomass", fg="blue", font=("Ariel", 11, "bold")))
    y9_biomass.place(relx=0, rely=0.78)

    # Création legume fraction
    y9_legumefrac = (tkinter.Label(frame9, text="Legume fraction", fg="blue", font=("Ariel", 11, "bold")))
    y9_legumefrac.place(relx=0.15, rely=0.78)

    # Création pruned fronts placement
    y9_prunedfr = (tkinter.Label(frame9, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y9_prunedfr.place(relx=0, rely=0.92)

    # Création atmospheric depositions
    y9_quantityNatmo = (tkinter.Label(frame9, text="Quantity of nitrogen\n (in kg/ha/yr)", fg="blue", font=("Ariel", 11, "bold")))
    y9_quantityNatmo.place(relx=0.55, rely=0.82)

    # Fonction pour récupérer toutes les valeurs des mois pour Type N ferti
    def get_all_month_valuestypeNfertiy9():
        month_valuestypeNfertiy9 = [
            y1_Jan(y9_Jan_typeNfertivar),
            y1_Feb(y9_Feb_typeNfertivar),
            y1_Mar(y9_Mar_typeNfertivar),
            y1_Apr(y9_Apr_typeNfertivar),
            y1_Maymonth(y9_Maymonth_typeNfertivar),
            y1_Jun(y9_Jun_typeNfertivar),
            y1_Jul(y9_Jul_typeNfertivar),
            y1_Aug(y9_Aug_typeNfertivar),
            y1_Sep(y9_Sep_typeNfertivar),
            y1_Oct(y9_Oct_typeNfertivar),
            y1_Nov(y9_Nov_typeNfertivar),
            y1_Dec(y9_Dec_typeNfertivar)
        ]

        return month_valuestypeNfertiy9

    # Créer une variable Tkinter pour stocker l'élément sélectionné Nfertitype
    # Création combobox
    # Janvier
    y9_Jan_typeNfertivar = ttk.Combobox(frame9, values=typeNferti,
                                        width=10)
    y9_Jan_typeNfertivar.set("*None")
    y9_Jan_typeNfertivar.place(relx=0.04, rely=0.14)
    # Février
    y9_Feb_typeNfertivar = ttk.Combobox(frame9, values=typeNferti,
                                        width=10)
    y9_Feb_typeNfertivar.set("*None")
    y9_Feb_typeNfertivar.place(relx=0.12, rely=0.14)
    # Mars
    y9_Mar_typeNfertivar = ttk.Combobox(frame9, values=typeNferti,
                                        width=10)
    y9_Mar_typeNfertivar.set("*None")
    y9_Mar_typeNfertivar.place(relx=0.2, rely=0.14)
    # Avril
    y9_Apr_typeNfertivar = ttk.Combobox(frame9, values=typeNferti,
                                        width=10)
    y9_Apr_typeNfertivar.set("*None")
    y9_Apr_typeNfertivar.place(relx=0.28, rely=0.14)
    # May
    y9_Maymonth_typeNfertivar = ttk.Combobox(frame9, values=typeNferti,
                                             width=10)
    y9_Maymonth_typeNfertivar.set("*None")
    y9_Maymonth_typeNfertivar.place(relx=0.36, rely=0.14)
    # Juin
    y9_Jun_typeNfertivar = ttk.Combobox(frame9, values=typeNferti,
                                        width=10)
    y9_Jun_typeNfertivar.set("*None")
    y9_Jun_typeNfertivar.place(relx=0.44, rely=0.14)
    # July
    y9_Jul_typeNfertivar = ttk.Combobox(frame9, values=typeNferti,
                                        width=10)
    y9_Jul_typeNfertivar.set("*None")
    y9_Jul_typeNfertivar.place(relx=0.52, rely=0.14)
    # Aout
    y9_Aug_typeNfertivar = ttk.Combobox(frame9, values=typeNferti,
                                        width=10)
    y9_Aug_typeNfertivar.set("*None")
    y9_Aug_typeNfertivar.place(relx=0.6, rely=0.14)
    # Septembre
    y9_Sep_typeNfertivar = ttk.Combobox(frame9, values=typeNferti,
                                        width=10)
    y9_Sep_typeNfertivar.set("*None")
    y9_Sep_typeNfertivar.place(relx=0.68, rely=0.14)
    # Octobre
    y9_Oct_typeNfertivar = ttk.Combobox(frame9, values=typeNferti,
                                        width=10)
    y9_Oct_typeNfertivar.set("*None")
    y9_Oct_typeNfertivar.place(relx=0.76, rely=0.14)
    # Novembre
    y9_Nov_typeNfertivar = ttk.Combobox(frame9, values=typeNferti,
                                        width=10)
    y9_Nov_typeNfertivar.set("*None")
    y9_Nov_typeNfertivar.place(relx=0.84, rely=0.14)
    # Décembre
    y9_Dec_typeNfertivar = ttk.Combobox(frame9, values=typeNferti,
                                        width=10)
    y9_Dec_typeNfertivar.set("*None")
    y9_Dec_typeNfertivar.place(relx=0.92, rely=0.14)

    # Fonction pour récupérer toutes les valeurs des mois pour rate N ferti
    def get_all_month_valuesrateNfertiy9():
        month_valuesrateNfertiy9 = [
            y1_Jan(y9_Jan_rateNfertivar),
            y1_Feb(y9_Feb_rateNfertivar),
            y1_Mar(y9_Mar_rateNfertivar),
            y1_Apr(y9_Apr_rateNfertivar),
            y1_Maymonth(y9_Maymonth_rateNfertivar),
            y1_Jun(y9_Jun_rateNfertivar),
            y1_Jul(y9_Jul_rateNfertivar),
            y1_Aug(y9_Aug_rateNfertivar),
            y1_Sep(y9_Sep_rateNfertivar),
            y1_Oct(y9_Oct_rateNfertivar),
            y1_Nov(y9_Nov_rateNfertivar),
            y1_Dec(y9_Dec_rateNfertivar)
        ]
        return month_valuesrateNfertiy9

    # Créer une variable Tkinter pour stocker l'élément sélectionné NfertiRate
    # Création combobox
    # Janvier
    y9_Jan_rateNfertivar = tkinter.Entry(frame9,
                                         width=13,
                                         justify="right")
    y9_Jan_rateNfertivar.insert(tkinter.END, "0")
    y9_Jan_rateNfertivar.place(relx=0.04, rely=0.22)
    # Février
    y9_Feb_rateNfertivar = tkinter.Entry(frame9,
                                         width=13,
                                         justify="right")
    y9_Feb_rateNfertivar.insert(tkinter.END, "0")
    y9_Feb_rateNfertivar.place(relx=0.12, rely=0.22)
    # Mars
    y9_Mar_rateNfertivar = tkinter.Entry(frame9,
                                         width=13,
                                         justify="right")
    y9_Mar_rateNfertivar.insert(tkinter.END, "0")
    y9_Mar_rateNfertivar.place(relx=0.2, rely=0.22)
    # Avril
    y9_Apr_rateNfertivar = tkinter.Entry(frame9,
                                         width=13,
                                         justify="right")
    y9_Apr_rateNfertivar.insert(tkinter.END, "0")
    y9_Apr_rateNfertivar.place(relx=0.28, rely=0.22)
    # May
    y9_Maymonth_rateNfertivar = tkinter.Entry(frame9,
                                              width=13,
                                              justify="right")
    y9_Maymonth_rateNfertivar.insert(tkinter.END, "0")
    y9_Maymonth_rateNfertivar.place(relx=0.36, rely=0.22)
    # Juin
    y9_Jun_rateNfertivar = tkinter.Entry(frame9,
                                         width=13,
                                         justify="right")
    y9_Jun_rateNfertivar.insert(tkinter.END, "0")
    y9_Jun_rateNfertivar.place(relx=0.44, rely=0.22)
    # July
    y9_Jul_rateNfertivar = tkinter.Entry(frame9,
                                         width=13,
                                         justify="right")
    y9_Jul_rateNfertivar.insert(tkinter.END, "0")
    y9_Jul_rateNfertivar.place(relx=0.52, rely=0.22)
    # Aout
    y9_Aug_rateNfertivar = tkinter.Entry(frame9,
                                         width=13,
                                         justify="right")
    y9_Aug_rateNfertivar.insert(tkinter.END, "0")
    y9_Aug_rateNfertivar.place(relx=0.6, rely=0.22)
    # Septembre
    y9_Sep_rateNfertivar = tkinter.Entry(frame9,
                                         width=13,
                                         justify="right")
    y9_Sep_rateNfertivar.insert(tkinter.END, "0")
    y9_Sep_rateNfertivar.place(relx=0.68, rely=0.22)
    # Octobre
    y9_Oct_rateNfertivar = tkinter.Entry(frame9,
                                         width=13,
                                         justify="right")
    y9_Oct_rateNfertivar.insert(tkinter.END, "0")
    y9_Oct_rateNfertivar.place(relx=0.76, rely=0.22)
    # Novembre
    y9_Nov_rateNfertivar = tkinter.Entry(frame9,
                                         width=13,
                                         justify="right")
    y9_Nov_rateNfertivar.insert(tkinter.END, "0")
    y9_Nov_rateNfertivar.place(relx=0.84, rely=0.22)
    # Décembre
    y9_Dec_rateNfertivar = tkinter.Entry(frame9,
                                         width=13,
                                         justify="right")
    y9_Dec_rateNfertivar.insert(tkinter.END, "0")
    y9_Dec_rateNfertivar.place(relx=0.92, rely=0.22)

    # Calcule du taux d'N en kg/ha en fonction de l'apport et du type ferti
    def calculate_kgN9():
        # Mise des return list dans des listes spécifiques
        listferti = printlist()
        y9rateferti_str = listferti[81]
        y9typeferti = listferti[80]
        # Création d'une liste vide convertissant les rate str en float
        y9rateferti_float = []
        # Création d'une liste pour les résultats des calcules
        resultlist = []
        # Vérification que chaque élément de cette liste puisse être convertie + conversion

        try:
            for i in y9rateferti_str:
                y9rateferti_float.append(float(i))
        except ValueError:
            print("Error! Please check you rate data. Some data are not float")

        # Calcule taux N en fonction type ferti
        for i in range(12):  # Pour janvier (0) et février (1)
            if y9typeferti[i] == "*None" and y9rateferti_float[i] == 0:
                resultlist.append(0)
            elif y9typeferti[i] == "Ammo Chlo" and y9rateferti_float[i] > 0:
                resammochlo = round(0.25 * y9rateferti_float[i], 1)
                resultlist.append(resammochlo)
            elif y9typeferti[i] == "Ammo Nit" and y9rateferti_float[i] > 0:
                resammonit = round(0.34 * y9rateferti_float[i], 1)
                resultlist.append(resammonit)
            elif y9typeferti[i] == "Ammo Sulf" and y9rateferti_float[i] > 0:
                resammosulf = round(0.21 * y9rateferti_float[i], 1)
                resultlist.append(resammosulf)
            elif y9typeferti[i] == "Sod Nit" and y9rateferti_float[i] > 0:
                ressodnit = round(0.16 * y9rateferti_float[i], 1)
                resultlist.append(ressodnit)
            elif y9typeferti[i] == "Urea" and y9rateferti_float[i] > 0:
                resurea = round(0.46 * y9rateferti_float[i], 1)
                resultlist.append(resurea)
            elif y9typeferti[i] == "*None" and y9rateferti_float[i] > 0:
                resultlist.append("Error!")
            elif y9typeferti[i] != "*None" and y9typeferti[i] != "Ammo Chlo" and y9typeferti[i] != "Ammo Nit" and \
                    y9typeferti[i] != "Ammo Sulf" and y9typeferti[i] != "Sod Nit" and y9typeferti[i] != "Urea":
                resultlist.append("Error!")
            else:
                resultlist.append("Error!")

        # Information résultats
        # Janvier
        equnitrogenjan = tkinter.Label(frame9,
                                       text=resultlist[0], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjan.place(relx=0.04, rely=0.28)
        # Fevrier
        equnitrogenfev = tkinter.Label(frame9,
                                       text=resultlist[1], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenfev.place(relx=0.12, rely=0.28)
        # Mars
        equnitrogenmar = tkinter.Label(frame9,
                                       text=resultlist[2], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenmar.place(relx=0.2, rely=0.28)
        # Avril
        equnitrogenapr = tkinter.Label(frame9,
                                       text=resultlist[3], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenapr.place(relx=0.28, rely=0.28)
        # Mai
        equnitrogenmay = tkinter.Label(frame9,
                                       text=resultlist[4], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenmay.place(relx=0.36, rely=0.28)
        # Juin
        equnitrogenjun = tkinter.Label(frame9,
                                       text=resultlist[5], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjun.place(relx=0.44, rely=0.28)
        # Juillet
        equnitrogenjul = tkinter.Label(frame9,
                                       text=resultlist[6], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjul.place(relx=0.52, rely=0.28)
        # Aout
        equnitrogenaug = tkinter.Label(frame9,
                                       text=resultlist[7], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenaug.place(relx=0.6, rely=0.28)
        # September
        equnitrogensep = tkinter.Label(frame9,
                                       text=resultlist[8], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogensep.place(relx=0.68, rely=0.28)
        # Octobre
        equnitrogenoct = tkinter.Label(frame9,
                                       text=resultlist[9], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenoct.place(relx=0.76, rely=0.28)
        # Novembre
        equnitrogennov = tkinter.Label(frame9,
                                       text=resultlist[10], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogennov.place(relx=0.84, rely=0.28)
        # Decembre
        equnitrogendec = tkinter.Label(frame9,
                                       text=resultlist[11], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogendec.place(relx=0.92, rely=0.28)

        # Calcule total annuelle
        yearcumul = 0
        resultlist_float = []
        try:
            for i in resultlist:
                resultlist_float.append(float(i))
        except ValueError:
            return
        for i in resultlist_float:
            if isinstance(i, float):
                yearcumul = round(i + yearcumul,1)
        # label cacule annuel
        Nfertianuel = tkinter.Label(frame9, text=f"Cumulative nitrogen for year: {yearcumul}")
        Nfertianuel.place(relx=0.04, rely=0.35)

    # Création bouton calcul équivalent azote N ferti
    button = tkinter.Button(frame9, text="Nitrogen equivalent (in kg/ha)",
                            width=100,
                            font=("Ariel", 10, "bold"), bg="lightblue",
                            command=lambda: [calculate_kgN9(), calculate_kgNorga9()])
    button.place(relx=0.2, rely=0.4)

    # Fonction pour récupérer toutes les infos placement
    def get_placement9():
        placementfertiy9 = [
            y1_Jan(y9_placementferti)]
        return placementfertiy9

    # Création combobox placement N ferti
    y9_placementferti = ttk.Combobox(frame9, values=Nfertiplacement,
                                     width=21)
    y9_placementferti.set("*Choice*")
    y9_placementferti.place(relx=0.06, rely=0.47)

    # Fonction pour récupérer toute la valeur de quantity organic
    def get_quantityorgafertiy9():
        quantityorgafertiy9list = [
            y1_Jan(y9_quantityorgavar)]
        return quantityorgafertiy9list

    # Création quantité fertilisation organique
    y9_quantityorgavar = tkinter.Entry(frame9,
                                       width=8,
                                       justify="right")
    y9_quantityorgavar.insert(tkinter.END, "0")
    y9_quantityorgavar.place(relx=0.1, rely=0.63)

    # Fonction pour récupérer la valeur de type organic
    def get_typeorgafertiy9():
        typeorgafertiy9list = [
            y1_Jan(y9_typeorgavar)]
        return typeorgafertiy9list

    # Création quantité fertilisation organique
    y9_typeorgavar = ttk.Combobox(frame9, values=Orgafertitype,
                                  width=10)
    y9_typeorgavar.set("*Choice*")
    y9_typeorgavar.place(relx=0.185, rely=0.63)

    # Calcule équivalent N ferti orga
    def calculate_kgNorga9():
        # Mise des return list dans des listes spécifiques
        listferti = printlist()
        y9_typefertiorga = listferti[84]
        y9_quantityfertiorga = listferti[83]
        # Création d'une liste vide permettant conversion liste en float
        y9_quantityfertiorga_float = []
        # Création liste pour valeurs
        Nfertiorga = []
        # Vérification que chaque élément de cette liste puisse être convertie + conversion
        try:
            for i in y9_quantityfertiorga:
                y9_quantityfertiorga_float.append(float(i))
        except ValueError:
            print("Error! Please check you rate data. Some data are not float")
            return
        # Calcule taux N en fonction type ferti orga si plusieurs valeurs
        for i in range(1):
            if y9_typefertiorga[i] == "*Choice*" and y9_quantityfertiorga_float[i] == 0:
                Nfertiorga.append(0)
            elif y9_typefertiorga[i] == "EFB" and y9_quantityfertiorga_float[i] > 0:
                # 0.90% N in DM * 0.36tDM/tFM (cf pg Pardon)
                Nfertiorgacal = round(3.24 * y9_quantityfertiorga_float[i], 1)
                Nfertiorga.append(Nfertiorgacal)
            elif y9_typefertiorga[i] == "Compost" and y9_quantityfertiorga_float[i] > 0:
                # 2.05% N in DM * 0.41tDM/tFM (cf pg Pardon)
                Nfertiorgacal = round(8.405 * y9_quantityfertiorga_float[i], 1)
                Nfertiorga.append(Nfertiorgacal)
            elif y9_typefertiorga[i] == "*Choice*" and y9_quantityfertiorga_float[i] > 0:
                Nfertiorga.append("Error!")
            elif y9_typefertiorga[i] != "*Choice*" and y9_typefertiorga[i] != "EFB" and y9_typefertiorga[
                i] != "Compost":
                Nfertiorga.append("Error!")
            else:
                Nfertiorga.append("Error!")

            # Information résultats
        equilabelnitroorgaferti = tkinter.Label(frame9,
                                                text="Nitrogen equivalent organic fertilization (in kgN/ha/yr) :")
        equilabelnitroorgaferti.place(relx=0.45, rely=0.63)
        equnitrogenorgaferti = tkinter.Label(frame9,
                                             text=Nfertiorga[0], font=("Ariel", 9, "bold"),
                                             bg="white", fg="blue", justify="right",
                                             width=10,
                                             relief="groove", borderwidth=5)
        equnitrogenorgaferti.place(relx=0.68, rely=0.63)

    # Fonction pour récupérer la valeur de placement organic
    def get_placementorgafertiy9():
        placementorgafertiy9list = [
            y1_Jan(y9_placementorgavar)]
        return placementorgafertiy9list

    # Création placement ferti organique
    y9_placementorgavar = ttk.Combobox(frame9, values=Orgafertiplacement,
                                       width=20)
    y9_placementorgavar.set("*Choice*")
    y9_placementorgavar.place(relx=0.31, rely=0.63)

    # Fonction pour récupérer la valeur de biomasse understorey
    def get_understoreybiomassy9():
        understoreybiomassy9list = [
            y1_Jan(y9_understoreybiomass)]
        return understoreybiomassy9list

    # Création biomasse understorey
    y9_understoreybiomass = ttk.Combobox(frame9, values=understoreybiomass,
                                         width=10)
    y9_understoreybiomass.set("*Choice*")
    y9_understoreybiomass.place(relx=0.05, rely=0.78)

    # Fonction pour récupérer la valeur de biomasse understorey
    def get_legumefractiony9():
        legumefractiony9list = [
            y1_Jan(y9_legumefraction)]
        return legumefractiony9list

    # Création legume fraction
    y9_legumefraction = ttk.Combobox(frame9, values=understoreylegumefraction,
                                     width=10)
    y9_legumefraction.set("*Choice*")
    y9_legumefraction.place(relx=0.24, rely=0.78)

    # Fonction pour récupérer la valeur pruned fronds
    def get_prunedy9():
        prunedy9list = [
            y1_Jan(y9_pruned)]
        return prunedy9list

    # Création combobox pruned fronds
    y9_pruned = ttk.Combobox(frame9, values=Prunedfronds,
                             width=20)
    y9_pruned.set("*Choice*")
    y9_pruned.place(relx=0.07, rely=0.92)

    # Fonction pour récupérer toute la valeur Natmo
    def get_Natmodepoy9():
        Natmoy9list = [
            y1_Jan(y9_Natmodepo)]
        return Natmoy9list

    # Création quantité Natmo
    y9_Natmodepo = tkinter.Entry(frame9,
                                 width=8,
                                 justify="right")
    y9_Natmodepo.insert(tkinter.END, "18")
    y9_Natmodepo.place(relx=0.66, rely=0.84)

    ################################################################################################################
    ###################################Year 10#######################################################################
    ################################################################################################################
    # Intégration de Second year dans la fenêtre
    year10 = (tkinter.Label(main_frame,
                           text="Tenth year", font=("Ariel", 20, 'underline')))
    year10.pack(anchor="w", pady=5)

    # Intégration du bloc data pour chaque type
    # Création encadré
    frame10 = tkinter.Frame(main_frame, bd=2, relief="solid", width=1450, height=400, padx=5, pady=2)
    frame10.pack(anchor="w", padx=15, pady=5, fill="none")

    # Mise de titre Mineral N ferti
    y10_MineralNfertilizer = (tkinter.Label(frame10,
                                           text="Mineral Nitrogen fertilizer", justify="center",
                                           font=("Ariel", 13, "bold", "underline")))
    y10_MineralNfertilizer.place(relx=0.01)

    # Mise de titre organic fertilizer
    y10_Organicfertilizer = (tkinter.Label(frame10,
                                          text="Organic fertilizer", justify="center",
                                          font=("Ariel", 13, "bold", "underline")))
    y10_Organicfertilizer.place(relx=0.01, rely=0.55)

    # Mise de titre understorey
    y10_Understorey = (tkinter.Label(frame10,
                                    text="Understorey", justify="center",
                                    font=("Ariel", 13, "bold", "underline")))
    y10_Understorey.place(relx=0.01, rely=0.7)

    # Mise de titre Pruned fronds
    y10_Prunedfronds = (tkinter.Label(frame10,
                                     text="Pruned fronds", justify="center",
                                     font=("Ariel", 13, "bold", "underline")))
    y10_Prunedfronds.place(relx=0.01, rely=0.85)

    # Mise titre atmospheric depositions
    y10_atmodepo = (tkinter.Label(frame10,
                                 text="Atmospheric depositions", justify="center",
                                 font=("Ariel", 13, "bold", "underline")))
    y10_atmodepo.place(relx=0.55, rely=0.75)

    # Intégration des mois
    y10_January = (tkinter.Label(frame10, text="January", font=("Ariel", 9), fg="blue"))
    y10_January.place(relx=0.06, rely=0.08)
    y10_February = (tkinter.Label(frame10, text="February", font=("Ariel", 9), fg="blue"))
    y10_February.place(relx=0.14, rely=0.08)
    y10_March = (tkinter.Label(frame10, text="March", font=("Ariel", 9), fg="blue"))
    y10_March.place(relx=0.22, rely=0.08)
    y10_April = (tkinter.Label(frame10, text="April", font=("Ariel", 9), fg="blue"))
    y10_April.place(relx=0.295, rely=0.08)
    y10_May = (tkinter.Label(frame10, text="May", font=("Ariel", 9), fg="blue"))
    y10_May.place(relx=0.377, rely=0.08)
    y10_June = (tkinter.Label(frame10, text="June", font=("Ariel", 9), fg="blue"))
    y10_June.place(relx=0.46, rely=0.08)
    y10_July = (tkinter.Label(frame10, text="July", font=("Ariel", 9), fg="blue"))
    y10_July.place(relx=0.54, rely=0.08)
    y10_August = (tkinter.Label(frame10, text="August", font=("Ariel", 9), fg="blue"))
    y10_August.place(relx=0.62, rely=0.08)
    y10_September = (tkinter.Label(frame10, text="September", font=("Ariel", 9), fg="blue"))
    y10_September.place(relx=0.69, rely=0.08)
    y10_October = (tkinter.Label(frame10, text="October", font=("Ariel", 9), fg="blue"))
    y10_October.place(relx=0.78, rely=0.08)
    y10_November = (tkinter.Label(frame10, text="November", font=("Ariel", 9), fg="blue"))
    y10_November.place(relx=0.85, rely=0.08)
    y10_December = (tkinter.Label(frame10, text="December", font=("Ariel", 9), fg="blue"))
    y10_December.place(relx=0.93, rely=0.08)

    # Création du type
    y10_type = (tkinter.Label(frame10, text="Type", fg="blue", font=("Ariel", 11, "bold")))
    y10_type.place(relx=0, rely=0.14)

    # Création data rate
    y10_rate = (tkinter.Label(frame10, text="Rate \n(kg/ha)", fg="blue", font=("Ariel", 11, "bold")))
    y10_rate.place(relx=0, rely=0.21)

    # Création placement
    y10_placementferti = (tkinter.Label(frame10, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y10_placementferti.place(relx=0, rely=0.47)

    # Création quantity ferti orga
    y10_quantityorga = (tkinter.Label(frame10, text="Quantity (in tFM)", fg="blue", font=("Ariel", 11, "bold")))
    y10_quantityorga.place(relx=0, rely=0.63)

    # Création type ferti orga
    y10_typeorga = (tkinter.Label(frame10, text="Type", fg="blue", font=("Ariel", 11, "bold")))
    y10_typeorga.place(relx=0.15, rely=0.63)

    # Création placement ferti orga
    y10_placementorga = (tkinter.Label(frame10, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y10_placementorga.place(relx=0.25, rely=0.63)

    # Création biomasse understorey
    y10_biomass = (tkinter.Label(frame10, text="Biomass", fg="blue", font=("Ariel", 11, "bold")))
    y10_biomass.place(relx=0, rely=0.78)

    # Création legume fraction
    y10_legumefrac = (tkinter.Label(frame10, text="Legume fraction", fg="blue", font=("Ariel", 11, "bold")))
    y10_legumefrac.place(relx=0.15, rely=0.78)

    # Création pruned fronts placement
    y10_prunedfr = (tkinter.Label(frame10, text="Placement", fg="blue", font=("Ariel", 11, "bold")))
    y10_prunedfr.place(relx=0, rely=0.92)

    # Création atmospheric depositions
    y10_quantityNatmo = (
        tkinter.Label(frame10, text="Quantity of nitrogen\n (in kg/ha/yr)", fg="blue", font=("Ariel", 11, "bold")))
    y10_quantityNatmo.place(relx=0.55, rely=0.82)

    # Fonction pour récupérer toutes les valeurs des mois pour Type N ferti
    def get_all_month_valuestypeNfertiy10():
        month_valuestypeNfertiy10 = [
            y1_Jan(y10_Jan_typeNfertivar),
            y1_Feb(y10_Feb_typeNfertivar),
            y1_Mar(y10_Mar_typeNfertivar),
            y1_Apr(y10_Apr_typeNfertivar),
            y1_Maymonth(y10_Maymonth_typeNfertivar),
            y1_Jun(y10_Jun_typeNfertivar),
            y1_Jul(y10_Jul_typeNfertivar),
            y1_Aug(y10_Aug_typeNfertivar),
            y1_Sep(y10_Sep_typeNfertivar),
            y1_Oct(y10_Oct_typeNfertivar),
            y1_Nov(y10_Nov_typeNfertivar),
            y1_Dec(y10_Dec_typeNfertivar)
        ]

        return month_valuestypeNfertiy10

    # Créer une variable Tkinter pour stocker l'élément sélectionné Nfertitype
    # Création combobox
    # Janvier
    y10_Jan_typeNfertivar = ttk.Combobox(frame10, values=typeNferti,
                                        width=10)
    y10_Jan_typeNfertivar.set("*None")
    y10_Jan_typeNfertivar.place(relx=0.04, rely=0.14)
    # Février
    y10_Feb_typeNfertivar = ttk.Combobox(frame10, values=typeNferti,
                                        width=10)
    y10_Feb_typeNfertivar.set("*None")
    y10_Feb_typeNfertivar.place(relx=0.12, rely=0.14)
    # Mars
    y10_Mar_typeNfertivar = ttk.Combobox(frame10, values=typeNferti,
                                        width=10)
    y10_Mar_typeNfertivar.set("*None")
    y10_Mar_typeNfertivar.place(relx=0.2, rely=0.14)
    # Avril
    y10_Apr_typeNfertivar = ttk.Combobox(frame10, values=typeNferti,
                                        width=10)
    y10_Apr_typeNfertivar.set("*None")
    y10_Apr_typeNfertivar.place(relx=0.28, rely=0.14)
    # May
    y10_Maymonth_typeNfertivar = ttk.Combobox(frame10, values=typeNferti,
                                             width=10)
    y10_Maymonth_typeNfertivar.set("*None")
    y10_Maymonth_typeNfertivar.place(relx=0.36, rely=0.14)
    # Juin
    y10_Jun_typeNfertivar = ttk.Combobox(frame10, values=typeNferti,
                                        width=10)
    y10_Jun_typeNfertivar.set("*None")
    y10_Jun_typeNfertivar.place(relx=0.44, rely=0.14)
    # July
    y10_Jul_typeNfertivar = ttk.Combobox(frame10, values=typeNferti,
                                        width=10)
    y10_Jul_typeNfertivar.set("*None")
    y10_Jul_typeNfertivar.place(relx=0.52, rely=0.14)
    # Aout
    y10_Aug_typeNfertivar = ttk.Combobox(frame10, values=typeNferti,
                                        width=10)
    y10_Aug_typeNfertivar.set("*None")
    y10_Aug_typeNfertivar.place(relx=0.6, rely=0.14)
    # Septembre
    y10_Sep_typeNfertivar = ttk.Combobox(frame10, values=typeNferti,
                                        width=10)
    y10_Sep_typeNfertivar.set("*None")
    y10_Sep_typeNfertivar.place(relx=0.68, rely=0.14)
    # Octobre
    y10_Oct_typeNfertivar = ttk.Combobox(frame10, values=typeNferti,
                                        width=10)
    y10_Oct_typeNfertivar.set("*None")
    y10_Oct_typeNfertivar.place(relx=0.76, rely=0.14)
    # Novembre
    y10_Nov_typeNfertivar = ttk.Combobox(frame10, values=typeNferti,
                                        width=10)
    y10_Nov_typeNfertivar.set("*None")
    y10_Nov_typeNfertivar.place(relx=0.84, rely=0.14)
    # Décembre
    y10_Dec_typeNfertivar = ttk.Combobox(frame10, values=typeNferti,
                                        width=10)
    y10_Dec_typeNfertivar.set("*None")
    y10_Dec_typeNfertivar.place(relx=0.92, rely=0.14)

    # Fonction pour récupérer toutes les valeurs des mois pour rate N ferti
    def get_all_month_valuesrateNfertiy10():
        month_valuesrateNfertiy10 = [
            y1_Jan(y10_Jan_rateNfertivar),
            y1_Feb(y10_Feb_rateNfertivar),
            y1_Mar(y10_Mar_rateNfertivar),
            y1_Apr(y10_Apr_rateNfertivar),
            y1_Maymonth(y10_Maymonth_rateNfertivar),
            y1_Jun(y10_Jun_rateNfertivar),
            y1_Jul(y10_Jul_rateNfertivar),
            y1_Aug(y10_Aug_rateNfertivar),
            y1_Sep(y10_Sep_rateNfertivar),
            y1_Oct(y10_Oct_rateNfertivar),
            y1_Nov(y10_Nov_rateNfertivar),
            y1_Dec(y10_Dec_rateNfertivar)
        ]
        return month_valuesrateNfertiy10

    # Créer une variable Tkinter pour stocker l'élément sélectionné NfertiRate
    # Création combobox
    # Janvier
    y10_Jan_rateNfertivar = tkinter.Entry(frame10,
                                         width=13,
                                         justify="right")
    y10_Jan_rateNfertivar.insert(tkinter.END, "0")
    y10_Jan_rateNfertivar.place(relx=0.04, rely=0.22)
    # Février
    y10_Feb_rateNfertivar = tkinter.Entry(frame10,
                                         width=13,
                                         justify="right")
    y10_Feb_rateNfertivar.insert(tkinter.END, "0")
    y10_Feb_rateNfertivar.place(relx=0.12, rely=0.22)
    # Mars
    y10_Mar_rateNfertivar = tkinter.Entry(frame10,
                                         width=13,
                                         justify="right")
    y10_Mar_rateNfertivar.insert(tkinter.END, "0")
    y10_Mar_rateNfertivar.place(relx=0.2, rely=0.22)
    # Avril
    y10_Apr_rateNfertivar = tkinter.Entry(frame10,
                                         width=13,
                                         justify="right")
    y10_Apr_rateNfertivar.insert(tkinter.END, "0")
    y10_Apr_rateNfertivar.place(relx=0.28, rely=0.22)
    # May
    y10_Maymonth_rateNfertivar = tkinter.Entry(frame10,
                                              width=13,
                                              justify="right")
    y10_Maymonth_rateNfertivar.insert(tkinter.END, "0")
    y10_Maymonth_rateNfertivar.place(relx=0.36, rely=0.22)
    # Juin
    y10_Jun_rateNfertivar = tkinter.Entry(frame10,
                                         width=13,
                                         justify="right")
    y10_Jun_rateNfertivar.insert(tkinter.END, "0")
    y10_Jun_rateNfertivar.place(relx=0.44, rely=0.22)
    # July
    y10_Jul_rateNfertivar = tkinter.Entry(frame10,
                                         width=13,
                                         justify="right")
    y10_Jul_rateNfertivar.insert(tkinter.END, "0")
    y10_Jul_rateNfertivar.place(relx=0.52, rely=0.22)
    # Aout
    y10_Aug_rateNfertivar = tkinter.Entry(frame10,
                                         width=13,
                                         justify="right")
    y10_Aug_rateNfertivar.insert(tkinter.END, "0")
    y10_Aug_rateNfertivar.place(relx=0.6, rely=0.22)
    # Septembre
    y10_Sep_rateNfertivar = tkinter.Entry(frame10,
                                         width=13,
                                         justify="right")
    y10_Sep_rateNfertivar.insert(tkinter.END, "0")
    y10_Sep_rateNfertivar.place(relx=0.68, rely=0.22)
    # Octobre
    y10_Oct_rateNfertivar = tkinter.Entry(frame10,
                                         width=13,
                                         justify="right")
    y10_Oct_rateNfertivar.insert(tkinter.END, "0")
    y10_Oct_rateNfertivar.place(relx=0.76, rely=0.22)
    # Novembre
    y10_Nov_rateNfertivar = tkinter.Entry(frame10,
                                         width=13,
                                         justify="right")
    y10_Nov_rateNfertivar.insert(tkinter.END, "0")
    y10_Nov_rateNfertivar.place(relx=0.84, rely=0.22)
    # Décembre
    y10_Dec_rateNfertivar = tkinter.Entry(frame10,
                                         width=13,
                                         justify="right")
    y10_Dec_rateNfertivar.insert(tkinter.END, "0")
    y10_Dec_rateNfertivar.place(relx=0.92, rely=0.22)

    # Calcule du taux d'N en kg/ha en fonction de l'apport et du type ferti
    def calculate_kgN10():
        # Mise des return list dans des listes spécifiques
        listferti = printlist()
        y10rateferti_str = listferti[91]
        y10typeferti = listferti[90]
        # Création d'une liste vide convertissant les rate str en float
        y10rateferti_float = []
        # Création d'une liste pour les résultats des calcules
        resultlist = []
        # Vérification que chaque élément de cette liste puisse être convertie + conversion

        try:
            for i in y10rateferti_str:
                y10rateferti_float.append(float(i))
        except ValueError:
            print("Error! Please check you rate data. Some data are not float")

        # Calcule taux N en fonction type ferti
        for i in range(12):  # Pour janvier (0) et février (1)
            if y10typeferti[i] == "*None" and y10rateferti_float[i] == 0:
                resultlist.append(0)
            elif y10typeferti[i] == "Ammo Chlo" and y10rateferti_float[i] > 0:
                resammochlo = round(0.25 * y10rateferti_float[i], 1)
                resultlist.append(resammochlo)
            elif y10typeferti[i] == "Ammo Nit" and y10rateferti_float[i] > 0:
                resammonit = round(0.34 * y10rateferti_float[i], 1)
                resultlist.append(resammonit)
            elif y10typeferti[i] == "Ammo Sulf" and y10rateferti_float[i] > 0:
                resammosulf = round(0.21 * y10rateferti_float[i], 1)
                resultlist.append(resammosulf)
            elif y10typeferti[i] == "Sod Nit" and y10rateferti_float[i] > 0:
                ressodnit = round(0.16 * y10rateferti_float[i], 1)
                resultlist.append(ressodnit)
            elif y10typeferti[i] == "Urea" and y10rateferti_float[i] > 0:
                resurea = round(0.46 * y10rateferti_float[i], 1)
                resultlist.append(resurea)
            elif y10typeferti[i] == "*None" and y10rateferti_float[i] > 0:
                resultlist.append("Error!")
            elif y10typeferti[i] != "*None" and y10typeferti[i] != "Ammo Chlo" and y10typeferti[i] != "Ammo Nit" and \
                    y10typeferti[i] != "Ammo Sulf" and y10typeferti[i] != "Sod Nit" and y10typeferti[i] != "Urea":
                resultlist.append("Error!")
            else:
                resultlist.append("Error!")

        # Information résultats
        # Janvier
        equnitrogenjan = tkinter.Label(frame10,
                                       text=resultlist[0], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjan.place(relx=0.04, rely=0.28)
        # Fevrier
        equnitrogenfev = tkinter.Label(frame10,
                                       text=resultlist[1], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenfev.place(relx=0.12, rely=0.28)
        # Mars
        equnitrogenmar = tkinter.Label(frame10,
                                       text=resultlist[2], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenmar.place(relx=0.2, rely=0.28)
        # Avril
        equnitrogenapr = tkinter.Label(frame10,
                                       text=resultlist[3], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenapr.place(relx=0.28, rely=0.28)
        # Mai
        equnitrogenmay = tkinter.Label(frame10,
                                       text=resultlist[4], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenmay.place(relx=0.36, rely=0.28)
        # Juin
        equnitrogenjun = tkinter.Label(frame10,
                                       text=resultlist[5], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjun.place(relx=0.44, rely=0.28)
        # Juillet
        equnitrogenjul = tkinter.Label(frame10,
                                       text=resultlist[6], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenjul.place(relx=0.52, rely=0.28)
        # Aout
        equnitrogenaug = tkinter.Label(frame10,
                                       text=resultlist[7], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenaug.place(relx=0.6, rely=0.28)
        # September
        equnitrogensep = tkinter.Label(frame10,
                                       text=resultlist[8], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogensep.place(relx=0.68, rely=0.28)
        # Octobre
        equnitrogenoct = tkinter.Label(frame10,
                                       text=resultlist[9], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogenoct.place(relx=0.76, rely=0.28)
        # Novembre
        equnitrogennov = tkinter.Label(frame10,
                                       text=resultlist[10], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogennov.place(relx=0.84, rely=0.28)
        # Decembre
        equnitrogendec = tkinter.Label(frame10,
                                       text=resultlist[11], font=("Ariel", 9, "bold"),
                                       bg="white", fg="blue", justify="right",
                                       width=10,
                                       relief="groove", borderwidth=5)
        equnitrogendec.place(relx=0.92, rely=0.28)

        # Calcule total annuelle
        yearcumul = 0
        resultlist_float = []
        try:
            for i in resultlist:
                resultlist_float.append(float(i))
        except ValueError:
            return
        for i in resultlist_float:
            if isinstance(i, float):
                yearcumul = round(i + yearcumul,1)
        # label cacule annuel
        Nfertianuel = tkinter.Label(frame10, text=f"Cumulative nitrogen for year: {yearcumul}")
        Nfertianuel.place(relx=0.04, rely=0.35)

    # Création bouton calcul équivalent azote N ferti
    button = tkinter.Button(frame10, text="Nitrogen equivalent (in kg/ha)",
                            width=100,
                            font=("Ariel", 10, "bold"), bg="lightblue",
                            command=lambda: [calculate_kgN10(), calculate_kgNorga10()])
    button.place(relx=0.2, rely=0.4)

    # Fonction pour récupérer toutes les infos placement
    def get_placement10():
        placementfertiy10 = [
            y1_Jan(y10_placementferti)]
        return placementfertiy10

    # Création combobox placement N ferti
    y10_placementferti = ttk.Combobox(frame10, values=Nfertiplacement,
                                     width=21)
    y10_placementferti.set("*Choice*")
    y10_placementferti.place(relx=0.06, rely=0.47)

    # Fonction pour récupérer toute la valeur de quantity organic
    def get_quantityorgafertiy10():
        quantityorgafertiy10list = [
            y1_Jan(y10_quantityorgavar)]
        return quantityorgafertiy10list

    # Création quantité fertilisation organique
    y10_quantityorgavar = tkinter.Entry(frame10,
                                       width=8,
                                       justify="right")
    y10_quantityorgavar.insert(tkinter.END, "0")
    y10_quantityorgavar.place(relx=0.1, rely=0.63)

    # Fonction pour récupérer la valeur de type organic
    def get_typeorgafertiy10():
        typeorgafertiy10list = [
            y1_Jan(y10_typeorgavar)]
        return typeorgafertiy10list

    # Création quantité fertilisation organique
    y10_typeorgavar = ttk.Combobox(frame10, values=Orgafertitype,
                                  width=10)
    y10_typeorgavar.set("*Choice*")
    y10_typeorgavar.place(relx=0.185, rely=0.63)

    # Calcule équivalent N ferti orga
    def calculate_kgNorga10():
        # Mise des return list dans des listes spécifiques
        listferti = printlist()
        y10_typefertiorga = listferti[94]
        y10_quantityfertiorga = listferti[93]
        # Création d'une liste vide permettant conversion liste en float
        y10_quantityfertiorga_float = []
        # Création liste pour valeurs
        Nfertiorga = []
        # Vérification que chaque élément de cette liste puisse être convertie + conversion
        try:
            for i in y10_quantityfertiorga:
                y10_quantityfertiorga_float.append(float(i))
        except ValueError:
            print("Error! Please check you rate data. Some data are not float")
            return
        # Calcule taux N en fonction type ferti orga si plusieurs valeurs
        for i in range(1):
            if y10_typefertiorga[i] == "*Choice*" and y10_quantityfertiorga_float[i] == 0:
                Nfertiorga.append(0)
            elif y10_typefertiorga[i] == "EFB" and y10_quantityfertiorga_float[i] > 0:
                # 0.90% N in DM * 0.36tDM/tFM (cf pg Pardon)
                Nfertiorgacal = round(3.24 * y10_quantityfertiorga_float[i], 1)
                Nfertiorga.append(Nfertiorgacal)
            elif y10_typefertiorga[i] == "Compost" and y10_quantityfertiorga_float[i] > 0:
                # 2.05% N in DM * 0.41tDM/tFM (cf pg Pardon)
                Nfertiorgacal = round(8.405 * y10_quantityfertiorga_float[i], 1)
                Nfertiorga.append(Nfertiorgacal)
            elif y10_typefertiorga[i] == "*Choice*" and y10_quantityfertiorga_float[i] > 0:
                Nfertiorga.append("Error!")
            elif y10_typefertiorga[i] != "*Choice*" and y10_typefertiorga[i] != "EFB" and y10_typefertiorga[
                i] != "Compost":
                Nfertiorga.append("Error!")
            else:
                Nfertiorga.append("Error!")

            # Information résultats
        equilabelnitroorgaferti = tkinter.Label(frame10,
                                                text="Nitrogen equivalent organic fertilization (in kgN/ha/yr) :")
        equilabelnitroorgaferti.place(relx=0.45, rely=0.63)
        equnitrogenorgaferti = tkinter.Label(frame10,
                                             text=Nfertiorga[0], font=("Ariel", 9, "bold"),
                                             bg="white", fg="blue", justify="right",
                                             width=10,
                                             relief="groove", borderwidth=5)
        equnitrogenorgaferti.place(relx=0.68, rely=0.63)

    # Fonction pour récupérer la valeur de placement organic
    def get_placementorgafertiy10():
        placementorgafertiy10list = [
            y1_Jan(y10_placementorgavar)]
        return placementorgafertiy10list

    # Création placement ferti organique
    y10_placementorgavar = ttk.Combobox(frame10, values=Orgafertiplacement,
                                       width=20)
    y10_placementorgavar.set("*Choice*")
    y10_placementorgavar.place(relx=0.31, rely=0.63)

    # Fonction pour récupérer la valeur de biomasse understorey
    def get_understoreybiomassy10():
        understoreybiomassy10list = [
            y1_Jan(y10_understoreybiomass)]
        return understoreybiomassy10list

    # Création biomasse understorey
    y10_understoreybiomass = ttk.Combobox(frame10, values=understoreybiomass,
                                         width=10)
    y10_understoreybiomass.set("*Choice*")
    y10_understoreybiomass.place(relx=0.05, rely=0.78)

    # Fonction pour récupérer la valeur de biomasse understorey
    def get_legumefractiony10():
        legumefractiony10list = [
            y1_Jan(y10_legumefraction)]
        return legumefractiony10list

    # Création legume fraction
    y10_legumefraction = ttk.Combobox(frame10, values=understoreylegumefraction,
                                     width=10)
    y10_legumefraction.set("*Choice*")
    y10_legumefraction.place(relx=0.24, rely=0.78)

    # Fonction pour récupérer la valeur pruned fronds
    def get_prunedy10():
        prunedy10list = [
            y1_Jan(y10_pruned)]
        return prunedy10list

    # Création combobox pruned fronds
    y10_pruned = ttk.Combobox(frame10, values=Prunedfronds,
                             width=20)
    y10_pruned.set("*Choice*")
    y10_pruned.place(relx=0.07, rely=0.92)

    # Fonction pour récupérer toute la valeur Natmo
    def get_Natmodepoy10():
        Natmoy10list = [
            y1_Jan(y10_Natmodepo)]
        return Natmoy10list

    # Création quantité Natmo
    y10_Natmodepo = tkinter.Entry(frame10,
                                 width=8,
                                 justify="right")
    y10_Natmodepo.insert(tkinter.END, "18")
    y10_Natmodepo.place(relx=0.66, rely=0.84)

    def printlist():
        organic_carbon=get_orgaC()
        texture_soil=get_Texturesoil()
        slope_info=get_slope()
        Land_Terraces=get_Terraces()
        Previous_palm=get_Prevpalm()
        y1Nfertitype = get_all_month_valuestypeNfertiy1()
        y1Nfertirate=get_all_month_valuesrateNfertiy1()
        y1placement=get_placement1()
        y1_quantityfertiorga=get_quantityorgafertiy1()
        y1_typefertiorga = get_typeorgafertiy1()
        y1_placementfertiorga = get_placementorgafertiy1()
        y1biomasseunderstorey=get_understoreybiomassy1()
        y1legumefractionunderstorey=get_legumefractiony1()
        y1prunedfronds=get_prunedy1()
        y1atmodepo = get_Natmodepoy1()
        y2Nfertitype = get_all_month_valuestypeNfertiy2()
        y2Nfertirate = get_all_month_valuesrateNfertiy2()
        y2placement = get_placement2()
        y2_quantityfertiorga = get_quantityorgafertiy2()
        y2_typefertiorga = get_typeorgafertiy2()
        y2_placementfertiorga = get_placementorgafertiy2()
        y2biomasseunderstorey = get_understoreybiomassy2()
        y2legumefractionunderstorey = get_legumefractiony2()
        y2prunedfronds = get_prunedy2()
        y2atmodepo = get_Natmodepoy2()
        y3Nfertitype = get_all_month_valuestypeNfertiy3()
        y3Nfertirate = get_all_month_valuesrateNfertiy3()
        y3placement = get_placement3()
        y3_quantityfertiorga = get_quantityorgafertiy3()
        y3_typefertiorga = get_typeorgafertiy3()
        y3_placementfertiorga = get_placementorgafertiy3()
        y3biomasseunderstorey = get_understoreybiomassy3()
        y3legumefractionunderstorey = get_legumefractiony3()
        y3prunedfronds = get_prunedy3()
        y3atmodepo = get_Natmodepoy3()
        y4Nfertitype = get_all_month_valuestypeNfertiy4()
        y4Nfertirate = get_all_month_valuesrateNfertiy4()
        y4placement = get_placement4()
        y4_quantityfertiorga = get_quantityorgafertiy4()
        y4_typefertiorga = get_typeorgafertiy4()
        y4_placementfertiorga = get_placementorgafertiy4()
        y4biomasseunderstorey = get_understoreybiomassy4()
        y4legumefractionunderstorey = get_legumefractiony4()
        y4prunedfronds = get_prunedy4()
        y4atmodepo = get_Natmodepoy4()
        y5Nfertitype = get_all_month_valuestypeNfertiy5()
        y5Nfertirate = get_all_month_valuesrateNfertiy5()
        y5placement = get_placement5()
        y5_quantityfertiorga = get_quantityorgafertiy5()
        y5_typefertiorga = get_typeorgafertiy5()
        y5_placementfertiorga = get_placementorgafertiy5()
        y5biomasseunderstorey = get_understoreybiomassy5()
        y5legumefractionunderstorey = get_legumefractiony5()
        y5prunedfronds = get_prunedy5()
        y5atmodepo = get_Natmodepoy5()
        y6Nfertitype = get_all_month_valuestypeNfertiy6()
        y6Nfertirate = get_all_month_valuesrateNfertiy6()
        y6placement = get_placement6()
        y6_quantityfertiorga = get_quantityorgafertiy6()
        y6_typefertiorga = get_typeorgafertiy6()
        y6_placementfertiorga = get_placementorgafertiy6()
        y6biomasseunderstorey = get_understoreybiomassy6()
        y6legumefractionunderstorey = get_legumefractiony6()
        y6prunedfronds = get_prunedy6()
        y6atmodepo = get_Natmodepoy6()
        y7Nfertitype = get_all_month_valuestypeNfertiy7()
        y7Nfertirate = get_all_month_valuesrateNfertiy7()
        y7placement = get_placement7()
        y7_quantityfertiorga = get_quantityorgafertiy7()
        y7_typefertiorga = get_typeorgafertiy7()
        y7_placementfertiorga = get_placementorgafertiy7()
        y7biomasseunderstorey = get_understoreybiomassy7()
        y7legumefractionunderstorey = get_legumefractiony7()
        y7prunedfronds = get_prunedy7()
        y7atmodepo = get_Natmodepoy7()
        y8Nfertitype = get_all_month_valuestypeNfertiy8()
        y8Nfertirate = get_all_month_valuesrateNfertiy8()
        y8placement = get_placement8()
        y8_quantityfertiorga = get_quantityorgafertiy8()
        y8_typefertiorga = get_typeorgafertiy8()
        y8_placementfertiorga = get_placementorgafertiy8()
        y8biomasseunderstorey = get_understoreybiomassy8()
        y8legumefractionunderstorey = get_legumefractiony8()
        y8prunedfronds = get_prunedy8()
        y8atmodepo = get_Natmodepoy8()
        y9Nfertitype = get_all_month_valuestypeNfertiy9()
        y9Nfertirate = get_all_month_valuesrateNfertiy9()
        y9placement = get_placement9()
        y9_quantityfertiorga = get_quantityorgafertiy9()
        y9_typefertiorga = get_typeorgafertiy9()
        y9_placementfertiorga = get_placementorgafertiy9()
        y9biomasseunderstorey = get_understoreybiomassy9()
        y9legumefractionunderstorey = get_legumefractiony9()
        y9prunedfronds = get_prunedy9()
        y9atmodepo = get_Natmodepoy9()
        y10Nfertitype = get_all_month_valuestypeNfertiy10()
        y10Nfertirate = get_all_month_valuesrateNfertiy10()
        y10placement = get_placement10()
        y10_quantityfertiorga = get_quantityorgafertiy10()
        y10_typefertiorga = get_typeorgafertiy10()
        y10_placementfertiorga = get_placementorgafertiy10()
        y10biomasseunderstorey = get_understoreybiomassy10()
        y10legumefractionunderstorey = get_legumefractiony10()
        y10prunedfronds = get_prunedy10()
        y10atmodepo = get_Natmodepoy10()


        return organic_carbon,texture_soil, slope_info,Land_Terraces, Previous_palm\
            ,y1Nfertitype, y1Nfertirate, y1placement, y1_quantityfertiorga, y1_typefertiorga, y1_placementfertiorga, y1biomasseunderstorey, y1legumefractionunderstorey, y1prunedfronds, y1atmodepo\
            , y2Nfertitype, y2Nfertirate, y2placement, y2_quantityfertiorga, y2_typefertiorga, y2_placementfertiorga, y2biomasseunderstorey, y2legumefractionunderstorey,y2prunedfronds, y2atmodepo\
            , y3Nfertitype, y3Nfertirate, y3placement, y3_quantityfertiorga, y3_typefertiorga, y3_placementfertiorga, y3biomasseunderstorey, y3legumefractionunderstorey, y3prunedfronds,y3atmodepo \
            , y4Nfertitype, y4Nfertirate, y4placement, y4_quantityfertiorga, y4_typefertiorga, y4_placementfertiorga, y4biomasseunderstorey, y4legumefractionunderstorey, y4prunedfronds, y4atmodepo \
            , y5Nfertitype, y5Nfertirate, y5placement, y5_quantityfertiorga, y5_typefertiorga, y5_placementfertiorga, y5biomasseunderstorey, y5legumefractionunderstorey, y5prunedfronds, y5atmodepo \
            , y6Nfertitype, y6Nfertirate, y6placement, y6_quantityfertiorga, y6_typefertiorga, y6_placementfertiorga, y6biomasseunderstorey, y6legumefractionunderstorey, y6prunedfronds, y6atmodepo \
            , y7Nfertitype, y7Nfertirate, y7placement, y7_quantityfertiorga, y7_typefertiorga, y7_placementfertiorga, y7biomasseunderstorey, y7legumefractionunderstorey, y7prunedfronds, y7atmodepo \
            , y8Nfertitype, y8Nfertirate, y8placement, y8_quantityfertiorga, y8_typefertiorga, y8_placementfertiorga, y8biomasseunderstorey, y8legumefractionunderstorey, y8prunedfronds, y8atmodepo \
            , y9Nfertitype, y9Nfertirate, y9placement, y9_quantityfertiorga, y9_typefertiorga, y9_placementfertiorga, y9biomasseunderstorey, y9legumefractionunderstorey, y9prunedfronds, y9atmodepo \
            , y10Nfertitype, y10Nfertirate, y10placement, y10_quantityfertiorga, y10_typefertiorga, y10_placementfertiorga, y10biomasseunderstorey, y10legumefractionunderstorey, y10prunedfronds, y10atmodepo


    button = tkinter.Button(main_frame, text="Continue analyse",
                            width=20,height=3,
                            font=("Ariel",20,"bold"),
                            fg="white",bg="blue",
                            command=printlist)
    button.pack(pady=10,padx=50)


    infopracticeroot.mainloop()


#Fonction pour sauvegarde des données
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
                                   width=15,height=2,
                                   command=lambda :Managementpracticesinterface(functioncount=0,file_path=""))#Rajouter une command d'appel au parent weatherdata()
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



