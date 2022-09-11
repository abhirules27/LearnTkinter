# Learn Frame and Radio Buttons

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
# root.geometry("100x200")
# root.config(bg = "#000080")              # Configure Background colour
root.title("Hacker's Home")
root.iconbitmap("hacker_117746.ico")
# frame = LabelFrame(root, text="This is my frame", padx=50, pady=50)         # Padding inside frame i.e. Frame border & button
frame = LabelFrame(root, padx=50, pady=50)         # Padding inside frame i.e. Frame border & button
frame.pack(padx=30, pady=30)                                                # Padding outside frame i.e. Frame border & widget border

# b1 = Button(frame, text = "Don't Click Here!")
# b1.grid(row=0, column=0)
#
# b2 = Button(frame, text = "Don't Click Here!")
# b2.grid(row=1, column=1)

r = IntVar()                                                           # Defining a Tkinter Variable. Integer Variable in this case
# r = StrVar()                                                         # Defining a Tkinter Variable. String Variable in this case
# r.set("2")
# r.get()

TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


# Radiobutton(root, text="Option 1", variable=r, value=1, command= lambda : clicked(r.get())).pack()         # When someone clicks on this, value of variable will be 1 (can be anything)
# # Radiobutton(root, text="Option 1", variable=r, value="1").pack()     # Incase r is StrVar
# Radiobutton(root, text="Option 2", variable=r, value=2, command= lambda : clicked(r.get())).pack()         # When someone clicks on this, value of variable will be 2 (can be anything)

# myLabel = Label(root, text=pizza.get())
# myLabel.pack()

myButton = Button(root, text="Click Me!", command=lambda :clicked(pizza.get()))
myButton.pack()
root.mainloop()