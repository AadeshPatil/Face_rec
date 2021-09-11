from pathlib import Path
import tkinter
from tkinter  import*
from tkinter import ttk
from  PIL import Image,ImageTk
import os 
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import csv
from tkinter import filedialog


class Unautharise:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face_recognition")
        self.root.config(bg="powder blue")
        self.root.iconbitmap('icon.ico')


        
        img=Image.open(r"img\un_access.png")
        img=img.resize((1530,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        label_img=Label(self.root,image=self.photoimg)
        label_img.place(x=0,y=0,width=1530,height=200)


        title_lbl=Label(self.root,text=" Unauthurised Access ",font=("comicsansns",25,"bold"),fg='red',bg="powder blue")
        title_lbl.place(x=500,y=200)

        img4=Image.open(r"img\home_icon.png")
        img4=img4.resize((40,40),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(self.root,image=self.photoimg4,bd=0,cursor="hand2", command=root.destroy)
        b1.place(x=5,y=200)

# *******    FRAME ***********

        main_frame=LabelFrame(self.root,bd=2,bg="dark blue",relief=RIDGE,font=("times new romen",12,"bold"))
        main_frame.place(x=15,y=250,width=700,height=400)

        reset_btn=Button(self.root,text="Reset table",command=self.Reset_system,width=15,font=("times new romen",13,"bold"),bg="red",fg="white")
        reset_btn.place(x=525,y=650)


#***********************table*************

        table_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width=680,height=390)

        #scroll bar

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.UnAccess_table=ttk.Treeview(table_frame,column=("srNo","date","time","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.UnAccess_table.xview)
        scroll_y.config(command=self.UnAccess_table.yview)


        self.UnAccess_table.heading("srNo",text="srNo")
        self.UnAccess_table.heading("date",text="Date")
        self.UnAccess_table.heading("time",text="Time")
        self.UnAccess_table.heading("photo",text="photo")
        self.UnAccess_table["show"]="headings"


        self.UnAccess_table.column("srNo",width=1)
        self.UnAccess_table.column("date",width=20)
        self.UnAccess_table.column("time",width=20)
        self.UnAccess_table.column("photo",width=20)
    
        self.UnAccess_table.pack(fill=BOTH,expand=1)
        self.UnAccess_table.bind("<ButtonRelease>",self.get_cursor)
   
        self.fetch_data()
          
    def get_cursor(self,event=""):
            cursor_focus=self.UnAccess_table.focus()
            content=self.UnAccess_table.item(cursor_focus)
            data=content["values"]

            path = data[3]

            img1=Image.open(path)
            img1=img1.resize((600,400),Image.ANTIALIAS)
            self.photoimg1=ImageTk.PhotoImage(img1)
        
            label_img=Label(self.root,image=self.photoimg1)
            label_img.place(x=725,y=250,width=600,height=400) 
        


    # functions
    def fetch_data(self):
             conn=mysql.connector.connect(host="localhost",user="root",password="2412",database="face_rec")
             my_curser=conn.cursor()
             my_curser.execute("select * from unautharisedaccess order by srNo desc")
             data=my_curser.fetchall()

             if len(data)!=0:
                     self.UnAccess_table.delete(*self.UnAccess_table.get_children())
                     for i in data:
                             self.UnAccess_table.insert("",END,values=i)
                     conn.commit()
             conn.close()

    def Reset_system(self):
           self.fetch_data()
           delete=messagebox.askyesno("Reset Data","Do you want yo delete this data",parent=self.root)
           if delete>0:
                  conn=mysql.connector.connect(host="localhost",user="root",password="2412",database="face_rec")
                  my_curser=conn.cursor()
                  my_curser.execute("TRUNCATE TABLE unautharisedaccess")
                  messagebox.showinfo("Succefully","Your system has been Reset succefully",parent=self.root) 
                  self.empty()
                  conn.commit()
                  conn.close()
                  self.fetch_data()


    def empty(self):
                dir = 'security'
                for f in os.listdir(dir):
                        os.remove(os.path.join(dir, f)) 





if __name__ =="__main__":
        root = Tk()
        obj=Unautharise(root)
        root.mainloop()