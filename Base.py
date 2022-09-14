from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning Base")
root.iconbitmap("Messages.ico")
root.geometry("740x570")
root.config(bg = "#0fde99")              # Configure Background colour

# Exit Button
button_exit = Button(root, text="Exit Program", command=root.quit)
button_exit.pack()

def open():
    global my_Image
    top = Toplevel()
    top.title("Image One in Display")
    my_Image = ImageTk.PhotoImage(Image.open("1.jpg"))
    lbl1 = Label(top, image=my_Image).pack()
    lbl2 = Label(top, text="Hello Abhishek").pack()
    btn2 = Button(top, text="Close Window", command=top.destroy).pack()

btn = Button(root, text="Open Image", command=open).pack()

root.mainloop()