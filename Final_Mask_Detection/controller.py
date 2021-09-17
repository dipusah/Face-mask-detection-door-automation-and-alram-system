from pyfirmata import Arduino,SERVO
import serial

with serial.Serial('COM4', 9600, serial.EIGHTBITS,timeout=0,parity=serial.PARITY_NONE,
rtscts=1) as ser:
    print(ser.is_open)
    ser.close()



    pin=10

    board=Arduino(ser.name)

    board.digital[pin].mode=SERVO

    def rotateServo(pin,angle):
        board.digital[pin].write(angle)

    def doorAutomate(val):
        if val==0:
            rotateServo(pin,180)
        elif val==1:
            rotateServo(pin,40)


