from tkinter import *
expr = "" 
def display(num):  
	global expr
	expr = expr + str(num) 
	e1.set(expr) 
def epress(): 
        try:
            global expr
            total = str(eval(expr)) 
            e1.set(total) 
            expr = "" 
        except: 
               e1.set(" error ")
               expr = "" 
def cl(): 
	global expr 
	expr = "" 
	e1.set("") 

if __name__ == "__main__": 
	x= Tk()   
	x.title("Calculator")  
	x.geometry("300x150") 
	x.configure(background="powderblue")
	e1 = StringVar() 
	x.resizable(width=True,height=True)
	efield = Entry(x,textvariable=e1,font=('times',18)) 
	efield.grid(columnspan=4, ipadx=30)
	b1 = Button(x, text=' 1 ', fg='white', bg='black',
                    command=lambda: display(1), height=1, width=7) 
	b1.grid(row=2, column=0) 
	b2 = Button(x, text=' 2 ', fg='white', bg='black', 
					command=lambda: display(2), height=1, width=7) 
	b2.grid(row=2, column=1) 
	b3 = Button(x, text=' 3 ', fg='white', bg='black', 
					command=lambda: display(3), height=1, width=7) 
	b3.grid(row=2, column=2) 

	b4 = Button(x, text=' 4 ', fg='white', bg='black', 
					command=lambda: display(4), height=1, width=7) 
	b4.grid(row=3, column=0) 

	b5 = Button(x, text=' 5 ', fg='white', bg='black', 
					command=lambda: display(5), height=1, width=7) 
	b5.grid(row=3, column=1) 

	b6 = Button(x, text=' 6 ', fg='white', bg='black', 
					command=lambda: display(6), height=1, width=7) 
	b6.grid(row=3, column=2) 

	b7 = Button(x, text=' 7 ', fg='white', bg='black' ,
					command=lambda: display(7), height=1, width=7) 
	b7.grid(row=4, column=0) 

	b8 = Button(x, text=' 8 ', fg='white', bg='black', 
					command=lambda: display(8), height=1, width=7) 
	b8.grid(row=4, column=1) 

	b9 = Button(x, text=' 9 ', fg='white', bg='black',
					command=lambda: display(9), height=1, width=7) 
	b9.grid(row=4, column=2) 

	b0 = Button(x, text=' 0 ', fg='white', bg='black', 
					command=lambda: display(0), height=1, width=7) 
	b0.grid(row=5, column=0) 

	plus = Button(x, text=' + ', fg='white', bg='black', 
				command=lambda: display("+"), height=1, width=7) 
	plus.grid(row=2, column=3) 

	min = Button(x, text=' - ', fg='white', bg='black',
				command=lambda: display("-"), height=1, width=7) 
	min.grid(row=3, column=3) 

	mul = Button(x, text=' * ', fg='white', bg='black', 
					command=lambda: display("*"), height=1, width=7) 
	mul.grid(row=4, column=3) 

	div = Button(x, text=' / ', fg='white', bg='black', 
					command=lambda: display("/"), height=1, width=7) 
	div.grid(row=5, column=3) 

	equ = Button(x, text=' = ', fg='white', bg='black', 
				command=epress, height=1, width=7) 
	equ.grid(row=5, column=2) 

	clear= Button(x, text='Clear', fg='white', bg='red', 
				command=cl, height=1, width=7) 
	clear.grid(row=5, column='1') 
	x.mainloop()
