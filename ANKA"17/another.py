import glob
import serial
from tkinter import *
Info ="telemetry"

BASE = RAISED
SELECTED = FLAT

class Tab(Frame):
    def __init__(self, master, name):
        Frame.__init__(self, master)
        self.tab_name = name

class TabBar(Frame):
    def __init__(self, master=None, init_name=None):
        Frame.__init__(self, master)
        self.tabs = {}
        self.buttons = {}
        self.current_tab = None
        self.init_name = init_name

    def show(self):
        self.pack(side=TOP, expand=YES, fill=X)
        self.switch_tab(self.init_name or self.tabs.keys()[-1])  # switch the tab to the first tab

    def add(self, tab):
        tab.pack_forget()  # hide the tab on init

        self.tabs[tab.tab_name] = tab  # add it to the list of tabs
        b = Button(self, text=tab.tab_name, relief=BASE,  # basic button stuff
                   command=(lambda name=tab.tab_name: self.switch_tab(name)))  # set the command to switch tabs
        b.pack(side=LEFT)  # pack the buttont to the left mose of self
        self.buttons[tab.tab_name] = b  # add it to the list of buttons

    def delete(self, tabname):

        if tabname == self.current_tab:
            self.current_tab = None
            self.tabs[tabname].pack_forget()
            del self.tabs[tabname]
            self.switch_tab(self.tabs.keys()[0])

        else:
            del self.tabs[tabname]

        self.buttons[tabname].pack_forget()
        del self.buttons[tabname]

    def switch_tab(self, name):
        if self.current_tab:
            self.buttons[self.current_tab].config(relief=BASE)
            self.tabs[self.current_tab].pack_forget()  # hide the current tab
        self.tabs[name].pack(side=BOTTOM)  # add the new tab to the display
        self.current_tab = name  # set the current tab to itself

        self.buttons[name].config(relief=SELECTED)  # set it to the selected style

def serial_ports():
   """
   Lists serial port names

       :raises EnvironmentError:
           On unsupported or unknown platforms
       :returns:
           A list of the serial ports available on the system
   """
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
    file = open("gatheredData.txt", "w")

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
                    print(variable.get())

                    #print("Gathered value: ", root)
                    #file.write(value)

            value = StringVar()
            valueDisp = Label(root, textvariable=value)
            valueDisp.pack()
            #file.close()

            global ser
            update(variable.get())

        except ValueError:
            print("Port not found.")

    button1 = Button(app, text="Start", command=run_port)
    button1.config(width=10)
    button1.grid()

if __name__ == '__main__':

    root = Tk()
    root.title("Telemetry")
    root.geometry("1205x130")
    bar = TabBar(root, "Info")

    tab1 = Tab(root, "Minimum Temperature")
    tab2 = Tab(root, "Maximum Temperature")
    tab3 = Tab(root, "Average Temperature")
    tab4 = Tab(root, "Minimum Voltage")
    tab5 = Tab(root, "Maximum Voltage")
    tab6 = Tab(root, "Average Voltage")
    tab7 = Tab(root, "Current")
    tab8 = Tab(root, "Velocity")

    tab9= Tab(root, "Serial Ports")
    Button(tab9, text="PRESS ME!", command=(lambda :gather_data())).pack(side=BOTTOM, expand=YES,fill=BOTH)

    tab10 = Tab(root, "Info")

    bar.add(tab1)
    bar.add(tab2)
    bar.add(tab3)
    bar.add(tab4)
    bar.add(tab5)
    bar.add(tab6)
    bar.add(tab7)
    bar.add(tab8)
    bar.add(tab9)
    bar.add(tab10)

    bar.show()
    root.mainloop()