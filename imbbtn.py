import Tkinter
from PIL import ImageTk

root = tk.Tk()
def make_button():
    b = tk.Button(root)
    image = ImageTk.PhotoImage(file="1.png")
    b.config(image=image)
    b.image = image
    b.pack()
make_button()

root.mainloop()
