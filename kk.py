import serial
import time
ard = serial.Serial(port="com17", baudrate=9600)
#time.sleep(1)
while True:
    #x = input("Command: ")
    #print(type(x))
    #ard.reset_output_buffer()
    time.sleep(1.5)
    ard.write("ON".encode("utf-8"))

    output = ard.readline().decode(encoding="utf-8").strip()
    print("Arduino>>> ", output)
    #ard.reset_input_buffer()
