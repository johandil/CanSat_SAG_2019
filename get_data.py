import serial
import time

port_number = 'COM4'  # choose port for the Arduino
ser = serial.Serial()  # set Serial() object to ser
ser.port = port_number  # set port to port_number
ser.baudrate = 9600  # set baudrate
ser.open()  # open port
while(ser.in_waiting > 0):  # While there are bites in the port
    with open("datatry.txt", 'ab') as file:
        file.write(ser.readline())


"""
cleaner = [x.strip() for x in readings]
print(cleaner)
cleanest = list(map(int, cleaner))
# print(cleanest)
ser.readlines(100)
"""

