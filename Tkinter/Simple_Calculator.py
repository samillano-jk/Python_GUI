from tkinter import *

root = Tk()
root.title("Simple Calculator")

myEntry = Entry(root, width=35, borderwidth=5)
myEntry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Functions

def button_num(number):
    current = myEntry.get()
    myEntry.delete(0, END)
    myEntry.insert(0, str(current) + str(number))
    
# Operations   
def button_op(op):
    global operation, f_num
    operation = str(op)
    first_num = myEntry.get()
    f_num = float(first_num)
    myEntry.delete(0, END)
    
    

def button_equal():
    try: 
        second_num = float(myEntry.get())
        myEntry.delete(0, END)

        print(f"Operation: {operation}, Num1: {f_num}, num2: {second_num}")

        if operation == "+":
            myEntry.insert(0, f_num+second_num)
        if operation == "-":
            myEntry.insert(0, f_num-second_num)
        if operation == "x":
            myEntry.insert(0, f_num*second_num)
        if operation == "/":
            if second_num != 0:
                myEntry.insert(0, f_num/second_num)
            else: 
                myEntry.insert(0, "Zero Division Error")

        

    except ValueError as v:
        myEntry.insert(0, v)

    

def button_clear():
    myEntry.delete(0, END)



# Buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_num(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_num(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_num(3))

button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_num(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_num(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_num(6))

button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_num(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_num(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_num(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_num(0))

button_add = Button(root, text="+", padx=39, pady=20, command=lambda: button_op("+"))
button_subtract = Button(root, text="-", padx=39, pady=20, command=lambda: button_op("-"))
button_multiply = Button(root, text="x", padx=39, pady=20, command=lambda: button_op("x"))
button_divide = Button(root, text="/", padx=39, pady=20, command=lambda: button_op("/"))

button_equal = Button(root, text="=", padx=39, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=30, pady=20, command=button_clear)




# Button Placement
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=1)

button_add.grid(row=4, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=1, column=3)

button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=0)



root.mainloop()

