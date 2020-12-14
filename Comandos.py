# ----------------------------------------------
# Proyecto Final
# ----------------------------------------------
# Importación de librerias
from gpiozero import RGBLED
from gpiozero import LED
from datetime import datetime
from time import sleep
from datetime import time
import calendar
import paho.mqtt.client as mqtt
import paho.mqtt.client as paho
from Solo_funciones import*
from Control_luces import*

####################################################
# --------- Funciones del protocolo MQTT -----------
####################################################

def PRUEBA(objeto):
    print(objeto)

def conectado(client, userdata, flags, rc):
    print("CONECTADO A EL AULA Codigo de respuesta: "+str(rc))
    cliente.subscribe("Aula")

# ------------ Conexión del cliente -----------------
#------------ Datos del broker MQTT -----------------

broker = "192.168.1.30"
puerto = 5050

#------------ CICLO -----------------

while(True):
    print("SALON AAAAA")
    print(Aula_A_Lunes)
    print(Aula_A_Martes)
    print(Aula_A_Miercoles)
    print(Aula_A_Jueves)
    print(Aula_A_Viernes)
    print("SALON BBBB")
    print(Aula_B_Lunes)
    print(Aula_B_Martes)
    print(Aula_B_Miercoles)
    print(Aula_B_Jueves)
    print(Aula_B_Viernes)
    print("SALON CCCC")
    print(Aula_C_Lunes)
    print(Aula_C_Martes)
    print(Aula_C_Miercoles)
    print(Aula_C_Jueves)
    print(Aula_C_Viernes)
# --------------------- ESpera de comando ------------------------
    cliente = mqtt.Client()
    cliente.connect(broker,puerto)
    cliente.on_connect = conectado
    cliente.on_message = mensajeMQTT_AULA
    cliente.loop_forever()
# -----------------------------------------------------------------
    print("SALON AAAAA")
    print(Aula_A_Lunes)
    print(Aula_A_Martes)
    print(Aula_A_Miercoles)
    print(Aula_A_Jueves)
    print(Aula_A_Viernes)
    print("SALON BBBB")
    print(Aula_B_Lunes)
    print(Aula_B_Martes)
    print(Aula_B_Miercoles)
    print(Aula_B_Jueves)
    print(Aula_B_Viernes)
    print("SALON CCCC")
    print(Aula_C_Lunes)
    print(Aula_C_Martes)
    print(Aula_C_Miercoles)
    print(Aula_C_Jueves)
    print(Aula_C_Viernes)
    print("SALIMOS DE FINALLLLLLLLLLLLLLLLLL")
    c =input("¿Quieres seguir modificando? [S/s] ")
    if c == "S" or c == "s":
        continue
    Control_Luces(Aula_A_Lunes,Aula_A_Martes,Aula_A_Miercoles,Aula_A_Jueves,Aula_A_Viernes,
        Aula_B_Lunes,Aula_B_Martes,Aula_B_Miercoles,Aula_B_Jueves,Aula_B_Viernes,
        Aula_C_Lunes,Aula_C_Martes,Aula_C_Miercoles,Aula_C_Jueves,Aula_C_Viernes,FERIADO['Dia'])

