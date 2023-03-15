import wiringpi
import time

def turn(pin, nextpin):
    wiringpi.digitalWrite(pin, 1)
    wiringpi.digitalWrite(nextpin, 1)
    time.sleep(0.008)
    wiringpi.digitalWrite(pin, 0)
    wiringpi.digitalWrite(nextpin, 0)


# setup

print("start")
pin = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(3, 1)
wiringpi.pinMode(4, 1)
wiringpi.pinMode(6, 1)
wiringpi.pinMode(9, 1)

#main
for i in range(1,1000):
    turn(3,4)
    turn(4,6)
    turn(6,9)
    turn(9,3)

#cleanup
print("Done")
