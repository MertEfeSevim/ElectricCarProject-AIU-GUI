class App (object):
    def measureSpeed():
        GPIO.setmode(GPIO.BCM)
        reed_pin = 22  # 15 nolu pin

        GPIO.setup(reed_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # activate input with PullUp

        temp = False
        radius = 0.000270  # we need to recalculate
        teker = 2 * 3.14 * radius
        values = []

        i = 0
        zero_time = time.time()
        memory = 0

        while i < 4:

            while (GPIO.input(reed_pin) != 0):
                if float(time.time() - zero_time) > 3:
                    memory = 1
                    t0 = 1
                    t1 = 101
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

            hiz = teker / ((t1 - t0) / 3600)
            i += 1
            values.append(hiz)

        return round(sum(values) / len(values), 1)

    def __init__(self):

        #Arayüzün değişkenleri ve tanımları
        self.root=Tk()
        self.root.geometry("300x300")
        self.variable=StringVar()

        #Burada ki i yerine stringimiz gelecek,
        #i olarak kalırsa değişken ismi daha kolay olur
        self.i=0

        #Etiketi tanımlıyor
        self.your_label=Label(self.root,textvariable=self.variable)


    def grid(self):
        #Etiketi yerleştiriyor, istenirse butonda konulabilir sonra
        self.your_label.pack()


    def update_label(self):

        #Denemek için i döngüyle arttırılıyor
        self.i = self.measureSpeed()

        #Stringe çeviriyor datayı
        self.variable.set(str(self.i))
        self.root.after(3000,self.update_label)

        #Dosyayı açıp, stringi append ediyor
        with open("speedReceive.txt", "a") as file:
            file.write(str(self.i))
            file.write("\n")

        print("i",self.i) #Denemek için yazdım silinebilir


    def run(self):

        #3000 milisaniye bir güncelliyor, arayüzü açık tutuyor.
        self.grid()
        self.root.after(3000,self.update_label)
        self.root.mainloop()

if __name__=='__main__':

    from tkinter import *
    import time
    import RPi.GPIO as GPIO

    App().run()