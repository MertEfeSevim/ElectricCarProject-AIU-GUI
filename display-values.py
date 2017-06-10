def display():

   ser = serial.Serial('/dev/cu.usbmodem1411',9600)

   def update():
       while 1:
           reading.set(ser.readline())
           root.update()

   root = Tk()
   reading = StringVar()

   w = Label(root,textvariable = reading)
   w.pack()

   root.after(1,update)
   root.mainloop()