#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created 

@author: macbookpro
"""
import numpy as np
import matplotlib.pyplot as plt

# Generar datos aleatorios
np.random.seed(43)
data = np.random.normal(0, 1, 1000)
data.min()
data.max()
data.mean()
data.std()
len(data)

# Crear el histograma
plt.hist(data, bins=30)

# Personalizar el aspecto del histograma
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Histograma')

# Mostrar el histograma
plt.show()

############################################################
############################################################
############################################################

import matplotlib.pyplot as plt

import random

lista = [random.uniform(20, 30) for _ in range(25)] + \
        [random.uniform(30, 40) for _ in range(30)] + \
        [random.uniform(40, 50) for _ in range(15)] + \
        [random.uniform(50, 60) for _ in range(20)]

print(lista)

lista_nueva = [round(num, 0) for num in lista]

print(lista_nueva)

# Datos de ejemplo de las edades y sus frecuencias
edades = ['20-30', '30-40', '40-50', '50-60']
frecuencias = [-1, -1, -1, -1]
frecuencias[0]=sum(1 for valor in lista_nueva if valor >= 20 and valor <30)
frecuencias[1]=sum(1 for valor in lista_nueva if valor >= 30 and valor <40)
frecuencias[2]=sum(1 for valor in lista_nueva if valor >= 40 and valor <50)
frecuencias[3]=sum(1 for valor in lista_nueva if valor >= 50 and valor <60)

# Crear el gráfico de pie
plt.pie(frecuencias, labels=edades, autopct='%1.1f%%')

# Personalizar el aspecto del gráfico
plt.axis('equal')  # Para asegurar que el gráfico de pie se muestre como un círculo
plt.title('Distribución de Edades')

# Mostrar el gráfico
plt.show()
