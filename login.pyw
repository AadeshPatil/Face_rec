from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from regester import Register
import os
import sys
from main import Face_Recognition_system 
from cv2 import *
from time import strftime
from datetime import datetime
import datetime as dt
import random
from main import Face_Recognition_system
from playsound import playsound



class Login_data:
    def __init__(self , root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login system")
        self.root.config(bg="white")
        self.root.iconbitmap('icon.ico')
    
        self.var=IntVar()

        #bg img
        img3=Image.open(r"img\reg_bg.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=190,y=0,width=1530,height=710)

        #left  img
        img=Image.open(r"img\lock.jpg")
        img=img.resize((400,500),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        bg_img1=Label(self.root,image=self.photoimg)
        bg_img1.place(x=100,y=100,width=400,height=500)


        # ***** Login Frmae ******
        login_1=Frame(self.root,bg="white")
        login_1.place(x=480,y=100,width=700,height=500)


        #wish 
        currentTime = datetime.now()
        currentTime.hour

        if currentTime.hour < 12:
            a = 'Good Morning'
        elif 12 <= currentTime.hour < 18:
            a = 'Good afternoon'
        else:
            a = 'Good evening'

        wish_lbl=Label(login_1,text ="Hello ," + a  ,font=('Candara Light', -25,'bold italic'),bg="white",fg="blue").place(x=60,y=30)
        
        w = Label(bg_img1, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="white", bg="black", font=("helvetica", 20)).pack(side=TOP)
        #login here
        title_lbl=Label(login_1,text="*********LOGIN HERE*********",font=('Candara Light', -25,'bold italic'),bg="white",fg="green").place(x=60,y=80)

        #email
        email_label=Label(login_1,text="USERNAME   ",font=("times new romen",18,"bold"),bg="white",fg="gray").place(x=60,y=120)
        self.txt_email_label=Entry(login_1,font=("times new romen",18,"bold"),bg="lightgray")
        self.txt_email_label.place(x=60,y=160,width=350,height=35)
        
        #password
        pass_label=Label(login_1,text="PASSWORD    ",font=("times new romen",18,"bold"),bg="white",fg="gray").place(x=60,y=220)
        self.txt_pass_label=Entry(login_1,show="●",font=("times new romen",18,"bold"),bg="lightgray")
        self.txt_pass_label.place(x=60,y=260,width=350,height=35)
       
       #pw_hide_show
        bt = Checkbutton(login_1, command = self.mark, offvalue = 0, onvalue = 1, variable = self.var,bg="lightblue")
        bt.place(x = 420, y = 263)

        # forgot password
        btn_forget=Button(login_1,text="Forget password ? ",command=self.forget_pass,cursor="hand2",font=("times new romen",15,"bold"),bg="white",fg="#800857",bd=0)
        btn_forget.place(x=215,y=295)


        #login 
        btn_login=Button(login_1,text="LOGIN ⤞ ",command=self.login,cursor="hand2",font=("times new romen",15,"bold"),bg="blue",fg="white")
        btn_login.place(x=55,y=360,width=180)


# password hide show function

    def mark(self) :

        if self.var.get() == 1 :
            self.txt_pass_label.configure(show = "")
        elif self.var.get() == 0 :
            self.txt_pass_label.configure(show = "●")




    def login(self):
        if self.txt_email_label.get()=="" or self.txt_pass_label.get()=="":
            messagebox.showerror("error","All fields are Reqired",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="2412",database="face_rec")
                my_curser=conn.cursor()
                my_curser.execute("select * from users where email= '"+ self.txt_email_label.get() + "' and password='"+ self.txt_pass_label.get() +"'")
                row=my_curser.fetchone()
                if row==None:                  
                    camera = cv2.VideoCapture(0)
                    i = 0
                    r = random.randint(1,101)
                    while i < 1:
                        return_value, image = camera.read()
                        cv2.imwrite("security/wrongPw{}.png".format(r), image)
                        i+=1
                    del(camera)
                    conn1 = mysql.connector.connect(host="localhost",user="root",password="2412",database="face_rec")
                    my_curser1 = conn1.cursor()
                    now = datetime.now()

                    d1=now.strftime("%d/%m/%Y")
                    dtString=now.strftime("%H:%M:%S")
                    p  = "security/wrongPw{}.png".format(r)
                    my_curser1.execute("insert into unautharisedaccess (time,date,path) values(%s,%s,%s)",(dtString,d1,p))
                    conn1.commit()
                    conn1.close()
                    messagebox.showwarning("Error","You have Enter Wrong Password Your face has been Captured..!",parent=self.root)

                else:
                    messagebox.showinfo("Success","Welcome")
                   
                    self.home()

                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

    def home(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_system(self.new_window)
        
    
# forgert 
    def forget_ps(self):
        if self.txt_email_label.get()=="Select" or self.cmb_que.get()=="" or self.txt_anser.get()=="" or self.txt_anser.get()=="" :
                messagebox.showerror("Error","All field are required.!",parent=self.root2)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="2412",database="face_rec")
                my_curser=conn.cursor()

                my_curser.execute("select * from users where email= '"+ self.txt_email_label.get() + "' and Question='"+ self.cmb_que.get() + "' and answer='"+ self.txt_anser.get() + "'")
                row=my_curser.fetchone()
                if row==None:
                   messagebox.showerror("Error","Please select correct sequrity question Or Answer",parent=self.root2)
                else:
                    my_curser.execute("update users set password= '"+ self.new_password.get() + "' where email='"+ self.txt_email_label.get() + "'")
                    row=my_curser.fetchone()
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("success","You password reset succefully..!",parent=self.root2)
                    self.resets()
                    self.root2.destroy()
                    
            
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
                
    def resets(self):
        self.cmb_que.current(0)
        self.txt_pass_label.set=""
        self.txt_anser.set=""
        self.txt_email_label.set=""



    def forget_pass(self):
        if self.txt_email_label.get()=="":
            messagebox.showerror("error","plese enter email adrress",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="2412",database="face_rec")
                my_curser=conn.cursor()

                my_curser.execute("select * from users where email= '"+ self.txt_email_label.get() + "' or password='"+ self.txt_pass_label.get() +"'")
                row=my_curser.fetchone()
                if row==None:
                   messagebox.showerror("Error","Plese enter valid email to reset your password !",parent=self.root)
                    
                else:
                    conn.close()  
                    self.root2=Tk()
                    self.root2.title("Forgot passord")
                    self.root2.geometry("400x400+480+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t=Label(self.root2,text="Forgot password",font=("times new romen",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)
                    
                    # security 
                    question=Label(self.root2,text="Security  Question",font=("times new romen",15,"bold"),bg="white",fg="gray").place(x=80,y=100)
                    self.cmb_que=ttk.Combobox(self.root2,font=("times new romen",13),state='readonly',justify=CENTER)
                    self.cmb_que['values']=("Select","Your first pet","Your BirthPlace")
                    self.cmb_que.place(x=80,y=140,width=250)
                    self.cmb_que.current(0)

                    #answer
                    emial_name=Label(self.root2,text="Answer ",font=("times new romen",15,"bold"),bg="white",fg="gray").place(x=80,y=180)
                    self.txt_anser=Entry(self.root2,font=("times new romen",15),bg="lightgray")
                    self.txt_anser.place(x=80,y=220,width=250)
                    
                    #New password
                    password=Label(self.root2,text="New Password ",font=("times new romen",15,"bold"),bg="white",fg="gray").place(x=80,y=260)
                    self.new_password=Entry(self.root2,font=("times new romen",15),bg="lightgray")
                    self.new_password.place(x=80,y=300,width=250)

                        #reset btn

                    btn_reset=Button(self.root2,text="Reset password",command=self.forget_ps,cursor="hand2",font=("times new romen",12,"bold"),bg="green",fg="white")
                    btn_reset.place(x=90,y=340,width=140)

                    
                
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    
            

        
if __name__ =="__main__":
        root = Tk()
        obj=Login_data(root)
        root.mainloop()