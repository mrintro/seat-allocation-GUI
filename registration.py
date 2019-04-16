from tkinter import *
import pandas as pd
from PIL import ImageTk, Image
from tkinter.font import Font
import mysql.connector 


def validate(a,b,root):
        mydb = mysql.connector.connect(host="localhost",user="root",database = "josaa")
        cr=mydb.cursor()
        cr.execute("select * from student_detail")
        k=cr.fetchall()
        flag=True
        n=len(k)
        a=int(a)
        print(n)
        for i in range(0,n):
                if(k[i][2]==a and k[i][1]==b):
                        flag=False
                        break
        if(flag):
                print("yes")
        else:
                print("no")

def dbcreate(a,b,c,d,e,f,root):
        print("here")
        k=(a,b,c,d,e,f)
        choice(k,root)
        


def registration(root) :
        
        root.destroy()
        root = Tk()
        root.geometry("1920x1080")
        font1 = Font(family = "Times New Roman",size=20, weight="bold",underline=1)
        hor_frame = Frame(root, height = 15, width = 1700, bg = "blue").place(x=0,y=0)
        img = ImageTk.PhotoImage(Image.open("ashok.jpg"))
        img1 = ImageTk.PhotoImage(Image.open("josaa-logo.png"))
        panel = Label(root, image = img)
        panel1 = Label(root, image  = img1)
        panel.place(x = 150, y = 25)
        panel1.place(x = 1200, y = 25)
        label_1 = Label(root, text="Government of India",font=("bold", 10)).place(x=240,y=80)
        label_2 = Label(root, text="Ministry Of Human Resource Development",font=("bold", 12)).place(x=240,y=100)
        label_3 = Label(root, text="Joint Entrance Examination (MAINS)", font=("bold",30), fg= "blue").place(x = 480,y = 45)
        
        f3 = Frame(root, height = 5, width = 1700, bg = "grey").place(x=0,y=175)
        f1 = Frame(root, height = 18, width = 1700, bg = "red").place(x=0,y=180)
        f2 = Frame(root, height = 5, width = 1700, bg = "grey").place(x=0,y=198)
        label_4 = Label(root, text="Registration", font=font1).place(x = 650,y = 240)   

        name = Label(root, text="Name           : ",font=("bold", 14)).place(x=500,y=310)
        password = Label(root, text="Password   : ",font=("bold", 14)).place(x=500,y=340)
        jee_no = Label(root, text="JEE Roll Number      : ",font=("bold", 14)).place(x=500,y=370)
        jee_marks = Label(root, text="JEE Marks         : ",font=("bold", 14)).place(x=500,y=400)
        board_no = Label(root, text="Board Roll Number  : ",font=("bold", 14)).place(x=500,y=430)
        board_marks = Label(root, text="Board Percentage        : ",font=("bold", 14)).place(x=500,y=460)
        entry_name = Entry(root,width = 40)
        entry_name.place(x=700,y=310)
        entry_password = Entry(root,width = 40,show = "*")
        entry_password.place(x=700,y=340)
        entry_jee_no = Entry(root,width = 40)
        entry_jee_no.place(x=700,y=370)
        entry_jee_marks = Entry(root,width = 40)
        entry_jee_marks.place(x=700,y=400)
        entry_borad_no = Entry(root,width = 40)
        entry_borad_no.place(x=700,y=430)
        entry_board_marks = Entry(root,width = 40)
        entry_board_marks.place(x=700,y=460)
        Button(root, text='Submit',command = lambda: dbcreate(entry_name.get(),entry_password.get(),entry_jee_no.get(),entry_jee_marks.get(),entry_borad_no.get(),entry_board_marks.get(),root),width=18,bg='red',fg='white').place(x=700,y=520)

        label_4 = Label(root,text = "Disclaimer: This site is designed and hosted by NIC eCounselling Division and the contents are provided by NTA.",width = 200,fg = "white", bg="red",font =("bold",10)).place(x=0,y=590)

        


        root.mainloop()
