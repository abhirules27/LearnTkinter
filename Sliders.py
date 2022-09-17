from tkinter import *
from PIL import ImageTk, Image

root = Tk()

# 1. Box Geometry
root.title("Slider Box)")
root.iconbitmap("Messages.ico")
root.geometry("800x600")
root.config(bg = "#9fde99")              # Configure Background colour
# root.config(bg = "#C0C0C0")              # Configure Background colour
# root.config(bg = "#000080")              # Configure Background colour
root.iconbitmap("hacker_117746.ico")

# 2. Exit Button
button_exit = Button(root, text="Exit Program", command=root.quit)
button_exit.pack()

# 3. Vertical Slider
vertical = Scale(root, from_=0, to=400)
vertical.pack()

def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

# 4. Horizontal Slider
horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()

my_btn = Button(root, text="Click Me!!", command=slide).pack()
root.mainloop()