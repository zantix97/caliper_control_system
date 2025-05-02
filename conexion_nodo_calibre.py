# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 13:48:25 2025

@author: Superuser
"""

from opcua import Client
 
# Dirección del servidor OPC UA (reemplaza con la dirección de tu sistema QCS)
server_url = "opc.tcp://pm4opctd80:57888"
client = Client(server_url)
 
try:
    # Conectarse al servidor OPC UA
    client.connect()
    print("Conexión exitosa al servidor OPC UA.")
    """
    # Acceder al nodo que contiene el array (reemplaza con el NodeId de tu sistema)
    node_id = "ns=3;s=PM4CSQCS21->AccuRay.Object.Server.1->PM4.AC450B.FRAME1.CALIPER1.COMPPROF.ProfileArray"  # Modifica según tu sistema QCS
    node = client.get_node(node_id)
 
    # Leer el valor del nodo
    array_value = node.get_value()
    """
    # Imprimir o procesar el array
    #print("Array de perfil de calibre:", array_value)
    """
    # Si deseas trabajar con numpy para manipular el array
    import numpy as np
    array_numpy = np.array(array_value)
    print("Array como numpy:", array_numpy)
    """
    
    #node_id_2="ns=3;s=192.168.10.2->RSLinx Remote OPC Server->[WIS]test"
    node_id_2="ns=3;s=192.168.10.2->RSLinx OPC Server->[Gateway]Watchdog_Control_Corona"
    node_2=client.get_node(node_id_2)
    node_2.set_value(1000)
    print(node_2.get_value())
    
except Exception as e:
    print("Error:", e)
 
finally:
    # Desconectarse del servidor
    client.disconnect()
    print("Desconectado del servidor OPC UA.")
    
    