import tkinter as tk
import tkinter.messagebox as messagebox
global gameframe

a = open('D:\\Sai vinay\\Files\\Python\\CS project\\Theatre booking system\\x.txt','r')
screen = a.read(1)
a.close()
f = open("D:\\Sai vinay\\Files\\Python\\CS project\\Theatre booking system\\screen"+screen+".txt", 'r')
s = " "
board = list()
while s:
    s = f.readline().strip()
    try:
        board.append(eval(s))
    except:
        f.close()

root = tk.Tk()
root.title("Display")


b=65
gameframe = tk.Frame(root)
gameframe.pack()
    
display = tk.Entry(gameframe,text = "Screen, This way ^",bg='white', font = ("Calibri", 13))
display.grid(row = 0, column = 1,columnspan = 7)
display.insert(0, "      ^Screen, This way^")
    
for i,row in enumerate(board):
    for j,column in enumerate(row):
        x = tk.Label(gameframe, text="      ", bg= "grey" if board[i][j] == 'none' else board[i][j])
        x.grid(row=i+1,column=j+1,padx='3',pady='3')

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
c = tk.Button(gameframe, text = "  Close  ", font=("Arial", 12))
c.grid(row = 9, column = 0, columnspan = 10, pady=10)
c.bind('<Button-1>', lambda e : messagebox.showinfo("Close?","Close the Display window to continue."))
    
root.mainloop()
