# -*- coding: utf-8 -*-
import math
from tkinter import (Button, Tk, END, Entry, W, E)

root = Tk()
root.title('Scientific Calculator')
a = list()
i = 0

def mem_recall():
    global a,i
    if len(a)==0:
        clear_all()
        display.insert(0, "Error")
    else:
        display.insert(i,str(a[-1]))
        i += len(str(a[-1]))
        del a[-1]

def mem_store():
    global a
    a.append(display.get())    

def factorial():
    """Calculates the factorial of the number entered."""
    whole_string = display.get()
    number = int(whole_string)
    fact = 1
    counter = number 
    try:
        while counter > 0:
            fact = fact*counter
            counter -= 1
        clear_all()
        display.insert(0, fact)
    except Exception:
        clear_all()
        display.insert(0, "Error, press Clear All")


def clear_all():
    """clears all the content in the Entry widget"""
    display.delete(0, END)
    global i
    i = 0

def get_variables(num):
    """Gets the user input for operands and puts it inside the entry widget"""
    global i
    display.insert(i, num)
    i += 1

def get_operation(operator):
    """Gets the operand the user wants to apply on the functions"""
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length
def undo():
    """removes the last entered operator/variable from entry widget"""
    whole_string = display.get()
    if len(whole_string):        ## repeats until
        ## now just decrement the string by one index
        new_string = whole_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all() 
        display.insert(0, "Error, press Clear All")

def calculate():
    o=display.get()
    if "mod(" in o:
        l=o[4:len (o)-1]
        if l[0]=="-":
            x=math.fabs(float(l[1:]))
        else:
            x=math.fabs(float(l))
        clear_all()
        display.insert(0,x)
        
    elif "+" in o:
        l=o.split("+")
        x = 0
        for i in range(len(l)):
            x += float(l[i])
        clear_all()
        display.insert(0, x) 
        
    elif "-" in o:
        l=o.split("-")
        x = float(l[0])
        for i in range(1,len(l)):
            x -= float(l[i])
        clear_all()
        display.insert(0, x)

    elif "*" in o:
        l=o.split("*")
        x = 1
        for i in range(len(l)):
            x *= float(l[i])
        clear_all()
        display.insert(0, x)

    elif "/" in o:
        l=o.split("/")
        clear_all()
        display.insert(0, float (l[0]) / float (l[1]))

    elif "%" in o:
        l=o.split("%")
        clear_all()
        display.insert(0, (float (l[0]) / float (l[1]))*100)
        
    elif "sin(" in o:
        l = float(o[4:len(o)-1])
        x = math.sin(l)
        clear_all()
        display.insert(0, x)

    elif "log(" in o:
        l=float(o[4:len (o)-1])
        x=math.log(l,10)
        clear_all()
        display.insert(0,x)

    elif "ln(" in o:
        l=float(o[3:len (o)-1])
        x=math.log(l)
        clear_all()
        display.insert(0,x)

    elif "cos(" in o:
        l=float(o[4:len (o)-1])
        x=math.cos(l)
        clear_all()
        display.insert(0,x)

    elif "^2" in o:
        l=o.split("^")
        x=math.pow(float (l[0]),2)
        clear_all()
        display.insert(0,x)
        
    elif "^" in o:
        l=o.split("^")
        x=math.pow(float (l[0]), float (l[1]))
        clear_all()
        display.insert(0,x)
        
    elif "rad(" in o:
        l=float(o[4:len (o)-1])
        x=math.radians(l)
        clear_all()
        display.insert(0,x)

    elif "deg(" in o:
        l=float(o[4:len (o)-1])
        x=math.degrees(l)
        clear_all()
        display.insert(0,x)

        
root.columnconfigure(0,pad=3)
root.columnconfigure(1,pad=3)
root.columnconfigure(2,pad=3)
root.columnconfigure(3,pad=3)
root.columnconfigure(4,pad=3)
root.columnconfigure(7,pad=3)
root.columnconfigure(8,pad=3)
root.columnconfigure(5,pad=3)
root.columnconfigure(6,pad=3)

root.rowconfigure(0,pad=3)
root.rowconfigure(1,pad=3)
root.rowconfigure(2,pad=3)
root.rowconfigure(3,pad=3)
root.rowconfigure(4,pad=3)

display = Entry(root, font = ("Calibri", 13))
display.grid(row = 1, columnspan = 9    , sticky = W+E, padx=5, pady=5)

one = Button(root, text = " 1 ", command = lambda : get_variables(1), font=("Calibri", 12))
one.grid(row = 2, column = 1)
two = Button(root, text = " 2 ", command = lambda : get_variables(2), font=("Calibri", 12))
two.grid(row = 2, column = 2)
three = Button(root, text = " 3 ", command = lambda : get_variables(3), font=("Calibri", 12))
three.grid(row = 2, column = 3)

four = Button(root, text = " 4 ", command = lambda : get_variables(4), font=("Calibri", 12))
four.grid(row = 3 , column = 1)
five = Button(root, text = " 5 ", command = lambda : get_variables(5), font=("Calibri", 12))
five.grid(row = 3, column = 2)
six = Button(root, text = " 6 ", command = lambda : get_variables(6), font=("Calibri", 12))
six.grid(row = 3, column = 3)

seven = Button(root, text = " 7 ", command = lambda : get_variables(7), font=("Calibri", 12))
seven.grid(row = 4, column = 1)
eight = Button(root, text = " 8 ", command = lambda : get_variables(8), font=("Calibri", 12))
eight.grid(row = 4, column = 2)
nine = Button(root , text = " 9 ", command = lambda : get_variables(9), font=("Calibri", 12))
nine.grid(row = 4, column = 3)

cls = Button(root, text = " Clear all ", command = clear_all, font=("Calibri", 12), foreground = "red")
cls.grid(row = 5, column = 0, columnspan = 2)
zero = Button(root, text = " 0 ", command = lambda : get_variables(0), font=("Calibri", 12))
zero.grid(row = 5, column = 2)
dot = Button(root, text = " . ", command = lambda : get_variables("."), font=("Calibri", 12))
dot.grid(row = 5, column = 3)
result = Button(root, text = "  Result  ", command = calculate, font=("Calibri", 12), foreground = "red")
result.grid(row = 5, column = 4,columnspan = 2)

plus = Button(root, text = " + ", command =  lambda : get_operation("+"), font=("Calibri", 12))
plus.grid(row = 2, column = 4) 
minus = Button(root, text = "  - ", command =  lambda : get_operation("-"), font=("Calibri", 12))
minus.grid(row = 3, column = 4)
multiply = Button(root,text = " * ", command =  lambda : get_operation("*"), font=("Calibri", 12))
multiply.grid(row = 4, column = 4)
divide = Button(root, text = " / ", command = lambda :  get_operation("/"), font=("Calibri", 12))
divide.grid(row = 2, column = 5)

# adding new operations
pi = Button(root, text = " π ", command = lambda: get_operation(str(math.pi)), font =("Calibri", 12))
pi.grid(row = 2, column = 6)
modulo = Button(root, text = "% ", command = lambda :  get_operation("%"), font=("Calibri", 12))
modulo.grid(row = 3, column = 5)
left_bracket = Button(root, text = " ( ", command = lambda: get_operation("("), font =("Calibri", 12))
left_bracket.grid(row = 4, column = 5)
right_bracket = Button(root, text = " ) ", command = lambda: get_operation(")"), font =("Calibri", 12))
right_bracket.grid(row = 4, column = 6)
ms = Button(root,text = "Ms", command = mem_store, font = ("Calibri", 12))
ms.grid(row = 3, column = 0)
mr = Button(root,text = "Mr", command = mem_recall, font = ("Calibri", 12))
mr.grid(row = 4, column = 0)

# sin, cos, log, ln, mod
sin =Button(root, text="sin", command = lambda : get_operation("sin("), font=("Calibri", 12))
sin.grid(row=2, column=7)
cos =Button(root, text="cos", command = lambda : get_operation("cos("), font=("Calibri", 12))
cos.grid(row=3, column=7)
ln =Button(root, text="ln ", command = lambda : get_operation("ln("), font=("Calibri", 12))
ln.grid(row=3, column=8)
log =Button(root, text="log", command = lambda : get_operation("log("), font=("Calibri", 12))
log.grid(row=4, column=8)
undo_button = Button(root, text = "Del", command = undo, font =("Calibri", 12), foreground = "red")
undo_button.grid(row = 2, column = 0)
fact = Button(root, text = " x!", command = factorial, font=("Calibri", 12))
fact.grid(row = 4, column = 7)
exp = Button(root, text = "exp", command = lambda: get_operation("^"), font = ("Calibri", 12))
exp.grid(row = 2, column = 8)
square = Button(root, text = "^2", command = lambda: get_operation("^2"), font = ("Calibri", 12))
square.grid(row = 3, column = 6,padx=1)
mod = Button(root,text = "|x|", command = lambda: get_operation("mod("), font = ("Calibri", 12))
mod.grid(row = 5, column = 6)
rad = Button(root,text = "Rad", command = lambda: get_operation("rad("), font = ("Calibri", 12))
rad.grid(row = 5, column = 7)
deg = Button(root,text = "Deg", command = lambda: get_operation("deg("), font = ("Calibri", 12))
deg.grid(row = 5, column = 8)

root.mainloop()
