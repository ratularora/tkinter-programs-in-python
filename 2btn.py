from  Tkinter import * 
import tkMessageBox

top = Tk()

v = StringVar()
s=""
def helloCallBack():
   	tkMessageBox.showinfo( "Hello Python", "Hello World")
   	s=v.get()
	w=Label(top,text=s,bg="red",fg="black")
	w.pack()


c=Label(top,text="Button function",bg="red",fg="black")
x= Entry(top,text="enter user name",textvariable=v)
#photo=PhotoImage(file="/home/ratul/par.png")
B = Button(top, text ="Hello", command = helloCallBack)


#print s

#photo=PhotoImage()




c.place()
x.place()
B.pack()
#w.pack()
top.mainloop()


