# import tkinter
# Run _test() to see if tkinter is working properly
# tkinter._test()



from tkinter import *
from tkinter import ttk

# Create the Tk object
# It's common to call it root
root = Tk()
# root.Tk.iconbitmap(self, default="clienticon.ico")
# root.Tk.wm_title(self, "ENTER TITLE HERE")

# root.title("First Gui")
# ttk.Button(root, text="Hello TkInter").grid()

'''
frame = Frame(root)
labelText = StringVar()
label = Label(frame, textvariable = labelText)
button = Button(frame, text="Click Me")
labelText.set("I am a label")
label.pack()
button.pack()
frame.pack()
'''

'''
frame = Frame(root)
Label(frame, text="A Bunch of Buttons").pack()
Button(frame, text="B1").pack(side=LEFT, fill=Y)
Button(frame, text="B2").pack(side=TOP, fill=X)
Button(frame, text="B3").pack(side=RIGHT, fill=X)
Button(frame, text="B4").pack(side=LEFT, fill=X)
frame.pack()
'''

'''
Label(root, text="First Name").grid(row=0, sticky=W, padx =4)
Entry(root).grid(row=0, column=1, sticky=E, pady=4)

Label(root, text="Last Name").grid(row=1, sticky=W, padx =4)
Entry(root).grid(row=1, column=1, sticky=E, pady=4)

Button(root, text="Submit").grid(row=3)
'''

'''
Label(root, text="Description").grid(row=0, column=0, sticky=W)
Entry(root, width=50).grid(row=0, column=1)
Button(root, text="Submit").grid(row=0, column=8)

Label(root, text="Quality").grid(row=1, column=0, sticky=W)
Radiobutton(root, text="New", value=1).grid(row=2, column=0, sticky=W)
Radiobutton(root, text="Good", value=2).grid(row=3, column=0, sticky=W)
Radiobutton(root, text="Poor", value=3).grid(row=4, column=0, sticky=W)
Radiobutton(root, text="Damaged", value=4).grid(row=5, column=0, sticky=W)

Label(root, text="Benefits").grid(row=1, column=1, sticky=W)
Checkbutton(root, text="Free Shipping").grid(row=2, column=1, sticky=W)
Checkbutton(root, text="Bonus Gift").grid(row=3, column=1, sticky=W)
'''

def get_sum(event):
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())
    sum  = num1 + num2
    sumEntry.insert(0, sum)
    sumEntry.delete(0, "end")

num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

Label(root, text="+").pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

equalButton = Button(root, text="=")
equalButton.bind("<Button-1>", get_sum)
equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

# Keep the program running until the user closes it.
root.mainloop()

'''
Notes:
# Pack is a very simple geometry manager. It defines how all the components will be layed out.
# Grid is the most useful geometry manager. It lines up widgets on your screen using rows and columns.
  Each "cell" will only hold one widget, but a widget can cover multiple cells.
# Sticky defines how the widget is going to expand.
'''