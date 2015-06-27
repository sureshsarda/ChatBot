from Tkinter import *
import messageobject

def getText():
    print E1.get()

root = Tk()

label1 = Label( root, text="Enter the text")
text = Entry(root, bd =5)

submit = Button(root, text ="Submit", command = getText)

label1.pack()
text.pack()

submit.pack(side =BOTTOM) 
root.mainloop()