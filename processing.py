# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:00:57 2025

@author: Santiago Herrera
"""

import numpy as np
#import matplotlib.pyplot as plt
#from numpy.polynomial.polynomial import Polynomial


def processData(profiles):

    print('-'*40)
    print('INICIANDO PROCESAMIENTO DE LOS PERFILES DE CALIBRE')
    
    result=[]
    
    for profile in profiles:
        
        y=profile
        x=np.arange(len(y))
        coef=np.polyfit(x,y,2)
        
        
        if coef[0]>0:
            result.append('CONCAVO')
        elif coef[0]<0:
            result.append('CONVEXO')
        else:
            result.append('PLANO')
            
            
    print('-->',result)
    
    print('PROCESAMIENTO DE PERFILES DE CALIBRE FINALIZADA')        
    print('-'*40)
            
    return(result)
        
"""
# Generar puntos ajustados
x_fit = np.linspace(min(x), max(x), 600)
y_fit = Polynomial(x_fit)
 
# Graficar
figure=plt.figure(figsize=(15,7))
plt.scatter(x, y, label='Datos Originales', color='blue')
plt.plot(x_fit, y_fit, label='Polinomio Ajustado', color='red')
plt.xlabel('Data Box')
plt.ylabel('Caliper')
plt.title('Regresión Polinómica')
plt.legend()
plt.show()
"""
