#!/usr/bin/env python3

import csv

#Création du dictionnaire meteo
def infodico(dictionnary, town, country) :
    print(f"Monthly cumulative rainy statement\n"
          f"\tCountry:{country}\n"
          f"\tTown:{town}")
    print(dictionnary)
    for (years, months) in dictionnary.items():
        print(f"Year:{years}")
        for monthdata, data in months.items():
            print(f"{monthdata},rainfall: {data['Rainfall']}, rain frequency: {data['Rain frequency']}")
    # Sauvegarde des données dans un csv


def weatherdata():
    file="C:\\Users\\svrignon\\Desktop\\programme\\example.csv"

    #Contrôle que le fichier donné soit un fichier csv
    csvfile=file.split(".")
    if csvfile[-1]!="csv":
        print("please give an csv file")
    else:

        # Lecture du fichier CSV
        with open(file, mode='r',newline='', encoding='utf-8') as file:
            reader=csv.reader(file)
            # Lecture de la première ligne du fichier
            firstrow = next(reader)
            #Contrôle que les noms de colonnes soient bien identique à l'exemple
            firstrowsep=firstrow[0].split(";")
            if (firstrowsep[0] not in ("date","Date")) or (firstrowsep[1] not in("Rain (mm)","rain (mm)","Rain(mm)","rain(mm)")) or (firstrowsep[2] not in ("Country","country")) or (firstrowsep[3] not in ("Town","town")):
                print ("Please use the same format as example")
            else:

                #Initialisation de l'année précédente
                prevyear=99999

                #Intégration d'un booléen pour le contrôle du format de date et année
                error = False

                #Création d'un dictionnaire mensuel pour stockage données années
                Jandict={}
                Febdict={}
                Mardict={}
                Aprdict={}
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
                        print("please control your rain format: numbers must be separated by points (0.13) and not commas (0,13)")
                        exit()

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
                        if not error:
                            print("Month must be between 1 and 12.\nPlease convert your date in month/date/year")
                            error = True
                            exit()
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
                                print("Your years must be cumulative ")
                                error = True
                                exit()
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

        infodico(dictionnary,town, country)

#Sauvegarde des données dans un csv
#Faire clic
weatherdata()

global dictionnary
dictionnary={'2008': {'January': {'Rainfall': 12.17, 'Rain frequency': 9}, 'February': {'Rainfall': 15.51, 'Rain frequency': 8}, 'March': {'Rainfall': 47.76, 'Rain frequency': 15}, 'April': {'Rainfall': 250.93, 'Rain frequency': 15}, 'May': {'Rainfall': 199.5, 'Rain frequency': 11}, 'June': {'Rainfall': 128.3, 'Rain frequency': 8}, 'July': {'Rainfall': 180.0, 'Rain frequency': 8}, 'August': {'Rainfall': 222.0, 'Rain frequency': 10}, 'September': {'Rainfall': 317.5, 'Rain frequency': 13}, 'October': {'Rainfall': 320.8, 'Rain frequency': 18}, 'November': {'Rainfall': 153.4, 'Rain frequency': 9}, 'December': {'Rainfall': 170.5, 'Rain frequency': 11}},
             '2009': {'January': {'Rainfall': 107.5, 'Rain frequency': 8}, 'February': {'Rainfall': 113.7, 'Rain frequency': 13}, 'March': {'Rainfall': 115.89, 'Rain frequency': 13}, 'April': {'Rainfall': 301.5, 'Rain frequency': 13}, 'May': {'Rainfall': 76.4, 'Rain frequency': 9}, 'June': {'Rainfall': 211.4, 'Rain frequency': 8}, 'July': {'Rainfall': 152.0, 'Rain frequency': 5}, 'August': {'Rainfall': 318.5, 'Rain frequency': 8}, 'September': {'Rainfall': 187.5, 'Rain frequency': 10}, 'October': {'Rainfall': 465.5, 'Rain frequency': 16}, 'November': {'Rainfall': 223.5, 'Rain frequency': 13}, 'December': {'Rainfall': 588.5, 'Rain frequency': 15}},
             '2010': {'January': {'Rainfall': 329.5, 'Rain frequency': 16}, 'February': {'Rainfall': 127.0, 'Rain frequency': 11}, 'March': {'Rainfall': 398.7, 'Rain frequency': 17}, 'April': {'Rainfall': 282.5, 'Rain frequency': 14}, 'May': {'Rainfall': 170.5, 'Rain frequency': 11}, 'June': {'Rainfall': 101.5, 'Rain frequency': 6}, 'July': {'Rainfall': 150.0, 'Rain frequency': 14}, 'August': {'Rainfall': 245.5, 'Rain frequency': 14}, 'September': {'Rainfall': 230.1, 'Rain frequency': 12}, 'October': {'Rainfall': 215.0, 'Rain frequency': 12}, 'November': {'Rainfall': 224.4, 'Rain frequency': 15}, 'December': {'Rainfall': 90.0, 'Rain frequency': 10}},
             '2011': {'January': {'Rainfall': 269.0, 'Rain frequency': 21}, 'February': {'Rainfall': 127.4, 'Rain frequency': 6}, 'March': {'Rainfall': 230.6, 'Rain frequency': 15}, 'April': {'Rainfall': 208.4, 'Rain frequency': 17}, 'May': {'Rainfall': 104.3, 'Rain frequency': 10}, 'June': {'Rainfall': 72.2, 'Rain frequency': 6}, 'July': {'Rainfall': 30.1, 'Rain frequency': 6}, 'August': {'Rainfall': 100.0, 'Rain frequency': 6}, 'September': {'Rainfall': 201.8, 'Rain frequency': 11}, 'October': {'Rainfall': 413.0, 'Rain frequency': 16}, 'November': {'Rainfall': 233.2, 'Rain frequency': 17}, 'December': {'Rainfall': 249.0, 'Rain frequency': 20}},
             '2012': {'January': {'Rainfall': 145.3, 'Rain frequency': 14}, 'February': {'Rainfall': 187.9, 'Rain frequency': 18}, 'March': {'Rainfall': 170.4, 'Rain frequency': 15}, 'April': {'Rainfall': 229.9, 'Rain frequency': 12}, 'May': {'Rainfall': 117.4, 'Rain frequency': 9}, 'June': {'Rainfall': 52.1, 'Rain frequency': 8}, 'July': {'Rainfall': 78.5, 'Rain frequency': 11}, 'August': {'Rainfall': 264.1, 'Rain frequency': 12}, 'September': {'Rainfall': 156.46, 'Rain frequency': 8}, 'October': {'Rainfall': 277.2, 'Rain frequency': 16}, 'November': {'Rainfall': 392.5, 'Rain frequency': 21}, 'December': {'Rainfall': 542.0, 'Rain frequency': 15}},
             '2013': {'January': {'Rainfall': 195.5, 'Rain frequency': 12}, 'February': {'Rainfall': 168.8, 'Rain frequency': 16}, 'March': {'Rainfall': 242.6, 'Rain frequency': 12}, 'April': {'Rainfall': 227.8, 'Rain frequency': 12}, 'May': {'Rainfall': 247.7, 'Rain frequency': 13}, 'June': {'Rainfall': 90.0, 'Rain frequency': 7}, 'July': {'Rainfall': 82.5, 'Rain frequency': 4}, 'August': {'Rainfall': 111.9, 'Rain frequency': 7}, 'September': {'Rainfall': 248.4, 'Rain frequency': 11}, 'October': {'Rainfall': 309.1, 'Rain frequency': 18}, 'November': {'Rainfall': 477.5, 'Rain frequency': 20}, 'December': {'Rainfall': 326.7, 'Rain frequency': 14}},
             '2014': {'January': {'Rainfall': 269.3, 'Rain frequency': 8}, 'February': {'Rainfall': 4.0, 'Rain frequency': 1}, 'March': {'Rainfall': 107.8, 'Rain frequency': 7}, 'April': {'Rainfall': 157.2, 'Rain frequency': 15}, 'May': {'Rainfall': 230.6, 'Rain frequency': 14}, 'June': {'Rainfall': 131.0, 'Rain frequency': 4}, 'July': {'Rainfall': 68.7, 'Rain frequency': 7}, 'August': {'Rainfall': 176.9, 'Rain frequency': 13}, 'September': {'Rainfall': 143.6, 'Rain frequency': 7}, 'October': {'Rainfall': 132.5, 'Rain frequency': 13}, 'November': {'Rainfall': 319.6, 'Rain frequency': 19}, 'December': {'Rainfall': 405.5, 'Rain frequency': 16}},
             '2015': {'January': {'Rainfall': 92.5, 'Rain frequency': 11}, 'February': {'Rainfall': 29.0, 'Rain frequency': 2}, 'March': {'Rainfall': 138.2, 'Rain frequency': 13}, 'April': {'Rainfall': 208.1, 'Rain frequency': 14}, 'May': {'Rainfall': 158.9, 'Rain frequency': 12}, 'June': {'Rainfall': 83.9, 'Rain frequency': 10}, 'July': {'Rainfall': 84.5, 'Rain frequency': 4}, 'August': {'Rainfall': 34.2, 'Rain frequency': 8}, 'September': {'Rainfall': 155.7, 'Rain frequency': 7}, 'October': {'Rainfall': 130.9, 'Rain frequency': 7}, 'November': {'Rainfall': 413.9, 'Rain frequency': 19}, 'December': {'Rainfall': 197.6, 'Rain frequency': 12}}}
            #0 Soil caracteristic: orga C
printlist= (['1.7'],
            #1 Soil caracteristic: Texture
            ['Sandy clay loam'],
            #2 Soil caracteristic: Slope
            ['2'],
            #3 Land preparation : Terraces
            ['No'],
            #4 Land preparation : Previous
            ['Shredded left on soil'],
            #Year:Month data
            ###################################Y1##########################################
            #5 Y1:Miner Nferti: Type
            ['*None', 'Ammo Sulf', '*None', '*None', 'Ammo Sulf', '*None', '*None', '*None', '*None', 'Urea', '*None', '*None'],
            #6 Y1:Miner Nferti: Rate
            ['0', '44', '0', '0', '44', '0', '0', '0', '0', '14', '0', '0'],
            #7 Y1: :Miner Nferti: Placement
            ['In the circle, not buried'],
            #8 Y1:Orga ferti: Quantity
            ['57'],
            #9 Y1:Orga ferti: Type
            ['EFB'],
            #10 Y1:Orga ferti: Placement
            ['In the circle'],
            #11 Y1:Understorey: Biomass
            ['High'],
            #12 Y1:Understorey: Legume fraction
            ['No'],
            #13 Y1: Atmospheric deposition
            ['18'],
            ######################################################Y2########################################################
            #14 Y2:Miner Nferti: Type
            ['*None', 'Ammo Sulf', '*None', '*None', 'Ammo Sulf', '*None', '*None', '*None', '*None', 'Urea', '*None', '*None'],
            #15 Y2: Miner Nferti: Rate
            ['0', '18', '0', '0', '200', '0', '0', '0', '0', '10', '0', '0'],
            #16 Y2: :Miner Nferti: Placement
            ['In the circle, not buried'],
            #17 Y2:Orga ferti: Quantity
            ['0'],
            #18 Y2:Orga ferti: Type
            ['*Choice*'],
            #19 Y2:Orga ferti: Placement
            ['*Choice*'],
            #20 Y2:Understorey: Biomass
            ['Very high'],
            #21 Y2:Understorey: Legume fraction
            ['*Choice*'],
            #22 Y2: Atmospheric deposition
            ['18'],
            ########################################################Y3#############################################
            #23 Y3: Miner Nferti: Type
            ['*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None'],
            #24 Y3: Miner Nferti: Rate
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            #25 Y3: Miner Nferti: Placement
            ['*Choice*'],
            #26 Y3:Orga ferti: Quantity
            ['0'],
            #27 Y3:Orga ferti: Type
            ['*Choice*'],
            #28 Y3:Orga ferti: Placement
            ['*Choice*'],
            #29 Y3:Understorey: Biomass
            ['*Choice*'],
            #30 Y3:Understorey: Legume fraction
            ['*Choice*'],
            #31 Y3: Pruned frond
            ['*Choice*'],
            #32 Y3: Atmospheric deposition
            ['18'],
            #33 Y3: Yield
            ['0'],
            ######################################################Y4######################################################
            #34 Y4:Miner Nferti: Type
            ['*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None'],
            #35 Y4:Miner Nferti: Rate
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            #36 Y4:Miner Nferti: Placement
            ['*Choice*'],
            #37 Y4:Orga ferti: Quantity
            ['0'],
            #38 Y4 :Orga ferti: Type
            ['*Choice*'],
            #39 Y4:Orga ferti: Placement
            ['*Choice*'],
            #40 Y4:Understorey: Biomass
            ['*Choice*'],
            #41 Y4:Understorey: Legume fraction
            ['*Choice*'],
            #42 Y4: Pruned frond
            ['*Choice*'],
            #43 Y4: Atmospheric deposition
            ['18'],
            #44 Y4: Yield
            ['0'],
            ########################################################Y5###################################################
            #45 Y5 :Miner Nferti: Type
            ['*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None'],
            #46 Y5:Miner Nferti: Rate
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            #47 Y5 :Miner Nferti: Placement
            ['*Choice*'],
            #48 Y5:Orga ferti: Quantity
            ['0'],
            #49 Y5:Orga ferti: Type
            ['*Choice*'],
            #50 Y5:Orga ferti: Placement
            ['*Choice*'],
            #51 Y5:Understorey: Biomass
            ['*Choice*'],
            #52 Y5:Understorey: Legume fraction
            ['*Choice*'],
            #53 Y5: Pruned frond
            ['*Choice*'],
            #54 Y5: Atmospheric deposition
            ['18'],
            #55 Y5: Yield
            ['18'],
            ##############################################################Y6###############################################
            #56 Y6:Miner Nferti: Type
            ['*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None'],
            #57 Y6:Miner Nferti: Rate
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            #58 Y6 :Miner Nferti: Placement
            ['*Choice*'],
            #59 Y6:Orga ferti: Quantity
            ['0'],
            #60 Y6:Orga ferti: Type
            ['*Choice*'],
            #61 Y6:Orga ferti: Placement
            ['*Choice*'],
            #62 Y6:Understorey: Biomass
            ['*Choice*'],
            #63 Y6:Understorey: Legume fraction
            ['*Choice*'],
            #64 Y6: Pruned frond
            ['*Choice*'],
            #65 Y6: Atmospheric deposition
            ['18'],
            #66 Y6: Yield
            ['0'],
            ############################################Y7#####################################################################
            #67 Y7::Miner Nferti: Type
            ['*None', '*None', '*None', '*None', 'Ammo Sulf', '*None', '*None', '*None', '*None', 'Urea', '*None', '*None'],
            #68 Y7::Miner Nferti: Rate
            ['0', '0', '0', '0', '180', '0', '0', '0', '0', '26', '0', '0'],
            #69 Y7: :Miner Nferti: Placement
            ['In the circle + windrow'],
            #70 Y7::Orga ferti: Quantity
            ['0'],
            #71 Y7::Orga ferti: Type
            ['*Choice*'],
            #72 Y7::Orga ferti: Placement
            ['*Choice*'],
            #73 Y7::Understorey: Biomass
            ['Medium'],
            #74 Y7::Understorey: Legume fraction
            ['Low'],
            #75 Y7:: Pruned frond
            ['In windows'],
            #76 Y7:: Atmospheric deposition
            ['18'],
            #77 Y7:: Yield
            ['0'],
            ###############################################Y8###############################################################
            #78 Y8:Miner Nferti: Type
            ['*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None'],
            #79 Y8:Miner Nferti: Rate
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            #80 Y8 :Miner Nferti: Placement
            ['*Choice*'],
            #81 Y8:Orga ferti: Quantity
            ['0'],
            #82 Y8:Orga ferti: Type
            ['*Choice*'],
            #83 Y8:Orga ferti: Placement
            ['*Choice*'],
            #84 Y8:Understorey: Biomass
            ['Medium'],
            #85 Y8:Understorey: Legume fraction
            ['Low'],
            #86 Y8: Pruned frond
            ['In windows'],
            #87 Y8: Atmospheric deposition
            ['18'],
            #88 Y8: Yield
            ['18'],
            #######################################################Y9#####################################################
            #89 Y9:Miner Nferti: Type
            ['*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None'],
            #90 Y9:Miner Nferti: Rate
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            #91 Y9 :Miner Nferti: Placement
            ['*Choice*'],
            #92 Y9:Orga ferti: Quantity
            ['0'],
            #93 Y9:Orga ferti: Type
            ['*Choice*'],
            #94 Y9:Orga ferti: Placement
            ['*Choice*'],
            #95 Y9:Understorey: Biomass
            ['*Choice*'],
            #96 Y9:Understorey: Legume fraction
            ['*Choice*'],
            #97 Y9: Pruned frond
            ['*Choice*'],
            #98 Y9: Atmospheric deposition
            ['18'],
            #99 Y9: Yield
            ['0'],
            ################################################################Y10#############################################################
            #100 Y10:Miner Nferti: Type
            ['*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None', '*None'],
            #101 Y10:Miner Nferti: Rate
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            #102 Y10:Miner Nferti: Placement
            ['*Choice*'],
            #103 Y10:Orga ferti: Quantity
            ['0'],
            #104 Y10:Orga ferti: Type
            ['*Choice*'],
            #105 Y10:Orga ferti: Placement
            ['*Choice*'],
            #106 Y10:Understorey: Biomass
            ['*Choice*'],
            #107 Y10:Understorey: Legume fraction
            ['*Choice*'],
            #108 Y10: Pruned frond
            ['*Choice*'],
            #109 Y10: Atmospheric deposition
            ['18'],
            #110 Y10: Yield
            ['0']
            )


#Partie à intégrer au script
def dictionnary_complete(countfounction,printlist) :

    #Récupération des éléments
    #Données générales parcelles

        #Soil caracteristic
    OrganicC=printlist[0][0]
    Texture=printlist[1][0]
    Slope=printlist[2][0]
        #Land preparation
    Terraces=printlist[3][0]
    Previous=printlist[4][0]

    #Données annuelles
        #Mineral N ferti
    TypeNfertilist=(printlist[5]+
                    printlist[14]+
                    printlist[23]+
                    printlist[34]+
                    printlist[45]+
                    printlist[56]+
                    printlist[67]+
                    printlist[78]+
                    printlist[89]+
                    printlist[100])

    RateNferti=(printlist[6]+
                 printlist[15]+
                 printlist[24]+
                 printlist[35]+
                 printlist[46]+
                 printlist[57]+
                 printlist[68]+
                 printlist[79]+
                 printlist[90]+
                 printlist[101])


    PlacementNferti=(printlist[7][0],
                     printlist[16][0],
                     printlist[25][0],
                     printlist[36][0],
                     printlist[47][0],
                     printlist[58][0],
                     printlist[69][0],
                     printlist[80][0],
                     printlist[91][0],
                     printlist[102][0])

    #Organic fertilizer
    Quantityorgaferti=(printlist[8][0],
                       printlist[17][0],
                       printlist[26][0],
                       printlist[37][0],
                       printlist[48][0],
                       printlist[59][0],
                       printlist[70][0],
                       printlist[81][0],
                       printlist[92][0],
                       printlist[103][0])

    Typeorgaferti=(printlist[9][0],
                   printlist[18][0],
                   printlist[27][0],
                   printlist[38][0],
                   printlist[49][0],
                   printlist[60][0],
                   printlist[71][0],
                   printlist[82][0],
                   printlist[93][0],
                   printlist[104][0])

    Placementorgaferti = (printlist[10][0],
                     printlist[19][0],
                     printlist[28][0],
                     printlist[39][0],
                     printlist[50][0],
                     printlist[61][0],
                     printlist[72][0],
                     printlist[83][0],
                     printlist[94][0],
                     printlist[105][0])

    # Understorey
    Biomassunderstorey = (printlist[11][0],
                          printlist[20][0],
                          printlist[29][0],
                          printlist[40][0],
                          printlist[51][0],
                          printlist[62][0],
                          printlist[73][0],
                          printlist[84][0],
                          printlist[95][0],
                          printlist[106][0])

    Legumefunderstorey = (printlist[12][0],
                          printlist[21][0],
                          printlist[30][0],
                          printlist[41][0],
                          printlist[52][0],
                          printlist[63][0],
                          printlist[74][0],
                          printlist[85][0],
                          printlist[96][0],
                          printlist[107][0])

    #Atmospheric deposition
    atmosphdepostion=(printlist[13][0],
                      printlist[22][0],
                      printlist[32][0],
                      printlist[43][0],
                      printlist[54][0],
                      printlist[65][0],
                      printlist[76][0],
                      printlist[87][0],
                      printlist[98][0],
                      printlist[109][0])

    #Dictionnaire pruned
    Pruned=("",
            "",
            printlist[31][0],
            printlist[42][0],
            printlist[53][0],
            printlist[64][0],
            printlist[75][0],
            printlist[86][0],
            printlist[97][0],
            printlist[108][0])

    # Dictionnaire pruned
    Yield = ("",
              "",
              printlist[33][0],
              printlist[44][0],
              printlist[55][0],
              printlist[66][0],
              printlist[77][0],
              printlist[88][0],
              printlist[99][0],
              printlist[110][0])

    ######################### Vérification des données d'entrée
    # Création liste float pour liste data
    RateNferti_float = []
    Quantityorgaferti_float=[]
    atmosphdepostion_float=[]
    Yield_float=[]

    # Vérification pour chaque éléments chiffres entrées
    #OrganicC
    ##Chaque élément de cette liste est un float + conversion
    try:
        OrganicC_float=float(OrganicC)
    except ValueError:
        print("Error on Organic Carbon input data! Please check you rate data. Data are not float")
        return
    ##OrganicC toujours <10%
    if OrganicC_float <=0 or OrganicC_float > 10:
        print("Error on Organic Carbon input data! Your data must be 0% ≥ Organic Carbon ≤ 10% ")
        return

    # Slope
    ##Chaque élément de cette liste est un float + conversion
    try:
        Slope_float=float(Slope)
    except ValueError:
        print("Error on Slope input data! Please check you rate data. Data are not float")
        return
    ##Slope toujours >0 et <30%
    if Slope_float <=0 or Slope_float > 30:
        print("Error on Slope input data! Your data must be 0% ≥ Slope ≤ 30% ")
        return

    #Rate N ferti
    ##Chaque élément de la liste est un float + conversion
    try:
        for i in RateNferti:
            RateNferti_float.append(float(i))
    except ValueError:
        print("Error on rate Mineral Nitrogen fertilizer input data!\n Please check you rate data. Data are not float")
        return
        ##RateNferti toujours >0 voir pour valeur max
    for i in RateNferti_float:
        if i <0:
            print("Error on rate Mineral Nitrogen fertilizer input data! Your data must be ≥ 0")
            return

    # Quantityorgaferti
    ##Chaque élément de la liste est un float + conversion
    try:
        for i in Quantityorgaferti:
            Quantityorgaferti_float.append(float(i))
    except ValueError:
        print("Error on quantity Organic fertilizer input data!\n Please check you rate data. Data are not float")
        return
    ##Quantity organic ferti toujours >0 voir pour valeur max
    for i in Quantityorgaferti_float:
            if i < 0:
                print(f"Error on quantity Organic fertilizer input data! Your data must be ≥ 0")
                return

    # Atmospheric deposition
    ##Chaque élément de la liste est un float + conversion
    count=0
    try:
        for i in atmosphdepostion:
            count=count+1
            atmosphdepostion_float.append(float(i))
    except ValueError:
        print(f"Error on {count}th year of quantity atmospheric deposition input data!\n Please check you rate data. Data are not float")
        return
    ##Quantity organic ferti toujours >0 voir pour valeur max
    count=0
    for i in atmosphdepostion_float:
        count=count+1
        if i < 0:
            print(f"Error on {count}th year of quantity atmospheric deposition input data! Your data must be ≥ 0")
            return

    #Yield
    ##Chaque élément de la liste est un float +conversion
    count=2
    try:
        for i in Yield[2:]:
            count=count+1
            Yield_float.append(float(i))
    except ValueError:
        print(f"Error {count}th year on Yield input data!\n Please check you data. Data are not float")
        return
    ##Quantity Yield toujours >0 et <40 voir pour valeur max
    count=2
    for i in Yield_float:
        count=count+1
        if i < 0 or i >40:
            print(f"Error on {count}th year on Yield input data!\n Your data must be 0 tFFB/ha/year ≥ Yield ≤ 40 tFFB/ha/year")
            return
    #Suppresion variable vérification données d'entrée
    del RateNferti_float,Quantityorgaferti_float,atmosphdepostion_float,Yield_float
    del Slope_float,OrganicC_float

    #Vérification lien entre les entrées et la correspondances
    #Général

    #Texture dois être rempli
    if Texture=="*Choice*":
        print("Error! Please complete the field texture")

    #Terraces dois être rempli
    if Terraces == "*Choice*":
        print("Error! Please complete the field Terraces")

    # Terraces dois être rempli
    if Previous == "*Choice*":
        print("Error! Please complete the field Previous")

    #Chaque année
    #Mineral Nitrogen fertilizer
    ##Lien entre Type et rate
    for i in range(0,len(TypeNfertilist)):
        if TypeNfertilist[i]!="*None":
            if RateNferti[i]=="0":
                print("Error! Data input between Type, Rate and Placement on Mineral Nitrogen fertilizer must be consistent.\n"
                      "Please complete all informations ")
                return
    for i in range(0,len(RateNferti)):
        if RateNferti[i]!="0":
            if TypeNfertilist[i] == "*None":
                print("Error! Data input between Type, Rate and Placement on Mineral Nitrogen fertilizer must be consistent.\n"
                      "Please complete all informations ")
                return
    ##Lien entre placement et type/Rate
    ###Year 1
    for i in range(0,12):
        if TypeNfertilist[i]!="*None" or RateNferti[i]!='0':
            if PlacementNferti[0]=="*Choice*":
                print("Error! Data input between Type, Rate and Placement on Mineral Nitrogen fertilizer must be consistent.\n"
                      "Please complete all informations")
                return
    #Year 2
    for i in range(12,24):
        if TypeNfertilist[i]!="*None" or RateNferti[i]!='0':
            if PlacementNferti[1]=="*Choice*":
                print("Error! Data input between Type, Rate and Placement on Mineral Nitrogen fertilizer must be consistent.\n"
                      "Please complete all informations")
                return
    #Year 3
    for i in range(24,36):
        if TypeNfertilist[i]!="*None" or RateNferti[i]!='0':
            if PlacementNferti[2]=="*Choice*":
                print("Error! Data input between Type, Rate and Placement on Mineral Nitrogen fertilizer must be consistent.\n"
                      "Please complete all informations")
                return
    #Year 4
    for i in range(36,48):
        if TypeNfertilist[i]!="*None" or RateNferti[i]!='0':
            if PlacementNferti[3]=="*Choice*":
                print("Error! Data input between Type, Rate and Placement on Mineral Nitrogen fertilizer must be consistent.\n"
                      "Please complete all informations")
                return
    #Year 5
    for i in range(48,60):
        if TypeNfertilist[i]!="*None" or RateNferti[i]!='0':
            if PlacementNferti[4]=="*Choice*":
                print("Error! Data input between Type, Rate and Placement on Mineral Nitrogen fertilizer must be consistent.\n"
                      "Please complete all informations")
                return
    #Year 6
    for i in range(60,72):
        if TypeNfertilist[i]!="*None" or RateNferti[i]!='0':
            if PlacementNferti[5]=="*Choice*":
                print("Error! Data input between Type, Rate and Placement on Mineral Nitrogen fertilizer must be consistent.\n"
                      "Please complete all informations")
                return
    #Year 7
    for i in range(72,84):
        if TypeNfertilist[i]!="*None" or RateNferti[i]!='0':
            if PlacementNferti[6]=="*Choice*":
                print("Error! Data input between Type, Rate and Placement on Mineral Nitrogen fertilizer must be consistent.\n"
                      "Please complete all informations")
                return
    #Year 8
    for i in range(84,96):
        if TypeNfertilist[i]!="*None" or RateNferti[i]!='0':
            if PlacementNferti[7]=="*Choice*":
                print("Error! Data input between Type, Rate and Placement on Mineral Nitrogen fertilizer must be consistent.\n"
                      "Please complete all informations")
                return
    #Year 9
    for i in range(96,108):
        if TypeNfertilist[i]!="*None" or RateNferti[i]!='0':
            if PlacementNferti[8]=="*Choice*":
                print("Error! Data input between Type, Rate and Placement on Mineral Nitrogen fertilizer must be consistent.\n"
                      "Please complete all informations")
                return
    #Year 10
    for i in range(108,len(TypeNfertilist)):
        if TypeNfertilist[i]!="*None" or RateNferti[i]!='0':
            if PlacementNferti[9]=="*Choice*":
                print("Error! Data input between Type, Rate and Placement on Mineral Nitrogen fertilizer must be consistent.\n"
                      "Please complete all informations")
                return

    # Organic fertilizer
    ##Lien entre Quantity Type et placement
        for i in range(0, len(Typeorgaferti)):
            if Typeorgaferti[i] != "*Choice*":
                if Quantityorgaferti[i] == "0":
                    print("Error! Data input between Type, Quantity and Placement on Organic fertilizer must be consistent.\n"
                          "Please complete all informations ")
                    return
                elif Placementorgaferti[i] =="*Choice*":
                    print("Error! Data input between Type, Quantity and Placement on Organic fertilizer must be consistent.\n"
                          "Please complete all informations ")
                    return
        for i in range(0, len(Placementorgaferti)):
            if Placementorgaferti[i] != "*Choice*":
                if Quantityorgaferti[i] == "0":
                    print("Error! Data input between Type, Quantity and Placement on Organic fertilizer must be consistent.\n"
                          "Please complete all informations ")
                    return
                elif Typeorgaferti[i] =="*Choice*":
                    print("Error! Data input between Type, Quantity and Placement on Organic fertilizer must be consistent.\n"
                          "Please complete all informations ")
                    return
        for i in range(0, len(Quantityorgaferti)):
            if Quantityorgaferti[i] != "0":
                if Typeorgaferti[i] == "*Choice*":
                    print("Error! Data input between Type, Quantity and Placement on Organic fertilizer must be consistent.\n"
                          "Please complete all informations ")
                    return
                elif Placementorgaferti[i] =="*Choice*":
                    print("Error! Data input between Type, Quantity and Placement on Organic fertilizer must be consistent.\n"
                          "Please complete all informations ")
                    return











    ###################Création dictionnary final avec les informations parcelles
    complete_dictionnary={'Field information':
                              {'Soil caracteristic':
                                   {'Organic Carbon':OrganicC,
                                    'Texture':Texture,
                                    'Slope':Slope},
                               'Land preparation':
                                   {'Terraces':Terraces,
                                    'Previous':Previous}}}

    # Création du dictionnaire temporaire
    essai = {}

    # Ajout de l'ensemble des informations dans dictionnaire year
    #idx car pas forcément 10 de données donc suppression de tout ce qui est supérieur
    for idx, (year, months) in enumerate(dictionnary.items()):
        # Ajouter les données générales pour chaque année

        essai[year] = {
            'Month': months,  # Ajout des mois pour chaque année
            'General data': {
                'Mineral nitrogen fertilizer': PlacementNferti[idx] if idx < len(PlacementNferti) else None,
                'Organic fertilizer': {
                    'Quantity': Quantityorgaferti[idx] if idx < len(Quantityorgaferti) else None,
                    'Type': Typeorgaferti[idx] if idx < len(Typeorgaferti) else None,
                    'Placement': Placementorgaferti[idx] if idx < len(Placementorgaferti) else None
                },
                'Understorey': {
                    'Biomass': Biomassunderstorey[idx] if idx < len(Biomassunderstorey) else None,
                    'Legume fraction': Legumefunderstorey[idx] if idx < len(Legumefunderstorey) else None
                },
                'Atmospheric deposition': atmosphdepostion[idx] if idx < len(atmosphdepostion) else None
            }
        }

        # Ajout des informations mineral N ferti pour chacun des mois (rate et type)
        for idxidx, (month, data) in enumerate(months.items()):
            essai[year]['Month'][month] = {
                'Weather': data,  # Ajout des données météo
                'Mineral nitrogen fertilizer': {
                    'Type': TypeNfertilist[idxidx] if idxidx < len(TypeNfertilist) else None,
                    'Rate': RateNferti[idxidx] if idxidx < len(RateNferti) else None
                }
            }
    #Rajout spécifique des données pruned frond à partir de la troisième année
    for idx, (year, year_data) in enumerate(essai.items()):
        if idx > 1:  # Tu veux traiter les années à partir de l'indice 2
            # On ajoute des données supplémentaires sous 'General data'
            year_data['General data']['Pruned frond'] = Pruned[idx] if idx < len(Pruned) else None
            year_data['General data']['Yield']= Yield[idx] if idx < len(Yield) else None


    #Création du complete_dictionnary par combinaison des deux dictionnaires Year et complete_dictionnary
    for general,typetype in complete_dictionnary.items():
        complete_dictionnary[general]['Year']=essai

    ###########################################Hors import script###################################
    # Afficher le dictionnaire Year pour vérifier la structure
    #print(complete_dictionnary['Year'])
    #Exemple recherche de l'ensemble des données de Land préparation
    #print(complete_dictionnary)
    #for month, data in complete_dictionnary['2009'].items():
    #    print(f"Rainfall for {month} 2009: {data['Rainfall']} mm")
    #print(complete_dictionnary)
    #for year, month in complete_dictionnary.items():
    #    print (f"1: {year}")
    #    for i,j in month.items():
    #        print(f"\t2: {i}")
    #        for l,k in j.items():
    #            print(f"\t\t3: {l}")
    #            if l=='2010':
    #                for m,n in k.items():
    #                    print(f"\t\t\t4: {m}")
    #                    for o,p in n.items():
    #                        print (f"\t\t\t\t5: {o}")
    #                        if o!="Atmospheric deposition" and o!="Pruned frond" and o!="Mineral nitrogen fertilizer" and o!="February" and o!="March" and o!="April" and o!="May" and o!="June" and o!="July" and o!="August" and o!="September" and o!="October" and o!="November" and o!="December" and o!="Yield":
    #                            for q,r in p.items():
    #                                print(f"\t\t\t\t\t6: {q}")
    #                                if o!="Organic fertilizer" and o!="Understorey":
    #                                    for s,t in r.items():
    #                                        print(f"\t\t\t\t\t\t7: {s}")

    #print(complete_dictionnary['Field information']['Year']['2008'])


dictionnary_complete(1,printlist)


