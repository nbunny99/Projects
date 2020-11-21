ch=0
k=0
l = list()

import tkinter as tk
import tkinter.messagebox as messagebox
import time
import os
import sys
import fileinput
import random

def login():
        s="\n\t>>LOGIN\n"
        for i in s:
            print(i, end=' ')
            time.sleep(0.05)
        answer='y'
        while answer=='y':
            password=input("\nEnter the password:")
            if password=="sas123":
                obj.mainmenu()
            else:
                print("incorrect password!!")
                answer=input("press 'y' to try again:")

def introduction():
        print("\n")
        p= "\t\t\t\t\tRED CARPET CINEMAS "
        for j in p:
            print(j, end=' ')
            time.sleep(0.05)
        print("\n")
        time.sleep(0.03)
        input(">Press Enter to continue:")
        obj.movies()
                              
def choice(ch):
        if ch==1:
                obj.availability()
        elif ch==2:
                obj.book()
        elif ch==3:
                obj.display()
        elif ch==4:
                obj.ticket()
        elif ch==5:
                obj.Quit()
        obj.mainmenu()
                
class cinemas(object):
        def __init__(self):
                self.movie_name=""
                self.phone=0
                self.amount=0.0
                self.screen=0
                self.show_time=""
                self.seat_no=0
                self.ticket_id=0
                self.tax=0.0
                self.total_amount=0.0
        
        def mainmenu(self):
                print("\n")
                print("\t\t\tWELCOME TO RED CARPET CINEMAS ")
                print("\n")
                print("\t\t |**************************************|")
                print("\t\t |\t\tMAIN MENU \t\t|")
                print("\t\t |**************************************|")
                print("\t\t |\t1. CHECK AVAILABILITY           |")
                print("\t\t |\t2. BOOK SHOW                    |")
                print("\t\t |\t3. DISPLAY TICKET               |")
                print("\t\t |\t4. PRINT TICKET                 |")
                print("\t\t |\t5. EXIT                         |")
                print("\t\t |**************************************|")
                print("\n ")                                                 
                ch=eval(input("Enter your choice:"))
                choice(ch)

        def movies(self):
                global l
                print("\t\t\t\tLIST OF MOVIES AND SHOW TIMINGS\n\n")
                print("| Sr.No.","|","         Movie Name          ","|","Show time 1","|","Show time 2","|","Show time 3","|","Show time 4","|","Screen No.","|"," Rating  |")
                rec=" "
                file1=open("D:\\Sai vinay\\Files\\Python\\CS project\\Theatre booking system\\movies.txt","r+")
                while rec:
                        rec=file1.readline().rstrip("\n")
                        if rec == "":
                                pass
                        else:
                                l.append(rec.split("|"))
                                print("|"+rec+"|")
                        time.sleep(0.03)
                file1.close()
                for i,row in enumerate(l):
                        for j in range(len(row)):
                                l[i][j] = l[i][j].strip()
                                
                print("\n")
                input(">Press Enter to continue:")
                login()
                
        def availability(self):
                global l
                a = input("Enter the name of the movie you want to check:")
                for i in l:
                        if i[1].lower() == a:
                                a = i[6]
                f = open("D:\\Sai vinay\\Files\\Python\\CS project\\Theatre booking system\\z.txt",'w')
                f.write(a)
                f.close()
                
                os.system("start "+ "display.py")
                input(">Press Enter to continue")
                
        def book(self):
                global k,l
                print("\n")
                print("\t\tWELCOME TO RED CARPET CINEMAS ")
                print("\n")
                print("\t\t\tBOOK YOUR TICKETS!!")
                k=int(eval(input("Enter the no of tickets you want to book:")))
                f = open("D:\\Sai vinay\\Files\\Python\\CS project\\Theatre booking system\\x.txt",'w')
                f.write(str(k))
                self.name=input("Enter your name(short):")
                self.phone=input("Enter your phone number:")
                self.movie_name=input("Enter movie you want to watch:").lower()
                for i in l:
                        if self.movie_name == i[1].lower():
                                print("\t|***********************************************|")
                                print("\t|\t\tSEAT SELECTION TYPE             |")
                                print("\t|***********************************************|")
                                print("\t|\t1.PLATINUM \t  per ticket RS.300/-   |")
                                print("\t|\t2.GOLD     \t  per ticket RS.230/-   |")
                                print("\t|\t3.SILVER   \t  per ticket RS.150/-   |")
                                print("\t|***********************************************|")
                                f.write("\n"+i[6])
                                f.close()
                                
                                os.system("start "+ "screen.py")
                                input(">Press Enter to continue")
                                f = open("D:\\Sai vinay\\Files\\Python\\CS project\\Theatre booking system\\y.txt",'r')
                                self.show_time = f.readline().strip()
                                self.seat_no = f.readline().strip().rstrip(",")
                                self.amount = int(f.readline().strip())
                                self.screen = int(i[6])
                                f.close()
                return self
                        
        def ticket(self):
                print("\t********************************************************")
                print("\t\tRED CARPET CINEMAS                 \t")
                print("\t********************************************************")
                print("\t\t\tTICKET\t\t      \t")
                print("\t********************************************************")
                print("\t--------------------------------------------------------")
                print("\tNAME:\t\t\t",self.name,"\t","     ","\t")
                print("\tMOVIE:\t\t\t",self.movie_name,"\t      \t")
                print("\tTICKET ID:\t\t",self.ticket_id,"\t      \t")
                print("\tSHOW TIME:\t\t",self.show_time,"\t      \t")
                print("\tSCREEN NO:\t\t",self.screen,"\t      \t")
                print("\tSEAT NUMBER:\t\t",self.seat_no,"\t      \t")
                print("\tSEAT CHARGES:\t\t",self.amount,"\t      \t")
                print("\tADDITIONAL TAXES:\t","Rs",self.tax,"\t      \t")
                print("\t--------------------------------------------------------")
                print("\tNET AMOUNT:\t\t","Rs",self.total_amount,"\t      \t")
                print("\t********************************************************")
                print("\n")
                print("\t\tPlease pay Rs:",self.total_amount,"!!")
                print("\n")
                
        def display(self):
                self.tax=self.amount*3/100
                self.total_amount=self.amount+self.tax
                self.ticket_id=random.randint(1000,2000)
                print("\tCustomer Name:",self.name)
                print("\tMovie Name:",self.movie_name)
                print("\tTicket ID",self.ticket_id)
                print("\tScreen No.:",self.screen)
                print("\tShow Time:",self.show_time)
                print("\tSeat Number:",self.seat_no)
                print("\tSeat Charges:",self.amount)
                print("\tAdditional Taxes:","Rs",self.tax)
                print("\tNet Amount:","Rs",self.total_amount)
                time.sleep(0.1)
                return self

        def Quit(self):
                print("\tLooking forward to watching more blockbusters with us?")
                print("\n")        
                print("\tPlease stay connected with us for latest offers:")
                print("\tsms to #141")
                print("\n")
                print("\t\t--------------------Thank you------------------------")
                time.sleep(0.1)
                input(">Press Enter to Quit")
                exit()
            
obj=cinemas()
introduction()
