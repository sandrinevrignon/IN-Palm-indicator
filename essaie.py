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
                yearcumul = i + yearcumul
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
        y3_typefertiorga = listferti[22]
        y3_quantityfertiorga = listferti[23]
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
                yearcumul = i + yearcumul
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
        y4_typefertiorga = listferti[32]
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
                yearcumul = i + yearcumul
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
        y5_typefertiorga = listferti[42]
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
                           text="Fifth year", font=("Ariel", 20, 'underline')))
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
                yearcumul = i + yearcumul
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
        y6_typefertiorga = listferti[52]
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
        y3Nfertitype = get_all_month_valuestypeNfertiy3()
        print(y3Nfertitype)
        y3Nfertirate = get_all_month_valuesrateNfertiy3()
        print(y3Nfertirate)
        y3placement = get_placement3()
        print(y3placement)
        y3_quantityfertiorga = get_quantityorgafertiy3()
        print(y3_quantityfertiorga)
        y3_typefertiorga = get_typeorgafertiy3()
        print(y3_typefertiorga)
        y3_placementfertiorga = get_placementorgafertiy3()
        print(y3_placementfertiorga)
        y3biomasseunderstorey = get_understoreybiomassy3()
        print(y3biomasseunderstorey)
        y3legumefractionunderstorey = get_legumefractiony3()
        print(y3legumefractionunderstorey)
        y3prunedfronds = get_prunedy3()
        print(y3prunedfronds)
        y3atmodepo = get_Natmodepoy3()
        print(y3atmodepo)
        y4Nfertitype = get_all_month_valuestypeNfertiy4()
        print(y4Nfertitype)
        y4Nfertirate = get_all_month_valuesrateNfertiy4()
        print(y4Nfertirate)
        y4placement = get_placement4()
        print(y4placement)
        y4_quantityfertiorga = get_quantityorgafertiy4()
        print(y4_quantityfertiorga)
        y4_typefertiorga = get_typeorgafertiy4()
        print(y4_typefertiorga)
        y4_placementfertiorga = get_placementorgafertiy4()
        print(y4_placementfertiorga)
        y4biomasseunderstorey = get_understoreybiomassy4()
        print(y4biomasseunderstorey)
        y4legumefractionunderstorey = get_legumefractiony4()
        print(y4legumefractionunderstorey)
        y4prunedfronds = get_prunedy4()
        print(y4prunedfronds)
        y4atmodepo = get_Natmodepoy4()
        print(y4atmodepo)
        y5Nfertitype = get_all_month_valuestypeNfertiy5()
        print(y5Nfertitype)
        y5Nfertirate = get_all_month_valuesrateNfertiy5()
        print(y5Nfertirate)
        y5placement = get_placement5()
        print(y5placement)
        y5_quantityfertiorga = get_quantityorgafertiy5()
        print(y5_quantityfertiorga)
        y5_typefertiorga = get_typeorgafertiy5()
        print(y5_typefertiorga)
        y5_placementfertiorga = get_placementorgafertiy5()
        print(y5_placementfertiorga)
        y5biomasseunderstorey = get_understoreybiomassy5()
        print(y5biomasseunderstorey)
        y5legumefractionunderstorey = get_legumefractiony5()
        print(y5legumefractionunderstorey)
        y5prunedfronds = get_prunedy5()
        print(y5prunedfronds)
        y5atmodepo = get_Natmodepoy5()
        print(y5atmodepo)
        y6Nfertitype = get_all_month_valuestypeNfertiy6()
        print(y6Nfertitype)
        y6Nfertirate = get_all_month_valuesrateNfertiy6()
        print(y6Nfertirate)
        y6placement = get_placement6()
        print(y6placement)
        y6_quantityfertiorga = get_quantityorgafertiy6()
        print(y6_quantityfertiorga)
        y6_typefertiorga = get_typeorgafertiy6()
        print(y6_typefertiorga)
        y6_placementfertiorga = get_placementorgafertiy6()
        print(y6_placementfertiorga)
        y6biomasseunderstorey = get_understoreybiomassy6()
        print(y6biomasseunderstorey)
        y6legumefractionunderstorey = get_legumefractiony6()
        print(y6legumefractionunderstorey)
        y6prunedfronds = get_prunedy6()
        print(y6prunedfronds)
        y6atmodepo = get_Natmodepoy6()
        print(y6atmodepo)


        return y1Nfertitype, y1Nfertirate, y1placement, y1_quantityfertiorga, y1_typefertiorga, y1_placementfertiorga, y1biomasseunderstorey, y1legumefractionunderstorey, y1prunedfronds, y1atmodepo\
            , y2Nfertitype, y2Nfertirate, y2placement, y2_quantityfertiorga, y2_typefertiorga, y2_placementfertiorga, y2biomasseunderstorey, y2legumefractionunderstorey,y2prunedfronds, y2atmodepo\
            , y3Nfertitype, y3Nfertirate, y3placement, y3_quantityfertiorga, y3_typefertiorga, y3_placementfertiorga, y3biomasseunderstorey, y3legumefractionunderstorey, y3prunedfronds,y3atmodepo \
            , y4Nfertitype, y4Nfertirate, y4placement, y4_quantityfertiorga, y4_typefertiorga, y4_placementfertiorga, y4biomasseunderstorey, y4legumefractionunderstorey, y4prunedfronds, y4atmodepo \
            , y5Nfertitype, y5Nfertirate, y5placement, y5_quantityfertiorga, y5_typefertiorga, y5_placementfertiorga, y5biomasseunderstorey, y5legumefractionunderstorey, y5prunedfronds, y5atmodepo \
            , y6Nfertitype, y6Nfertirate, y6placement, y6_quantityfertiorga, y6_typefertiorga, y6_placementfertiorga, y6biomasseunderstorey, y6legumefractionunderstorey, y6prunedfronds, y6atmodepo
















    button = tkinter.Button(frame, text="confirmation", command=printlist)
    button.place(relx=0.6, rely=0.9)

    infopracticeroot.mainloop()




    # Création d'un encadré



Managementpracticesinterface(functioncount=1,file_path="")
