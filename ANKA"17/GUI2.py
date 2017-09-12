def measureSpeed():

    GPIO.setmode(GPIO.BCM)

    reed_pin = 22  # 15 nolu pin

    GPIO.setup(reed_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # activate input with PullUp

    temp = False

    radius = 0.000095  # we need to recalculate

    teker = 2 * 3.14 * radius

    values = []

    i = 0

    memory = 0

    while i < 4:

        zero_time = time.time()

        while (GPIO.input(reed_pin) != 0):

            if float(time.time() - zero_time) > 3:

                memory = 1

                t0 = 1

                t1 = 101

                values.append(0)

                break

        if memory == 1:

            break

        else:

            if temp == False:

                temp = True

                t0 = time.time()

            zero_time = time.time()

            while (GPIO.input(reed_pin) != 1):

                if float(time.time() - zero_time) > 2:

                    memory = 1

                    t0 = 1

                    t1 = 101

                    values.append(0)

                    break

                if memory == 1:

                    break

            if temp == True:

                temp = False

            zero_time = time.time()

            while (GPIO.input(reed_pin) != 0):

                if float(time.time() - zero_time) > 2:

                    memory = 1

                    t0 = 1

                    t1 = 101

                    values.append(0)

                    break

                if memory == 1:

                    break

            if temp == False:

                temp = True

                t1 = time.time()

        hiz = teker / ((t1 - t0) / 3600)

        i += 1

        values.append(hiz)

    return str(int(sum(values) / len(values)))

def BVDecode(lineElements):
    '''
    function evaluates the battery voltage summary sentence from the BMS.
    returns the voltages[] list: {minv, maxv, avgv, totalv}

    INPUT (in hexadecimal):
    min cell voltage: lineElements[2]
    max cell voltage: lineElements[3]
    avg cell voltage: lineElements[4]
    total voltage: lineElements[5]

    first, convert the value (lineElements[n]) from hex to decimal
    formula: (value + offset)*multiplier
    for minV, maxV and avgV, offset: 200, multiplier: 0.01
    for total voltage offset: 0, multiplier 0.01

    i = int(s, 16)   -----> Converts hex s to int i
    str(i)  ------> Converts integer i to string

    IMPORTANT NOTE: The calculated min, max, avg values are in the form:
    "a,b". This value is multiplied by 10 to send as "ab", so that a smaller
    packet can be sent. This "ab" value must be divided by 10 to obtain
    "a,b" on the receiver side.
    '''

    voltages = []

    #                                                Multiply by 10 <-
    #                                                   Offset <-    |
    #                                                           |    |
    voltages.append(str(int((int(lineElements[2], 16) + 200) * 0.01 * 10)))
    voltages.append(str(int((int(lineElements[3], 16) + 200) * 0.01 * 10)))
    voltages.append(str(int((int(lineElements[4], 16) + 200) * 0.01 * 10)))
    voltages.append(str(int(int(lineElements[5], 16) * 0.01 * 10)))

    # The total voltage is of the form "ab,c". It is converted to "abc".

    return voltages

def BTDecode(lineElements):
    '''
    function evaluates the battery temperature summary sentence from the BMS.
    returns the temps[] list: {mintemp, maxtemp, avgtemp}

    INPUT (in hexadecimal):
    min cell temperature: lineElements[2]
    max cell temperature: lineElements[3]
    avg cell temperature: lineElements[4]

    first, convert the value (lineElements[n]) from hex to decimal
    formula: (value + offset)*multiplier
    offset: -100, multiplier: 1

    i = int(s, 16)   -----> Converts hex s to int i
    str(i)  ------> Converts integer i to string

    The values of the form "ab,xyz" are rounded to "ab"
    '''
    temps = []
    temps.append(str(int((int(lineElements[2], 16) - 100))))
    temps.append(str(int((int(lineElements[3], 16) - 100))))
    temps.append(str(int((int(lineElements[4], 16) - 100))))

    return temps

def CVDecode(lineElements):
    '''
    function evaluates the current & voltage sentence from the BMS.
    returns the current

    INPUT (in hexadecimal):
    current: lineElements[2]

    first, convert the value (lineElements[n]) from hex to decimal
    formula: (value + offset)*multiplier
    offset: 0, multiplier: 0.1

    i = int(s, 16)   -----> Converts hex s to int i
    str(i)  ------> Converts integer i to string

    The current is of the form "ab,xyz" is multiplied by 10
    and sent as "abx". This should be corrected at the receiver side.
    '''

    #                            multiply by 10 <-
    #                           multiplier <-    |
    return str(int(int(lineElements[2], 16) * 0.1 * 10))

def BCDecode(lineElements):
    '''
    function evaluates the battery charge sentence from the BMS.
    returns the state of charge

    INPUT (in hexadecimal):
    state of charge: lineElements[3]

    first, convert the value (lineElements[n]) from hex to decimal
    formula: (value + offset)*multiplier
    offset: 0, multiplier: 0.01

    i = int(s, 16)   -----> Converts hex s to int i
    str(i)  ------> Converts integer i to string

    The current is of the form "ab,xyz" is multiplied by 10
    and sent as "abx". This should be corrected at the receiver side.
    '''

    return str(int(int(lineElements[3], 16) * 0.1))


class GUI (object):
    def __init__(self):
        self.root = Tk()
        # self.root.attributes('-fullscreen',True) #RPI'de yorum kalkacak.
        #self.root.attributes('-zoomed', True)  # Maximized window with title bar
        self.root.title("ABU Telemetry")

        # Deneme değerleri
        self.i = 0

        # Değerlerin tek tek dağıtılması gerekiyor
        self.remChar = StringVar()
        self.minVol = StringVar()
        self.aveVol = StringVar()
        self.maxVol = StringVar()
        self.minTemp = StringVar()
        self.totVol = StringVar()
        self.aveTemp = StringVar()
        self.maxTemp = StringVar()
        self.curr = StringVar()
        self.speed = StringVar()

        # AIU Logo
        self.logo = PhotoImage(file="Logo.png")
        # Frame
        self.frame = Frame(self.root)
        self.frame.pack(side=TOP, fill=BOTH, expand=YES)
        self.label20 = Label(self.frame, compound=CENTER, image=self.logo)

        # Frame1
        self.frame1 = Frame(self.root)
        self.frame1.pack(side=TOP, fill=BOTH, expand=YES)
        self.labelStart = Label(self.frame1, text="AIU Control Center",
                                font=(18, 18, "bold"), foreground="dark blue")
        self.label5 = Label(self.frame1, text="\tMinimum ", font=(26, 26), foreground="red")
        self.label6 = Label(self.frame1, text="\tAverage ", font=(26, 26))
        self.label7 = Label(self.frame1, text="\tMaximum", font=(26, 26), foreground="green")
        self.labelTotal = Label(self.frame1, text="\tTotal vol.", font=(26, 26), foreground="gray")
        self.label0 = Label(self.frame1, textvariable=self.remChar, font=(
            26, 26), foreground="blue")  # variable yerine remChar gelecek

        # Frame2
        self.frame2 = Frame(self.root)
        self.frame2.pack(side=TOP, fill=BOTH, expand=YES)
        self.label1 = Label(self.frame2, text="Voltage         ", font=(
            26, 26, "bold"), foreground="blue", background="light blue")
        self.label8 = Label(self.frame2, textvariable=self.minVol, font=(
            20, 20, "bold"), foreground="red", background="light blue")  # minVol
        self.label9 = Label(self.frame2, textvariable=self.aveVol,
                            font=(20, 20, "bold"), background="light blue")
        self.label10 = Label(self.frame2, textvariable=self.maxVol, font=(
            20, 20, "bold"), foreground="green", background="light blue")
        self.labelTotalVol = Label(self.frame2, textvariable=self.totVol, font=(
            20, 20, "bold"), foreground="gray", background="light blue")

        # Frame3
        self.frame3 = Frame(self.root)
        self.frame3.pack(side=TOP, fill=BOTH, expand=YES)
        self.label2 = Label(self.frame3, text="Temperature", font=(
            26, 26, "bold"), foreground="dark green", background="light green")
        self.label11 = Label(self.frame3, textvariable=self.minTemp, font=(
            20, 20, "bold"), foreground="red", background="light green")  # minTemp
        self.label12 = Label(self.frame3, textvariable=self.aveTemp,
                             font=(20, 20, "bold"), background="light green")
        self.label13 = Label(self.frame3, textvariable=self.maxTemp, font=(
            20, 20, "bold"), foreground="green", background="light green")
        self.labelSpace = Label(self.frame3, text="-", font=(20, 20, "bold"),
                                foreground="gray", background="light green")

        # Frame4
        self.frame4 = Frame(self.root)
        self.frame4.pack(side=TOP, fill=BOTH, expand=YES)
        self.label3 = Label(self.frame4, text="Current         ", font=(
            26, 26, "bold"), foreground="light yellow", background="gold")
        self.label17 = Label(self.frame4, text="-", font=(20, 20, "bold"),
                             foreground="red", background="gold")
        self.label14 = Label(self.frame4, textvariable=self.curr,
                             font=(20, 20, "bold"), background="gold")  # curr
        self.label18 = Label(self.frame4, text="-", font=(20, 20, "bold"),
                             foreground="green", background="gold")
        self.labelSpace1 = Label(self.frame4, text="-", font=(20, 20, "bold"),
                                 foreground="gray", background="gold")

        # Frame5
        self.frame5 = Frame(self.root)
        self.frame5.pack(side=TOP, fill=BOTH, expand=YES)
        self.label4 = Label(self.frame5, text="Speed           ", font=(
            26, 26, "bold"), foreground="purple", background="pink")
        self.label16 = Label(self.frame5, text="-", font=(20, 20, "bold"),
                             foreground="red", background="pink")
        self.label15 = Label(self.frame5, textvariable=self.speed,
                             font=(20, 20, "bold"), background="pink")  # speed
        self.label19 = Label(self.frame5, text="-", font=(20, 20, "bold"),
                             foreground="green", background="pink")
        self.labelSpace2 = Label(self.frame5, text="-", font=(20, 20, "bold"),
                                 foreground="gray", background="pink")

    def grid(self):
        self.label20.pack(side=LEFT, fill=BOTH, expand=YES)

        self.label1.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label2.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label3.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label4.pack(side=LEFT, fill=BOTH, expand=YES)

        self.labelStart.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label5.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label6.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label7.pack(side=LEFT, fill=BOTH, expand=YES)
        self.labelTotal.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label0.pack(side=LEFT, fill=BOTH, expand=YES)

        self.label8.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label9.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label10.pack(side=LEFT, fill=BOTH, expand=YES)
        self.labelTotalVol.pack(side=LEFT, fill=BOTH, expand=YES)

        self.label11.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label12.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label13.pack(side=LEFT, fill=BOTH, expand=YES)
        self.labelSpace.pack(side=LEFT, fill=BOTH, expand=YES)

        self.label17.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label14.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label18.pack(side=LEFT, fill=BOTH, expand=YES)
        self.labelSpace1.pack(side=LEFT, fill=BOTH, expand=YES)

        self.label16.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label15.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label19.pack(side=LEFT, fill=BOTH, expand=YES)
        self.labelSpace2.pack(side=LEFT, fill=BOTH, expand=YES)

    def update_label(self):
        message = ""  # message to be shown on gui
        i = 0

        while True:
            line = ser.readline()  # read line from the BMS serial port
            # split the message at each "," occurance.
            # splitted message is stored in the list "lineElements"
            # print (line)

            # BMS may give meaningless characters at
            # the beginning of the serial read.
            # To prevent crashing, try-catch is used.
            try:
                line = line.decode('utf-8')
            except(UnicodeDecodeError):
                time.sleep(0.1)
                continue

            lineElements = line.split(",")

            try:
                if lineElements[0] == "BC1" and i == 0:   # Detect BC1 sentence
                    message += BCDecode(lineElements) + ","
                    time.sleep(0.02)
                    i = 1
                    continue
                elif lineElements[0] == "BV1" and i == 1:       # Detect BV1 sentence
                    message += BVDecode(lineElements)[0] + "," + BVDecode(lineElements)[1] + ","
                    message += BVDecode(lineElements)[2] + "," + BVDecode(lineElements)[3] + ","
                    time.sleep(0.02)
                    i = 2
                    continue
                elif lineElements[0] == "BT1" and i == 2:      # Detect BT1 sentence
                    message += BTDecode(lineElements)[0] + "," + BTDecode(lineElements)[1] + ","
                    message += BTDecode(lineElements)[2] + ","
                    time.sleep(0.02)
                    i = 3
                    continue
                elif lineElements[0] == "CV1" and i == 3:      # Detect CV1 sentence
                    message += CVDecode(lineElements) + ","
                    time.sleep(0.02)
                    i = 0
                else:
                    time.sleep(0.02)
                    continue
            except(ValueError):  # sometimes hex to decimal conversion fails
                # print("exception handled")
                message = ""
                i = 0
                continue

            speed = measureSpeed()
            message += speed
            message = list(message)

            # append zeros to the end of the message
            while len(message) < 32:
                message.append('0')

            if len(message) > 32:
                # print("length limit")
                message = ""
                continue

            radio.write(message)
            # print("Sent the message: {}".format(message))
            break
            # message = "" #reset the message after sending
            # time.sleep(2)

        if len(message) == 32:
            message = "".join(message)
            data = message.split(',')

            self.remChar.set(str(float(data[0]) / 10) + '%')
            self.minVol.set(str(float(data[1]) / 10))
            self.maxVol.set(str(float(data[2]) / 10))
            self.aveVol.set(str(float(data[3]) / 10))
            self.totVol.set(str(float(data[4]) / 10))
            self.minTemp.set(str(data[5]))
            self.maxTemp.set(str(data[6]))
            self.aveTemp.set(str(data[7]))
            self.curr.set(str(float(data[8]) / 10))
            self.speed.set(str(int(data[9])))

            with open("telemetry_logs.txt", "a") as thefile:
                if self.i == 0:
                    thefile.write(
                        '\t\t\t\tRemain Charge\tMin Volt\tMax Volt\tAvg Volt\tTotal Volt\tMin Temp\tMax Temp\tAvg Temp\tCurrent\t\tSpeed\n')
                    self.i += 1
                else:
                    thefile.write(time.ctime() + '\t' + self.remChar.get() + 2 * '\t' + self.minVol.get() + 2 * '\t' +
                                  self.maxVol.get() + 2 * '\t' + self.aveVol.get() + 2 * '\t' +
                                  self.totVol.get() + 2 * '\t' + self.minTemp.get() + 2 * '\t' +
                                  self.maxTemp.get() + 2 * '\t' + self.aveTemp.get() + 2 * '\t' +
                                  self.curr.get() + 2 * '\t' + self.speed.get())
                    thefile.write("\n")
                thefile.close()

        self.root.after(2000, self.update_label)

    def run(self):
        self.grid()
        self.root.after(2000, self.update_label)
        self.root.mainloop()


if __name__ == '__main__':
    from tkinter import *
    import tkinter.font
    from tkinter.ttk import *
    import time
    import glob
    import serial
    import sys
    import binascii
    import RPi.GPIO as GPIO
    from lib_nrf24 import NRF24
    import spidev

    ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=57600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
    )

    # --------RF TRANSMISSION SETUP--------- #

    GPIO.setwarnings(False)

    # setup GPIO
    GPIO.setmode(GPIO.BCM)

    # setup send & receive adresses
    pipes = [[0xE8, 0xE8, 0xF0, 0xF0, 0xE1], [0xF0, 0xF0, 0xF0, 0xF0, 0xE1]]

    # create an instance of radio
    radio = NRF24(GPIO, spidev.SpiDev())
    # initialize radio
    radio.begin(0, 17)

    # size of the message
    radio.setPayloadSize(32)
    # channel 0x76 because why not
    radio.setChannel(0x76)
    # set data rate
    radio.setDataRate(NRF24.BR_1MBPS)
    # power level: more power for more range
    radio.setPALevel(NRF24.PA_MAX)

    # set mode to writing
    radio.openWritingPipe(pipes[0])
    # radio.printDetails()
    GUI().run()
    ser.close()
