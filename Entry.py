from tkinter import *

root =Tk()

e = Entry(root, width=50, bg="#fd1223", fg = "white", borderwidth=2)
e.pack()
e.insert(0,"Enter your Name: ")                 # Put default text inside the text box
def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text = hello, fg = "Green", bg = "Yellow")
    myLabel.pack()

myButton = Button(root, text="Enter your Name: ", fg = "Pink", bg = "#234554", command=myClick)
myButton.pack()

root.mainloop()