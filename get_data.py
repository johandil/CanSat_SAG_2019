import serial
import time

port_number = 'COM4'

ser = serial.Serial()
ser.port = port_number
ser.baudrate = 9600

print(ser)
ser.open()
print(ser.is_open)
time.sleep(2)
while(True == True):
    with open("datatry.txt", 'ab') as file:
        file.write(ser.readline())


"""
cleaner = [x.strip() for x in readings]
print(cleaner)
cleanest = list(map(int, cleaner))
# print(cleanest)
ser.readlines(100)
"""

