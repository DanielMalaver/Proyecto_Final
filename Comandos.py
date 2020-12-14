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
SALIDA = {'Control':0}

def conectado(client, userdata, flags, rc):
    print("CONECTADO A EL AULA Codigo de respuesta: "+str(rc))
    cliente.subscribe("Horario")

def conectadoPantalla(client, userdata, flags, rc):
    print("Conectado a Pantalla de control Codigo de respuesta: "+str(rc))
    cliente.subscribe("Pantalla_de_control")

def mensajeMQTT_Pantalla(client, userdata, msg):
    recibido = msg.payload.decode()
    if recibido == "S" or recibido == "s":
        SALIDA['Control'] = "S"
    else:
        SALIDA['Control'] = "N"
    client.disconnect()

# ------------ Conexión del cliente -----------------
#------------ Datos del broker MQTT -----------------

broker = "192.168.1.30"
puerto = 5050

#------------ CICLO -----------------

while(True):
#------------ Imprime horario inicial a modo de comprobacion -----------------
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
# --------------------- Solicita y recibe comando ------------------------
    Pantalla = "Ingrese un comando o ingrese la letra x para continuar:\n"
    cliente = paho.Client()
    cliente.connect(broker,puerto)
    mensaje = cliente.publish("Pantalla_de_control",Pantalla)
    cliente = mqtt.Client()
    cliente.connect(broker,puerto)
    cliente.on_connect = conectado
    cliente.on_message = mensajeMQTT_Horario
    cliente.loop_forever()
# -----------------------------------------------------------------
#------------ Imprime horariomodificado a modo de comprobacion -----------------
    print("SALON A")
    print(Aula_A_Lunes)
    print(Aula_A_Martes)
    print(Aula_A_Miercoles)
    print(Aula_A_Jueves)
    print(Aula_A_Viernes)
    print("SALON B")
    print(Aula_B_Lunes)
    print(Aula_B_Martes)
    print(Aula_B_Miercoles)
    print(Aula_B_Jueves)
    print(Aula_B_Viernes)
    print("SALON C")
    print(Aula_C_Lunes)
    print(Aula_C_Martes)
    print(Aula_C_Miercoles)
    print(Aula_C_Jueves)
    print(Aula_C_Viernes)

# --------- Mostrar en Pantalla de control ---------------------
    Pantalla = "¿Quieres continuar en la pantalla de control?"
    cliente = paho.Client()
    cliente.connect(broker,puerto)
    mensaje = cliente.publish("Pantalla_de_control",Pantalla)
#---------------------------------------------------------------
# ----------Ingresar respuesta ---------------------------------
    cliente = mqtt.Client()
    cliente.connect(broker,puerto)
    cliente.on_connect = conectadoPantalla
    cliente.on_message = mensajeMQTT_Pantalla
    cliente.loop_forever()
# ------------------------------------------------------------------
# ------ Comienza a correr el cronometro y el control de luces ------------------------------------
    if SALIDA['Control'] == "S" or SALIDA['Control'] == "s":
        continue
    Control_Luces(Aula_A_Lunes,Aula_A_Martes,Aula_A_Miercoles,Aula_A_Jueves,Aula_A_Viernes,
        Aula_B_Lunes,Aula_B_Martes,Aula_B_Miercoles,Aula_B_Jueves,Aula_B_Viernes,
        Aula_C_Lunes,Aula_C_Martes,Aula_C_Miercoles,Aula_C_Jueves,Aula_C_Viernes,FERIADO['Dia'])

