from tkinter import *
root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=27, borderwidth=2, bg="White")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)                  # Delete whatever was in the Box
    e.insert(0, str(current) + str(number))                 # Inserting the Input
def button_clear():
    e.delete(0, END)
def button_Add():
    first_number = e.get()
    global f_num
    global math
    math = "Add"
    f_num = int(first_number)
    e.delete(0, END)
def button_Sub():
    first_number = e.get()
    global f_num
    global math
    math = "Sub"
    f_num = int(first_number)
    e.delete(0, END)
def button_Div():
    first_number = e.get()
    global f_num
    global math
    math = "Div"
    f_num = int(first_number)
    e.delete(0, END)
def button_Mul():
    first_number = e.get()
    global f_num
    global math
    math = "Mul"
    f_num = int(first_number)
    e.delete(0, END)

def button_Eq():
    second_number = e.get()
    e.delete(0, END)
    if math == "Add":
        e.insert(0, f_num + int(second_number))

    if math == "Sub":
        e.insert(0, f_num - int(second_number))

    if math == "Div":
        try:
            e.insert(0, f_num / int(second_number))
        except ZeroDivisionError:
            err = 0
            e.insert(0, err)


    if math == "Mul":
        e.insert(0, f_num * int(second_number))
# Define Buttons
button_1 = Button(root, text="1", font=10, padx=20, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", font=10, padx=20, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", font=10, padx=20, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", font=10, padx=20, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", font=10, padx=20, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", font=10, padx=20, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", font=10, padx=20, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", font=10, padx=20, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", font=10, padx=20, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", font=10, padx=20, pady=20, command=lambda: button_click(0))

button_Add = Button(root, text="+", font=10, bg="LightGreen", padx=20, pady=20, command=button_Add)
button_Sub = Button(root, text="-", font=10, bg="LightGreen", padx=22, pady=20, command=button_Sub)
button_Div = Button(root, text="/", font=10, bg="LightGreen", padx=22, pady=20, command=button_Div)
button_Mul = Button(root, text="x", font=10, bg="LightGreen", padx=21, pady=20, command=button_Mul)
button_Eq = Button(root, text="=", font=10, bg="LightBlue", padx=20, pady=20, command=button_Eq)
button_Clr = Button(root, text="C",font=10, bg="LightYellow", padx=18, pady=20, command=button_clear)

# Placing the Buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_Add.grid(row=1, column=4)
button_Sub.grid(row=2, column=4)
button_Div.grid(row=3, column=4)
button_Mul.grid(row=4, column=4)
button_Eq.grid(row=4, column=2)
button_Clr.grid(row=4, column=1)

root.mainloop()

