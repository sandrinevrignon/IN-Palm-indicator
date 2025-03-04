import numpy
import skfuzzy as fuzz
import matplotlib.pyplot as matplot

##############################Dictionnaire exemple pour test fonction
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
                                               'Mineral nitrogen fertilizer': {'Rate': 20, 'Type': 'Urea'}},
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
                                                   'Mineral nitrogen fertilizer': {'Rate': 27, 'Type': 'Urea'}},
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
                                                   {'Rate': 61, 'Type': 'Ammo Nit'}}},
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
                                                   {'Rate': 42, 'Type': 'Ammo Sulf'}},
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
                                                   {'Rate': 115, 'Type': 'Urea'}},
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
                                                   {'Rate': 96, 'Type': 'Sod Nit'}},
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
def Fraction_of_soil_covered_2_1 (complete_dictionnary) :
    print("ok")




Fraction_of_soil_covered_2_1 (complete_dictionnary)


