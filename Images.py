from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Offensive Hacking")

root.geometry("3200x956")
root.config(bg = "#9fde99")              # Configure Background colour
# root.config(bg = "#C0C0C0")              # Configure Background colour
# root.config(bg = "#000080")              # Configure Background colour
root.iconbitmap("hacker_117746.ico")
# pip install Pillow
# pip freeze

my_img1 = ImageTk.PhotoImage(Image.open("1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("5.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("5.jpg"))
my_label = Label(image=my_img)
my_label.pack()









button_quit = Button(root, text="Exit Program", font=("calibre", 15, "bold"), command=root.quit)
# button_quit.place(x=40, y=13, height=20, width=50)

# sd_button = Button(clock, text = "Shutdown", font = ("Time New Roman", 15, "bold"),
#                   relief = RAISED, cursor = "plus", command=Shutdown)
# sd_button.place(x=300, y=152, height=34, width=150)

button_quit.pack()
root.mainloop()