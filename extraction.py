# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:43:13 2025

@author: Santiago Herrera
"""

#from opcua import Client
import time
import config

def extractData(client,node_id_calibre):
    #Definicion de variables de funcionamiento
    scan_number=config.SCAN_NUMBER
    sample_interval=config.SAMPLE_INTERVAL
    

    #Lista donde se almacenaran los perfiles de calibre
    profiles=[]
    
    print('-'*40)
    print('INICIANDO EXTRACCION DE LOS PERFILES DE CALIBRE')
    

    try:
        
        node_calibre = client.get_node(node_id_calibre)
     
        # agregamos el primer perfil de calibre
        profiles.append(node_calibre.get_value())
        
        print('-->Perfil 1 agregado')
        
        while len(profiles) < scan_number:
            
            #Espera para toma de siguiente muestra
            time.sleep(sample_interval)
            
            if profiles[-1]!=node_calibre.get_value():
                profiles.append(node_calibre.get_value())
                print('-->perfil {} agregado'.format(len(profiles)))
                
                
        print('EXTRACCION DE PERFILES DE CALIBRE FINALIZADA')        
        print('-'*40)
       
        
    except Exception as e:
        print("Error:", e)
     
        

    return(profiles)
    
    
