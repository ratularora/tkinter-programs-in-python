from Tkinter import *

a=Tk()
b1=Button(a,text="Flat",relief=FLAT)
b2=Button(a,text="Raised",relief=RAISED)
b3=Button(a,text="Sunken",relief=SUNKEN)
b4=Button(a,text="Groove",relief=GROOVE)
b5=Button(a,text="Ridge",relief=RIDGE)

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()

a.mainloop()


