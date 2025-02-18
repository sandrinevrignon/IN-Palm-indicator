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
    global Orgafertitype
    global Orgafertiplacement
    global understoreybiomass
    global understoreylegumefraction
    global Prunedfronds

    #Création de la fenêtre
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
    Nfertiplacement = ["In the circle, buried", "In the circle, not buried", "In the circle + windrow", "Evenly distributed"]
    Orgafertitype = ["EFB", "Compost"]
    Orgafertiplacement = ["In the circle", "In the harvesting path", "Spread (anti erosion)"]
    understoreybiomass = ["Very high", "High", "Medium", "Low", "No"]
    understoreylegumefraction = ["Very high", "High", "Medium", "Low", "No"]
    Prunedfronds = ["Exported", "In heaps", "In windows", "Spread (anti erosion)"]

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

    #Intégration des instructions de remplissage
    # Intégration des instructions
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
                yearcumul=i+yearcumul
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
                yearcumul = i + yearcumul
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
            y1_Jan(y1_placementferti)]
        return placementfertiy2

    # Création combobox placement N ferti
    y1_placementferti = ttk.Combobox(frame2, values=Nfertiplacement,
                                     width=21)
    y1_placementferti.set("*Choice*")
    y1_placementferti.place(relx=0.06, rely=0.47)

    # Fonction pour récupérer toute la valeur de quantity organic
    def get_quantityorgafertiy2():
        quantityorgafertiy1list = [
            y1_Jan(y2_quantityorgavar)]
        return quantityorgafertiy1list

    # Création quantité fertilisation organique
    y2_quantityorgavar = tkinter.Entry(frame2,
                                       width=8,
                                       justify="right")
    y2_quantityorgavar.insert(tkinter.END, "0")
    y2_quantityorgavar.place(relx=0.1, rely=0.63)

    # Fonction pour récupérer la valeur de type organic
    def get_typeorgafertiy2():
        typeorgafertiy1list = [
            y1_Jan(y2_typeorgavar)]
        return typeorgafertiy1list

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
            y1_Jan(y1_legumefraction)]
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
                yearcumul = i + yearcumul
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
            y1_Jan(y1_placementferti)]
        return placementfertiy2

    # Création combobox placement N ferti
    y1_placementferti = ttk.Combobox(frame2, values=Nfertiplacement,
                                     width=21)
    y1_placementferti.set("*Choice*")
    y1_placementferti.place(relx=0.06, rely=0.47)

    # Fonction pour récupérer toute la valeur de quantity organic
    def get_quantityorgafertiy2():
        quantityorgafertiy1list = [
            y1_Jan(y2_quantityorgavar)]
        return quantityorgafertiy1list

    # Création quantité fertilisation organique
    y2_quantityorgavar = tkinter.Entry(frame2,
                                       width=8,
                                       justify="right")
    y2_quantityorgavar.insert(tkinter.END, "0")
    y2_quantityorgavar.place(relx=0.1, rely=0.63)

    # Fonction pour récupérer la valeur de type organic
    def get_typeorgafertiy2():
        typeorgafertiy1list = [
            y1_Jan(y2_typeorgavar)]
        return typeorgafertiy1list

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
            y1_Jan(y1_legumefraction)]
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










    def printlist():
        y1Nfertitype = get_all_month_valuestypeNfertiy1()
        print (y1Nfertitype)
        y1Nfertirate=get_all_month_valuesrateNfertiy1()
        print(y1Nfertirate)
        y1placement=get_placement1()
        print(y1placement)
        y1_quantityfertiorga=get_quantityorgafertiy1()
        print(y1_quantityfertiorga)
        y1_typefertiorga = get_typeorgafertiy1()
        print(y1_typefertiorga)
        y1_placementfertiorga = get_placementorgafertiy1()
        print(y1_placementfertiorga)
        y1biomasseunderstorey=get_understoreybiomassy1()
        print(y1biomasseunderstorey)
        y1legumefractionunderstorey=get_legumefractiony1()
        print(y1legumefractionunderstorey)
        y1prunedfronds=get_prunedy1()
        print(y1prunedfronds)
        y1atmodepo = get_Natmodepoy1()
        print(y1atmodepo)
        y2Nfertitype = get_all_month_valuestypeNfertiy2()
        print(y2Nfertitype)
        y2Nfertirate = get_all_month_valuesrateNfertiy2()
        print(y2Nfertirate)
        y2placement = get_placement2()
        print(y2placement)
        y2_quantityfertiorga = get_quantityorgafertiy2()
        print(y2_quantityfertiorga)
        y2_typefertiorga = get_typeorgafertiy2()
        print(y2_typefertiorga)
        y2_placementfertiorga = get_placementorgafertiy2()
        print(y2_placementfertiorga)
        y2biomasseunderstorey = get_understoreybiomassy2()
        print(y2biomasseunderstorey)
        y2legumefractionunderstorey = get_legumefractiony2()
        print(y2legumefractionunderstorey)
        y2prunedfronds = get_prunedy2()
        print(y2prunedfronds)
        y2atmodepo = get_Natmodepoy2()
        print(y2atmodepo)

        return y1Nfertitype,y1Nfertirate,y1placement,y1_quantityfertiorga,y1_typefertiorga,y1_placementfertiorga, y1biomasseunderstorey,y1legumefractionunderstorey,y1prunedfronds,y1atmodepo,y2Nfertitype,y2Nfertirate,y2placement,y2_quantityfertiorga,y2_typefertiorga,y2_placementfertiorga, y2biomasseunderstorey,y2legumefractionunderstorey,y2prunedfronds,y2atmodepo



    button = tkinter.Button(frame, text="confirmation", command=printlist)
    button.place(relx=0.6, rely=0.9)

    infopracticeroot.mainloop()




    # Création d'un encadré



Managementpracticesinterface(functioncount=1,file_path="")
