# @Author: Vegard S. <BioVegas>
# @Date:   17-Nov-2016
# @Email:  vegard.stuerzinger@gmail.com
# @Project: BiSci
# @Filename: SIZExWEIGHT.py
# @Last modified by:   BioVegas
# @Last modified time: 17-Nov-2016
# @Copyright: Open Source


import numpy as np
from Tkinter import *
#saving entry fields
filename="SIZExWEIGHT.txt"
file=open(filename, "w")
file.close()
def show_entry_fields():
    print ("size: %s\nweight: %s" % (c1.get(),c2.get()))

def save_entry_fields():
    file=open(filename,"a")
    file.write(c1.get())
    file.write(",")
    file.write(c2.get())
    file.write("\n")
    file.close()

#Entry fields and buttons
top = Tk()
top.title("Size vs Weight")
t1=Label(top,text="Size")
t1.pack(side=LEFT)
c1=Entry(top, bd=5)
c1.pack(side=RIGHT)
t2=Label(top, text="Weight")
t2.pack(side=LEFT)
c2=Entry(top, bd=5)
c2.pack(side=RIGHT)
b1= Button(top, text="show", command=show_entry_fields)
b2= Button(top, text="save data", command=save_entry_fields)

#Formatting
t1.grid(row=0, column=0)
c1.grid(row=0, column=1)
t2.grid(row=1, column=0)
c2.grid(row=1, column=1)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
top.mainloop()
