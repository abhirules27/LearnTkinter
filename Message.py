from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Message Box')
root.iconbitmap("Messages.ico")
root.geometry("740x570")
root.config(bg = "#9fde99")              # Configure Background colour

# Exit Button
button_exit = Button(root, text="Exit Program", command=root.quit)
button_exit.pack()

# Types of Boxes: showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    # messagebox.showinfo("This is my PopUp", "Hello World")
    # messagebox.showwarning("This is my PopUp", "Hello World")
    # messagebox.showerror("This is my PopUp", "Hello World")
    # messagebox.askquestion("This is my PopUp", "Hello World")
    # messagebox.askokcancel("This is my PopUp", "Hello World")
    # messagebox.askyesno("This is my PopUp", "Hello World")
    response = messagebox.askquestion("This is my PopUp", "Hello World")
    Label(root, text=response).pack()

    if response == "yes":
        Label(root, text="You Clicked Yes!").pack()
    else:
        Label(root, text="You Clicked No!").pack()

Button(root, text= "Popup", command=popup).pack()
root.mainloop()