class GUI (object):
    def __init__(self):
        self.root = Tk()
        #self.root.attributes('-fullscreen', True)
        self.root.title("AIU Telemetry")

        # Deneme değerleri
        self.variable = StringVar()
        self.i = 0

        # Değerlerin tek tek dağıtılması gerekiyor
        self.remChar = StringVar()
        self.minVol = StringVar()
        self.aveVol = StringVar()
        self.maxVol = StringVar()
        self.minTemp = StringVar()
        self.aveTemp = StringVar()
        self.maxTemp = StringVar()
        self.curr = StringVar()
        self.speed = StringVar()

        # AIU Logo
        #self.logo = PhotoImage(file="Logo.gif")

        # Frame
        self.frame = Frame(self.root)
        self.frame.pack(side=TOP, fill=BOTH, expand=YES)
        #self.label20 = Label(self.frame, compound=CENTER, image=self.logo)

        # Frame1
        self.frame1 = Frame(self.root)
        self.frame1.pack(side=TOP, fill=BOTH, expand=YES)
        self.labelStart = Label(self.frame1, text="ABU Control Center", font=(12, 12), foreground="dark blue", background="light pink")
        self.label5 = Label(self.frame1, text="                Minimum      ",font=(20, 20), foreground="red")
        self.label6 = Label(self.frame1, text="Average   ", font=(20, 20))
        self.label7 = Label(self.frame1, text="  Maximum ", font=(20, 20), foreground="green")
        self.label0 = Label(self.frame1, textvariable=self.variable, font=(20, 20), foreground="blue")  # variable yerine remChar gelecek

        # Frame2
        self.frame2 = Frame(self.root)
        self.frame2.pack(side=TOP, fill=BOTH, expand=YES)
        self.label1 = Label(self.frame2, text="Voltage        ", font=(20, 20), foreground="blue", background="light blue")
        self.label8 = Label(self.frame2, textvariable=self.variable, font=(14, 14), foreground="red", background="light blue")  # minVol
        self.label9 = Label(self.frame2, textvariable=self.variable,font=(14, 14), background="light blue")
        self.label10 = Label(self.frame2, textvariable=self.variable, font=(14, 14), foreground="green", background="light blue")

        # Frame3
        self.frame3 = Frame(self.root)
        self.frame3.pack(side=TOP, fill=BOTH, expand=YES)
        self.label2 = Label(self.frame3, text="Temperature", font=(20, 20),foreground="dark green", background="light green")
        self.label11 = Label(self.frame3, textvariable=self.variable, font=(14, 14), foreground="red", background="light green")  # minTemp
        self.label12 = Label(self.frame3, textvariable=self.variable,font=(14, 14), background="light green")
        self.label13 = Label(self.frame3, textvariable=self.variable, font=(14, 14), foreground="green", background="light green")

        # Frame4
        self.frame4 = Frame(self.root)
        self.frame4.pack(side=TOP, fill=BOTH, expand=YES)
        self.label3 = Label(self.frame4, text="Current        ", font=(20, 20), foreground="light yellow", background="gold")
        self.label17 = Label(self.frame4, text="-", font=(14, 14),foreground="red", background="gold")
        self.label14 = Label(self.frame4, textvariable=self.variable,font=(14, 14), background="gold")  # curr
        self.label18 = Label(self.frame4, text="-", font=(14, 14),foreground="green", background="gold")

        # Frame5
        self.frame5 = Frame(self.root)
        self.frame5.pack(side=TOP, fill=BOTH, expand=YES)
        self.label4 = Label(self.frame5, text="Speed         ", font=(20, 20), foreground="purple", background="pink")
        self.label16 = Label(self.frame5, text="-", font=(14, 14),foreground="red", background="pink")
        self.label15 = Label(self.frame5, textvariable=self.variable, font=(14, 14), background="pink")  # speed
        self.label19 = Label(self.frame5, text="-", font=(14, 14), foreground="green", background="pink")

    def grid(self):
        #self.label20.pack(side=LEFT, fill=BOTH, expand=YES)

        self.label1.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label2.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label3.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label4.pack(side=LEFT, fill=BOTH, expand=YES)

        self.labelStart.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label5.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label6.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label7.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label0.pack(side=LEFT, fill=BOTH, expand=YES)

        self.label8.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label9.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label10.pack(side=LEFT, fill=BOTH, expand=YES)

        self.label11.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label12.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label13.pack(side=LEFT, fill=BOTH, expand=YES)

        self.label17.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label14.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label18.pack(side=LEFT, fill=BOTH, expand=YES)

        self.label16.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label15.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label19.pack(side=LEFT, fill=BOTH, expand=YES)

    def update_label(self):
        # Methodun benzerinin her değer için kullanılması gerekiyor.
        self.i = self.i + 1
        self.variable.set(str(self.i))
        self.root.after(2000, self.update_label)

        # Dosyayı açıp yazıyor
        with open("telemetry.txt", "a") as thefile:
            thefile.write(str(self.i))
            thefile.write("\n")
            thefile.close()

        print("i", self.i)

    def run(self):
        self.grid()
        self.root.after(2000, self.update_label)
        self.root.mainloop()


if __name__ == '__main__':
    from tkinter import *
    from tkinter.ttk import *
    GUI().run()
