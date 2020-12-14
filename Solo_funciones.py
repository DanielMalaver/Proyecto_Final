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
#from SensorPir import*
#import RPi.GPIO as GPIO

####################################################
# -------- Funciones de COntrol de Comandos --------
####################################################

def COMANDOCambiarBloque(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
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

    if recibido[22] == "B":
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

    if recibido[22] == "C":
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

    if recibido[22] == "D":
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

    if recibido[22] == "E":
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

def COMANDOConfigurardia(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
    if recibido[16:21] == "Lunes":
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

    elif recibido[16:24] == "Miercoles":
        MIERCOLES['A'] = int(recibido[33])
        MIERCOLES['B'] = int(recibido[43])
        MIERCOLES['C'] = int(recibido[53])
        MIERCOLES['D'] = int(recibido[63])
        MIERCOLES['E'] = int(recibido[73])
        if recibido[0] == "A":
           Aula_A_Miercoles = MIERCOLES
        elif recibido[0] == "B":
           Aula_B_Miercoles = MIERCOLES
        elif recibido[0] == "C":
           Aula_C_Miercoles = MIERCOLES
    
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

def COMANDOAsignarAsignatura(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
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

def COMANDOHorarioSemana(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
    print("Horario Semanal -> Aula:",recibido[0])
    print("Lunes:")
    print("TURNO A: ASIGNATURA: ",LUNES['A'],"- TURNO B: ASIGNATURA: ",LUNES['B']," - TURNO C: ASIGNATURA: ",LUNES['C']," - TURNO D: ASIGNATURA: ",LUNES['D']," - TURNO E - ASIGNATURA: ",LUNES['E'])
    print("Martes:")
    print("TURNO A: ASIGNATURA: ",MARTES['A'],"- TURNO B: ASIGNATURA: ",MARTES['B']," - TURNO C: ASIGNATURA: ",MARTES['C']," - TURNO D: ASIGNATURA: ",MARTES['D']," - TURNO E - ASIGNATURA: ",MARTES['E'])
    print("Miercoles:")
    print("TURNO A: ASIGNATURA: ",MIERCOLES['A'],"- TURNO B: ASIGNATURA: ",MIERCOLES['B']," - TURNO C: ASIGNATURA: ",MIERCOLES['C']," - TURNO D: ASIGNATURA: ",MIERCOLES['D']," - TURNO E - ASIGNATURA: ",MIERCOLES['E'])
    print("Jueves:")
    print("TURNO A: ASIGNATURA: ",JUEVES['A'],"- TURNO B: ASIGNATURA: ",JUEVES['B']," - TURNO C: ASIGNATURA: ",JUEVES['C']," - TURNO D: ASIGNATURA: ",JUEVES['D']," - TURNO E - ASIGNATURA: ",JUEVES['E'])
    print("Viernes:")
    print("TURNO A: ASIGNATURA: ",VIERNES['A'],"- TURNO B: ASIGNATURA: ",VIERNES['B']," - TURNO C: ASIGNATURA: ",VIERNES['C']," - TURNO D: ASIGNATURA: ",VIERNES['D']," - TURNO E - ASIGNATURA: ",VIERNES['E'])

def COMANDOHorario(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
    if recibido[10:15] == "Lunes":
        print("Horario Lunes -> Aula: ",recibido[0])
        print("TURNO A: ASIGNATURA: ",LUNES['A'],"- TURNO B: ASIGNATURA: ",LUNES['B']," - TURNO C: ASIGNATURA: ",LUNES['C']," - TURNO D: ASIGNATURA: ",LUNES['D']," - TURNO E - ASIGNATURA: ",LUNES['E'])
    elif recibido[10:16] == "Martes":
        print("Horario Martes -> Aula: ",recibido[0])
        print("TURNO A: ASIGNATURA: ",MARTES['A'],"- TURNO B: ASIGNATURA: ",MARTES['B']," - TURNO C: ASIGNATURA: ",MARTES['C']," - TURNO D: ASIGNATURA: ",MARTES['D']," - TURNO E - ASIGNATURA: ",MARTES['E'])
    elif recibido[10:19] == "Miercoles":
        print("Horario Miercoles -> Aula: ",recibido[0])
        print("TURNO A: ASIGNATURA:",MIERCOLES['A'],"- TURNO B: ASIGNATURA: ",MIERCOLES['B']," - TURNO C: ASIGNATURA: ",MIERCOLES['C']," - TURNO D: ASIGNATURA: ",MIERCOLES['D']," - TURNO E - ASIGNATURA: ",MIERCOLES['E'])
    elif recibido[10:16] == "Jueves ":
        print("Horario Jueves -> Aula: ",recibido[0])
        print("TURNO A: ASIGNATURA: ",JUEVES['A'],"- TURNO B: ASIGNATURA: ",JUEVES['B']," - TURNO C: ASIGNATURA: ",JUEVES['C']," - TURNO D: ASIGNATURA: ",JUEVES['D']," - TURNO E - ASIGNATURA: ",JUEVES['E'])
    elif recibido[10:17] == "Viernes":
        print("Horario Viernes -> Aula: ",recibido[0])
        print("TURNO A: ASIGNATURA: ",VIERNES['A'],"- TURNO B: ASIGNATURA: ",VIERNES['B']," - TURNO C: ASIGNATURA: ",VIERNES['C']," - TURNO D: ASIGNATURA: ",VIERNES['D']," - TURNO E - ASIGNATURA: ",VIERNES['E'])

def COMANDOCadaAula(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
    if recibido[9:14] == "Lunes":
        print("Horario Lunes Aula A\n")
        print("TURNO A: ASIGNATURA: ",Aula_A_Lunes['A'],"- TURNO B: ASIGNATURA: ",Aula_A_Lunes['B']," - TURNO C: ASIGNATURA: ",Aula_A_Lunes['C']," - TURNO D: ASIGNATURA: ",Aula_A_Lunes['D']," - TURNO E - ASIGNATURA: ",Aula_A_Lunes['E'])
        print("Horario Lunes Aula B\n")
        print("TURNO A: ASIGNATURA: ",Aula_B_Lunes['A'],"- TURNO B: ASIGNATURA: ",Aula_B_Lunes['B']," - TURNO C: ASIGNATURA: ",Aula_B_Lunes['C']," - TURNO D: ASIGNATURA: ",Aula_B_Lunes['D']," - TURNO E - ASIGNATURA: ",Aula_B_Lunes['E'])
        print("Horario Lunes Aula C\n")
        print("TURNO A: ASIGNATURA: ",Aula_C_Lunes['A'],"- TURNO B: ASIGNATURA: ",Aula_C_Lunes['B']," - TURNO C: ASIGNATURA: ",Aula_C_Lunes['C']," - TURNO D: ASIGNATURA: ",Aula_C_Lunes['D']," - TURNO E - ASIGNATURA: ",Aula_C_Lunes['E'])
    if recibido[9:15] == "Martes":
        print("Horario Martes Aula A\n")
        print("TURNO A: ASIGNATURA: ",Aula_A_Martes['A'],"- TURNO B: ASIGNATURA: ",Aula_A_Martes['B']," - TURNO C: ASIGNATURA: ",Aula_A_Martes['C']," - TURNO D: ASIGNATURA: ",Aula_A_Martes['D']," - TURNO E - ASIGNATURA: ",Aula_A_Martes['E'])
        print("Horario Martes Aula B\n")
        print("TURNO A: ASIGNATURA: ",Aula_B_Martes['A'],"- TURNO B: ASIGNATURA: ",Aula_B_Martes['B']," - TURNO C: ASIGNATURA: ",Aula_B_Martes['C']," - TURNO D: ASIGNATURA: ",Aula_B_Martes['D']," - TURNO E - ASIGNATURA: ",Aula_B_Martes['E'])
        print("Horario MArtes Aula C\n")
        print("TURNO A: ASIGNATURA: ",Aula_C_Martes['A'],"- TURNO B: ASIGNATURA: ",Aula_C_Martes['B']," - TURNO C: ASIGNATURA: ",Aula_C_Martes['C']," - TURNO D: ASIGNATURA: ",Aula_C_Martes['D']," - TURNO E - ASIGNATURA: ",Aula_C_Martes['E'])
    if recibido[9:18] == "Miercoles":
        print("Horario Miercoles Aula A\n")
        print("TURNO A: ASIGNATURA: ",Aula_A_Miercoles['A'],"- TURNO B: ASIGNATURA: ",Aula_A_Miercoles['B']," - TURNO C: ASIGNATURA: ",Aula_A_Miercoles['C']," - TURNO D: ASIGNATURA: ",Aula_A_Miercoles['D']," - TURNO E - ASIGNATURA: ",Aula_A_Miercoles['E'])
        print("Horario Miercoles Aula B\n")
        print("TURNO A: ASIGNATURA: ",Aula_B_Miercoles['A'],"- TURNO B: ASIGNATURA: ",Aula_B_Miercoles['B']," - TURNO C: ASIGNATURA: ",Aula_B_Miercoles['C']," - TURNO D: ASIGNATURA: ",Aula_B_Miercoles['D']," - TURNO E - ASIGNATURA: ",Aula_B_Miercoles['E'])
        print("Horario Miercoles Aula C\n")
        print("TURNO A: ASIGNATURA: ",Aula_C_Miercoles['A'],"- TURNO B: ASIGNATURA: ",Aula_C_Miercoles['B']," - TURNO C: ASIGNATURA: ",Aula_C_Miercoles['C']," - TURNO D: ASIGNATURA: ",Aula_C_Miercoles['D']," - TURNO E - ASIGNATURA: ",Aula_C_Miercoles['E'])
    if recibido[9:15] == "Jueves":
        print("Horario Jueves Aula A\n")
        print("TURNO A: ASIGNATURA: ",Aula_A_Jueves['A'],"- TURNO B: ASIGNATURA: ",Aula_A_Jueves['B']," - TURNO C: ASIGNATURA: ",Aula_A_Jueves['C']," - TURNO D: ASIGNATURA: ",Aula_A_Jueves['D']," - TURNO E - ASIGNATURA: ",Aula_A_Jueves['E'])
        print("Horario Jueves Aula B\n")
        print("TURNO A: ASIGNATURA: ",Aula_B_Jueves['A'],"- TURNO B: ASIGNATURA: ",Aula_B_Jueves['B']," - TURNO C: ASIGNATURA: ",Aula_B_Jueves['C']," - TURNO D: ASIGNATURA: ",Aula_B_Jueves['D']," - TURNO E - ASIGNATURA: ",Aula_B_Jueves['E'])
        print("Horario Jueves Aula C\n")
        print("TURNO A: ASIGNATURA: ",Aula_C_Jueves['A'],"- TURNO B: ASIGNATURA: ",Aula_C_Jueves['B']," - TURNO C: ASIGNATURA: ",Aula_C_Jueves['C']," - TURNO D: ASIGNATURA: ",Aula_C_Jueves['D']," - TURNO E - ASIGNATURA: ",Aula_C_Jueves['E'])
    if recibido[9:16] == "Viernes":
        print("Horario Viernes Aula A\n")
        print("TURNO A: ASIGNATURA: ",Aula_A_Viernes['A'],"- TURNO B: ASIGNATURA: ",Aula_A_Viernes['B']," - TURNO C: ASIGNATURA: ",Aula_A_Viernes['C']," - TURNO D: ASIGNATURA: ",Aula_A_Viernes['D']," - TURNO E - ASIGNATURA: ",Aula_A_Viernes['E'])
        print("Horario Viernes Aula B\n")
        print("TURNO A: ASIGNATURA: ",Aula_B_Viernes['A'],"- TURNO B: ASIGNATURA: ",Aula_B_Viernes['B']," - TURNO C: ASIGNATURA: ",Aula_B_Viernes['C']," - TURNO D: ASIGNATURA: ",Aula_B_Viernes['D']," - TURNO E - ASIGNATURA: ",Aula_B_Viernes['E'])
        print("Horario Viernes Aula C\n")
        print("TURNO A: ASIGNATURA: ",Aula_C_Viernes['A'],"- TURNO B: ASIGNATURA: ",Aula_C_Viernes['B']," - TURNO C: ASIGNATURA: ",Aula_C_Viernes['C']," - TURNO D: ASIGNATURA: ",Aula_C_Viernes['D']," - TURNO E - ASIGNATURA: ",Aula_C_Viernes['E'])

def COMANDOAsignaturaInfo(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
    for i in Aula_A_Lunes:
        if Aula_A_Lunes[i] == int(recibido[15:17]):
            print("Aula A: Lunes -> Bloque",i)
    for i in Aula_A_Martes:
        if Aula_A_Martes[i] == int(recibido[15:17]):
            print("Aula A: Martes -> Bloque",i)
    for i in Aula_A_Miercoles:
        if Aula_A_Miercoles[i] == int(recibido[15:17]):
            print("Aula A: Miercoles -> Bloque",i)
    for i in Aula_A_Jueves:
        if Aula_A_Jueves[i] == int(recibido[15:17]):
            print("Aula A: Jueves -> Bloque",i)
    for i in Aula_A_Viernes:
        if Aula_A_Viernes[i] == int(recibido[15:17]):
            print("Aula A: Viernes -> Bloque",i)

    for i in Aula_B_Lunes:
        if Aula_B_Lunes[i] == int(recibido[15:17]):
            print("Aula B: Lunes -> Bloque",i)
    for i in Aula_B_Martes:
        if Aula_B_Martes[i] == int(recibido[15:17]):
            print("Aula B: Martes -> Bloque",i)
    for i in Aula_B_Miercoles:
        if Aula_B_Miercoles[i] == int(recibido[15:17]):
            print("Aula B: Miercoles -> Bloque",i)
    for i in Aula_B_Jueves:
        if Aula_B_Jueves[i] == int(recibido[15:17]):
            print("Aula B: Jueves -> Bloque",i)
    for i in Aula_B_Viernes:
        if Aula_B_Viernes[i] == int(recibido[15:17]):
            print("Aula B: Viernes -> Bloque",i)

    for i in Aula_C_Lunes:
        if Aula_C_Lunes[i] == int(recibido[15:17]):
            print("Aula C: Lunes -> Bloque",i)
    for i in Aula_C_Martes:
        if Aula_C_Martes[i] == int(recibido[15:17]):
            print("Aula C: Martes -> Bloque",i)
    for i in Aula_C_Miercoles:
        if Aula_C_Miercoles[i] == int(recibido[15:17]):
            print("Aula C: Miercoles -> Bloque",i)
    for i in Aula_C_Jueves:
        if Aula_C_Jueves[i] == int(recibido[15:17]):
            print("Aula C: Jueves -> Bloque",i)
    for i in Aula_C_Viernes:
        if Aula_C_Viernes[i] == int(recibido[15:17]):
            print("Aula C: Viernes -> Bloque",i)

def COMANDOEliminaDia(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
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

def COMANDOEliminaHorario(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
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

def COMANDOAsignaturaEliminada(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
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

def COMANDOBorrarTodo(recibido,LUNES,MARTES,MIERCOLES,JUEVES,VIERNES):
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

def COMANDODiasLibres(dia_libre):
    print("SI ESTA ENTRANDO")
    FERIADO = 1


def mensajeMQTT_AULA(client, userdata, msg):
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
    else:
        print("SALON INCORRECTO")
        client.disconnect()
# COmando CambiarBloque"
# Aula CambiarBloque BLOQUE LUNES #Asig MARTES #Asig MIercoles #ASig Jueves #Asig Viernes #Asig 
    if recibido[2:15] == "CambiarBloque":
        COMANDOCambiarBloque(recibido,Aula_LUNES,Aula_MARTES,Aula_MIERCOLES,Aula_JUEVES,Aula_VIERNES)
        client.disconnect()

# COMANDO ConfigurarDIa
#Aula configura r d i a   L U N E S   B L O Q U E A   1   B L O Q U E B   1   B L O Q U E C   1   B L O Q U E D   1   B L O Q U E E   1
#   012345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970       
    elif recibido[2:15] == "ConfigurarDia":
        COMANDOConfigurardia(recibido,Aula_LUNES,Aula_MARTES,Aula_MIERCOLES,Aula_JUEVES,Aula_VIERNES)
        client.disconnect()
        
# COMANDO AsignarAsignatura
# DIA BLOQUEX NumeroDeAsignatura
    elif recibido[2:19] == "AsignarAsignatura":
        COMANDOAsignarAsignatura(recibido,Aula_LUNES,Aula_MARTES,Aula_MIERCOLES,Aula_JUEVES,Aula_VIERNES)
        client.disconnect()

# COMANDO HorarioSemana(De todos los dias)
        #AULA HorarioSemana
    elif recibido[2:15] == "HorarioSemana":
        COMANDOHorarioSemana(recibido,Aula_LUNES,Aula_MARTES,Aula_MIERCOLES,Aula_JUEVES,Aula_VIERNES)
        client.disconnect()
# COMANDO Horario(De un dia)
        # AULA HORARIO Dia 
    elif recibido[2:9] == "Horario":
        COMANDOHorario(recibido,Aula_LUNES,Aula_MARTES,Aula_MIERCOLES,Aula_JUEVES,Aula_VIERNES)
        client.disconnect()

# COMANDO CadaAula para un dia determinado
        # CadaAula DIA 
    elif recibido[0:8] == "CadaAula":
        COMANDOCadaAula(recibido,Aula_LUNES,Aula_MARTES,Aula_MIERCOLES,Aula_JUEVES,Aula_VIERNES)
        client.disconnect()

# COMANDO InfoAsignatura en cada aula y horario
    #InfoAsignatura #Asig  
    elif recibido[0:14] == "AsignaturaInfo":
        COMANDOAsignaturaInfo(recibido,Aula_LUNES,Aula_MARTES,Aula_MIERCOLES,Aula_JUEVES,Aula_VIERNES)
        client.disconnect()    

# COMANDO EliminaDia en cada aula y horario
    #Aula EliminaDia Dia  
    elif recibido[2:12] == "EliminaDia":
        COMANDOEliminaDia(recibido,Aula_LUNES,Aula_MARTES,Aula_MIERCOLES,Aula_JUEVES,Aula_VIERNES)
        client.disconnect()

# COMANDO EliminaHorario
    #Aula EliminaHorario
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

    elif recibido[0:8] == "DiaLibre":
        FERIADO['Dia'] = 1
        client.disconnect()

# ---------- HORARIOS INICIALES --------------------
Aula_A_Lunes = {'A':1,'B':2,'C':3,'D':0,'E':0}
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

# ------------ Conexión del cliente -----------------
#------------ Datos del broker MQTT -----------------

broker = "192.168.1.30"
puerto = 5050


