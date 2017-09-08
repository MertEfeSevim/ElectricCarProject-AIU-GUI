import time
import RPi.GPIO as GPIO

def measureSpeed():
    GPIO.setmode(GPIO.BCM)
    reed_pin = 22 #15 nolu pin

    GPIO.setup(reed_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP) # activate input with PullUp

    temp = False
    radius = 0.000270    #we need to recalculate 
    teker = 2*3.14*radius
    values = []

    i = 0
    zero_time = time.time()
    memory=0
    
    while i < 4:
        
        while (GPIO.input(reed_pin) != 0):
            if float(time.time()-zero_time) > 3:
                memory=1
                t0=1
                t1=101
                values.append(0)
                break
        if memory == 1:
            break
            
        if temp == False and GPIO.input(reed_pin) == 0:
            temp = True
            t0 = time.time()
            
        while (GPIO.input(reed_pin) != 1):
            print()
            
        if temp == True and GPIO.input(reed_pin) == 1:
            temp = False
            t1 = time.time()
            
        hiz = teker / ((t1-t0) / 3600)
        i+=1
        values.append(hiz)
        
    return round(sum(values) / len(values), 1)
        
    


#for _ in range(15):
#    print(measureSpeed())





