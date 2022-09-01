from tkinter import *

root = Tk()                             # Making Root Class

# Creating label widget
myLabel1 = Label(root, text="Abhishek")
myLabel2 = Label(root, text="Mishra")

# Display it on screen
# myLabel.pack()                        # Normal Display
# myLabel1.grid(row=3, column=4)          # Using Grid to Display
# myLabel2.grid(row=2, column=4)

def myClick():
    myLabel = Label(root, text="Clicked")
    myLabel.pack()

# Creating a Button
# myButton = Button(root, text="Click Me", padx = 10, pady = 10)
myButton = Button(root, text="Click Me", padx = 10, pady = 10, command=myClick, fg="Blue", bg="#5f3f1f")
myButton.pack()
root.mainloop()                         # To loop eternally
