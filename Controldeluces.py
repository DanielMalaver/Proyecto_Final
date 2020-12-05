# -------------------------------------------------
#    Control de luces en los salones
# -------------------------------------------------
# Importación de librerias
from gpiozero import RGBLED
from gpiozero import LED
from datetime import datetime
from time import sleep
from datetime import time
import calendar

#Diccionarios
Meses = {1:'enero',2:'febrero',3:'marzo',4:'abril',
        5:'mayo',6:'junio',7:'julio',8:'agosto',
        9:'septimebre',10:'octubre',11:'noviembre',12:'diciembre'}

Dias = {0:'Lunes',1:'Martes',2:'Miercoles',3:'Jueves',
        4:'Viernes',5:'Sabado',6:'Domingo'}

#Variables para control de tiempo hasta la alrma------------------
T_inicio = datetime.now()
Time = datetime.time(T_inicio)
Empieza_BLOQUE_A = '02:22pm'
Empieza_BLOQUE_B = '02:23pm'
Empieza_BLOQUE_C = '02:24pm'
Empieza_BLOQUE_D = '02:25pm'
Empieza_BLOQUE_E = '02:11pm'
Termina_BLOQUE_E = '02:12pm'

T_Empieza_BLOQUE_A = datetime.strptime(Empieza_BLOQUE_A, '%I:%M%p')
T_Empieza_BLOQUE_B = datetime.strptime(Empieza_BLOQUE_B, '%I:%M%p')
T_Empieza_BLOQUE_C = datetime.strptime(Empieza_BLOQUE_C, '%I:%M%p')
T_Empieza_BLOQUE_D = datetime.strptime(Empieza_BLOQUE_D, '%I:%M%p')
T_Empieza_BLOQUE_E = datetime.strptime(Empieza_BLOQUE_E, '%I:%M%p')
T_Termina_BLOQUE_E = datetime.strptime(Termina_BLOQUE_E, '%I:%M%p')

#----------------------Terminales de salida ------------------------
rgbA = RGBLED(18,23,24)
rgbB = RGBLED(12,16,26)
rgbC = RGBLED(17,27,13)
buzzer = LED(10)

#----------------------Funciones
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
     
def Comparar(actual):
    if Antes == 0:
        Final = T_Empieza_BLOQUE_A - actual
    elif Antes == 1:
        Final = T_Empieza_BLOQUE_B - actual
    elif Antes == 2:
        Final = T_Empieza_BLOQUE_C - actual
    elif Antes == 3:
        Final = T_Empieza_BLOQUE_D - actual
    elif Antes == 4:
        Final = T_Empieza_BLOQUE_E - actual
    else:
        Final = T_Termina_BLOQUE_E - actual
    diccFINAL = {
        'Segundos':Final.seconds,
        'Dias':Final.days,
        'Todo':Final
    }
    return diccFINAL

#----------------- Inicia Código como tal: --------------------------------------
LIBRE = 0
while(True):
    Antes = 0
    tiempo = Capturar()
    print("------------ Día, FECHA Y HORA ACTUAL -----------")
    HOY = calendar.weekday(tiempo['año'],tiempo['mes'],tiempo['dia']) 
    print("Hoy es el día:",Dias[HOY])
    print(tiempo['dia'],"de",Meses[tiempo['mes']],"del",tiempo['año'])
    print(tiempo['hora'],":",tiempo['Minutos'],":",tiempo['Segundos'])

    print("------------ TEMPORIZADOR ACTIVO ----------")
    Temporizador = Comparar(tiempo['todo'])

    # Bucle repetición ------------------------------
    while Temporizador['Segundos'] >= 0:
        Actual = Capturar()
        Temporizador = Comparar(Actual['todo'])
        if (Dias[HOY] == 'Sabado'): # or (Dias[HOY] == 'Domingo'):
            rgbA.color = (0,0,0)
            print("Hoy es fin de semana y no trabajamos")
            #print("Faltan",Temporizador['Segundos'],"Segundos para iniciar el trabajo")
            sleep(1)
            continue
        if Temporizador['Segundos'] > 0:      
            if Antes == 0:
                rgbA.color = (0,0,0)
                print("Faltan",Temporizador['Segundos'],"Segundos para Iniciar BLOQUE A")
            elif Antes == 1:
                print("Faltan",Temporizador['Segundos'],"Segundos para Iniciar BLOQUE B") 
            elif Antes == 2:      
                print("Faltan",Temporizador['Segundos'],"Segundos para Iniciar BLOQUE C")  
            elif Antes == 3:   
                print("Faltan",Temporizador['Segundos'],"Segundos para Terminar BLOQUE D")   
            elif Antes == 4:
                print("Faltan",Temporizador['Segundos'],"Segundos para Iniciar BLOQUE E") 
            elif Antes == 5:      
                print("Faltan",Temporizador['Segundos'],"Segundos para Terminar BLOQUE E")                  
        elif (Temporizador['Segundos']) == 0:
            Antes = Antes + 1
            if Antes == 1:
                print("Empezó el BLOQUE A")

                rgbB.color = (1,1,1)
                Actual = Capturar()
                Temporizador = Comparar(Actual['todo'])
                sleep(2)
            elif Antes == 2:
                print("Empezó BLOQUE B")
                rgbB.color = (1,1,1)
                Actual = Capturar()
                Temporizador = Comparar(Actual['todo'])
                sleep(2)
            elif Antes == 3:
                print("Empezó el BLOQUE C")
                rgbC.color = (1,1,1)
                Actual = Capturar()
                Temporizador = Comparar(Actual['todo'])
                sleep(2)
            elif Antes == 4:
                print("Empezó BLOQUE D")
                rgbA.color = (1,0,0)
                Actual = Capturar()
                Temporizador = Comparar(Actual['todo'])
                sleep(2)
            elif Antes == 5:
                print("Empezó BLOQUE E")
                rgbA.color = (0,0,1)
                Actual = Capturar()
                Temporizador = Comparar(Actual['todo'])
                sleep(2)
            elif Antes == 6:
                print("Terminó LA JORNADA DE HOY")
                rgbA.color = (0,0,0)
                Actual = Capturar()
                break
        sleep(1)
print("----------- FIN -------------------")

