import numpy
import skfuzzy as fuzz
import matplotlib.pyplot as matplot

complete_dictionnary={'Field information':
                          {'Soil caracteristic':
                               {'Organic Carbon': 9,
                                'Texture': 'Coarse',
                                'Slope': 15.0},
                           'Land preparation':
                               {'Terraces': 'Yes',
                                'Previous': 'No (first cycle)'},
                           'Year':
                               {'2008':
                                    {'Month':
                                         {'January':
                                              {'Weather':
                                                   {'Rainfall': 12.17, 'Rain frequency': 9},
                                               'Mineral nitrogen fertilizer': {'Rate': 44.5, 'Type': 'Urea'}},
                                          'February':
                                              {'Weather': {'Rainfall': 15.51, 'Rain frequency': 8},
                                               'Mineral nitrogen fertilizer': {'Rate': 0.0, 'Type': '*None'}},
                                          'March': {'Weather': {'Rainfall': 47.76, 'Rain frequency': 15},
                                                    'Mineral nitrogen fertilizer': {'Rate': 0.0, 'Type': '*None'}},
                                          'April': {'Weather': {'Rainfall': 250.93, 'Rain frequency': 15},
                                                    'Mineral nitrogen fertilizer': {'Rate': 0.0, 'Type': '*None'}},
                                          'May': {'Weather': {'Rainfall': 199.5, 'Rain frequency': 11},
                                                  'Mineral nitrogen fertilizer': {'Rate': 0.0, 'Type': '*None'}},
                                          'June': {'Weather': {'Rainfall': 128.3, 'Rain frequency': 8},
                                                   'Mineral nitrogen fertilizer': {'Rate': 0.0, 'Type': '*None'}},
                                          'July': {'Weather': {'Rainfall': 180.0, 'Rain frequency': 8},
                                                   'Mineral nitrogen fertilizer': {'Rate': 58, 'Type': 'Urea'}},
                                          'August': {'Weather': {'Rainfall': 222.0, 'Rain frequency': 10},
                                                     'Mineral nitrogen fertilizer': {'Rate': 0.0, 'Type': '*None'}},
                                          'September': {'Weather': {'Rainfall': 317.5, 'Rain frequency': 13},
                                                        'Mineral nitrogen fertilizer': {'Rate': 0.0, 'Type': '*None'}},
                                          'October': {'Weather': {'Rainfall': 320.8, 'Rain frequency': 18},
                                                      'Mineral nitrogen fertilizer': {'Rate': 0.0, 'Type': '*None'}},
                                          'November': {'Weather': {'Rainfall': 153.4, 'Rain frequency': 9},
                                                       'Mineral nitrogen fertilizer': {'Rate': 0.0, 'Type': '*None'}},
                                          'December': {'Weather': {'Rainfall': 170.5, 'Rain frequency': 11},
                                                       'Mineral nitrogen fertilizer': {'Rate': 0.0, 'Type': '*None'}}},
                                     'General data': {'Mineral nitrogen fertilizer': 'In the circle, buried',
                                                      'Organic fertilizer': {'Quantity': None, 'Type': '*Choice*', 'Placement': '*Choice*'},
                                                      'Understorey': {'Biomass': '*Choice*', 'Legume fraction': '*Choice*'},
                                                      'Atmospheric deposition': 18.0}},
                                '2009':
                                    {'Month':
                                         {'January':
                                              {'Weather':
                                                   {'Rainfall': 107.5, 'Rain frequency': 8},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'February':
                                              {'Weather':
                                                   {'Rainfall': 113.7, 'Rain frequency': 13},
                                               'Mineral nitrogen fertilizer': {'Rate': 0.0, 'Type': '*None'}},
                                          'March':
                                              {'Weather':
                                                   {'Rainfall': 115.89, 'Rain frequency': 13},
                                               'Mineral nitrogen fertilizer': {'Rate': 0.0, 'Type': '*None'}},
                                          'April':
                                              {'Weather':
                                                   {'Rainfall': 301.5, 'Rain frequency': 13},
                                               'Mineral nitrogen fertilizer': {'Rate': 0.0, 'Type': '*None'}},
                                          'May':
                                              {'Weather':
                                                   {'Rainfall': 76.4, 'Rain frequency': 9},
                                               'Mineral nitrogen fertilizer': {'Rate': 0.0, 'Type': '*None'}},
                                          'June':
                                              {'Weather':
                                                   {'Rainfall': 211.4, 'Rain frequency': 8},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'July':
                                              {'Weather':
                                                   {'Rainfall': 152.0, 'Rain frequency': 5},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'August':
                                              {'Weather':
                                                   {'Rainfall': 318.5, 'Rain frequency': 8},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'September':
                                              {'Weather':
                                                   {'Rainfall': 187.5, 'Rain frequency': 10},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'October':
                                              {'Weather':
                                                   {'Rainfall': 465.5, 'Rain frequency': 16},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'November':
                                              {'Weather':
                                                   {'Rainfall': 223.5, 'Rain frequency': 13},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'December':
                                              {'Weather':
                                                   {'Rainfall': 588.5, 'Rain frequency': 15},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}}},
                                     'General data':
                                         {'Mineral nitrogen fertilizer': '*Choice*',
                                          'Organic fertilizer':
                                              {'Quantity': None, 'Type': '*Choice*', 'Placement': '*Choice*'},
                                          'Understorey':
                                              {'Biomass': '*Choice*', 'Legume fraction': '*Choice*'},
                                          'Atmospheric deposition': 18.0}},
                                '2010':
                                    {'Month':
                                         {'January':
                                              {'Weather':
                                                   {'Rainfall': 329.5, 'Rain frequency': 16},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'February':
                                              {'Weather':
                                                   {'Rainfall': 127.0, 'Rain frequency': 11},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'March':
                                              {'Weather':
                                                   {'Rainfall': 398.7, 'Rain frequency': 17},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'April':
                                              {'Weather':
                                                   {'Rainfall': 282.5, 'Rain frequency': 14},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'May':
                                              {'Weather':
                                                   {'Rainfall': 170.5, 'Rain frequency': 11},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'June':
                                              {'Weather':
                                                   {'Rainfall': 101.5, 'Rain frequency': 6},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'July':
                                              {'Weather':
                                                   {'Rainfall': 150.0, 'Rain frequency': 14},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'August':
                                              {'Weather':
                                                   {'Rainfall': 245.5, 'Rain frequency': 14},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'September':
                                              {'Weather':
                                                   {'Rainfall': 230.1, 'Rain frequency': 12},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'October':
                                              {'Weather':
                                                   {'Rainfall': 215.0, 'Rain frequency': 12},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'November':
                                              {'Weather':
                                                   {'Rainfall': 224.4, 'Rain frequency': 15},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'December':
                                              {'Weather':
                                                   {'Rainfall': 90.0, 'Rain frequency': 10},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 180, 'Type': 'Ammo Nit'}}},
                                     'General data': {'Mineral nitrogen fertilizer': 'In the circle, not buried',
                                                      'Organic fertilizer':
                                                          {'Quantity': None, 'Type': '*Choice*', 'Placement': '*Choice*'},
                                                      'Understorey': {'Biomass': '*Choice*', 'Legume fraction': '*Choice*'},
                                                      'Atmospheric deposition': 18.0, 'Pruned frond': '*Choice*', 'Yield': 0.0}},
                                '2011':
                                    {'Month':
                                         {'January':
                                              {'Weather':
                                                   {'Rainfall': 269.0, 'Rain frequency': 21},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'February':
                                              {'Weather':
                                                   {'Rainfall': 127.4, 'Rain frequency': 6},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'March':
                                              {'Weather':
                                                   {'Rainfall': 230.6, 'Rain frequency': 15},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'April':
                                              {'Weather':
                                                   {'Rainfall': 208.4, 'Rain frequency': 17},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 200, 'Type': 'Ammo Sulf'}},
                                          'May':
                                              {'Weather':
                                                   {'Rainfall': 104.3, 'Rain frequency': 10},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'June':
                                              {'Weather':
                                                   {'Rainfall': 72.2, 'Rain frequency': 6},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'July':
                                              {'Weather':
                                                   {'Rainfall': 30.1, 'Rain frequency': 6},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'August':
                                              {'Weather':
                                                   {'Rainfall': 100.0, 'Rain frequency': 6},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'September':
                                              {'Weather':
                                                   {'Rainfall': 201.8, 'Rain frequency': 11},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'October':
                                              {'Weather':
                                                   {'Rainfall': 413.0, 'Rain frequency': 16},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'November':
                                              {'Weather':
                                                   {'Rainfall': 233.2, 'Rain frequency': 17},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'December':
                                              {'Weather':
                                                   {'Rainfall': 249.0, 'Rain frequency': 20},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}}},
                                     'General data':
                                         {'Mineral nitrogen fertilizer': 'In the circle + windrow', 'Organic fertilizer':
                                             {'Quantity': None, 'Type': '*Choice*', 'Placement': '*Choice*'},
                                          'Understorey':
                                              {'Biomass': '*Choice*', 'Legume fraction': '*Choice*'},
                                          'Atmospheric deposition': 18.0, 'Pruned frond': '*Choice*', 'Yield': 0.0}},
                                '2012':
                                    {'Month':
                                         {'January':
                                              {'Weather':
                                                   {'Rainfall': 145.3, 'Rain frequency': 14},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'February':
                                              {'Weather':
                                                   {'Rainfall': 187.9, 'Rain frequency': 18},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'March':
                                              {'Weather':
                                                   {'Rainfall': 170.4, 'Rain frequency': 15},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'April':
                                              {'Weather':
                                                   {'Rainfall': 229.9, 'Rain frequency': 12},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'May':
                                              {'Weather':
                                                   {'Rainfall': 117.4, 'Rain frequency': 9},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 200, 'Type': 'Urea'}},
                                          'June':
                                              {'Weather':
                                                   {'Rainfall': 52.1, 'Rain frequency': 8},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'July':
                                              {'Weather':
                                                   {'Rainfall': 78.5, 'Rain frequency': 11},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'August':
                                              {'Weather':
                                                   {'Rainfall': 264.1, 'Rain frequency': 12},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 600, 'Type': 'Sod Nit'}},
                                          'September':
                                              {'Weather':
                                                   {'Rainfall': 156.46, 'Rain frequency': 8},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'October':
                                              {'Weather':
                                                   {'Rainfall': 277.2, 'Rain frequency': 16},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'November':
                                              {'Weather':
                                                   {'Rainfall': 392.5, 'Rain frequency': 21},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'December':
                                              {'Weather':
                                                   {'Rainfall': 542.0, 'Rain frequency': 15},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}}},
                                     'General data':
                                         {'Mineral nitrogen fertilizer': 'Evenly distributed',
                                          'Organic fertilizer':
                                              {'Quantity': None, 'Type': '*Choice*', 'Placement': '*Choice*'},
                                          'Understorey':
                                              {'Biomass': '*Choice*', 'Legume fraction': '*Choice*'},
                                          'Atmospheric deposition': 18.0, 'Pruned frond': '*Choice*', 'Yield': 0.0}},
                                '2013':
                                    {'Month':
                                         {'January':
                                              {'Weather':
                                                   {'Rainfall': 195.5, 'Rain frequency': 12},
                                               'Mineral nitrogen fertilizer': {'Rate': 0.0, 'Type': '*None'}},
                                          'February':
                                              {'Weather':
                                                   {'Rainfall': 168.8, 'Rain frequency': 16},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'March':
                                              {'Weather':
                                                   {'Rainfall': 242.6, 'Rain frequency': 12},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'April':
                                              {'Weather':
                                                   {'Rainfall': 227.8, 'Rain frequency': 12},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'May':
                                              {'Weather':
                                                   {'Rainfall': 247.7, 'Rain frequency': 13},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'June':
                                              {'Weather':
                                                   {'Rainfall': 90.0, 'Rain frequency': 7},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'July':
                                              {'Weather':
                                                   {'Rainfall': 82.5, 'Rain frequency': 4},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'August':
                                              {'Weather':
                                                   {'Rainfall': 111.9, 'Rain frequency': 7},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'September':
                                              {'Weather':
                                                   {'Rainfall': 248.4, 'Rain frequency': 11},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'October':
                                              {'Weather':
                                                   {'Rainfall': 309.1, 'Rain frequency': 18},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'November':
                                              {'Weather':
                                                   {'Rainfall': 477.5, 'Rain frequency': 20},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'December':
                                              {'Weather':
                                                   {'Rainfall': 326.7, 'Rain frequency': 14},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}}},
                                     'General data':
                                         {'Mineral nitrogen fertilizer': '*Choice*',
                                          'Organic fertilizer':
                                              {'Quantity': None, 'Type': '*Choice*', 'Placement': '*Choice*'},
                                          'Understorey': {'Biomass': '*Choice*', 'Legume fraction': '*Choice*'},
                                          'Atmospheric deposition': 18.0, 'Pruned frond': '*Choice*', 'Yield': 0.0}},
                                '2014':
                                    {'Month':
                                         {'January':
                                              {'Weather':
                                                   {'Rainfall': 269.3, 'Rain frequency': 8},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'February':
                                              {'Weather':
                                                   {'Rainfall': 4.0, 'Rain frequency': 1},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'March':
                                              {'Weather':
                                                   {'Rainfall': 107.8, 'Rain frequency': 7},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'April':
                                              {'Weather':
                                                   {'Rainfall': 157.2, 'Rain frequency': 15},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'May':
                                              {'Weather':
                                                   {'Rainfall': 230.6, 'Rain frequency': 14},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'June':
                                              {'Weather':
                                                   {'Rainfall': 131.0, 'Rain frequency': 4},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'July':
                                              {'Weather':
                                                   {'Rainfall': 68.7, 'Rain frequency': 7},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'August':
                                              {'Weather':
                                                   {'Rainfall': 176.9, 'Rain frequency': 13},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'September':
                                              {'Weather':
                                                   {'Rainfall': 143.6, 'Rain frequency': 7},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'October':
                                              {'Weather':
                                                   {'Rainfall': 132.5, 'Rain frequency': 13},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'November':
                                              {'Weather':
                                                   {'Rainfall': 319.6, 'Rain frequency': 19},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'December':
                                              {'Weather':
                                                   {'Rainfall': 405.5, 'Rain frequency': 16},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}}},
                                     'General data':
                                         {'Mineral nitrogen fertilizer': '*Choice*',
                                          'Organic fertilizer':
                                              {'Quantity': None, 'Type': '*Choice*', 'Placement': '*Choice*'},
                                          'Understorey': {'Biomass': '*Choice*', 'Legume fraction': '*Choice*'},
                                          'Atmospheric deposition': 18.0, 'Pruned frond': '*Choice*', 'Yield': 0.0}},
                                '2015':
                                    {'Month':
                                         {'January':
                                              {'Weather':
                                                   {'Rainfall': 92.5, 'Rain frequency': 11},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'February':
                                              {'Weather':
                                                   {'Rainfall': 29.0, 'Rain frequency': 2},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'March':
                                              {'Weather':
                                                   {'Rainfall': 138.2, 'Rain frequency': 13},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'April':
                                              {'Weather':
                                                   {'Rainfall': 208.1, 'Rain frequency': 14},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'May':
                                              {'Weather':
                                                   {'Rainfall': 158.9, 'Rain frequency': 12},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'June':
                                              {'Weather':
                                                   {'Rainfall': 83.9, 'Rain frequency': 10},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'July':
                                              {'Weather':
                                                   {'Rainfall': 84.5, 'Rain frequency': 4},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'August':
                                              {'Weather':
                                                   {'Rainfall': 34.2, 'Rain frequency': 8},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'September':
                                              {'Weather':
                                                   {'Rainfall': 155.7, 'Rain frequency': 7},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'October':
                                              {'Weather':
                                                   {'Rainfall': 130.9, 'Rain frequency': 7},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'November':
                                              {'Weather':
                                                   {'Rainfall': 413.9, 'Rain frequency': 19},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}},
                                          'December':
                                              {'Weather':
                                                   {'Rainfall': 197.6, 'Rain frequency': 12},
                                               'Mineral nitrogen fertilizer':
                                                   {'Rate': 0.0, 'Type': '*None'}}},
                                     'General data':
                                         {'Mineral nitrogen fertilizer': '*Choice*',
                                          'Organic fertilizer':
                                              {'Quantity': None, 'Type': '*Choice*', 'Placement': '*Choice*'},
                                          'Understorey': {'Biomass': '*Choice*', 'Legume fraction': '*Choice*'},
                                          'Atmospheric deposition': 18.0, 'Pruned frond': '*Choice*', 'Yield': 0.0}}}}}

###############################################################
#########################################FUzzy models
####Attention retirer le dictionnaire en entrée de la fonction

def R_NH3_Mineral1_1(countfounction,complete_dictionnary):
    #Définition des plages de données pour construction des fonctions d'appartenance
    data_range=numpy.arange(0,1.01,0.01)

    # Définition des fonctions d'appartenance cosinusidale
    ##########Fonction favorable
    def favourable_membership(data_range):
        return (1 / 2) * (1 + numpy.cos(data_range * numpy.pi + numpy.pi))
    ##########Fonction d'appartenance défavorable
    def unfavourable_membership(data_range):
        return (1 / 2) * (1 + numpy.cos(data_range * numpy.pi))

    ############### Tracage des fonctions d'appartenance
    #matplot.plot(data_range, favourable_membership(data_range), label="Favourable")
    #matplot.plot(data_range, unfavourable_membership(data_range), label="Unfavourable")
    #matplot.title("Fonctions d'appartenance")
    #matplot.xlabel("Normalized input data")
    #matplot.ylabel("Appartenance")
    #matplot.legend()
    #matplot.show()

    #Normalisation des données d'entrée

    #Fonction pour la normalisation texture du sol
    def normTexture_function():
        #Pour les infos niveau 1
        for field, caract in complete_dictionnary.items():
            #Recherche information texture
            for  typ,info in caract.items():
                if typ=="Soil caracteristic":
                    for soilcaract, soilcaract_info in info.items():

                        #Normalisation de la texture
                        if soilcaract=="Texture":
                            if soilcaract_info=="Fine":
                                normTexture=1
                            elif soilcaract_info=="Medium":
                                normTexture=0.5
                            else:
                                normTexture=0
        return normTexture


    #Fonction normalisation age de la plantation
    def normage_function():
        #Définition des variables
        normage = []
        age=0
        #Recherche de l'année de plantation
        for field, caract in complete_dictionnary.items():
            for typ, info in caract.items():
                # Si l'info niveau 2 == year
                if typ == "Year":
                    for year, year_info in info.items():
                        age = age + 1
                        ##Normalisation de l'age
                        if age <= 4:
                            normage.append(0)
                        elif age > 4 and age < 10:
                            normage.append(round(((age - 4) / (10 - 4)), 2))
                        elif age >= 10:
                            normage.append(1)
        return normage

    #Fonction pour la ferti minerale placement
    def normMinferNPlacement_function():
        # Définition des variables
        normMinNplacement=[]
        # Recherche de l'info placement ferti minerale
        for field, caract in complete_dictionnary.items():
            for typ, info in caract.items():
                if typ == "Year":
                    for year, year_info in info.items():
                        for monthgeneral, monthgeneral_info in year_info.items():
                            if monthgeneral == "General data":
                                for data, data_info in monthgeneral_info.items():
                                    if data == "Mineral nitrogen fertilizer":

                                        # Normalisation de MinNferti placement
                                        if data_info not in ["In the circle, buried", "*Choice*"]:
                                            normMinNplacement.append(0)
                                        else:
                                            normMinNplacement.append(1)
        return normMinNplacement

    #Fonction pour ferti mineral type
    def normMinferNType_function():
        # Définition des variables
        normMinNtype = []
        # Recherche de l'info placement ferti minerale
        for field, caract in complete_dictionnary.items():
            for typ, info in caract.items():
                if typ == "Year":
                    for year, year_info in info.items():
                        for monthgeneral, monthgeneral_info in year_info.items():
                            # Recherche pour les informations mensuelles
                            if monthgeneral == "Month":
                                for months, months_info in monthgeneral_info.items():
                                    for weather_minnitro, weather_minnitro_info in months_info.items():
                                        # Recherche de mineralN type
                                        if weather_minnitro == "Mineral nitrogen fertilizer":
                                            for ratetype, ratetype_info in weather_minnitro_info.items():
                                                # Normalisation minNtype
                                                if ratetype == "Type":
                                                    if ratetype_info == "Urea":
                                                        normMinNtype.append(0)
                                                    else:
                                                        normMinNtype.append(1)
        return normMinNtype

    #Fonction pour nb de jour pluie
    def normrainfreq_function():
        # Définition des variables
        normrainfreq = []
        # Recherche de l'info placement ferti minerale
        for field, caract in complete_dictionnary.items():
            for typ, info in caract.items():
                if typ == "Year":
                    for year, year_info in info.items():
                        for monthgeneral, monthgeneral_info in year_info.items():
                            # Recherche pour les informations mensuelles
                            if monthgeneral == "Month":
                                for months, months_info in monthgeneral_info.items():
                                    for weather_minnitro, weather_minnitro_info in months_info.items():
                                        # Recherche de mineralN type
                                        if weather_minnitro == "Weather":
                                            for weather, weather_info in weather_minnitro_info.items():

                                                # Normalisation de rain frequency
                                                if weather == "Rain frequency":
                                                    if weather_info <= 7.5:
                                                        normrainfreq.append(0)
                                                    elif weather_info > 7.5 and weather_info < 30:
                                                        normrainfreq.append(round((weather_info - 7.5) / (30 - 7.5), 2))
                                                    elif weather_info >= 30:
                                                        normrainfreq.append(1)
        return normrainfreq

    #Fuzzification des données
    ####Texture
    Rule_Texture_favourable=fuzz.interp_membership(data_range,favourable_membership(data_range),normTexture_function())
    Rule_Texture_unfavourable=fuzz.interp_membership(data_range,unfavourable_membership(data_range),normTexture_function())

    ####Age plantation
    Rule_Age_favourable=[]
    Rule_Age_unfavourable=[]
    for i in normage_function():
        Rule_Age_favourable.append(float(round(fuzz.interp_membership(data_range, favourable_membership(data_range), i),2)))
        Rule_Age_unfavourable.append(float(round(fuzz.interp_membership(data_range, unfavourable_membership(data_range), i),2)))

    ####MinNfertiPlacement
    Rule_MinNfertiPlacement_favourable=[]
    Rule_MinNfertiPlacement_unfavourable = []
    for i in normMinferNPlacement_function():
        Rule_MinNfertiPlacement_favourable.append(float(round(fuzz.interp_membership(data_range, favourable_membership(data_range), i),2)))
        Rule_MinNfertiPlacement_unfavourable.append(float(round(fuzz.interp_membership(data_range, unfavourable_membership(data_range), i), 2)))

    ####MinNfertiType
    Rule_MinNfertiType_favourable = []
    Rule_MinNfertiType_unfavourable = []
    for i in normMinferNType_function():
        Rule_MinNfertiType_favourable.append(float(round(fuzz.interp_membership(data_range, favourable_membership(data_range), i),2)))
        Rule_MinNfertiType_unfavourable.append(float(round(fuzz.interp_membership(data_range, unfavourable_membership(data_range), i), 2)))

    ####Rain frequency
    Rule_RainFrequency_favourable = []
    Rule_RainFrequency_unfavourable = []
    for i in normrainfreq_function():
        Rule_RainFrequency_favourable.append(float(round(fuzz.interp_membership(data_range, favourable_membership(data_range), i), 2)))
        Rule_RainFrequency_unfavourable.append(float(round(fuzz.interp_membership(data_range, unfavourable_membership(data_range), i), 2)))

    #Application des règles floues





    print(f"\n{normage_function()}")
    print(normTexture_function())
    print(normMinferNPlacement_function())
    print(normMinferNType_function())
    print(normrainfreq_function())


R_NH3_Mineral1_1(0,complete_dictionnary)