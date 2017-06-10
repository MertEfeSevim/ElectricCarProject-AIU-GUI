from tkinter import *
root = Tk()
variable = StringVar()

def gather_data():
    #will gets string
    i = 0
    while 1:
        i += 1
        variable.set(str(i))
        root.update()




b0 = Label(root, text="Minimum Temperature /")
b1 = Label(root, text="Maximum Temperature /")
b2 = Label(root, text="Average Temperature /")
b3 = Label(root, text="Minimum Voltage /")
b4 = Label(root, text="Maximum Voltage /")
b5 = Label(root, text="Average Voltage /")
b6 = Label(root, text="Current /")
b7 = Label(root, text="Velocity")
b8 = Label(root, text=variable)
startButton = Button(root,text="Start",command=gather_data)

b0.pack(side=LEFT)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
b4.pack(side=LEFT)
b5.pack(side=LEFT)
b6.pack(side=LEFT)
b7.pack(side=LEFT)
b8.pack(side=BOTTOM)
startButton.pack(side=BOTTOM)


root.mainloop()

