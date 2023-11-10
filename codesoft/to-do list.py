#creating a simple to-do list #
from  tkinter import * 
from tkinter import messagebox
def newtask():
    task=my_entry.get()
    if task !="":
        lb.insert(END,task)
        my_entry.delete(0,"end")
    else:
        messagebox.showwarning("warning","NO task is assigned.")

def deletetask():
    lb.delete(ANCHOR)


x=Tk()
x.geometry('600x500+300+400')
x.title("simple to-do list")
x.config(bg='#223aa1')
x.resizable(width=True, height=True)

frame=Frame(x)
frame.pack(pady=15)

lb=Listbox(
frame,
width=25,
height=10,bd=0,fg='#aa464a',
font=('Heather',16),
selectbackground='#a345c5',
activestyle='none'
)
lb.pack(side=LEFT,fill=BOTH)

task_list=['go to gym','read books','drink water','do the homework',
           'pratice coding','learn a hobby']
for i in task_list:
    lb.insert(END,i)

sb=Scrollbar(frame)
sb.pack(side=RIGHT,fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry=Entry(
    x,font=('ariel',18)
    )
my_entry.pack(pady=20)
button_frame=Frame(x)
button_frame.pack(pady=20)

addtask_btn=Button(
    button_frame, 
    text='New Task',font=('times',14),bg='#c5f775',
    padx=20,pady=10,command=newtask)

addtask_btn.pack(fill=BOTH,expand=True, side=LEFT)
deltask_btn=Button(
    button_frame,
    text='Delete task',
    bg='#ff8b61',
    padx=20,
    pady=10,command=deletetask
    )
deltask_btn.pack(fill=BOTH,expand=True, side=LEFT)
x.mainloop()


           
      
