from Tkinter import *
import os
def firefox():
	os.system("firefox google.com &")

def reboot():
	os.system("sudo reboot")

def shutdown():
	os.system("sudo poweroff")

a1=Tk()
m=Menu(a1 ,bg="black",fg="white")

m1=Menu(m,tearoff=0,bg="yellow" ,fg="red")
m.add_cascade(label="Menu1",menu=m1)

m2=Menu(m,tearoff=0,bg="blue")
m.add_cascade(label="Menu2",menu=m2)

m3=Menu(m,tearoff=0)
m.add_cascade(label="Menu3",menu=m3)

m1.add_command(label="Firefox",command=firefox)
m1.add_command(label="Reboot",command=reboot)
m2.add_command(label="Shutdown",command=shutdown)

a1.config(menu=m)
a1.mainloop()
