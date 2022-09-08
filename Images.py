from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Offensive Hacking")

root.geometry("1440x970")
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

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

# image_list[1]
status = Label(root,text="Image 1 of " + str(len(image_list)) + "  ", bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda : forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda : back(image_number - 1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)) + "  ", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # Decrementing status bar
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)) + "  ", bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda : forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)

# button_quit = Button(root, text="Exit Program", font=("calibre", 15, "bold"), command=root.quit)
# # button_quit.place(x=40, y=13, height=20, width=50)
#
# # sd_button = Button(clock, text = "Shutdown", font = ("Time New Roman", 15, "bold"),
# #                   relief = RAISED, cursor = "plus", command=Shutdown)
# # sd_button.place(x=300, y=152, height=34, width=150)
#
# button_quit.pack()
status.grid(row=2, column=0, columnspan=3, sticky=W+E)
root.mainloop()