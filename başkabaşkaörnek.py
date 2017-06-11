from tkinter import *

root = Tk()

# fonts for all widgets
root.option_add("*Font", "courier")

# font to use for label widgets
root.option_add("*Label.Font", "helvetica 20 bold")

# make all widgets light blue
root.option_add("*Background", "light blue")

# use gold/black for selections
root.option_add("*selectBackground", "gold")
root.option_add("*selectForeground", "black")

# the root window was already created, so we
# have to update it ourselves
root.config(background="light blue")

#
# display a bunch of widgets

Label(root, text="a label").pack()

Button(root, text="a button").pack()

Message(root, text="a message").pack()

w = Listbox(root)
for i in range(10):
    w.insert(i, "item %d" % (i+1))
w.pack()

w = Text(root, width=20, height=10)
w.insert(1.0, "a text widget")
w.pack()

root.mainloop()