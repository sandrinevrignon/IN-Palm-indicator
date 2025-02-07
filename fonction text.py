#!/usr/bin/env python3

import csv

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

    print (dictionnary)
    print(country)
    print(town)

#Sauvegarde des données dans un csv
#Faire clic
weatherdata()

