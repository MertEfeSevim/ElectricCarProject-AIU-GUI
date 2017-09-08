"""import glob
import serial
from tkinter import *

def callback():
    return "a"

def serial_ports():
   
   Lists serial port names

       :raises EnvironmentError:
           On unsupported or unknown platforms
       :returns:
           A list of the serial ports available on the system
   
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
   return result

def gather_data():
    app = Frame(root)
    app.grid()

    variable = StringVar(root)
    w = OptionMenu(root, variable, *serial_ports())
    w.config(width=6)
    w.grid()

    def run_port():
        try:
            def update(portNo):
                while 1:
                    ser = serial.Serial(portNo, 9600)
                    value.set(ser.readline())
                    root.update()

                    print("running port")
                    print("Selection: ", variable.get())
                    print("Selection index: ", serial_ports().index(variable.get()))

            value = StringVar()

            valueDisp = Label(root, textvariable=value)
            valueDisp.pack()

            global ser
            update(variable.get())

        except ValueError:
            print("Port not found.")

    button1 = Button(app, text="Start", command=run_port)
    button1.config(width=10)
    button1.grid()


def create_window():
    window = Tk.winfo_toplevel(root)

if __name__ == '__main__':

    root = Tk()
    root.title("Telemetry")


    b0 = Button(root, text="Minimum Temperature", command=callback)
    b1 = Button(root, text="Maximum Temperature", command=callback)
    b2 = Button(root, text="Average Temperature", command=callback)
    b3 = Button(root, text="Minimum Voltage",     command=callback)
    b4 = Button(root, text="Maximum Voltage",     command=callback)
    b5 = Button(root, text="Average Voltage",     command=callback)
    b6 = Button(root, text="Current",             command=callback)
    b7 = Button(root, text="Velocity",            command=callback)
    b8 = Button(root, text="Serial Ports",        command=create_window())

    b0.pack(side=LEFT)
    b1.pack(side=LEFT)
    b2.pack(side=LEFT)
    b3.pack(side=LEFT)
    b4.pack(side=LEFT)
    b5.pack(side=LEFT)
    b6.pack(side=LEFT)
    b7.pack(side=LEFT)
    b8.pack(side=LEFT)

    root.mainloop()
"""
from tkinter import *

root=Tk()

variable=StringVar()

def update_label():
    i=0
    while 1:
        i=i+1
        variable.set(str(i))
        root.update()

your_label=Label(root,textvariable=variable)
your_label.pack()

start_button=Button(root,text="start",command=update_label)
start_button.pack()

root.mainloop()