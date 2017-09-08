import time
import RPi.GPIO as io

def measureSpeed():
    io.setmode(io.BCM)
    reed_pin = 22 #15 nolu pin

    io.setup(reed_pin, io.IN, pull_up_down=io.PUD_UP) # activate input with PullUp

    temp=False
    teker=0.000541
    values=[]

    for i in range(8):

        while True:
            if io.input(reed_pin) and temp == False:
                temp=True
                t0=time.time()

            if (io.input(reed_pin)== None or io.input(reed_pin)== False) and temp == True:
                temp=False
                t1 = time.time()
                break

            else:
                t0 = 1
                t1 = 101
                values.append(1)
                break

        values.append(teker/((t1-t0)/3600))

    return sum(values)/len(values)
