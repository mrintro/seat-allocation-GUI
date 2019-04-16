from tkinter import *
import pandas as pd
from PIL import ImageTk, Image
from tkinter.font import Font
import mysql.connector 
from frontpage import frontpage
from guest import guest
from registration import registration,validate

root = Tk()
def dbcreate(k,a,b,c,d,e,f,root):
    
    p=(a,b,c,d,e,f)
    p=k+p
    print(p)
    mydb = mysql.connector.connect(host="localhost",user="root",database = "josaa")
    cr=mydb.cursor()
    query = "INSERT INTO student_detail(name,password,jee_main_no,jee_mains_marks,board_no,board_marks,f_pref_clg,f_pref_branch,s_pref_clg,s_pref_branch,t_pref_clg,t_pref_branch) " \
                    "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    temp=cr.execute(query, p)
    mydb.commit()

def choice(k,root) :
	root.destroy()
	print(k)
	root = Tk()
	root.geometry("1920x1080")
	font1 = Font(family = "Times New Roman",size=20, weight="bold",underline=1)
	hor_frame = Frame(root, height = 15, width = 1700, bg = "blue").place(x=0,y=0)
	list_college = ['NATIONAL INSTITUTE OF TECHNOLOGY, TRICHY','NATIONAL INSTITUTE OF TECHNOLOGY, ALLAHABAD','NATIONAL INSTITUTE OF TECHNOLOGY, KURUKSHETRA','NATIONAL INSTITUTE OF TECHNOLOGY, JAIPUR','NATIONAL INSTITUTE OF TECHNOLOGY, HAMIRPUR']
	list_branch = ['CS','IT','ECE']
	
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
	Button(root,text = "HOME", width = 18,bg = 'red', fg = 'white', command = frontpage()).place(x = 1400,y=198)
	label_4 = Label(root, text="Choice Filling", font=font1).place(x = 650,y = 240)	
	label_5 = Label(root, text="Choose colleges according to your priority. After submission they cannot be changed.",font=("bold", 10)).place(x=500,y=290)
	label_6 = Label(root, text="Choice 1 : ",font=("bold", 14)).place(x=350,y=330)
	
	c = StringVar(root)
	d = StringVar(root)
	dlist = OptionMenu(root,c, *list_college)
	dlist.config(width = 50)
	c.set("Select College")
	dlist.place(x=500,y=330)
	dlist = OptionMenu(root,d, *list_branch)
	dlist.config(width = 15)
	d.set("Select Branch")
	dlist.place(x=850,y=330)

	label_7 = Label(root, text="Choice 2 : ",font=("bold", 14)).place(x=350,y=380)
	
	e = StringVar(root)
	f = StringVar(root)
	dlist = OptionMenu(root,e, *list_college)
	dlist.config(width = 50)
	e.set("Select College")
	dlist.place(x=500,y=380)
	dlist = OptionMenu(root,f, *list_branch)
	dlist.config(width = 15)
	f.set("Select Branch")
	dlist.place(x=850,y=380)

	label_7 = Label(root, text="Choice 3 : ",font=("bold", 14)).place(x=350,y=430)
	
	g = StringVar(root)
	h = StringVar(root)
	dlist = OptionMenu(root,g, *list_college)
	dlist.config(width = 50)
	g.set("Select College")
	dlist.place(x=500,y=430)
	dlist = OptionMenu(root,h, *list_branch)
	dlist.config(width = 15)
	h.set("Select Branch")
	dlist.place(x=850,y=430)
	Button(root, text = "SUBMIT", width = 18,bg = 'red', fg = 'white', command = lambda: dbcreate(k,c.get(),d.get(),e.get(),f.get(),g.get(),h.get(),root)).place(x = 850,y=480)

	label_8 = Label(root,text = "Disclaimer: This site is designed and hosted by NIC eCounselling Division and the contents are provided by NTA.",width = 200,fg = "white", bg="red",font =("bold",10)).place(x=0,y=590)







	root.mainloop()

choice(1,root)
