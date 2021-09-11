from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os



class Register:
    def __init__(self , root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("registration Window")
        self.root.config(bg="white")
        self.root.iconbitmap('icon.ico')


        
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
        
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=100,y=100,width=400,height=500)


        # ***** Register Frmae ******
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

       

        title_lbl=Label(frame1,text="REGISTER HERE",font=("times new romen",20,"bold"),bg="white",fg="green").place(x=50,y=30)


        #first name
        f_name=Label(frame1,text="First Name",font=("times new romen",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new romen",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

        #last name
        L_name=Label(frame1,text="Last Name",font=("times new romen",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.L_fname=Entry(frame1,font=("times new romen",15),bg="lightgray")
        self.L_fname.place(x=370,y=130,width=250)

        #contct no
        contact_name=Label(frame1,text="Contact no",font=("times new romen",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contct=Entry(frame1,font=("times new romen",15),bg="lightgray")
        self.txt_contct.place(x=50,y=200,width=250)

        #email
        emial_name=Label(frame1,text="Email ",font=("times new romen",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new romen",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)

         # security 
        question=Label(frame1,text="Security  Question",font=("times new romen",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.cmb_que=ttk.Combobox(frame1,font=("times new romen",13),state='readonly',justify=CENTER)
        self.cmb_que['values']=("Select","Your first pet","Your BirthPlace")
        self.cmb_que.place(x=50,y=270,width=250)
        self.cmb_que.current(0)

        #answer
        emial_name=Label(frame1,text="Answer ",font=("times new romen",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_anser=Entry(frame1,font=("times new romen",15),bg="lightgray")
        self.txt_anser.place(x=370,y=270,width=250)


        # password
        password=Label(frame1,text="Password *",font=("times new romen",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new romen",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)


        #confirm password
        con_password=Label(frame1,text="Confirm Password ",font=("times new romen",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_con_password=Entry(frame1,font=("times new romen",15),bg="lightgray")
        self.txt_con_password.place(x=370,y=340,width=250)


        #***** terms
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new romen",15,"bold"),bg="white",fg="gray").place(x=50,y=380)

        #***** button 

        btn_register=Button(frame1,text="Register Now ",command=self.register_data,cursor="hand2",font=("times new romen",15,"bold"),bg="green",fg="white")
        btn_register.place(x=50,y=450)


    def clear(self):
        self.txt_fname.delete(0,END)   
        self.L_fname.delete(0,END)  
        self.txt_contct.delete(0,END)  
        self.txt_email.delete(0,END)  
        self.cmb_que.current(0)
        self.txt_anser.delete(0,END)
        self.txt_password.delete(0,END)  
        self.txt_con_password.delete(0,END)  


    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contct.get()=="" or   self.txt_email.get()==" "  or   self.cmb_que.get()=="" or   self.txt_password.get()=="" or self.txt_con_password.get()=="" :
            messagebox.showerror("Error","All fields are required.!",parent=self.root)

        elif self.txt_password.get() != self.txt_con_password.get():
            messagebox.showerror("Error","Password must be same.!",parent=self.root)

        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Plese agree terms and conditon",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="2412",database="face_rec")
                my_curser=conn.cursor()
                my_curser.execute("select * from users where email='"+ self.txt_email.get() +"'")
                row=my_curser.fetchone()

                if row!=None:
                    messagebox.showerror("Error","user already exist",parent=self.root)
                else:
                    my_curser.execute("insert into users (fname,lname,contact,email,Question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                        (self.txt_fname.get(),
                            self.L_fname.get(),
                            self.txt_contct.get(),
                            self.txt_email.get(),
                            self.cmb_que.get(),
                            self.txt_anser.get(),
                            self.txt_password.get()
                            ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Register succesfull",parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)




if __name__ =="__main__":
        root = Tk()
        obj=Register(root)
        root.mainloop()