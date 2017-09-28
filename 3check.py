from Tkinter import *

import Tkinter

a= Tkinter.Tk()

v1 = StringVar()
v2 = IntVar()

def pi():
	str="value"+v1.get()
	l.configure(text=str)
c1=Checkbutton(a, text="Music", variable=v1 ,height=5,width=50 )
c2=Checkbutton(a, text="Video", variable=v2 ,height=5,width=50)

print v1
c1.pack()

c2.pack()
l=Label(a)
l.pack()
a.mainloop()
