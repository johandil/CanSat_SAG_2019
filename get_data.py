import serial

port_number = 'COM4'  # choose port for the Arduino
ser = serial.Serial()  # set Serial() object to ser
ser.port = port_number  # set port to port_number
ser.baudrate = 9600  # set baudrate
ser.open()  # open port
while(True is True):  # loops forever
    with open("maalinger.txt", 'ab') as file:  # append bytes to maalinger.txt
        file.write(ser.readline())
