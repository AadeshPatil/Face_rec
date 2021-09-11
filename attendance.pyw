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

my_data=[]
class Records:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face_recognition")
        self.root.iconbitmap('icon.ico')

        self.var_attendt_id=StringVar()
        self.var_attendt_name=StringVar()
        self.var_attendt_email=StringVar()
        self.var_attendt_time=StringVar()
        self.var_attendt_date=StringVar()

    
        # background image
        img=Image.open(r"img\bg.jpg")
        img=img.resize((1530,745),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=745)

        title_lbl=Label(bg_img,text=" Records ",font=("comicsansns",25,"bold"),bg="black",fg='white')
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img4=Image.open(r"img\home_icon.png")
        img4=img4.resize((40,40),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(title_lbl,image=self.photoimg4,bd=0,cursor="hand2", command=root.destroy)
        b1.place(x=5,y=0)



    # ** frame 
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=50,width=1500,height=600)


   #left side label 

        Left_frame=LabelFrame(main_frame,bd=2,bg="lightgray",relief=RIDGE,text="Records Details",font=("comicsansns",12,"bold"))
        Left_frame.place(x=10,y=10,width=650,height=580)

        Left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        Left_inside_frame.place(x=5,y=5,width=630,height=300)


        # label entry 
         #Id
        RecordsId=Label(Left_inside_frame,text=" ID ",font=("comicsansns",12,"bold"),bg="white")
        RecordsId.grid(row=0,column=0,padx=10)

        RecordsId_entry=ttk.Entry(Left_inside_frame,textvariable=self.var_attendt_id,width=20,font=("comicsansns",12,"bold"))
        RecordsId_entry.grid(row=0,column=1,padx=2,pady=10)


        # name 
        name_label=Label(Left_inside_frame,text=" Name ",font=("comicsansns",12,"bold"),bg="white")
        name_label.grid(row=0,column=2,padx=10)

        name_label_entry=ttk.Entry(Left_inside_frame,textvariable=self.var_attendt_name,width=20,font=("comicsansns",12,"bold"))
        name_label_entry.grid(row=0,column=3,padx=2,pady=10)

        # email
        email_label=Label(Left_inside_frame,text=" Email ",font=("comicsansns",12,"bold"),bg="white")
        email_label.grid(row=1,column=0,padx=10)

        dep_label_entry=ttk.Entry(Left_inside_frame,textvariable=self.var_attendt_email,width=20,font=("comicsansns",12,"bold"))
        dep_label_entry.grid(row=1,column=1,padx=2,pady=10)


        # time 
        time_label=Label(Left_inside_frame,text=" Time ",font=("comicsansns",12,"bold"),bg="white")
        time_label.grid(row=1,column=2,padx=10)

        time_label_entry=ttk.Entry(Left_inside_frame,textvariable=self.var_attendt_time,width=20,font=("comicsansns",12,"bold"))
        time_label_entry.grid(row=1,column=3,padx=2,pady=10)

        #date
        date_label=Label(Left_inside_frame,text=" Date ",font=("comicsansns",12,"bold"),bg="white")
        date_label.grid(row=2,column=0,padx=10)

        date_label_entry=ttk.Entry(Left_inside_frame,textvariable=self.var_attendt_date,width=20,font=("comicsansns",12,"bold"))
        date_label_entry.grid(row=2,column=1,padx=2,pady=10)



        #button frame
        btn_frame=LabelFrame(Left_inside_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=190,width=600,height=30)

         #save button
        save_btn=Button(btn_frame,text="Import CSV",width=14,font=("times new romen",13,"bold"),bg="blue",fg="white",command=self.importCsv)
        save_btn.grid(row=0,column=0)

         #update button
        update_btn=Button(btn_frame,text="Export CSV",width=14,font=("times new romen",13,"bold"),bg="blue",fg="white",command=self.exportCsv)
        update_btn.grid(row=0,column=1)

        #delete button
        delete_btn=Button(btn_frame,text="update",width=14,font=("times new romen",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",width=14,font=("times new romen",13,"bold"),bg="blue",fg="white",command=self.reset_data)
        reset_btn.grid(row=0,column=3)

# left_down image
        img9=Image.open(r"img\record_1.png")
        img9=img9.resize((610,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        bg_img1=Label(Left_frame,image=self.photoimg9)
        bg_img1.place(x=10,y=330,width=610,height=200)


  #right side label 

        Right_frame=LabelFrame(main_frame,bd=2,bg="lightgray",relief=RIDGE,text="Records Details",font=("comicsansns",12,"bold"))
        Right_frame.place(x=680,y=10,width=660,height=580)


        table_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=640,height=500)

        # srollbar and table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.Records_Table=ttk.Treeview(table_frame,column=("id","name","email","time","date"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Records_Table.xview)
        scroll_y.config(command=self.Records_Table.yview)

        self.Records_Table.heading("id",text="Id")
        self.Records_Table.heading("name",text="Name")
        self.Records_Table.heading("email",text="Email")
        self.Records_Table.heading("time",text="Time")
        self.Records_Table.heading("date",text="Date")

        self.Records_Table["show"]="headings"

        self.Records_Table.column("id",width=100)
        self.Records_Table.column("name",width=100)
        self.Records_Table.column("email",width=100)
        self.Records_Table.column("time",width=100)
        self.Records_Table.column("date",width=100)
      
        self.Records_Table.pack(fill=BOTH,expand=1)
        self.Records_Table.bind("<ButtonRelease>",self.get_cursor)

    # ********** Fetch data *******

    def fetch_data(self,rows):
        self.Records_Table.delete(*self.Records_Table.get_children())
        for i in rows :
            self.Records_Table.insert("",END,values=i)


    def importCsv(self):
        global my_data 
        my_data.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("csv file","*.csv"),("All file","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                my_data.append(i)
            self.fetch_data(my_data)

    #for exporting data 
    def exportCsv(self):
        try :
            if len(my_data)<1:
                messagebox.showerror("No data","No Data Found",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("csv file","*.csv"),("All file","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in my_data:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Data Exported..!"+os.path.basename(fln)+"Succefully..!",parent=self.root)
        except Exception as es:
            messagebox.showerror("error",f"due to :{str(es)}",parent=self.root)



    def get_cursor(self,event=""):
        cursor_row=self.Records_Table.focus()
        content=self.Records_Table.item(cursor_row)
        rows=content['values']
        self.var_attendt_id.set(rows[0])
        self.var_attendt_name.set(rows[1])
        self.var_attendt_email.set(rows[2])
        self.var_attendt_time.set(rows[3])
        self.var_attendt_date.set(rows[4])

    

    def reset_data(self):
        self.var_attendt_id.set("")
        self.var_attendt_name.set("")
        self.var_attendt_email.set("")
        self.var_attendt_time.set("")
        self.var_attendt_date.set("")
        





if __name__ =="__main__":
        root = Tk()
        obj=Records(root)
        root.mainloop()