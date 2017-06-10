from tkinter import *
from tkinter import ttk

def mainGUI():
    root = Tk()
    root.title("ECP - Telemetry")
    root.geometry("400x400")

    label = Label(root,text="Select port")
    label.pack()


    v = StringVar()
    combobox = ttk.Combobox(root, textvariable=v ,values = serial_ports())
    combobox.current(1)
    combobox.pack()


    root.mainloop()

if __name__ == '__main__':
    mainGUI()
