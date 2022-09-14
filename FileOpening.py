from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("File Handling")
root.iconbitmap("Messages.ico")

root.filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))  # "/" Means C Drive
root.mainloop()