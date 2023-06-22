# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 11:13:43 2023

@author: Sami
"""
import math
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure() #définition d'une figure vide
ax = fig.add_subplot(111, projection='3d') #définition des axes en tant que projection 3d


amplitude = 1 #définition de l'amplitude
frequence = 1 #définition de la fréquence
debut = 0 #point de départ de l'interval
arrive = math.pi*20 #point d'arrivé de l'interval
k = 1000 #nombre de points régulièrement espacés

y = np.linspace(debut, arrive, k) #définition d'une linspace y qui renvoie un tableau de 1000 nombres régulièrement espacés dans l'intervalle [debut, arrive]
x = amplitude*np.cos(frequence*y) #definition de la coordonnée x en tant que cosinus
z = amplitude*np.sin(frequence*y) #définition de la cordonnée y en tant que sinus

ax.plot(x,y,z) #tracé de l'hélice

plt.title("Hélice sur un cylindre dessinant un nuage de points")

plt.show()
