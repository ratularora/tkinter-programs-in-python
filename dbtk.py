from Tkinter import *
import MySQLdb
#import tkmessagebox as tm
from tkMessageBox import *

def put(*args):
	e_code = i_code.get()
    	e_name = i_name.get()
    	e_price = i_price.get()
 	db = MySQLdb.connect("localhost","root","root","test" )
    	cur = db.cursor()
    	cur.execute("insert into book(book_code, book_name, book_price) values ('"+str(e_code)+"', '"+e_name+"', '"+str(e_price)+"')")
	db.commit()    	
	db.close()



root = Tk()
root.title("GET DATA")

mainframe = Frame(root)
mainframe.pack()

i_code = IntVar()
i_name = StringVar()
i_price = IntVar()


codeEntry = Entry(mainframe, width=7, textvariable=i_code)
nameEntry = Entry(mainframe, width=7, textvariable=i_name)
priceEntry = Entry(mainframe, width=7, textvariable=i_price)

codeEntry.grid(row=0, column=1)
nameEntry.grid(row=1, column=1)
priceEntry.grid(row=2, column=1)

Label(mainframe, text='Book Code').grid(row=0, column=0)
Label(mainframe, text='Book Name').grid(row=1, column=0)
Label(mainframe, text='Book Price').grid(row=2, column=0)

Button(mainframe, text="Insert", command=put).grid(row=3, column=1)

root.mainloop()
