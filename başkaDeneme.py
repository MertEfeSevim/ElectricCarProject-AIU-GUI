class App (object):
    def __init__(self):
        self.root=Tk()
        self.root.geometry("200x140")
        self.variable=StringVar()
        self.i=0

        self.remainCharge=StringVar()

        self.minVol=StringVar()
        self.aveVol=StringVar() #Değerlerin tek tek dağıtılması gerekiyor
        self.maxVol=StringVar()

        self.minTemp=StringVar()
        self.aveTemp=StringVar() #Değerlerin tek tek dağıtılması gerekiyor
        self.maxTemp=StringVar()

        self.curr=StringVar()
        self.speed=StringVar() #Değerlerin tek tek dağıtılması gerekiyor



        self.frame=Frame(self.root)
        self.frame.pack(side=LEFT)

        self.label1=Label(self.frame,text="Voltage")
        self.label2=Label(self.frame,text="Temperature")
        self.label3=Label(self.frame,text="Current")
        self.label4=Label(self.frame,text="Speed")


        self.frame1 = Frame(self.root)
        self.frame1.pack(side=TOP)

        self.label5=Label(self.frame1,text="Min")
        self.label6=Label(self.frame1,text="Ave")
        self.label7=Label(self.frame1,text="Max")
        self.label0=Label(self.frame1,textvariable=self.variable) #variable yerine remainCharge gelecek


        self.frame2 = Frame(self.root)
        self.frame2.pack(side=TOP)

        self.label8=Label(self.frame2,textvariable=self.variable)#minVol
        self.label9=Label(self.frame2,textvariable=self.variable)
        self.label10=Label(self.frame2,textvariable=self.variable)


        self.frame3 = Frame(self.root)
        self.frame3.pack(side=TOP)

        self.label11=Label(self.frame3,textvariable=self.variable)#minTemp
        self.label12=Label(self.frame3,textvariable=self.variable)
        self.label13=Label(self.frame3,textvariable=self.variable)


        self.frame4 = Frame(self.root)
        self.frame4.pack(side=TOP)
        self.label14=Label(self.frame4,textvariable=self.variable) #curr

        self.frame5 = Frame(self.root)
        self.frame5.pack(side=TOP)
        self.label15=Label(self.frame5,textvariable=self.variable) #speed


    def grid(self):
        self.label1.pack(side=TOP)
        self.label2.pack(side=TOP)
        self.label3.pack(side=TOP)
        self.label4.pack(side=TOP)

        self.label5.pack(side=LEFT)
        self.label6.pack(side=LEFT)
        self.label7.pack(side=LEFT)
        self.label0.pack(side=LEFT)


        self.label8.pack(side=LEFT)
        self.label9.pack(side=LEFT)
        self.label10.pack(side=LEFT)

        self.label11.pack(side=LEFT)
        self.label12.pack(side=LEFT)
        self.label13.pack(side=LEFT)

        self.label14.pack()
        self.label15.pack()

    #def closeFile(self,fileName):
    #    self.fileName.close()

    def update_label(self):
        self.i=self.i+1
        self.variable.set(str(self.i))
        self.root.after(2000,self.update_label)

        with open("telemetry.txt", "a") as thefile:
            thefile.write(str(self.i))
            thefile.write("\n")

        print("i",self.i)
     #   self.closeFile(thefile)

    def run(self):
        self.grid()
        self.root.after(2000,self.update_label)
        self.root.mainloop()

if __name__=='__main__':
    from tkinter import *
    App().run()

    #file kapatmakta sorun var
