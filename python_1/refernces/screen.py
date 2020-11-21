import tkinter as tk
import tkinter.messagebox as messagebox
import time
from easygui import *

def en_show():
    global screen
    msg = "Select Show Time:"
    choices = ["09:00 am","02:00 pm","06:00 pm","10:30 pm"]
    n = buttonbox(msg,choices=choices)
    return n

def save():
    global screen,c
    m = 0
    f = open("D:\\Sai vinay\\Files\\Python\\CS project\\Theatre booking system\\y.txt",'w')
    f.write(c+"\n")
    n = list()
    for i, row in enumerate(board):
        for j,column in enumerate(row):
            if board[i][j] == "green":
                a = chr(65+i)+ str(j+1)+","
                n.append(a)
                f.write(a)
                board[i][j] = "red"
    for a in n:
        if a[0] in ["A","B"]:
            m += 150
        elif a[0] in ["C","D","E"]:
            m += 230
        elif a[0] in ["F","G","H"]:
            m += 300
            
    f.write("\n"+str(m))
    f.close()
    
    f = open("D:\\Sai vinay\\Files\\Python\\CS project\\Theatre booking system\\screen"+screen+".txt", 'w')
    for i in board:
        f.write(str(i)+"\n")
    f.close()
    
    time.sleep(1)
    messagebox.showinfo("Seats Confirmed!","Now, close the window to continue!")

def on_click(i,j,event):
    global a
    if a > 0:
        if board[i][j] == 'none':
            color = "green"
            event.widget.config(bg=color)
            board[i][j] = color
            a -= 1
        elif board[i][j] == 'green':
            color = "grey"
            event.widget.config(bg=color)
            board[i][j] = "none"
            a += 1
        else:
            messagebox.showinfo("Error","We regret the inconvenience.\nThis seat is already booked!")
    elif board[i][j] == 'green':
            color = "grey"
            event.widget.config(bg=color)
            board[i][j] = "none"
            a += 1     
    else :
        messagebox.showinfo("Error","Already selected the required number of seats!")

def draw():
    global gameframe
    global b
    gameframe = tk.Frame(root)
    gameframe.pack()
    
    display = tk.Entry(gameframe,text = "Screen, This way ^",bg='white', font = ("Calibri", 13))
    display.grid(row = 0, column = 1,columnspan = 7)
    display.insert(0, "      ^Screen, This way^")
    
    for i,row in enumerate(board):
        for j,column in enumerate(row):
            x = tk.Label(gameframe, text="      ", bg= "grey" if board[i][j] == 'none' else board[i][j])
            x.grid(row=i+1,column=j+1,padx='3',pady='3')
            x.bind('<Button-1>', lambda e,i=i,j=j:on_click(i,j,e))

    l = tk.Label(gameframe, text="Exit", bg= "#ffff00", font=("Calibri", 12))
    l.grid(column = 7,row = 4, rowspan = 2,padx='3',pady='3')
    j = tk.Label(gameframe, text="Entry", bg= "#00ffff", font=("Calibri", 12))
    j.grid(column = 6,row = 1, columnspan = 2,padx='3',pady='3')
    s = tk.Label(gameframe, text="Silver", bg= "white", font=("Calibri", 12))
    s.grid(column = 8,row = 1, rowspan = 2,padx='3',pady='3')
    g = tk.Label(gameframe, text="Gold", bg= "white", font=("Calibri", 12))
    g.grid(column = 8,row = 3, rowspan = 3,padx='3',pady='3')
    p = tk.Label(gameframe, text="Platinum", bg= "white", font=("Calibri", 12))
    p.grid(column = 8,row = 6, rowspan = 3,padx='3',pady='3')
    for j in range(len(board)):
        y = tk.Label(gameframe, text = chr(b), bg = "white")
        y.grid(row = j+1, column = 0,padx='3',pady='3')
        b += 1
    c = tk.Button(gameframe, text = "  Confirm  ", font=("Arial", 12))
    c.grid(row = 9, column = 0, columnspan = 9, pady=10)
    c.bind('<Button-1>', lambda e : save())


f = open("D:\\Sai vinay\\Files\\Python\\CS project\\Theatre booking system\\x.txt",'r')
a = int(f.readline().strip())
screen = f.readline().strip()
f.close()

f = open("D:\\Sai vinay\\Files\\Python\\CS project\\Theatre booking system\\screen"+screen+".txt", 'r+')
s = " "
board = list()
while s:
    s = f.readline().strip()
    try:
        board.append(eval(s))
    except:
        f.close()


b = 65
c = en_show()

root = tk.Tk()
root.title("Screen"+str(screen))

draw()
root.mainloop()
