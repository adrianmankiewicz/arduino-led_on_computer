import serial
import time
import keyboard

ser=serial.Serial(
port='COM3',
baudrate=9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)
    
value = 0

while True:  # making a loop
        while True:
                if keyboard.is_pressed("alt_gr+space"):  # włącza lampkę podpiętą do złącza "13" na arduino "prawy alt+space"
                        value = 1   
                        ser.write(str.encode(str(value)))
                        time.sleep(0.2)
                        break
        while True:
                if keyboard.is_pressed("alt_gr+space"):  # wyłącza lampkę podpiętą do złącza "13" na arduino 
                        value = 0   
                        ser.write(str.encode(str(value)))
                        time.sleep(0.2)
                        break
