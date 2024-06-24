from tkinter import *
from tkinter import messagebox

# Functions and Exceptional Handlings
def Addition():
    try:
        num1 = obj1.get()
        num2 = obj2.get()
        ttl = num1+num2
        l5.config(text=ttl)
    except ValueError:
        messagebox.showerror("Error Occured", "Only digits are allowed.")
    except TclError:
        messagebox.showerror("Error Occured", "Only digits are allowed.")
def Substraction():
    try:
        num1 = obj1.get()
        num2 = obj2.get()
        ttl = num1-num2
        l5.config(text=ttl)
    except ValueError:
        messagebox.showerror("Error Occured", "Only digits are allowed.")
    except TclError:
        messagebox.showerror("Error Occured", "Only digits are allowed.")
def Multiplication():
    try:
        num1 = obj1.get()
        num2 = obj2.get()
        ttl = num1*num2
        l5.config(text=ttl)
    except ValueError:
        messagebox.showerror("Error Occured", "Only digits are allowed.")
    except TclError:
        messagebox.showerror("Error Occured", "Only digits are allowed.")
def Division():
    try:
        num1 = obj1.get()
        num2 = obj2.get()
        ttl = num1/num2
        l5.config(text=ttl)
    except ValueError:
        messagebox.showerror("Error Occured", "Only digits are allowed.")
    except TclError:
        messagebox.showerror("Error Occured", "Only digits are allowed.")
    except ZeroDivisionError:
        messagebox.showerror("Error Occured","Can not divide by zero.")
def Clear():
    e1.delete(0,END)
    e2.delete(0,END)
    l5.config(text="")
    e1.focus()
def Quit():
    ans = messagebox.askyesno("Closing","Do you want to quit ???")
    if ans==True:
        root.destroy()

# Creating and Positioning Root Window
root = Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry("250x300")
root.title("CALCULATOR")

obj1 = IntVar()
obj2 = IntVar()

# Creating and seting properties of Widgets 
l1 = Label(root, text="Calculation Program", font="Arial 14 bold",relief="sunken",borderwidth=3,bg="Cyan")
l2 = Label(root, text="First No:")
e1 = Entry(root,textvariable=obj1)
e1.delete(0,END)
l3 = Label(root, text="Second No:")
e2 = Entry(root,textvariable=obj2)
e2.delete(0,END)
b1 = Button(root,text="Add",command=Addition)
b2 = Button(root,text="Minus",command=Substraction)
b3 = Button(root,text="Multiply",command=Multiplication)
b4 = Button(root,text="Divide",command=Division)
b5 = Button(root,text="Clear",command=Clear)
b6 = Button(root,text="Quit",command=Quit)
l4 = Label(text="Result",fg="White",bg="Green",width=10)
l5 = Label()

# Griding the widgets on root window 
l1.grid(row=0,column=0,columnspan=3)
l2.grid(row=1,column=0,sticky=E)
e1.grid(row=1,column=1,columnspan=2)
l3.grid(row=2,column=0)
e2.grid(row=2,column=1,columnspan=2)
b1.grid(row=3,column=0,sticky=E+W,)
b2.grid(row=3,column=1,sticky=E+W)
b3.grid(row=3,column=2,sticky=E+W)
b4.grid(row=4,column=0,sticky=E+W)
b5.grid(row=4,column=1,sticky=E+W)
b6.grid(row=4,column=2,sticky=E+W)
l4.grid(row=5,column=0)
l5.grid(row=5,column=1,columnspan=2)

root.mainloop()