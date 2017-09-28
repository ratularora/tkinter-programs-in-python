from Tkinter import *
from tkFileDialog  import askopenfilename      

def callback():
    name= askopenfilename() 
    print name
    

Button(text='File Open', command=callback).pack()
mainloop()
