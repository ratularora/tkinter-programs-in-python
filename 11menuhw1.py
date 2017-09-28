from Tkinter import *
import os

def new():
	os.system("gedit")
def ope():
	os.system("cd /home/ratul/Desktop/")
a1=Tk()

m=Menu(a1)

m1=Menu(m,tearoff=0)
m.add_cascade(label="File",menu=m1)

m2=Menu(m,tearoff=0)
m.add_cascade(label="Edit",menu=m2)

m3=Menu(m,tearoff=0)
m.add_cascade(label="Help",menu=m3)

m1.add_command(label="New",command=new)
m1.add_command(label="Open",command=ope)
m1.add_command(label="Save")
m1.add_command(label="Save As..")
m1.add_command(label="Close")
m1.add_separator()
m1.add_command(label="Exit")

m2.add_command(label="Undo")
m2.add_command(label="Cut")
m2.add_command(label="Copy")
m2.add_command(label="Paste")
m2.add_command(label="Delete")
m2.add_command(label="Select All")

m3.add_command(label="Help Index")
m3.add_command(label="About..")

a1.config(menu=m)
a1.mainloop()
