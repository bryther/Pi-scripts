import wiringpi
import time

def blink(pin):
    wiringpi.digitalWrite(pin, 1)
    time.sleep(0.008)
    wiringpi.digitalWrite(pin, 0)
    


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
    blink(3)
    blink(4)
    blink(6)
    blink(9)

#cleanup
print("Done")
