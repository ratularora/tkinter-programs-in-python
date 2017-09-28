from Tkinter import *

def show_values():
    print (w1.get(), w2.get())

a = Tk()
w1 = Scale(a, from_=0, to=42)
w1.set(19)
w1.pack()
w2 = Scale(a, from_=0, to=200, orient=HORIZONTAL)#horizontal must be in capital
w2.set(23)
w2.pack()
Button(a, text='Show', command=show_values).pack()

mainloop()
