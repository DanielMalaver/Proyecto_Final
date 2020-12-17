# -------------------------------------------------
#    Control de luces en los salones
# -------------------------------------------------
# Importación de librerias

from gpiozero import RGBLED
from gpiozero import MotionSensor, LED
from datetime import datetime
from time import sleep
from datetime import time
import calendar
import paho.mqtt.client as mqtt
import paho.mqtt.client as paho
from Solo_funciones import*
from signal import pause

# ---------------- Variables y Diccionarios el para control de tiempo de los bloques ------------------
Meses = {1:'enero',2:'febrero',3:'marzo',4:'abril',
        5:'mayo',6:'junio',7:'julio',8:'agosto',
        9:'septimebre',10:'octubre',11:'noviembre',12:'diciembre'}

Dias = {0:'Lunes',1:'Martes',2:'Miercoles',3:'Jueves',
        4:'Viernes',5:'Sabado',6:'Domingo'}

T_inicio = datetime.now()
Time = datetime.time(T_inicio)
Empieza_BLOQUE_A = '02:00pm'
Empieza_BLOQUE_B = '02:05pm'
Empieza_BLOQUE_C = '02:10pm'
Empieza_BLOQUE_D = '02:15pm'
Empieza_BLOQUE_E = '02:20pm'
Termina_BLOQUE_E = '02:22pm'

T_Empieza_BLOQUE_A = datetime.strptime(Empieza_BLOQUE_A, '%I:%M%p')
T_Empieza_BLOQUE_B = datetime.strptime(Empieza_BLOQUE_B, '%I:%M%p')
T_Empieza_BLOQUE_C = datetime.strptime(Empieza_BLOQUE_C, '%I:%M%p')
T_Empieza_BLOQUE_D = datetime.strptime(Empieza_BLOQUE_D, '%I:%M%p')
T_Empieza_BLOQUE_E = datetime.strptime(Empieza_BLOQUE_E, '%I:%M%p')
T_Termina_BLOQUE_E = datetime.strptime(Termina_BLOQUE_E, '%I:%M%p')

#----------------------Terminales de salida ------------------------

rgbA = RGBLED(18,23,24)
rgbB = RGBLED(17,27,22)
rgbC = RGBLED(12,16,26)
buzzer = LED(10)
pir = MotionSensor(21)

#----------------------FuncioneS--------------------------


# --------- Funcion para alarma de movimeinto una vez finalizada la jornada --------
def Detector_Movimiento(tiempo):
    delay = 0
    tiempo = tiempo - 1
    while tiempo > 60:
        Pantalla = "Faltan "+str(tiempo)+" para empezar el Bloque A"
        cliente = paho.Client()
        cliente.connect(broker,puerto)
        mensaje = cliente.publish("Pantalla_de_control",Pantalla)
        if pir.motion_detected:
            delay = 1
            for i in range(20):
                buzzer.on()
                rgbA.color = (1,1,1)
                sleep(0.12)
                buzzer.off()
                rgbA.color = (0,0,0)
                sleep(0.11)
        if delay == 1:
            tiempo = tiempo - 5
        else:
            tiempo = tiempo - 1
        delay = 0
        sleep(1)
    S = 0
    return S 

# --------- Funcion para capturar el tiempo actual --------
def Capturar():
    T = datetime.now()
    diccTiempo = {
        'todo':T,
        'dia':T.day,
        'mes':T.month,
        'año':T.year,
        'hora':T.hour,
        'Minutos':T.minute,
        'Segundos':T.second}
    return diccTiempo
     
# --------- Funcion para comparar el tiempo restante del bloque --------
def Comparar(actual,bloque):
    if bloque == 0:
        Final = T_Empieza_BLOQUE_A - actual
    elif bloque == 1:
        Final = T_Empieza_BLOQUE_B - actual
    elif bloque == 2:
        Final = T_Empieza_BLOQUE_C - actual
    elif bloque == 3:
        Final = T_Empieza_BLOQUE_D - actual
    elif bloque == 4:
        Final = T_Empieza_BLOQUE_E - actual
    else:
        Final = T_Termina_BLOQUE_E - actual
    diccFINAL = {
        'Segundos':Final.seconds,
        'Dias':Final.days,
        'Todo':Final
    }
    return diccFINAL

# --------- Funcion para fijar cada bloque --------
def Captura_Bloque(BLOQUE):
    T = BLOQUE
    diccTiempo = {
        'hora':T.hour,
        'Minutos':T.minute,
        'Segundos':T.second}
    return diccTiempo
"""
Empieza_BLOQUE_A = '10:49pm'
Empieza_BLOQUE_B = '11:14pm'
Empieza_BLOQUE_C = '11:15pm'
Empieza_BLOQUE_D = '11:16pm'
Empieza_BLOQUE_E = '11:17pm'
Termina_BLOQUE_E = '11:18pm'
"""
# --------- Funcion paradeterminar en que bloque estamos --------
def Seleccion_Bloque(Hora,Minutos,A,B,C,D,E,EF):
    print(Hora)
    if Hora >= 12:
        #Hora = Hora - 12
        #print(Hora)
        F = "p"
    else:
        F = "a"
    print(A['hora'])
    if Empieza_BLOQUE_A[5] == F:
        if int(A['hora']) >= Hora:
            if int(A['Minutos']) > Minutos:
                S = 0
                print(S)
                return S
    if Empieza_BLOQUE_B[5] == F:
        if int(B['hora']) >= Hora:
            if int(B['Minutos']) > Minutos:
                S = 1
                print(S)
                return S
    if Empieza_BLOQUE_C[5] == F:
        if int(C['hora']) >= Hora:
            if int(C['Minutos']) > Minutos:
                S = 2
                print(S)
                return S
    if Empieza_BLOQUE_D[5] == F:
        if int(D['hora']) >= Hora:
            if int(D['Minutos']) > Minutos:
                S = 3
                print(S)
                return S
    if Empieza_BLOQUE_E[5] == F:
        if int(E['hora']) >= Hora:
            if int(E['Minutos']) > Minutos:
                S = 4
                print(S)
                return S
    if Termina_BLOQUE_E[5] == F:
        if int(EF['hora']) >= Hora:
            if int(EF['Minutos']) > Minutos:
                S = 5
                print(S)
                return S
    S = 0
    print(S)
    return S

# --------- Funcion para determinar si encender o no las luces del aula --------  
def Revisa_Aula(turno,Dia,LuzA,LuzB,LuzC):
    if turno == 1:
        turno = 'A'
    elif turno == 2:
        turno = 'B'
    elif turno == 3:
        turno = 'C'
    elif turno == 4:
        turno = 'D'
    elif turno == 5:
        turno = 'E'

    if Dia == "Lunes":
        for i in Aula_A_Lunes:
            if i == turno:
                print(Aula_A_Lunes[i])
                if Aula_A_Lunes[i] == 0:
                    rgbA.color = (0,0,0)
                    LuzA = 0
                else:
                    rgbA.color = (1,0,0)
                    LuzA = 1
        for i in Aula_B_Lunes:
            if i == turno:
                print(Aula_B_Lunes[i])
                if Aula_B_Lunes[i] == 0:
                    rgbB.color = (0,0,0)
                    LuzB = 0
                else:
                    rgbB.color = (0,1,0)
                    LuzB = 1
        for i in Aula_C_Lunes:
            if i == turno:
                print(Aula_C_Lunes[i])
                if Aula_C_Lunes[i] == 0:
                    rgbC.color = (0,0,0)
                    LuzC = 0
                else:
                    rgbC.color = (0,0,1)
                    LuzC = 1

    elif Dia == "Martes":
        for i in Aula_A_Martes:
            if i == turno:
                print(Aula_A_Martes[i])
                if Aula_A_Martes[i] == 0:
                    rgbA.color = (0,0,0)
                    LuzA = 0
                else:
                    rgbA.color = (1,0,0)
                    LuzA = 1
        for i in Aula_B_Martes:
            if i == turno:
                print(Aula_B_Martes[i])
                if Aula_B_Martes[i] == 0:
                    rgbB.color = (0,0,0)
                    LuzB = 0
                else:
                    rgbB.color = (0,1,0)
                    LuzB = 1
        for i in Aula_C_Martes:
            if i == turno:
                print(Aula_C_Martes[i])
                if Aula_C_Martes[i] == 0:
                    rgbC.color = (0,0,0)
                    LuzC = 0
                else:
                    rgbC.color = (0,0,1)
                    LuzA = 1

    elif Dia == "Miercoles":
        for i in Aula_A_Miercoles:
            if i == turno:
                print(Aula_A_Miercoles[i])
                if Aula_A_Miercoles[i] == 0:
                    rgbA.color = (0,0,0)
                    LuzA = 0
                else:
                    rgbA.color = (1,0,0)
                    LuzA = 1
        for i in Aula_B_Miercoles:
            if i == turno:
                print(Aula_B_Miercoles[i])
                if Aula_B_Miercoles[i] == 0:
                    rgbB.color = (0,0,0)
                    LuzB = 0
                else:
                    rgbB.color = (0,1,0)
                    LuzB = 1
        for i in Aula_C_Miercoles:
            if i == turno:
                print(Aula_C_Miercoles[i])
                if Aula_C_Miercoles[i] == 0:
                    rgbC.color = (0,0,0)
                    LuzC = 0
                else:
                    rgbC.color = (0,0,1)
                    LuzC = 1
        
    elif Dia == 'Jueves':
        for i in Aula_A_Jueves:
            if i == turno:
                print(Aula_A_Jueves[i])
                if Aula_A_Jueves[i] == 0:
                    rgbA.color = (0,0,0)
                    LuzA = 0
                else:
                    rgbA.color = (1,0,0)
                    LuzA = 1
        for i in Aula_B_Jueves:
            if i == turno:
                print(Aula_B_Jueves[i])
                if Aula_B_Jueves[i] == 0:
                    rgbB.color = (0,0,0)
                    LuzB = 0
                else:
                    rgbB.color = (0,1,0)
                    LuzB = 1
        for i in Aula_C_Jueves:
            if i == turno:
                print(Aula_C_Jueves[i])
                if Aula_C_Jueves[i] == 0:
                    rgbC.color = (0,0,0)
                    LuzC = 0
                else:
                    rgbC.color = (0,0,1)
                    LuzC = 1
        
    elif Dia == "Viernes":
        for i in Aula_A_Viernes:
            if i == turno:
                print(Aula_A_Viernes[i])
                if Aula_A_Viernes[i] == 0:
                    rgbA.color = (0,0,0)
                    LuzA = 0
                else:
                    rgbA.color = (1,0,0)
                    LuzA = 1
        for i in Aula_B_Viernes:
            if i == turno:
                print(Aula_B_Viernes[i])
                if Aula_B_Viernes[i] == 0:
                    rgbB.color = (0,0,0)
                    LuzB = 0
                else:
                    rgbB.color = (0,1,0)
                    LuzB = 1
        for i in Aula_C_Viernes:
            if i == turno:
                print(Aula_C_Viernes[i])
                if Aula_C_Viernes[i] == 0:
                    rgbC.color = (0,0,0)
                    LuzC = 0
                else:
                    rgbC.color = (0,0,1)
                    LuzC = 1

    return [LuzA,LuzB,LuzC]

# ------------------------ Inicia ciclo de control de luces ----------------------------------------
def Control_Luces(Aula_a_Lunes,Aula_a_Martes,Aula_a_Miercoles,Aula_a_Jueves,Aula_a_Viernes,
            Aula_b_Lundes,Aula_b_Martes,Aula_b_Miercoles,Aula_b_Jueves,Aula_b_Viernes,
            Aula_c_Lunes,Aula_c_Mardes,Aula_c_Miercoles,Aula_c_Jueves,Aula_c_Viernes,feriado):
    LIBRE = 0
    tiempo = Capturar()
    A = Captura_Bloque(T_Empieza_BLOQUE_A)
    B = Captura_Bloque(T_Empieza_BLOQUE_B)
    C = Captura_Bloque(T_Empieza_BLOQUE_C)
    D = Captura_Bloque(T_Empieza_BLOQUE_D)
    E = Captura_Bloque(T_Empieza_BLOQUE_E)
    EF = Captura_Bloque(T_Termina_BLOQUE_E)
    BLOQUE = Seleccion_Bloque(tiempo['hora'],tiempo['Minutos'],A,B,C,D,E,EF)
    CAMBIAR = 0
    Pregunta = "N"
    BloqueMQTT = "A"
    Luz_A_MQTT = 0
    Luz_B_MQTT = 0
    Luz_C_MQTT = 0
    Control_dia = 0
    Luces = [0,0,0]
    S = [0,0,0]
    PIR = 0
    while(True):
        if Pregunta == "S" or Pregunta == "s":
            break
        Pantalla = "------------ Día, FECHA Y HORA ACTUAL -----------\n"
        HOY = calendar.weekday(tiempo['año'],tiempo['mes'],tiempo['dia']) 
        Pantalla2 = "Hoy es el día: "+str(Dias[HOY])+"\n"
        Pantalla3 = str(tiempo['dia'])+" de "+str(Meses[tiempo['mes']])+" del "+str(tiempo['año'])+"\n"
        Pantalla4 = str(tiempo['hora'])+" : "+str(tiempo['Minutos'])+" : "+str(tiempo['Segundos'])+"\n"
        sleep(1)
        cliente = paho.Client()
        cliente.connect(broker,puerto)
        mensaje = cliente.publish("Pantalla_de_control",Pantalla+Pantalla2+Pantalla3+Pantalla4)
#--------------------- PREGUNTA SI ES DÍA LIBRE ----------------------
        if Control_dia == Dias[HOY]:
            LIBRE = 0
            print("Hoy es Dia libre y no trabajamos")
            continue
        if (Dias[HOY] == 'Sabado') or (Dias[HOY] == 'Domingo'):
            rgbA.color = (0,0,0)
            rgbB.color = (0,0,0)
            rgbC.color = (0,0,0)
            print("Hoy es fin de semana y no trabajamos")
            LIBRE = 0
            sleep(1)
            continue
        elif LIBRE == 1:
            print("Mañana es fin de semana y no trabajamos")
            continue
        if feriado == 1 and LIBRE == 2:
            LIBRE = 3
            feriado = 0
            Control_dia = Dias[HOY+1]
            print("Mañana es Dia libre y no trabajamos")
            continue
        elif LIBRE == 3:
            print("Mañana es Dia libre y no trabajamos")
            continue
#---------------------------------------------------------------------

        print("------------ TEMPORIZADOR ACTIVO ----------")
        Temporizador = Comparar(tiempo['todo'],BLOQUE)

    # Bucle repetición del bloque en curso------------------------------
        while Temporizador['Segundos'] >= 0:
            Actual = Capturar()
            Temporizador = Comparar(Actual['todo'],BLOQUE)
            if Temporizador['Segundos'] > 0:      
                if BLOQUE == 0:
                    rgbA.color = (0,0,0)
                    Pantalla = "Faltan "+str(Temporizador['Segundos'])+" Segundos para Iniciar el BLOQUE A\n"
                elif BLOQUE == 1:
                    Pantalla = "Faltan "+str(Temporizador['Segundos'])+" Segundos para Iniciar el BLOQUE B\n"
                elif BLOQUE == 2:      
                    Pantalla = "Faltan "+str(Temporizador['Segundos'])+" Segundos para Iniciar el BLOQUE C\n" 
                elif BLOQUE == 3:   
                    Pantalla = "Faltan "+str(Temporizador['Segundos'])+" Segundos para Iniciar el BLOQUE D\n"   
                elif BLOQUE == 4:
                    Pantalla = "Faltan "+str(Temporizador['Segundos'])+" Segundos para Iniciar el BLOQUE E\n"
                elif BLOQUE == 5:      
                    Pantalla = "Faltan "+str(Temporizador['Segundos'])+" Segundos para Terminar el BLOQUE E\n"
                if PIR == 1:
                    PIR = Detector_Movimiento(Temporizador['Segundos'])
                    Actual = Capturar()
                    Temporizador = Comparar(Actual['todo'],BLOQUE) 
                cliente = paho.Client()
                cliente.connect(broker,puerto)
                mensaje = cliente.publish("Pantalla_de_control",Pantalla)  
# --------- Chequeo de aulas una vez empieza cada bloque --------           
            elif (Temporizador['Segundos']) == 0:
                BLOQUE = BLOQUE + 1
                if BLOQUE == 1:
                    BloqueMQTT = "A"
                    Pantalla= "Empezó el BLOQUE A"
                    Luces = Revisa_Aula(BLOQUE,Dias[HOY],Luz_A_MQTT,Luz_B_MQTT,Luz_C_MQTT)
                    Actual = Capturar()
                    print("la luz A esta: ",Luces[0])
                    print("la luz B esta: ",Luces[1])
                    print("la luz C esta: ",Luces[2])
                    Temporizador = Comparar(Actual['todo'],BLOQUE)
                    sleep(2)
                elif BLOQUE == 2:
                    BloqueMQTT = "B"
                    Pantalla= "Empezó el BLOQUE B"
                    Luces = Revisa_Aula(BLOQUE,Dias[HOY],Luz_A_MQTT,Luz_B_MQTT,Luz_C_MQTT)
                    Actual = Capturar()
                    print("la luz A esta: ",Luces[0])
                    print("la luz B esta: ",Luces[1])
                    print("la luz C esta: ",Luces[2])
                    Temporizador = Comparar(Actual['todo'],BLOQUE)
                    sleep(2)
                elif BLOQUE == 3:
                    BloqueMQTT = "C"
                    Pantalla= "Empezó el BLOQUE C"
                    Luces = Revisa_Aula(BLOQUE,Dias[HOY],Luz_A_MQTT,Luz_B_MQTT,Luz_C_MQTT)
                    Actual = Capturar()
                    print("la luz A esta: ",Luces[0])
                    print("la luz B esta: ",Luces[1])
                    print("la luz C esta: ",Luces[2])
                    Actual = Capturar()
                    Temporizador = Comparar(Actual['todo'],BLOQUE)
                    sleep(2)
                elif BLOQUE == 4:
                    BloqueMQTT = "D"
                    Pantalla= "Empezó el BLOQUE D"
                    Luces = Revisa_Aula(BLOQUE,Dias[HOY],Luz_A_MQTT,Luz_B_MQTT,Luz_C_MQTT)
                    Actual = Capturar()
                    print("la luz A esta: ",Luces[0])
                    print("la luz B esta: ",Luces[1])
                    print("la luz C esta: ",Luces[2])
                    Actual = Capturar()
                    Temporizador = Comparar(Actual['todo'],BLOQUE)
                    sleep(2)
                elif BLOQUE == 5:
                    BloqueMQTT = "E"
                    Pantalla= "Empezó el BLOQUE E"
                    Luces = Revisa_Aula(BLOQUE,Dias[HOY],Luz_A_MQTT,Luz_B_MQTT,Luz_C_MQTT)
                    Actual = Capturar()
                    print("la luz A esta: ",Luces[0])
                    print("la luz B esta: ",Luces[1])
                    print("la luz C esta: ",Luces[2])
                    Actual = Capturar()
                    Temporizador = Comparar(Actual['todo'],BLOQUE)
                    sleep(2)
                elif BLOQUE == 6:
                    BloqueMQTT = 6
                    Pantalla = "Terminó LA JORNADA DE HOY"
                    rgbA.color = (0,0,0)
                    rgbB.color = (0,0,0)
                    rgbC.color = (0,0,0)
                    BLOQUE = 0
                    Actual = Capturar()
                    LIBRE = 2
                    PIR = 1
                    #break
                cliente = paho.Client()
                cliente.connect(broker,puerto)
                mensaje = cliente.publish("Pantalla_de_control",Pantalla)
            CAMBIAR = CAMBIAR + 1
            sleep(1)
# ----------------------------------
            #if CAMBIAR == 30:
             #   CAMBIAR = 0
              #  Pregunta = input("¿Quieres realizar algun cambio en el horario? (Aplicable a partir dl siguiente bloque: ")
            #if Pregunta == "S" or Pregunta == "s":
             #   break
# --------------------------------
            if Temporizador['Segundos']%60 == 0 and Temporizador['Segundos'] != 0 and BLOQUE >= 1:
                print(Luces[0])
                print(Luces[1])
                print(Luces[2])
                for i in range(3):
                    if Luces[i] == 1:
                        S[i] = "Encendidas"
                    else:
                        S[i] = "Apagadas"
                print("VAMOS A PREGUNTAR:") 
                Aula_y_BLoque = "LAs luces del aula A se encuentran "+str(S[0])+" En el bloque: "+str(BloqueMQTT)
                cliente = paho.Client()
                cliente.connect(broker,puerto)
                mensaje = cliente.publish("Salon_A",Aula_y_BLoque)
                Aula_y_BLoque = "Las luces del aula B se encuentran "+str(S[1])+" En el bloque: "+str(BloqueMQTT)
                cliente = paho.Client()
                cliente.connect(broker,puerto)
                mensaje = cliente.publish("Salon_B",Aula_y_BLoque)
                Aula_y_BLoque = "Las luces del aula C se encuentran "+str(S[2])+" En el bloque: "+str(BloqueMQTT)
                cliente = paho.Client()
                cliente.connect(broker,puerto)
                mensaje = cliente.publish("Salon_C",Aula_y_BLoque)
        if Dias[HOY] == 'Viernes' and Pregunta != "S" and Pregunta != "s":
            LIBRE = 1
    print("----------- FIN -------------------")

