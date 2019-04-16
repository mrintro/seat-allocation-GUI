from tkinter import *
import pandas as pd
from PIL import ImageTk, Image
from tkinter.font import Font
import mysql.connector 
from guest import guest

from registration import registration,validate


def frontpage() :

	root = Tk()
	root.geometry("1920x1080")
	af = Font(family = "Helvetica",size=20, weight="bold",underline=1)
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
	ver_frame = Frame(root, height = 290, width = 5, bg = "black").place(x=600,y=220)
	label_4 = Label(root,text = "Security Tips", font =af).place(x = 100,y=250)
	label_5 = Label(root,text = "1.	Confidentiality of Password is the sole responsibility of the Candidates.", font =("bold",10)).place(x = 100,y=300)
	label_6 = Label(root,text = "2.	Change your Password at frequent interval.", font =("bold",10)).place(x = 100,y=330)
	label_7 = Label(root,text = "3.	Your IP Address will be captured for security reasons.", font =("bold",10)).place(x = 100,y=360)
	label_8 = Label(root,text = "Only Registered Candidates Sign In", font =af).place(x = 700,y=250)
	

	app_no = Label(root, text="JEE Roll Number 	: ",font=("bold", 13)).place(x=700,y=310)
	password = Label(root, text="Password 	: ",font=("bold", 13)).place(x=700,y=340)
	entry_app_no = Entry(root,width = 30)
	entry_app_no.place(x=900,y=310)
	entry_password = Entry(root,width = 30,show = "*")
	entry_password.place(x=900,y=340)
	Button(root, text='Login',width=18,bg='red',fg='white',command = lambda: validate(entry_app_no.get(),entry_password.get(),root)).place(x=900,y=380)

	label_9 = Label(root, text="Login as Guest 	: ",font=("bold", 13)).place(x=700,y=430)
	Button(root, text='Enter',width=18,bg='red',fg='white',command = lambda : guest(root)).place(x=900,y=430)
	label_10 = Label(root, text="Register 		: ",font=("bold", 13)).place(x=700,y=470)
	Button(root, text='Enter',width=18,bg='red',fg='white',command = lambda : registration(root)).place(x=900,y=470)

	label_4 = Label(root,text = "Disclaimer: This site is designed and hosted by NIC eCounselling Division and the contents are provided by NTA.",width = 200,fg = "white", bg="red",font =("bold",10)).place(x=0,y=520)

	


	root.mainloop()

frontpage()
