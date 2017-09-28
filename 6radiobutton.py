from Tkinter import *

a=Tk()
a.configure(bg="blue")
def func():
	s="You have selected Option"+str(v1.get())
	l1.configure(text=s)
v1=IntVar()	
r1=Radiobutton(a,text="Option 1",bg="yellow",variable=v1,value=10,command=func)
r1.grid()
r2=Radiobutton(a,text="Option 2",bg="yellow",variable=v1,value=20,command=func)
r2.grid()
r3=Radiobutton(a,text="Option 3",variable=v1,value=3,command=func)
r3.grid()

l1=Label(a)
l1.grid()
a.mainloop()

