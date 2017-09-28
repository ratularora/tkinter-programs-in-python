from Tkinter import *

a = Tk()

text1 = Text(a, height=40, width=80)
photo=PhotoImage(file='./par.png')
text1.insert(END,'\n')
text1.image_create(END,image=photo)
text1.pack(side=LEFT)

text2 = Text(a, height=40, width=100)
scroll = Scrollbar(a, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)

text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color', foreground='blue', font=('Tempus Sans ITC', 13, 'bold'))

text2.insert(END,'\nmy details\n', 'big')
quote = """
ratul arora
 software developer
for more info www.geeklanguages.blogspot.com
Location : Jalandhar
"""
text2.insert(END, quote, 'color')
text2.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)
a.mainloop()
