from datetime import datetime
from calendar import weekday
import paho.mqtt.client as paho
import calendar
from DS3231 import*
from SensorPir import*

#------------ Datos del broker MQTT -----------------
broker = "192.168.1.30"
puerto = 5050

# -------------- Hora actual del sistema ---------------
Ahora = datetime.now()
print("Fecha y Hora del Sistema:\n",Ahora,"\n")
# ----------------------------------------------------

# --------- Condiciones para la fecha y hora --------------
Mes = Ahora.month
if Ahora.month > 9:
    Mes = Mes + 6
HOY = calendar.weekday(Ahora.year,Ahora.month,Ahora.day) 
HOY = HOY + 2
if HOY == 7:
    HOY = 7
H = int('''{:02x}'''.format(RTCvalor['hora']))
if Ahora.hour > 12:
    HORA = Ahora.hour - 12
    FORMATO = 'PM' 
elif Ahora.hour == 0:
    FORMATO = 'AM'
    HORA = 12
else:
    FORMATO = 'AM'
    HORA = Ahora.hour
AÑO = Ahora.year - 2000
# -------------------------------------------------------------

# -------------- AJUSTES DE CLASE DE LO RECIBIDO DEL RTC DS3231-----------------------
S = int('''{:02x}'''.format(RTCvalor['segundos']))
m = int('''{:02x}'''.format(RTCvalor['minutos']))
F = int('''{:02x}'''.format(RTCvalor['fecha']))
M = '''{}'''.format(meses[RTCvalor['mes']])
Y = int('''{:02x}'''.format(RTCvalor['year']))
# ------------------------------------------------------------------------------------

# ----------------------------------- COMPARACIÓN  -------------------------------------------------------
if Y == AÑO and M == meses[Mes] and F == (Ahora.day) and H == HORA: 
    if m == Ahora.minute:
        if S >= Ahora.second + 2 or S <= Ahora.second - 2:
            print("Los segundos del RTC y del equipo no coinciden, se actualizará el RTC\n")
            HoraCero = DS3231.escribir(Ahora.day,Ahora.month,Y,HORA,Ahora.minute,Ahora.second,FORMATO,HOY)
            DS3231.leer()
        else:
            print("La hora del RTC está en el rango permitido\n")
    else:
        print("Los Minutos del RTC y del equipo no coinciden, se actualizará el RTC\n")
        HoraCero = DS3231.escribir(Ahora.day,Ahora.month,Y,HORA,Ahora.minute,Ahora.second,FORMATO,HOY)
        DS3231.leer()
else:
    print("La hora y fecha del RTC no coinciden con la del equipo, se actualizará el RTC\n")
    HoraCero = DS3231.escribir(Ahora.day,Ahora.month,Y,HORA,Ahora.minute,Ahora.second,FORMATO,HOY)
    DS3231.leer()
# ---------------------------------------------------------------------------------------------------------

# --------------- Terminales de salida ------------------------
rojo = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(rojo, GPIO.OUT)
verde = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(verde, GPIO.OUT)
azul = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(azul, GPIO.OUT)
buzzer = 19
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzer, GPIO.OUT)

print("------ Se activa el DHT11 ---------\n")
# -------------------- Registro de Temperatura ----------------------------
for i in range(2001):
    if i%100 == 0 and i !=0:
        lectura_temperatura = dht11(1,datetime.now())
        print(lectura_temperatura)
        lectura_temperaturaMQTT = str(lectura_temperatura)
        # Registrando temperatura en archivo de texto 1----------------
        archivo=open("Temperatura.txt", "a+")
        archivo.write(str(lectura_temperatura))
        archivo.close
        print(f"\rTemporizador {i/10} Segundos\n\rMedición de Temperatura y Humedad completada\n\r")
        cliente = paho.Client()
        cliente.connect(broker,puerto)
        mensaje = cliente.publish("Fecha_y_Temperatura",lectura_temperaturaMQTT)
    msRetardo(100)
    
GPIO.cleanup()

#### PRIMEA PREUBAAAA

"""
# --------- Conexión del cliente y publicación ------------
for i in range(3):
    cliente = paho.Client()
    cliente.connect(broker,puerto)
    mensaje = cliente.publish("topico_de_prueba","SAquenme de LatinoAmerica")
    """
