from Tkinter import *

a=Tk()
a.title("Smart")

r= StringVar()
def ex():
	b=Tk()
	a.destroy()
	r=e1.get()
		
a.configure(bg="yellow")

l1=Label(a,text="User name",bg="yellow")
l1.grid(row=0,column=1)

e1=Entry(a,bg="blue",fg="white",bd=2,w=20,textvariable=r)
e1.grid(row=0,column=2)

l2=Label(a,text="password",bg="yellow")
l2.grid(row=1,column=1)

e2=Entry(a,bg="blue",bd=2,w=20,fg="white" ,show="*")
e2.grid(row=1,column=2)

s=Button(a,text="submit",command=ex)
s.grid(row=2,column=2)
a.mainloop()
