import socket
import serial
from time import sleep

ser = serial.Serial('/dev/ttyUSB0', 115200)

HOST = "192.168.0.100"
PORT = 45678

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(5)

print 'Listening...'

while True:

    listen = True

    try:
        c, addr = s.accept()
    except:
        print 'Connection failed...'
        c.close()
        
    print 'Got incoming connection from ', addr
    c.send("Connected...\n")

    while listen:

        try:
            string = c.recv(1024)
            string = string[:-2]
        except:
            print 'Disconnected...'
            c.close()
            listen = False
            break
        
        if string == "Exit" or string == "exit":
            print 'Connection closed...'
            c.send("Disconnecting...\n")
            c.close()
            listen = False
            

        if string == "ON" or string == "on":
            print 'Turning the LED on...'
            ser.write('on')
            sleep(0.1) #Give Arduino time to respond
            response = ser.readline()
            if response == "on":
                c.send("The LED is ON...\n")
                

        if string == "OFF" or string == "off":
            print 'Turning the LED off...'
            ser.write('off')
            sleep(0.1) #Give Arduino time to respond
            response = ser.readline()
            if response == "off":
                c.send("The LED is OFF...\n")
            
            
        else:
            print string
            c.send("Recieved...\n")
