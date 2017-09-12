class GUI (object):

    def __init__(self):
        self.root = Tk()
        # self.root.attributes('-fullscreen',True)
        self.root.title("AIU Telemetry")

        # Deneme değerleri
        self.variable = StringVar()
        self.i = 0

        # Değerlerin tek tek dağıtılması gerekiyor
        self.speed = StringVar()

        # AIU Logo
        # Frame
        self.frame = Frame(self.root)
        self.frame.pack(side=TOP, fill=BOTH, expand=YES)

        # Frame1
        self.frame1 = Frame(self.root)
        self.frame1.pack(side=TOP, fill=BOTH, expand=YES)
        self.labelStart = Label(self.frame1, text="AIU Control Center",
                                font=(12, 12, "bold"), foreground="dark blue")
        self.label5 = Label(self.frame1, text="         Minimum ", font=(20, 20), foreground="red")
        self.label6 = Label(self.frame1, text="Average ", font=(20, 20))
        self.label7 = Label(self.frame1, text="Maximum", font=(20, 20), foreground="green")
        self.labelTotal = Label(self.frame1, text="Total val.", font=(20, 20), foreground="gray")
        self.label0 = Label(self.frame1, textvariable=self.variable, font=(
            20, 20), foreground="blue")  # variable yerine remChar gelecek

    def grid(self):

        self.label2.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label3.pack(side=LEFT, fill=BOTH, expand=YES)
        self.label4.pack(side=LEFT, fill=BOTH, expand=YES)

    def update_label(self):
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
        self.root.after(3000, self.update_label)
        self.root.mainloop()


if __name__ == '__main__':
    from tkinter import *
    from tkinter.ttk import *
    GUI().run()
