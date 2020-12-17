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
import csv

####################################################
# -------- Funciones de Control de Comandos --------
####################################################


# --------- Funcion para cambiar por completo las clases de un bloque en particular --------
def COMANDOCambiarBloque(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
    try:
        if recibido[22] == "A":
            LUNES[recibido[22]] = int(recibido[30])
            MARTES[recibido[22]] = int(recibido[39])
            MIERCOLES[recibido[22]] = int(recibido[51])
            JUEVES[recibido[22]] = int(recibido[60])
            VIERNES[recibido[22]] = int(recibido[70])
            if recibido[0] == "A":
                Aula_A_Lunes['A'] = LUNES[recibido[22]]
                Aula_A_Martes['A'] = MARTES[recibido[22]]
                Aula_A_Miercoles['A'] = MIERCOLES[recibido[22]]
                Aula_A_Jueves['A'] = JUEVES[recibido[22]]
                Aula_A_Viernes['A'] = VIERNES[recibido[22]]
            elif recibido[0] == "B":
                Aula_B_Lunes['A'] = LUNES[recibido[22]]
                Aula_B_Martes['A'] = MARTES[recibido[22]]
                Aula_B_Miercoles['A'] = MIERCOLES[recibido[22]]
                Aula_B_Jueves['A'] = JUEVES[recibido[22]]
                Aula_B_Viernes['A'] = VIERNES[recibido[22]]
            elif recibido[0] == "C":
                Aula_C_Lunes['A'] = LUNES[recibido[22]]
                Aula_C_Martes['A'] = MARTES[recibido[22]]
                Aula_C_Miercoles['A'] = MIERCOLES[recibido[22]]
                Aula_C_Jueves['A'] = JUEVES[recibido[22]]
                Aula_C_Viernes['A'] = VIERNES[recibido[22]]
            Equivocado['Paso'] == 0

        elif recibido[22] == "B":
            LUNES[recibido[22]] = int(recibido[30])
            MARTES[recibido[22]] = int(recibido[39])
            MIERCOLES[recibido[22]] = int(recibido[51])
            JUEVES[recibido[22]] = int(recibido[60])
            VIERNES[recibido[22]] = int(recibido[70])
            if recibido[0] == "A":
                Aula_A_Lunes['B'] = LUNES[recibido[22]]
                Aula_A_Martes['B'] = MARTES[recibido[22]]
                Aula_A_Miercoles['B'] = MIERCOLES[recibido[22]]
                Aula_A_Jueves['B'] = JUEVES[recibido[22]]
                Aula_A_Viernes['B'] = VIERNES[recibido[22]]
            elif recibido[0] == "B":
                Aula_B_Lunes['B'] = LUNES[recibido[22]]
                Aula_B_Martes['B'] = MARTES[recibido[22]]
                Aula_B_Miercoles['B'] = MIERCOLES[recibido[22]]
                Aula_B_Jueves['B'] = JUEVES[recibido[22]]
                Aula_B_Viernes['B'] = VIERNES[recibido[22]]
            elif recibido[0] == "C":
                Aula_C_Lunes['B'] = LUNES[recibido[22]]
                Aula_C_Martes['B'] = MARTES[recibido[22]]
                Aula_C_Miercoles['B'] = MIERCOLES[recibido[22]]
                Aula_C_Jueves['B'] = JUEVES[recibido[22]]
                Aula_C_Viernes['B'] = VIERNES[recibido[22]]
            Equivocado['Paso'] == 0

        elif recibido[22] == "C":
            LUNES[recibido[22]] = int(recibido[30])
            MARTES[recibido[22]] = int(recibido[39])
            MIERCOLES[recibido[22]] = int(recibido[51])
            JUEVES[recibido[22]] = int(recibido[60])
            VIERNES[recibido[22]] = int(recibido[70])
            if recibido[0] == "A":
                Aula_A_Lunes['C'] = LUNES[recibido[22]]
                Aula_A_Martes['C'] = MARTES[recibido[22]]
                Aula_A_Miercoles['C'] = MIERCOLES[recibido[22]]
                Aula_A_Jueves['C'] = JUEVES[recibido[22]]
                Aula_A_Viernes['C'] = VIERNES[recibido[22]]
            elif recibido[0] == "B":
                Aula_B_Lunes['C'] = LUNES[recibido[22]]
                Aula_B_Martes['C'] = MARTES[recibido[22]]
                Aula_B_Miercoles['C'] = MIERCOLES[recibido[22]]
                Aula_B_Jueves['C'] = JUEVES[recibido[22]]
                Aula_B_Viernes['C'] = VIERNES[recibido[22]]
            elif recibido[0] == "C":
                Aula_C_Lunes['C'] = LUNES[recibido[22]]
                Aula_C_Martes['C'] = MARTES[recibido[22]]
                Aula_C_Miercoles['C'] = MIERCOLES[recibido[22]]
                Aula_C_Jueves['C'] = JUEVES[recibido[22]]
                Aula_C_Viernes['C'] = VIERNES[recibido[22]]
            Equivocado['Paso'] == 0

        elif recibido[22] == "D":
            LUNES[recibido[22]] = int(recibido[30])
            MARTES[recibido[22]] = int(recibido[39])
            MIERCOLES[recibido[22]] = int(recibido[51])
            JUEVES[recibido[22]] = int(recibido[60])
            VIERNES[recibido[22]] = int(recibido[70])
            if recibido[0] == "A":
                Aula_A_Lunes['D'] = LUNES[recibido[22]]
                Aula_A_Martes['D'] = MARTES[recibido[22]]
                Aula_A_Miercoles['D'] = MIERCOLES[recibido[22]]
                Aula_A_Jueves['D'] = JUEVES[recibido[22]]
                Aula_A_Viernes['D'] = VIERNES[recibido[22]]
            elif recibido[0] == "B":
                Aula_B_Lunes['D'] = LUNES[recibido[22]]
                Aula_B_Martes['D'] = MARTES[recibido[22]]
                Aula_B_Miercoles['D'] = MIERCOLES[recibido[22]]
                Aula_B_Jueves['D'] = JUEVES[recibido[22]]
                Aula_B_Viernes['D'] = VIERNES[recibido[22]]
            elif recibido[0] == "C":
                Aula_C_Lunes['D'] = LUNES[recibido[22]]
                Aula_C_Martes['D'] = MARTES[recibido[22]]
                Aula_C_Miercoles['D'] = MIERCOLES[recibido[22]]
                Aula_C_Jueves['D'] = JUEVES[recibido[22]]
                Aula_C_Viernes['D'] = VIERNES[recibido[22]]
            Equivocado['Paso'] == 0

        elif recibido[22] == "E":
            LUNES[recibido[22]] = int(recibido[30])
            MARTES[recibido[22]] = int(recibido[39])
            MIERCOLES[recibido[22]] = int(recibido[51])
            JUEVES[recibido[22]] = int(recibido[60])
            VIERNES[recibido[22]] = int(recibido[70])
            if recibido[0] == "A":
                Aula_A_Lunes['E'] = LUNES[recibido[22]]
                Aula_A_Martes['E'] = MARTES[recibido[22]]
                Aula_A_Miercoles['E'] = MIERCOLES[recibido[22]]
                Aula_A_Jueves['E'] = JUEVES[recibido[22]]
                Aula_A_Viernes['E'] = VIERNES[recibido[22]]
            elif recibido[0] == "B":
                Aula_B_Lunes['E'] = LUNES[recibido[22]]
                Aula_B_Martes['E'] = MARTES[recibido[22]]
                Aula_B_Miercoles['E'] = MIERCOLES[recibido[22]]
                Aula_B_Jueves['E'] = JUEVES[recibido[22]]
                Aula_B_Viernes['E'] = VIERNES[recibido[22]]
            elif recibido[0] == "C":
                Aula_C_Lunes['E'] = LUNES[recibido[22]]
                Aula_C_Martes['E'] = MARTES[recibido[22]]
                Aula_C_Miercoles['E'] = MIERCOLES[recibido[22]]
                Aula_C_Jueves['E'] = JUEVES[recibido[22]]
                Aula_C_Viernes['E'] = VIERNES[recibido[22]]
            Equivocado['Paso'] == 0
        
        else:
            Equivocado['Paso'] = 1

    except:
        Equivocado['Paso'] = 1

# --------- Funcion para configurar un dia entero --------
def COMANDOConfigurardia(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
    try:
        if recibido[16:21] == "Lunes" or recibido[16:21] == "LUNES":
            LUNES['A'] = int(recibido[30])
            LUNES['B'] = int(recibido[40])
            LUNES['C'] = int(recibido[50])
            LUNES['D'] = int(recibido[60])
            LUNES['E'] = int(recibido[70])
            if recibido[0] == "A":
                Aula_A_Lunes = LUNES
            elif recibido[0] == "B":
                Aula_B_Lunes = LUNES
            elif recibido[0] == "C":
                Aula_C_Lunes = LUNES
            Equivocado['Paso'] = 0

        elif recibido[16:22] == "Martes":
            MARTES['A'] = int(recibido[31])
            MARTES['B'] = int(recibido[41])
            MARTES['C'] = int(recibido[51])
            MARTES['D'] = int(recibido[61])
            MARTES['E'] = int(recibido[71])
            if recibido[0] == "A":
                Aula_A_Martes = MARTES
            elif recibido[0] == "B":
                Aula_B_Martes = MARTES
            elif recibido[0] == "C":
                Aula_C_Martes = MARTES
            Equivocado['Paso'] = 0

        elif recibido[16:25] == "Miercoles":
            MIERCOLES['A'] = int(recibido[34])
            MIERCOLES['B'] = int(recibido[44])
            MIERCOLES['C'] = int(recibido[54])
            MIERCOLES['D'] = int(recibido[64])
            MIERCOLES['E'] = int(recibido[74])
            if recibido[0] == "A":
                Aula_A_Miercoles = MIERCOLES
            elif recibido[0] == "B":
                Aula_B_Miercoles = MIERCOLES
            elif recibido[0] == "C":
                Aula_C_Miercoles = MIERCOLES
            Equivocado['Paso'] = 0
    
        elif recibido[16:22] == "Jueves":
            JUEVES['A'] = int(recibido[31])
            JUEVES['B'] = int(recibido[41])
            JUEVES['C'] = int(recibido[51])
            JUEVES['D'] = int(recibido[61])
            JUEVES['E'] = int(recibido[71])
            if recibido[0] == "A":
                Aula_A_Jueves = JUEVES
            elif recibido[0] == "B":
                Aula_B_Jueves = JUEVES
            elif recibido[0] == "C":
                Aula_C_Jueves = JUEVES
            Equivocado['Paso'] = 0
    
        elif recibido[16:23] == "Viernes":
            VIERNES['A'] = int(recibido[32])
            VIERNES['B'] = int(recibido[42])
            VIERNES['C'] = int(recibido[52])
            VIERNES['D'] = int(recibido[62])
            VIERNES['E'] = int(recibido[72])
            if recibido[0] == "A":
                Aula_A_Viernes = VIERNES
            elif recibido[0] == "B":
                Aula_B_Viernes = VIERNES
            elif recibido[0] == "C":
                Aula_C_Viernes = VIERNES
            Equivocado['Paso'] = 0

        else:
            Equivocado['Paso'] = 1

    except:
        Equivocado['Paso'] = 1

# --------- Funcion para asignar un asignatura a un bloque de un dia en especifico--------
def COMANDOAsignarAsignatura(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
    try:
        if recibido[20:25] == "Lunes":
            LUNES[recibido[32]] = int(recibido[34])
            if recibido[0] == "A":
                Aula_A_Lunes = LUNES
            elif recibido[0] == "B":
                Aula_B_Lunes = LUNES
            elif recibido[0] == "C":
                Aula_C_Lunes = LUNES

        elif recibido[20:26] == "Martes":
            MARTES[recibido[33]] = int(recibido[35])
            if recibido[0] == "A":
                Aula_A_Martes = MARTES
            elif recibido[0] == "B":
                Aula_B_Martes = MARTES
            elif recibido[0] == "C":
                Aula_C_Martes = MARTES

        elif recibido[20:29] == "Miercoles":
            MIERCOLES[recibido[36]] = int(recibido[38])
            if recibido[0] == "A":
                Aula_A_Miercoles = MIERCOLES
            elif recibido[0] == "B":
                Aula_B_Miercoles = MIERCOLES
            elif recibido[0] == "C":
                Aula_C_Miercoles = MIERCOLES

        elif recibido[20:26] == "Jueves":
            JUEVES[recibido[33]] = int(recibido[35])
            if recibido[0] == "A":
                Aula_A_Jueves = JUEVES
            elif recibido[0] == "B":
                Aula_B_Jueves = JUEVES
            elif recibido[0] == "C":
                Aula_C_Jueves = JUEVES

        elif recibido[20:27] == "Viernes":
            VIERNES[recibido[34]] = int(recibido[36])
            if recibido[0] == "A":
                Aula_A_Viernes = VIERNES
            elif recibido[0] == "B":
                Aula_B_Viernes = VIERNES
            elif recibido[0] == "C":
                Aula_C_Viernes = VIERNES
        else:
            Equivocado['Paso'] = 1
        Equivocado['Paso'] = 0
        
    except:
        Equivocado['Paso'] = 1

# --------- Funcion para mostrar el horario semanal de un aula en especifico --------
def COMANDOHorarioSemana(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
    try:
        Pantalla1 = " Horario Semanal -> Aula: "+str(recibido[0])+"\n"
        Pantalla2 = " Lunes:\n"
        Pantalla3 = " TURNO A: ASIGNATURA: "+str(LUNES['A'])+" - TURNO B: ASIGNATURA: "+str(LUNES['B'])+" - TURNO C: ASIGNATURA: "+str(LUNES['C'])+" - TURNO D: ASIGNATURA: "+str(LUNES['D'])+" - TURNO E - ASIGNATURA: "+str(LUNES['E'])+"\n"
        Pantalla4 = " Martes:\n"
        Pantalla5 = " TURNO A: ASIGNATURA: "+str(MARTES['A'])+" - TURNO B: ASIGNATURA: "+str(MARTES['B'])+" - TURNO C: ASIGNATURA: "+str(MARTES['C'])+" - TURNO D: ASIGNATURA: "+str(MARTES['D'])+" - TURNO E - ASIGNATURA: "+str(MARTES['E'])+"\n"
        Pantalla6 = " Miercoles:\n"
        Pantalla7 = " TURNO A: ASIGNATURA: "+str(MIERCOLES['A'])+" - TURNO B: ASIGNATURA: "+str(MIERCOLES['B'])+" - TURNO C: ASIGNATURA: "+str(MIERCOLES['C'])+" - TURNO D: ASIGNATURA: "+str(MIERCOLES['D'])+" - TURNO E - ASIGNATURA: "+str(MIERCOLES['E'])+"\n"
        Pantalla8 = " Jueves:\n"
        Pantalla9 = " TURNO A: ASIGNATURA: "+str(JUEVES['A'])+" - TURNO B: ASIGNATURA: "+str(JUEVES['B'])+" - TURNO C: ASIGNATURA: "+str(JUEVES['C'])+" - TURNO D: ASIGNATURA: "+str(JUEVES['D'])+" - TURNO E - ASIGNATURA: "+str(JUEVES['E'])+"\n"
        Pantalla10 = " Viernes:\n"
        Pantalla11 = " TURNO A: ASIGNATURA: "+str(VIERNES['A'])+" - TURNO B: ASIGNATURA: "+str(VIERNES['B'])+" - TURNO C: ASIGNATURA: "+str(VIERNES['C'])+" - TURNO D: ASIGNATURA: "+str(VIERNES['D'])+" - TURNO E - ASIGNATURA: "+str(VIERNES['E'])+"\n"
        Equivocado['Paso'] = 0
        cliente = paho.Client()
        cliente.connect(broker,puerto)
        mensaje = cliente.publish("Pantalla_de_control",Pantalla1+Pantalla2+Pantalla3+Pantalla4+Pantalla5+Pantalla6+Pantalla7+Pantalla8+Pantalla9+Pantalla10+Pantalla11)
    
    except:
        Equivocado['Paso'] = 1

# --------- Funcion para mostrar el horario de un dia en particular de un aula en especifico--------
def COMANDOHorario(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
    try:
        if recibido[10:15] == "Lunes":
            Pantalla1 = "Horario Lunes -> Aula: "+str(recibido[0])+"\n"
            Pantalla2 = "TURNO A: ASIGNATURA: "+str(LUNES['A'])+" - TURNO B: ASIGNATURA: "+str(LUNES['B'])+" - TURNO C: ASIGNATURA: "+str(LUNES['C'])+" - TURNO D: ASIGNATURA: "+str(LUNES['D'])+" - TURNO E - ASIGNATURA: "+str(LUNES['E'])+"\n"

        elif recibido[10:16] == "Martes":
            Pantalla1 = " Horario Martes -> Aula: "+str(recibido[0])+"\n"
            Pantalla2 = " TURNO A: ASIGNATURA: "+str(MARTES['A'])+" - TURNO B: ASIGNATURA: "+str(MARTES['B'])+" - TURNO C: ASIGNATURA: "+str(MARTES['C'])+" - TURNO D: ASIGNATURA: "+str(MARTES['D'])+" - TURNO E - ASIGNATURA: "+str(MARTES['E'])+"\n"
    
        elif recibido[10:19] == "Miercoles":
            Pantalla1 = " Horario Miercoles -> Aula: "+str(recibido[0])+"\n"
            Pantalla2 = " TURNO A: ASIGNATURA:"+str(MIERCOLES['A'])+" - TURNO B: ASIGNATURA: "+str(MIERCOLES['B'])+" - TURNO C: ASIGNATURA: "+str(MIERCOLES['C'])+" - TURNO D: ASIGNATURA: "+str(MIERCOLES['D'])+" - TURNO E - ASIGNATURA: "+str(MIERCOLES['E'])+"\n"
    
        elif recibido[10:16] == "Jueves ":
            Pantalla1 = " Horario Jueves -> Aula: "+str(recibido[0])+"\n"
            Pantalla2 = " TURNO A: ASIGNATURA: "+str(JUEVES['A'])+" - TURNO B: ASIGNATURA: "+str(JUEVES['B'])+" - TURNO C: ASIGNATURA: "+str(JUEVES['C'])+" - TURNO D: ASIGNATURA: "+str(JUEVES['D'])+" - TURNO E - ASIGNATURA: "+str(JUEVES['E'])+"\n"
    
        elif recibido[10:17] == "Viernes":
            Pantalla1 = " Horario Viernes -> Aula: "+str(recibido[0])+"\n"
            Pantalla2 = " TURNO A: ASIGNATURA: "+str(VIERNES['A'])+"- TURNO B: ASIGNATURA: "+str(VIERNES['B'])+" - TURNO C: ASIGNATURA: "+str(VIERNES['C'])+" - TURNO D: ASIGNATURA: "+str(VIERNES['D'])+" - TURNO E - ASIGNATURA: "+str(VIERNES['E'])+"\n"
        
        Equivocado['Paso'] = 0
        cliente = paho.Client()
        cliente.connect(broker,puerto)
        mensaje = cliente.publish("Pantalla_de_control",Pantalla1+Pantalla2)

    except:
        Equivocado['Paso'] = 1

# --------- Funcion para mostrar el horario semanalde un dia especifico de cada aula --------
def COMANDOCadaAula(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
    try:
        if recibido[9:14] == "Lunes":
            Pantalla1 = " Horario Lunes Aula A\n"
            Pantalla2 = " TURNO A: ASIGNATURA: "+str(Aula_A_Lunes['A'])+" - TURNO B: ASIGNATURA: "+str(Aula_A_Lunes['B'])+" - TURNO C: ASIGNATURA: "+str(Aula_A_Lunes['C'])+" - TURNO D: ASIGNATURA: "+str(Aula_A_Lunes['D'])+" - TURNO E - ASIGNATURA: "+str(Aula_A_Lunes['E'])+"\n"
            Pantalla3 = " Horario Lunes Aula B\n"
            Pantalla4 = " TURNO A: ASIGNATURA: "+str(Aula_B_Lunes['A'])+" - TURNO B: ASIGNATURA: "+str(Aula_B_Lunes['B'])+" - TURNO C: ASIGNATURA: "+str(Aula_B_Lunes['C'])+" - TURNO D: ASIGNATURA: "+str(Aula_B_Lunes['D'])+" - TURNO E - ASIGNATURA: "+str(Aula_B_Lunes['E'])+"\n"
            Pantalla5 = " Horario Lunes Aula C\n"
            Pantalla6 = " TURNO A: ASIGNATURA: "+str(Aula_C_Lunes['A'])+" - TURNO B: ASIGNATURA: "+str(Aula_C_Lunes['B'])+" - TURNO C: ASIGNATURA: "+str(Aula_C_Lunes['C'])+" - TURNO D: ASIGNATURA: "+str(Aula_C_Lunes['D'])+" - TURNO E - ASIGNATURA: "+str(Aula_C_Lunes['E'])+"\n"
        elif recibido[9:15] == "Martes":
            Pantalla1 = " Horario Martes Aula A\n"
            Pantalla2 = " TURNO A: ASIGNATURA: "+str(Aula_A_Martes['A'])+" - TURNO B: ASIGNATURA: "+str(Aula_A_Martes['B'])+" - TURNO C: ASIGNATURA: "+str(Aula_A_Martes['C'])+" - TURNO D: ASIGNATURA: "+str(Aula_A_Martes['D'])+" - TURNO E - ASIGNATURA: "+str(Aula_A_Martes['E'])+"\n"
            Pantalla3 = " Horario Martes Aula B\n"
            Pantalla4 = " TURNO A: ASIGNATURA: "+str(Aula_B_Martes['A'])+" - TURNO B: ASIGNATURA: "+str(Aula_B_Martes['B'])+" - TURNO C: ASIGNATURA: "+str(Aula_B_Martes['C'])+" - TURNO D: ASIGNATURA: "+str(Aula_B_Martes['D'])+" - TURNO E - ASIGNATURA: "+str(Aula_B_Martes['E'])+"\n"
            Pantalla5 = " Horario Martes Aula C\n"
            Pantalla6 = " TURNO A: ASIGNATURA: "+str(Aula_C_Martes['A'])+" - TURNO B: ASIGNATURA: "+str(Aula_C_Martes['B'])+" - TURNO C: ASIGNATURA: "+str(Aula_C_Martes['C'])+" - TURNO D: ASIGNATURA: "+str(Aula_C_Martes['D'])+" - TURNO E - ASIGNATURA: "+str(Aula_C_Martes['E'])+"\n"
        elif recibido[9:18] == "Miercoles":
            Pantalla1 = " Horario Miercoles Aula A\n"
            Pantalla2 = " TURNO A: ASIGNATURA: "+str(Aula_A_Miercoles['A'])+" - TURNO B: ASIGNATURA: "+str(Aula_A_Miercoles['B'])+" - TURNO C: ASIGNATURA: "+str(Aula_A_Miercoles['C'])+" - TURNO D: ASIGNATURA: "+str(Aula_A_Miercoles['D'])+" - TURNO E - ASIGNATURA: "+str(Aula_A_Miercoles['E'])+"\n"
            Pantalla3 = " Horario Miercoles Aula B\n"
            Pantalla4 = " TURNO A: ASIGNATURA: "+str(Aula_B_Miercoles['A'])+" - TURNO B: ASIGNATURA: "+str(Aula_B_Miercoles['B'])+" - TURNO C: ASIGNATURA: "+str(Aula_B_Miercoles['C'])+" - TURNO D: ASIGNATURA: "+str(Aula_B_Miercoles['D'])+" - TURNO E - ASIGNATURA: "+str(Aula_B_Miercoles['E'])+"\n"
            Pantalla5 = " Horario Miercoles Aula C\n"
            Pantalla6 = " TURNO A: ASIGNATURA: "+str(Aula_C_Miercoles['A'])+" - TURNO B: ASIGNATURA: "+str(Aula_C_Miercoles['B'])+" - TURNO C: ASIGNATURA: "+str(Aula_C_Miercoles['C'])+" - TURNO D: ASIGNATURA: "+str(Aula_C_Miercoles['D'])+" - TURNO E - ASIGNATURA: "+str(Aula_C_Miercoles['E'])+"\n"
        elif recibido[9:15] == "Jueves":
            Pantalla1 = " Horario Jueves Aula A\n"
            Pantalla2 = " TURNO A: ASIGNATURA: "+str(Aula_A_Jueves['A'])+" - TURNO B: ASIGNATURA: "+str(Aula_A_Jueves['B'])+" - TURNO C: ASIGNATURA: "+str(Aula_A_Jueves['C'])+" - TURNO D: ASIGNATURA: "+str(Aula_A_Jueves['D'])+" - TURNO E - ASIGNATURA: "+str(Aula_A_Jueves['E'])+"\n"
            Pantalla3 = " Horario Jueves Aula B\n"
            Pantalla4 = " TURNO A: ASIGNATURA: "+str(Aula_B_Jueves['A'])+" - TURNO B: ASIGNATURA: "+str(Aula_B_Jueves['B'])+" - TURNO C: ASIGNATURA: "+str(Aula_B_Jueves['C'])+" - TURNO D: ASIGNATURA: "+str(Aula_B_Jueves['D'])+" - TURNO E - ASIGNATURA: "+str(Aula_B_Jueves['E'])+"\n"
            Pantalla5 = " Horario Jueves Aula C\n"
            Pantalla6 = " TURNO A: ASIGNATURA: "+str(Aula_C_Jueves['A'])+" - TURNO B: ASIGNATURA: "+str(Aula_C_Jueves['B'])+" - TURNO C: ASIGNATURA: "+str(Aula_C_Jueves['C'])+" - TURNO D: ASIGNATURA: "+str(Aula_C_Jueves['D'])+" - TURNO E - ASIGNATURA: "+str(Aula_C_Jueves['E'])+"\n"
        elif recibido[9:16] == "Viernes":
            Pantalla1 = " Horario Viernes Aula A\n"
            Pantalla2 = " TURNO A: ASIGNATURA: "+str(Aula_A_Viernes['A'])+" - TURNO B: ASIGNATURA: "+str(Aula_A_Viernes['B'])+" - TURNO C: ASIGNATURA: "+str(Aula_A_Viernes['C'])+" - TURNO D: ASIGNATURA: "+str(Aula_A_Viernes['D'])+" - TURNO E - ASIGNATURA: "+str(Aula_A_Viernes['E'])+"\n"
            Pantalla3 = " Horario Viernes Aula B\n"
            Pantalla4 = " TURNO A: ASIGNATURA: "+str(Aula_B_Viernes['A'])+" - TURNO B: ASIGNATURA: "+str(Aula_B_Viernes['B'])+" - TURNO C: ASIGNATURA: "+str(Aula_B_Viernes['C'])+" - TURNO D: ASIGNATURA: "+str(Aula_B_Viernes['D'])+" - TURNO E - ASIGNATURA: "+str(Aula_B_Viernes['E'])+"\n"
            Pantalla5 = " Horario Viernes Aula C\n"
            Pantalla6 = " TURNO A: ASIGNATURA: "+str(Aula_C_Viernes['A'])+" - TURNO B: ASIGNATURA: "+str(Aula_C_Viernes['B'])+" - TURNO C: ASIGNATURA: "+str(Aula_C_Viernes['C'])+" - TURNO D: ASIGNATURA: "+str(Aula_C_Viernes['D'])+" - TURNO E - ASIGNATURA: "+str(Aula_C_Viernes['E'])+"\n"
        Equivocado['Paso'] = 0
        cliente = paho.Client()
        cliente.connect(broker,puerto)
        mensaje = cliente.publish("Pantalla_de_control",Pantalla1+Pantalla2+Pantalla3+Pantalla4+Pantalla5+Pantalla6)

    except:
        Equivocado['Paso'] = 1

# --------- Funcion para saber en que bloques de cada aula se dicta determinada asignatura--------
def COMANDOAsignaturaInfo(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
    try:
        for i in Aula_A_Lunes:
            if Aula_A_Lunes[i] == int(recibido[15:17]):
                Pantalla = "Aula A: Lunes -> Bloque "+str(i)+"\n"
                cliente = paho.Client()
                cliente.connect(broker,puerto)
                mensaje = cliente.publish("Pantalla_de_control",Pantalla)
        for i in Aula_A_Martes:
            if Aula_A_Martes[i] == int(recibido[15:17]):
                Pantalla = "Aula A: Martes -> Bloque "+str(i)+"\n"
                cliente = paho.Client()
                cliente.connect(broker,puerto)
                mensaje = cliente.publish("Pantalla_de_control",Pantalla)
        for i in Aula_A_Miercoles:
            if Aula_A_Miercoles[i] == int(recibido[15:17]):
                Pantalla = "Aula A: Miercoles -> Bloque "+str(i)+"\n"
                cliente = paho.Client()
                cliente.connect(broker,puerto)
                mensaje = cliente.publish("Pantalla_de_control",Pantalla)
        for i in Aula_A_Jueves:
            if Aula_A_Jueves[i] == int(recibido[15:17]):
                Pantalla = "Aula A: Jueves -> Bloque "+str(i)+"\n"
                cliente = paho.Client()
                cliente.connect(broker,puerto)
                mensaje = cliente.publish("Pantalla_de_control",Pantalla)
        for i in Aula_A_Viernes:
            if Aula_A_Viernes[i] == int(recibido[15:17]):
                Pantalla = "Aula A: Viernes -> Bloque "+str(i)+"\n"
                cliente = paho.Client()
                cliente.connect(broker,puerto)
                mensaje = cliente.publish("Pantalla_de_control",Pantalla)

        for i in Aula_B_Lunes:
            if Aula_B_Lunes[i] == int(recibido[15:17]):
                Pantalla = "Aula B: Lunes -> Bloque "+str(i)+"\n"
                cliente = paho.Client()
                cliente.connect(broker,puerto)
                mensaje = cliente.publish("Pantalla_de_control",Pantalla)
        for i in Aula_B_Martes:
            if Aula_B_Martes[i] == int(recibido[15:17]):
                Pantalla = "Aula B: Martes -> Bloque "+str(i)+"\n"
                cliente = paho.Client()
                cliente.connect(broker,puerto)
                mensaje = cliente.publish("Pantalla_de_control",Pantalla)
        for i in Aula_B_Miercoles:
            if Aula_B_Miercoles[i] == int(recibido[15:17]):
                Pantalla = "Aula B: Miercoles -> Bloque "+str(i)+"\n"
                cliente = paho.Client()
                cliente.connect(broker,puerto)
                mensaje = cliente.publish("Pantalla_de_control",Pantalla)
        for i in Aula_B_Jueves:
            if Aula_B_Jueves[i] == int(recibido[15:17]):
                Pantalla = "Aula B: Jueves -> Bloque "+str(i)+"\n"
                cliente = paho.Client()
                cliente.connect(broker,puerto)
                mensaje = cliente.publish("Pantalla_de_control",Pantalla)
        for i in Aula_B_Viernes:
            if Aula_B_Viernes[i] == int(recibido[15:17]):
                Pantalla = "Aula B: Viernes -> Bloque "+str(i)+"\n"
                cliente = paho.Client()
                cliente.connect(broker,puerto)
                mensaje = cliente.publish("Pantalla_de_control",Pantalla)

        for i in Aula_C_Lunes:
            if Aula_C_Lunes[i] == int(recibido[15:17]):
                Pantalla = "Aula C: Lunes -> Bloque "+str(i)+"\n"
                cliente = paho.Client()
                cliente.connect(broker,puerto)
                mensaje = cliente.publish("Pantalla_de_control",Pantalla)
        for i in Aula_C_Martes:
            if Aula_C_Martes[i] == int(recibido[15:17]):
                Pantalla = "Aula C: Martes -> Bloque "+str(i)+"\n"
                cliente = paho.Client()
                cliente.connect(broker,puerto)
                mensaje = cliente.publish("Pantalla_de_control",Pantalla)
        for i in Aula_C_Miercoles:
            if Aula_C_Miercoles[i] == int(recibido[15:17]):
                Pantalla = "Aula C: Miercoles -> Bloque "+str(i)+"\n"
                cliente = paho.Client()
                cliente.connect(broker,puerto)
                mensaje = cliente.publish("Pantalla_de_control",Pantalla)
        for i in Aula_C_Jueves:
            if Aula_C_Jueves[i] == int(recibido[15:17]):
                Pantalla = "Aula C: Jueves -> Bloque "+str(i)+"\n"
                cliente = paho.Client()
                cliente.connect(broker,puerto)
                mensaje = cliente.publish("Pantalla_de_control",Pantalla)
        for i in Aula_C_Viernes:
            if Aula_C_Viernes[i] == int(recibido[15:17]):
                Pantalla = "Aula C: Viernes -> Bloque "+str(i)+"\n"
                cliente = paho.Client()
                cliente.connect(broker,puerto)
                mensaje = cliente.publish("Pantalla_de_control",Pantalla)
        Equivocado['Paso'] = 0
    except:
        Equivocado['Paso'] = 1

# --------- Funcion para elminar todas las asignaturas de un dia en especifico --------
def COMANDOEliminaDia(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
    try:
        print("ENTRO ELIMINA")
        if recibido[13:18] == "Lunes":
            LUNES['A'] = 0
            LUNES['B'] = 0
            LUNES['C'] = 0
            LUNES['D'] = 0
            LUNES['E'] = 0
            if recibido[0] == "A":
                Aula_A_Lunes = LUNES
            elif recibido[0] == "B":
                Aula_B_Lunes = LUNES
            elif recibido[0] == "C":
                Aula_C_Lunes = LUNES
            Equivocado['Paso'] = 0

        elif recibido[13:19] == "Martes":
            MARTES['A'] = 0
            MARTES['B'] = 0
            MARTES['C'] = 0
            MARTES['D'] = 0
            MARTES['E'] = 0
            if recibido[0] == "A":
                Aula_A_Martes = MARTES
            elif recibido[0] == "B":
                Aula_B_Martes = MARTES
            elif recibido[0] == "C":
                Aula_C_Martes = MARTES
            Equivocado['Paso'] = 0

        elif recibido[13:22] == "Miercoles":
            MIERCOLES['A'] = 0
            MIERCOLES['B'] = 0
            MIERCOLES['C'] = 0
            MIERCOLES['D'] = 0
            MIERCOLES['E'] = 0
            if recibido[0] == "A":
                Aula_A_Miercoles = MIERCOLES
            elif recibido[0] == "B":
                Aula_B_Miercoles = MIERCOLES
            elif recibido[0] == "C":
                Aula_C_Miercoles = MIERCOLES
            Equivocado['Paso'] = 0
    
        elif recibido[13:19] == "Jueves":
            JUEVES['A'] = 0
            JUEVES['B'] = 0
            JUEVES['C'] = 0
            JUEVES['D'] = 0
            JUEVES['E'] = 0
            if recibido[0] == "A":
                Aula_A_Jueves = JUEVES
            elif recibido[0] == "B":
                Aula_B_Jueves = JUEVES
            elif recibido[0] == "C":
                Aula_C_Jueves = JUEVES
            Equivocado['Paso'] = 0
    
        elif recibido[13:20] == "Viernes":
            VIERNES['A'] = 0
            VIERNES['B'] = 0
            VIERNES['C'] = 0
            VIERNES['D'] = 0
            VIERNES['E'] = 0
            if recibido[0] == "A":
                Aula_A_Viernes = VIERNES
            elif recibido[0] == "B":
                Aula_B_Viernes = VIERNES
            elif recibido[0] == "C":
                Aula_C_Viernes = VIERNES
            Equivocado['Paso'] = 0
        else:
            Equivocado['Paso'] = 1

    except:
        Equivocado['Paso'] = 1

# --------- Funcion para reiniciar todos los horarios de un aula en especifico --------
def COMANDOEliminaHorario(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
    try:
        LUNES['A'] = 0
        LUNES['B'] = 0
        LUNES['C'] = 0
        LUNES['D'] = 0
        LUNES['E'] = 0
        MARTES['A'] = 0
        MARTES['B'] = 0
        MARTES['C'] = 0
        MARTES['D'] = 0
        MARTES['E'] = 0
        MIERCOLES['A'] = 0
        MIERCOLES['B'] = 0
        MIERCOLES['C'] = 0
        MIERCOLES['D'] = 0
        MIERCOLES['E'] = 0
        JUEVES['A'] = 0
        JUEVES['B'] = 0
        JUEVES['C'] = 0
        JUEVES['D'] = 0
        JUEVES['E'] = 0
        VIERNES['A'] = 0
        VIERNES['B'] = 0
        VIERNES['C'] = 0
        VIERNES['D'] = 0
        VIERNES['E'] = 0
        if recibido[0] == "A":
            Aula_A_Lunes = LUNES
            Aula_A_Martes = MARTES
            Aula_A_Miercoles = MIERCOLES
            Aula_A_Jueves = JUEVES
            Aula_A_Viernes = VIERNES
        if recibido[0] == "B":
            Aula_B_Lunes = LUNES
            Aula_B_Martes = MARTES
            Aula_B_Miercoles = MIERCOLES
            Aula_B_Jueves = JUEVES
            Aula_B_Viernes = VIERNES
        if recibido[0] == "C":
            Aula_C_Lunes = LUNES
            Aula_C_Martes = MARTES
            Aula_C_Miercoles = MIERCOLES
            Aula_C_Jueves = JUEVES
            Aula_C_Viernes = VIERNES
        Equivocado['Paso'] = 0

    except:
        Equivocado['Paso'] = 1

# --------- Funcion para eliminar una asignatura en especifico de cada dia y cada bloque de cada aula--------
def COMANDOAsignaturaEliminada(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
    try:
        for i in Aula_A_Lunes:
            if Aula_A_Lunes[i] == int(recibido[20:22]):
                Aula_A_Lunes[i] = 0
        for i in Aula_A_Martes:
            if Aula_A_Martes[i] == int(recibido[20:22]):
                Aula_A_Martes[i] = 0
        for i in Aula_A_Miercoles:
            if Aula_A_Miercoles[i] == int(recibido[20:22]):
                Aula_A_Miercoles[i] = 0
        for i in Aula_A_Jueves:
            if Aula_A_Jueves[i] == int(recibido[20:22]):
                Aula_A_Jueves[i] = 0
        for i in Aula_A_Viernes:
            if Aula_A_Viernes[i] == int(recibido[20:22]):
                Aula_A_Viernes[i] = 0

        for i in Aula_B_Lunes:
            if Aula_B_Lunes[i] == int(recibido[20:22]):
                Aula_B_Lunes[i] = 0
        for i in Aula_B_Martes:
            if Aula_B_Martes[i] == int(recibido[20:22]):
                Aula_B_Martes[i] = 0
        for i in Aula_B_Miercoles:
            if Aula_B_Miercoles[i] == int(recibido[20:22]):
                Aula_B_Miercoles[i] = 0
        for i in Aula_B_Jueves:
            if Aula_B_Jueves[i] == int(recibido[20:22]):
                Aula_B_Jueves[i] = 0
        for i in Aula_B_Viernes:
            if Aula_B_Viernes[i] == int(recibido[20:22]):
                Aula_B_Viernes[i] = 0
    
        for i in Aula_C_Lunes:
            if Aula_C_Lunes[i] == int(recibido[20:22]):
                Aula_C_Lunes[i] = 0
        for i in Aula_C_Martes:
            if Aula_C_Martes[i] == int(recibido[20:22]):
                Aula_C_Martes[i] = 0
        for i in Aula_C_Miercoles:
            if Aula_C_Miercoles[i] == int(recibido[20:22]):
                Aula_C_Miercoles[i] = 0
        for i in Aula_C_Jueves:
            if Aula_C_Jueves[i] == int(recibido[20:22]):
                Aula_C_Jueves[i] = 0
        for i in Aula_C_Viernes:
            if Aula_C_Viernes[i] == int(recibido[20:22]):
                Aula_C_Viernes[i] = 0
        Equivocado['Paso'] = 0

    except:
        Equivocado['Paso'] = 1

# --------- Funcion para reiniciar topdos los horarios --------
def COMANDOBorrarTodo(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
    try:
        for i in Aula_A_Lunes:
            Aula_A_Lunes[i] = 0
        for i in Aula_A_Martes:
            Aula_A_Martes[i] = 0
        for i in Aula_A_Miercoles:
            Aula_A_Miercoles[i] = 0
        for i in Aula_A_Jueves:
            Aula_A_Jueves[i] = 0
        for i in Aula_A_Viernes:
            Aula_A_Viernes[i] = 0

        for i in Aula_B_Lunes:
            Aula_B_Lunes[i] = 0
        for i in Aula_B_Martes:
            Aula_B_Martes[i] = 0
        for i in Aula_B_Miercoles:
            Aula_B_Miercoles[i] = 0
        for i in Aula_B_Jueves:
            Aula_B_Jueves[i] = 0
        for i in Aula_B_Viernes:
            Aula_B_Viernes[i] = 0
    
        for i in Aula_C_Lunes:
            Aula_C_Lunes[i] = 0
        for i in Aula_C_Martes:
            Aula_C_Martes[i] = 0
        for i in Aula_C_Miercoles:
            Aula_C_Miercoles[i] = 0
        for i in Aula_C_Jueves:
            Aula_C_Jueves[i] = 0
        for i in Aula_C_Viernes:
            Aula_C_Viernes[i] = 0 
    
    except:
        Equivocado['Paso'] = 1


# --------- Funcion para asignar como día libre el siguiente día --------
def COMANDODiasLibres(dia_libre):
    print("SI ESTA ENTRANDO")
    FERIADO = 1

def ComandoArchivo():
    try:
        data = [
            ['Aula A'],
            ['Bloque\Día','Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes'],
            ['A',str("Asignatura ")+str(Aula_A_Lunes['A']), str("Asignatura ")+str(Aula_A_Martes['A']), str("Asignatura ")+str(Aula_A_Miercoles['A']), str("Asignatura ")+str(Aula_A_Jueves['A']), str("Asignatura ")+str(Aula_A_Viernes['A'])],
            ['B',str("Asignatura ")+str(Aula_A_Lunes['B']), str("Asignatura ")+str(Aula_A_Martes['B']), str("Asignatura ")+str(Aula_A_Miercoles['B']), str("Asignatura ")+str(Aula_A_Jueves['B']), str("Asignatura ")+str(Aula_A_Viernes['B'])],
            ['C',str("Asignatura ")+str(Aula_A_Lunes['C']), str("Asignatura ")+str(Aula_A_Martes['C']), str("Asignatura ")+str(Aula_A_Miercoles['C']), str("Asignatura ")+str(Aula_A_Jueves['C']), str("Asignatura ")+str(Aula_A_Viernes['C'])],
            ['D',str("Asignatura ")+str(Aula_A_Lunes['D']), str("Asignatura ")+str(Aula_A_Martes['D']), str("Asignatura ")+str(Aula_A_Miercoles['D']), str("Asignatura ")+str(Aula_A_Jueves['D']), str("Asignatura ")+str(Aula_A_Viernes['D'])],
            ['E',str("Asignatura ")+str(Aula_A_Lunes['E']), str("Asignatura ")+str(Aula_A_Martes['E']), str("Asignatura ")+str(Aula_A_Miercoles['E']), str("Asignatura ")+str(Aula_A_Jueves['E']), str("Asignatura ")+str(Aula_A_Viernes['E'])],
            [' '],
            ['Aula B'],
            ['Bloque\Día','Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes'],
            ['A',str("Asignatura ")+str(Aula_B_Lunes['A']), str("Asignatura ")+str(Aula_B_Martes['A']), str("Asignatura ")+str(Aula_B_Miercoles['A']), str("Asignatura ")+str(Aula_B_Jueves['A']), str("Asignatura ")+str(Aula_B_Viernes['A'])],
            ['B',str("Asignatura ")+str(Aula_B_Lunes['B']), str("Asignatura ")+str(Aula_B_Martes['B']), str("Asignatura ")+str(Aula_B_Miercoles['B']), str("Asignatura ")+str(Aula_B_Jueves['B']), str("Asignatura ")+str(Aula_B_Viernes['B'])],
            ['C',str("Asignatura ")+str(Aula_B_Lunes['C']), str("Asignatura ")+str(Aula_B_Martes['C']), str("Asignatura ")+str(Aula_B_Miercoles['C']), str("Asignatura ")+str(Aula_B_Jueves['C']), str("Asignatura ")+str(Aula_B_Viernes['C'])],
            ['D',str("Asignatura ")+str(Aula_B_Lunes['D']), str("Asignatura ")+str(Aula_B_Martes['D']), str("Asignatura ")+str(Aula_B_Miercoles['D']), str("Asignatura ")+str(Aula_B_Jueves['D']), str("Asignatura ")+str(Aula_B_Viernes['D'])],
            ['E',str("Asignatura ")+str(Aula_B_Lunes['E']), str("Asignatura ")+str(Aula_B_Martes['E']), str("Asignatura ")+str(Aula_B_Miercoles['E']), str("Asignatura ")+str(Aula_B_Jueves['E']), str("Asignatura ")+str(Aula_B_Viernes['E'])],
            [' '],
            ['Aula C'],
            ['Bloque\Día','Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes'],
            ['A',str("Asignatura ")+str(Aula_C_Lunes['A']), str("Asignatura ")+str(Aula_C_Martes['A']), str("Asignatura ")+str(Aula_C_Miercoles['A']), str("Asignatura ")+str(Aula_C_Jueves['A']), str("Asignatura ")+str(Aula_C_Viernes['A'])],
            ['B',str("Asignatura ")+str(Aula_C_Lunes['B']), str("Asignatura ")+str(Aula_C_Martes['B']), str("Asignatura ")+str(Aula_C_Miercoles['B']), str("Asignatura ")+str(Aula_C_Jueves['B']), str("Asignatura ")+str(Aula_C_Viernes['B'])],
            ['C',str("Asignatura ")+str(Aula_C_Lunes['C']), str("Asignatura ")+str(Aula_C_Martes['C']), str("Asignatura ")+str(Aula_C_Miercoles['C']), str("Asignatura ")+str(Aula_C_Jueves['C']), str("Asignatura ")+str(Aula_C_Viernes['C'])],
            ['D',str("Asignatura ")+str(Aula_C_Lunes['D']), str("Asignatura ")+str(Aula_C_Martes['D']), str("Asignatura ")+str(Aula_C_Miercoles['D']), str("Asignatura ")+str(Aula_C_Jueves['D']), str("Asignatura ")+str(Aula_C_Viernes['D'])],
            ['E',str("Asignatura ")+str(Aula_C_Lunes['E']), str("Asignatura ")+str(Aula_C_Martes['E']), str("Asignatura ")+str(Aula_C_Miercoles['E']), str("Asignatura ")+str(Aula_C_Jueves['E']), str("Asignatura ")+str(Aula_C_Viernes['E'])],
            [' '],
        ]
        with open('PRUEBA.csv', 'a',newline='') as file:
            writer = csv.writer(file,delimiter=';')
            writer.writerows(data)
    except:
        Pantalla = "Hubo un error al ingresar el comando, vuelva a intentar"
        cliente = paho.Client()
        cliente.connect(broker,puerto)
        mensaje = cliente.publish("Pantalla_de_control",Pantalla)

####################################################
# --------- Funcion de Recepción de mensaje --------
####################################################

def mensajeMQTT_Horario(client, userdata, msg):
    Turno['Paso'] = Turno['Paso'] + 1
    recibido = msg.payload.decode()
    if recibido[0] == "A":
        print("ESTAMOS EN EL SALON A")
        Aula_LUNES = Aula_A_Lunes
        Aula_MARTES = Aula_A_Martes
        Aula_MIERCOLES = Aula_A_Miercoles
        Aula_JUEVES = Aula_A_Jueves
        Aula_VIERNES = Aula_A_Viernes
    elif recibido[0] == "B":
        print("ESTAMOS EN EL SALON B")
        Aula_LUNES = Aula_B_Lunes
        Aula_MARTES = Aula_B_Martes
        Aula_MIERCOLES = Aula_B_Miercoles
        Aula_JUEVES = Aula_B_Jueves
        Aula_VIERNES = Aula_B_Viernes
    elif recibido[0] == "C":
        print("ESTAMOS EN EL SALON C")
        Aula_LUNES = Aula_C_Lunes
        Aula_MARTES = Aula_C_Martes
        Aula_MIERCOLES = Aula_C_Miercoles
        Aula_JUEVES = Aula_C_Jueves
        Aula_VIERNES = Aula_C_Viernes

# COmando CambiarBloque"
#Aula(Solo letra) CambiarBloque BLOQUEX LUNES #Asig MARTES #Asig MIercoles #ASig Jueves #Asig Viernes #Asig  #ERROR DE PRIMERA VEZ CON RECIBIDO
    if recibido[2:15] == "CambiarBloque":
        COMANDOCambiarBloque(recibido,Aula_LUNES,Aula_MARTES,Aula_MIERCOLES,Aula_JUEVES,Aula_VIERNES)
        client.disconnect()

# COMANDO ConfigurarDIa
#Aula(Solo letra) Configurardia LUNES BLOQUEA 1 BLOQUEB 2 BLOQUEC 3 BLOQUED 4 BLOQUEE 5   #ERROR DE PRIMERA VEZ CON RECIBIDO
    elif recibido[2:15] == "ConfigurarDia":
        COMANDOConfigurardia(recibido,Aula_LUNES,Aula_MARTES,Aula_MIERCOLES,Aula_JUEVES,Aula_VIERNES)
        client.disconnect()
        
# COMANDO AsignarAsignatura
#Aula(Solo letra) AsignarAsignatura Dia BLOQUEX NumeroDeAsignatura   
    elif recibido[2:19] == "AsignarAsignatura":
        COMANDOAsignarAsignatura(recibido,Aula_LUNES,Aula_MARTES,Aula_MIERCOLES,Aula_JUEVES,Aula_VIERNES)
        client.disconnect()

# COMANDO HorarioSemana (De todos los dias de un aula)                  #ERROR DE PRIMERA VEZ CON RECIBIDO
#AULA(Solo letra) HorarioSemana
    elif recibido[2:15] == "HorarioSemana":
        COMANDOHorarioSemana(recibido,Aula_LUNES,Aula_MARTES,Aula_MIERCOLES,Aula_JUEVES,Aula_VIERNES)
        client.disconnect()

# COMANDO Horario(De un dia)
# AULA(Solo letra) HORARIO Dia 
    elif recibido[2:9] == "Horario":
        COMANDOHorario(recibido,Aula_LUNES,Aula_MARTES,Aula_MIERCOLES,Aula_JUEVES,Aula_VIERNES)
        client.disconnect()

# COMANDO CadaAula para un dia determinado
# CadaAula DIA 
    elif recibido[0:8] == "CadaAula":
        COMANDOCadaAula(recibido,Aula_LUNES,Aula_MARTES,Aula_MIERCOLES,Aula_JUEVES,Aula_VIERNES)
        client.disconnect()

# COMANDO AsignaturaInfo en cada aula y horario  PROBELMNAS CON EL ERROR
#AsignaturaInfo #Asig  
    elif recibido[0:14] == "AsignaturaInfo":
        COMANDOAsignaturaInfo(recibido,Aula_LUNES,Aula_MARTES,Aula_MIERCOLES,Aula_JUEVES,Aula_VIERNES)
        client.disconnect()   

# COMANDO EliminaDia en cada aula y horario    #ERROR DE PRIMERA VEZ CON RECIBIDO
#Aula(Solo letra) EliminaDia Dia  
    elif recibido[2:12] == "EliminaDia": 
        COMANDOEliminaDia(recibido,Aula_LUNES,Aula_MARTES,Aula_MIERCOLES,Aula_JUEVES,Aula_VIERNES)
        client.disconnect()

# COMANDO EliminaHorario                    #ERROR DE PRIMERA VEZ CON RECIBIDO
#Aula(Solo letra) EliminaHorario
    elif recibido[2:16] == "EliminaHorario":
        COMANDOEliminaHorario(recibido,Aula_LUNES,Aula_MARTES,Aula_MIERCOLES,Aula_JUEVES,Aula_VIERNES)
        client.disconnect()

# COMANDO AsignaturaEliminada
#AsignaturaEliminada #Asig
    elif recibido[0:19] == "AsignaturaEliminada":
        COMANDOAsignaturaEliminada(recibido,Aula_LUNES,Aula_MARTES,Aula_MIERCOLES,Aula_JUEVES,Aula_VIERNES)
        client.disconnect()

# COMANDO BorrarTodo
#BorrarTodo
    elif recibido[0:10] == "BorrarTodo":
        COMANDOBorrarTodo(recibido,Aula_LUNES,Aula_MARTES,Aula_MIERCOLES,Aula_JUEVES,Aula_VIERNES)
        client.disconnect()

# COMANDO DiaLibre (HArá que el siguiente día sea libre)
    elif recibido[0:8] == "DiaLibre":
        Control['Paso'] = 1
        FERIADO['Dia'] = 1
        client.disconnect()

    elif recibido[0] == "x" or recibido[0] == "X":
        client.disconnect()
        
    else:
        Equivocado['Paso'] = 1
        client.disconnect()

    if Equivocado['Paso'] == 1 and Turno['Paso']%2 == 0:
        Equivocado['Paso'] = 0
        Pantalla = "Hubo un error al ingresar el comando, vuelva a intentar"
        cliente = paho.Client()
        cliente.connect(broker,puerto)
        mensaje = cliente.publish("Pantalla_de_control",Pantalla)
    ComandoArchivo()
# ---------- HORARIOS INICIALES --------------------
Aula_A_Lunes = {'A':0,'B':1,'C':2,'D':3,'E':0}
Aula_A_Martes = {'A':4,'B':5,'C':0,'D':0,'E':0}
Aula_A_Miercoles = {'A':0,'B':0,'C':2,'D':3,'E':0}
Aula_A_Jueves = {'A':4,'B':5,'C':0,'D':6,'E':6}
Aula_A_Viernes = {'A':0,'B':1,'C':2,'D':3,'E':0}

Aula_B_Lunes = {'A':3,'B':2,'C':0,'D':0,'E':0}
Aula_B_Martes = {'A':1,'B':4,'C':5,'D':6,'E':6}
Aula_B_Miercoles = {'A':3,'B':2,'C':0,'D':0,'E':0}
Aula_B_Jueves = {'A':1,'B':4,'C':5,'D':0,'E':0}
Aula_B_Viernes = {'A':3,'B':2,'C':0,'D':0,'E':0}

Aula_C_Lunes = {'A':2,'B':3,'C':1,'D':0,'E':0}
Aula_C_Martes = {'A':0,'B':0,'C':0,'D':5,'E':4}
Aula_C_Miercoles = {'A':2,'B':3,'C':0,'D':6,'E':6}
Aula_C_Jueves = {'A':0,'B':0,'C':0,'D':5,'E':4}
Aula_C_Viernes = {'A':2,'B':3,'C':1,'D':0,'E':0}

FERIADO = {'Dia':0}
Control = {'Paso':0}
Equivocado = {'Paso':0}
Turno = {'Paso':0}

# ------------ Conexión del cliente -----------------
#------------ Datos del broker MQTT -----------------

broker = "192.168.1.30"
puerto = 5050


