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
                #initialisation de l'année précédente
                prevyear=99999
                #Intégration d'un booléen pour le contrôle du format de date et année
                error = False
                #Intégration d'un compteur pour le nombre de jour de pluie
                counter=0
                for i in reader:
                    #Définition de chaque élément
                    element=i[0].split(";")
                    #Défintion des éléments de la date
                    date=element[0].split("/")
                    year=date[-1]
                    month = date[0]
                    #Conversion en integer
                    intyear=int(year)
                    intmonth=int(month)
                    #Contrôle qu'il y ait bien 12 mois
                    if intmonth>12:
                        if not error:
                            print("Month must be between 1 and 12.\nPlease convert your date in month/date/year")
                            error = True
                            exit()
                    else:
                        #Contrôle des années cumulatives
                        if intyear == prevyear or intyear == prevyear+1 or prevyear==99999 :
                            #Calcule pour chaque mois et chaque année du nombre de pluie et somme cumul pluie

                            counter=counter+1
                            print(counter)
                            print (date)
                            print (prevyear)
                        else:
                                print("Your years must be cumulative ")
                                error = True
                                exit()
                    prevyear = intyear








weatherdata()

