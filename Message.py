from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Message Box')
root.iconbitmap("Messages.ico")
root.geometry("1440x970")
root.config(bg = "#9fde99")              # Configure Background colour
# my_label.grid(row=0, column=0, columnspan=3)

# e = Entry(root, width=27, borderwidth=2, bg="White")
# root.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_exit = Button(root, text="Exit Program", command=root.quit)
button_exit.grid(row=1, column=3, columnspan=5)
button_exit.pack()

button_exit1 = Button(root, text="Exit Program", command=root.quit)
# button_exit1.grid(row=2, column=3)
button_exit1.pack()



root.mainloop()