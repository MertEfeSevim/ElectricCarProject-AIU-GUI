"""import glob
from tkinter import ttk
import serial
from tkinter import *

def serial_ports():

    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []

    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass

    print(result)
    return result

def GUI():
    root = Tk()
    root.title(serial_ports())
    root.title("Telemetry")

    label = Label(root,text="Select Port")
    label.pack()

    ser = serial.Serial(("/dev/tty.usbmodem1411"),9600)
    label2 = Label(root,text=ser)
    label2.pack()

    #country = ttk.Combobox(root, values = serial_ports())
    #country.pack()

    root.mainloop()

if __name__ == '__main__':
    GUI()

"""""""""""
def readingData(variable):
    def update(ser):
        while 1:
            reading.set(ser.readline())
            root.update()

    try:
        global ser
        ser = serial.Serial(serial_ports()[serial_ports().index(variable.get())], 9600)
        while 1:
            update(ser)
    except ValueError:
        print("Port not found.")

    reading = StringVar()
    w = Label(root, textvariable=reading)
    w.pack()
"""""
"""""""""

countryvar = StringVar()
country = ttk.Combobox(parent, textvariable=countryvar)

ent = Entry(root)
btn = Button(root, text="Choose this port")

ent.pack()
btn.pack()

def GUI():

    root = Tk()
    root.title(serial_ports())
    root.title("Telemetry")
    root.geometry("300x300")
    root.resizable(width=True, height=True)

    label = Label(root, text="Select serial port:")
    label.pack()

    variable = StringVar(root)
    w = OptionMenu(root, *serial_ports())


    button1 = Button(root, text="Choose", command = readingData(variable))
    button1.pack()
    button1.grid()

    w.config(width=6)
    w.grid()
    root.mainloop()
"""
""""""""""
def run_port():
try:
print("running port")
print("Selection: ", variable.get())
print("Selection index: ", serial_ports().index(variable.get()))
global ser
ser = serial.Serial(serial_ports()[serial_ports().index(variable.get())], 9600)
while True:
print(ser.readline())

except ValueError:
print("Port not found.")


button1 = Button(app, text="OK", command=run_port)
button1.config(width=10)
button1.grid()

root.mainloop()
""""""""""""""