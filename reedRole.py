import time
import RPi.GPIO as io
def measureSpeed():
    io.setmode(io.BCM)
    reed_pin = 22 #15 nolu pin

    io.setup(reed_pin, io.IN, pull_up_down=io.PUD_UP) # activate input with PullUp

    temp=0
    teker=0.000541
    values=[]
    for i in range(8):
        while True:
            if io.input(reed_pin) and temp==0:
                temp=1
                t0=time.time()

            if io.input(reed_pin)==False and temp==1:
                temp=0
                t1 = time.time()
                break
        averagetimer=(t1-t0)/3600
        values.append(teker/averagetimer)
    result=sum(values)/len(values)
    return result
