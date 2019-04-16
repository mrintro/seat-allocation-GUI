from tkinter import *
import pandas as pd
from PIL import ImageTk, Image
from tkinter.font import Font
import mysql.connector 

def guest(root) :
	root.destroy()
#	from frontpage import frontpage
	
	mydb = mysql.connector.connect(host="localhost",user="root",database = "josaa")
	mycursor = mydb.cursor()
	mycursor.execute("select * from college")
	res = mycursor.fetchall()
	root = Tk()
	root.title("Guest Login")
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
#	Button(root, text='Home',width=18,bg='red',fg='white',command = frontpage.frontpage()).place(x=600,y=180)
	f2 = Frame(root, height = 5, width = 1700, bg = "grey").place(x=0,y=198)
	f = Frame(root)
	f.place(relx = 0.5,rely=0.6,anchor = CENTER)
	name = Label(f, text="S.No",font=("bold", 14)).grid(row=0,column=0)
	name = Label(f, text="College",font=("bold", 14)).grid(row=0,column=1)
	name = Label(f, text="branch",font=("bold", 14)).grid(row=0,column=2)
	name = Label(f, text="seats",font=("bold", 14)).grid(row=0,column=3)
	for i in range (0,15):
		for j in range (0,4):
			Label(f,text=res[i][j],font=("bold", 15)).grid(row=i+1,column=j)

	root.mainloop()




