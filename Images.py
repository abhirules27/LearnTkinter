from tkinter import *

root = Tk()
root.title("Offensive Hacking")

root.geometry("470x206")
root.config(bg = "#9fde99")              # Configure Background colour
# root.config(bg = "#C0C0C0")              # Configure Background colour
# root.config(bg = "#000080")              # Configure Background colour
root.iconbitmap("C:/Users/abhir/Downloads/hacker_117746.ico")











button_quit = Button(root, text="Exit Program", font=("calibre", 15, "bold"), command=root.quit)
# button_quit.place(x=40, y=13, height=20, width=50)

# sd_button = Button(clock, text = "Shutdown", font = ("Time New Roman", 15, "bold"),
#                   relief = RAISED, cursor = "plus", command=Shutdown)
# sd_button.place(x=300, y=152, height=34, width=150)

button_quit.pack()
root.mainloop()