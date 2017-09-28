import Tkinter
import os

a=Tkinter.Tk()
a.title("test")
a.geometry("150x100")
a.configure(bg="yellow")
v1=Tkinter.IntVar()

c=0
def func():
	global c
	c=c+1
	if(c%2!=0):
		os.system("firefox &")
	else:
		os.system("pkill firefox")
		

c1=Tkinter.Checkbutton(a,text="firefox",bg="yellow",command=func)

c1.pack()
a.mainloop()
