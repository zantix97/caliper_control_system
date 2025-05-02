# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 07:31:11 2025

@author: Santiago Herrera
"""

from extraction import *
from processing import *
from action import *
import config

import threading
import time
from opcua import Client 

global running, client

server_url = config.SERVER_URL

running=True
node_id_watchdog=config.NODE_ID_WATCHDOG
node_id_concavo=config.NODE_ID_CONCAVO
node_id_convexo=config.NODE_ID_CONVEXO
node_id_calibre = config.NODE_ID_CALIBRE
time_reset_control=config.TIME_RESET_CONTROL

client = Client(server_url)


def watchdog():
    while running:
        try:
            
            node_watchdog=client.get_node(node_id_watchdog)
            
            watchdog_value=0
            
            while running:
                watchdog_value+=1
                
                if watchdog_value > 1000:
                    watchdog_value=0
                
                node_watchdog.set_value(watchdog_value)
                time.sleep(1)
            
            
        except Exception as e:
            print("Error:", e)
     
    
        

def controlTask():
    while running:
        profiles=extractData(client,node_id_calibre)
        result=processData(profiles)
        controlAction(result,client,node_id_concavo,node_id_convexo)
        
        time.sleep(time_reset_control)
    
def main():
    """Función principal."""
    
    try:
        
        client.connect()
        print('Conectado al servidor OPC')
        
        
        # Crear y arrancar los hilos
        watchdog_thread = threading.Thread(target=watchdog)
        controlTask_thread = threading.Thread(target=controlTask)
 
        watchdog_thread.start()
        controlTask_thread.start()
 
        # Ejecutar indefinidamente hasta que el usuario lo detenga
        while True:
            time.sleep(0.1)  # Mantener el programa vivo
            
    except KeyboardInterrupt:
        print("Deteniendo hilos...")
        running = False  # Detener los hilos
        
        # Esperar a que los hilos terminen
        #watchdog_thread.join()
        #controlTask_thread.join()
 
    finally:
        client.disconnect()
        print("Ejecución finalizada")


if __name__ == "__main__":
    main()
