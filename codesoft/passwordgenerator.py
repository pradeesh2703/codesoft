# to craete a strong password
import random
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
def low():
        my_entry.delete(0, END)
        length = var1.get()
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
        password = ""
        if var.get() == 1:
                for i in range(0, length):
                        password = password + random.choice(lower)
                return password

	
        elif var.get() == 2:
                for i in range(0, length):
                        password = password + random.choice(upper)
                return password

        elif var.get() == 3:
                for i in range(0, length):
                        password = password + random.choice(digits)
                return password
        else:
              messagebox.showwarning("warning", "Please select the choice.")  



def generate():
	password1 = low()
	my_entry.insert(10, password1)


x = Tk()
var = IntVar()
var1 = IntVar()

x.geometry('500x450+500+200')
x.title("Password generator")
x.resizable(width=True, height=True)

Random_password = Label(x, text="Password")
Random_password.grid(row=0)
my_entry = Entry(x)
my_entry.grid(row=0, column=1)
x.configure(background="powderblue")


c_label = Label(x, text="Length")
c_label.grid(row=1)


generate_button = Button(x, text="Generate",command=generate)
generate_button.grid(row=0, column=3)

radio_low = Radiobutton(x, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')
radio_middle = Radiobutton(x, text="Medium", variable=var, value=2)
radio_middle.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(x, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')
c = Combobox(x, textvariable=var1)


c['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,17, 18, 19, 20, 21, 22, 23, 24, 25,"Length")
c.current(0)
c.bind('<<ComboboxSelected>>')
c.grid(column=1, row=1)

x.mainloop()
