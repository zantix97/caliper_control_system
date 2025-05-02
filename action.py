# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 08:23:55 2025

@author: Santiago Herrera
"""

#from opcua import Client 
import time
import config


def controlAction(result,client,node_id_concavo,node_id_convexo):
    print('-'*40)
    print('INICIO DE ACCIÓN DE CONTROL')        
    
    pulse_time=config.PULSE_TIME
    
    if all(valor=='CONCAVO' for valor in result):
        
        print('-->PERFIL DE CALIBRE CONCAVO')
        
        try:

            node_concavo=client.get_node(node_id_concavo)
            node_concavo.set_value(1)
            time.sleep(pulse_time)
            node_concavo.set_value(0)
            
            
        except Exception as e:
            print("Error:", e)
         
        
            
            
    elif all(valor=='CONVEXO' for valor in result):
        
        print('-->PERFIL DE CALIBRE CONVEXO')
        
        try:
            
            node_convexo=client.get_node(node_id_convexo)
            node_convexo.set_value(1)
            time.sleep(pulse_time)
            node_convexo.set_value(0)
            
            
        except Exception as e:
            print("Error:", e)
         
            
            
    else:
        print('-->WARNING: LA CONCAVIDAD DEL PERFIL DE CALIBRE ESTA OSCILANDO \n NO SE TOMARA ACCIÓN DE CONTROL')
        
    print('ACCIÓN DE CONTROL FINALIZADA')        
    print('-'*40)
    
