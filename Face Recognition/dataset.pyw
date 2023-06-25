import os
import tkinter
from tkinter import *
from tkinter import messagebox, ttk
import cv2
import mysql.connector
from PIL import Image, ImageTk


class Dataset:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face_recognition")
        self.root.iconbitmap('icon.ico')

# variables
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_mobileNo = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_age = StringVar()
        self.var_address = StringVar()

# img1
        img = Image.open(r"img\dem.png")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
# img2

        img1 = Image.open(r"img\dem.png")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

# img3
        img2 = Image.open(r"img\dem.png")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

# bg image
        img3 = Image.open(r"img\bg.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=660)

        title_lbl = Label(bg_img, text="Manage Dataset", font=(
            "times new romen", 25, "bold"), bg="black", fg='white')
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img4 = Image.open(r"img\home_icon.png")
        img4 = img4.resize((40, 40), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(title_lbl, image=self.photoimg4, bd=0,
                    cursor="hand2", command=root.destroy)
        b1.place(x=5, y=0)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=45, width=1490, height=500)

        # upper side label

        Upper_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Details", font=("times new romen", 12, "bold"))
        Upper_frame.place(x=10, y=10, width=1325, height=240)

        # class dataset cource
        class_frame = LabelFrame(Upper_frame, bd=2, bg="white", relief=RIDGE, font=(
            "times new romen", 12, "bold"))
        class_frame.place(x=5, y=15, width=1300, height=200)

        # name
        srNo_label = Label(class_frame, text=" srNo ", font=(
            "times new romen", 12, "bold"), bg="white")
        srNo_label.grid(row=0, column=0, padx=0)

        # srNo_entry = Entry(root, textvariable=self.var_name, width=20, font=(
        #     "times new romen", 12, "bold"), bg="lightgray")
        # srNo_entry.grid(row=0, column=0, padx=0, pady=0)
        # name
        name_label = Label(class_frame, text=" Name ", font=(
            "times new romen", 12, "bold"), bg="white")
        name_label.grid(row=0, column=0, padx=5)

        name_entry = Entry(class_frame, textvariable=self.var_name, width=20, font=(
            "times new romen", 12, "bold"), bg="lightgray")
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Id
        ID_label = Label(class_frame, text=" ID ", font=(
            "times new romen", 12, "bold"), bg="white")
        ID_label.grid(row=0, column=2, padx=5)

        ID_entry = Entry(class_frame, textvariable=self.var_id, width=20, font=(
            "times new romen", 12, "bold"), bg="lightgray")
        ID_entry.grid(row=0, column=3, padx=2, pady=5)

        # Email
        email_label = Label(class_frame, text=" Email", font=(
            "times new romen", 12, "bold"), bg="white")
        email_label.grid(row=1, column=0, padx=5)

        email_entry = Entry(class_frame, textvariable=self.var_email, width=20, font=(
            "times new romen", 12, "bold"), bg="lightgray")
        email_entry.grid(row=1, column=1, padx=5, pady=5)

        # mobile_No
        mobile_label = Label(class_frame, text="Mobile No ", font=(
            "times new romen", 12, "bold"), bg="white")
        mobile_label.grid(row=1, column=2, padx=5)

        mobile_entry = Entry(class_frame, textvariable=self.var_mobileNo, width=20, font=(
            "times new romen", 12, "bold"), bg="lightgray")
        mobile_entry.grid(row=1, column=3, padx=5, pady=5)

        # gender
        Gender_label = Label(class_frame, text=" Gender", font=(
            "times new romen", 12, "bold"), bg="white")
        Gender_label.grid(row=2, column=0, padx=5)

        gender_combo = ttk.Combobox(class_frame, textvariable=self.var_gender, font=(
            "times new romen", 12, "bold"), width="18", state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=5, pady=5)

        # dob
        dob_label = Label(class_frame, text="DOB ", font=(
            "times new romen", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=5)

        dob_entry = Entry(class_frame, textvariable=self.var_dob, width=20, font=(
            "times new romen", 12, "bold"), bg="lightgray")
        dob_entry.grid(row=2, column=3, padx=5, pady=5)

        # age
        age_label = Label(class_frame, text=" Age", font=(
            "times new romen", 12, "bold"), bg="white")
        age_label.grid(row=3, column=0, padx=5)

        age_entry = Entry(class_frame, textvariable=self.var_age, width=20, font=(
            "times new romen", 12, "bold"), bg="lightgray")
        age_entry.grid(row=3, column=1, padx=5, pady=5)

        # Address
        add_label = Label(class_frame, text=" Address", font=(
            "times new romen", 12, "bold"), bg="white")
        add_label.grid(row=3, column=2, padx=5)

        add_entry = Entry(class_frame, textvariable=self.var_address, width=20, font=(
            "times new romen", 12, "bold"), bg="lightgray")
        add_entry.grid(row=3, column=3, padx=5, pady=5)

        # radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = Radiobutton(class_frame, variable=self.var_radio1, text="Take Photo Sample",
                                value="Yes", font=("times new romen", 12, "bold"), bg="white")
        radiobtn1.place(x=20, y=150)

        radiobtn2 = Radiobutton(class_frame, variable=self.var_radio1, text="NO Photo Sample",
                                value="No", font=("times new romen", 12, "bold"), bg="white")
        radiobtn2.place(x=300, y=150)

 # *********   button frame
       # btn_frame=LabelFrame(class_frame,bd=2,relief=RIDGE)
        # btn_frame.place(x=0,y=190,width=1490,height=240)

        # save button
        save_btn = Button(class_frame, text="Save", command=self.add_data, width=30, font=(
            "times new romen", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=7)

        # update button
        update_btn = Button(class_frame, command=self.update_data, text="Update", width=30, font=(
            "times new romen", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=1, column=7)

        # delete button
        delete_btn = Button(class_frame, text="Delete", command=self.delete_data, width=30, font=(
            "times new romen", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=2, column=7)

        # reset button
        reset_btn = Button(class_frame, text="Reset", command=self.reset_data, width=30, font=(
            "times new romen", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=3, column=7)

        # Take_photo sample
        take_photo_sample = Button(class_frame, command=self.genrate_dataset, text="Take Photo Sample", width=20, font=(
            "times new romen", 13, "bold"), bg="darkblue", fg="white")
        take_photo_sample.place(x=950, y=60)

  # down side label

        Right_frame = LabelFrame(main_frame, bd=2, bg="lightgray", relief=RIDGE, font=(
            "times new romen", 12, "bold"))
        Right_frame.place(x=0, y=255, width=1490, height=250)

# ************search system***************

        # class dataset cource
        lbl = Label(Right_frame, text="DataBase", bd=0, relief=RIDGE, font=(
            "times new romen", 20, "bold"), bg="lightgray", fg="black")
        lbl.place(x=25, y=5, width=1300, height=50)

# ***********************table*************
        table_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=25, y=55, width=1300, height=150)

        # scroll bar

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.dataset_table = ttk.Treeview(table_frame, column=("srNo", "name", "id", "email", "mobileNo", "gender",
                                          "dob", "age", "address", "photosample"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.dataset_table.xview)
        scroll_y.config(command=self.dataset_table.yview)

        self.dataset_table.heading("srNo", text="srNo")
        self.dataset_table.heading("name", text="Name")
        self.dataset_table.heading("id", text="Id")
        self.dataset_table.heading("email", text="Email")
        self.dataset_table.heading("mobileNo", text="MobileNo")
        self.dataset_table.heading("gender", text="gender")
        self.dataset_table.heading("dob", text="dob")
        self.dataset_table.heading("age", text="Age")
        self.dataset_table.heading("address", text="Address")
        self.dataset_table.heading("photosample", text="photoSampleStatus")
        self.dataset_table["show"] = "headings"

        self.dataset_table.column("srNo", width=100)
        self.dataset_table.column("name", width=100)
        self.dataset_table.column("id", width=100)
        self.dataset_table.column("email", width=100)
        self.dataset_table.column("mobileNo", width=100)
        self.dataset_table.column("gender", width=100)
        self.dataset_table.column("dob", width=100)
        self.dataset_table.column("age", width=100)
        self.dataset_table.column("address", width=100)
        self.dataset_table.column("photosample", width=100)

        self.dataset_table.pack(fill=BOTH, expand=1)
        self.dataset_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


# function declaration \
    def add_data(self):
        if self.var_name.get() == "" or self.var_id.get() == "" or self.var_email.get() == "":
            messagebox.showerror(
                "error", "all field are reqired", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="2412", database="face_rec")
                my_curser = conn.cursor()
                my_curser.execute("insert into dataset values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_id.get(),
                    self.var_email.get(),
                    self.var_mobileNo.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_age.get(),
                    self.var_address.get(),
                    self.var_radio1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "suceess", "dataset details have been submited", parent=self.root)
            except Exception as es:
                print(str(es))
                messagebox.showerror(
                    "error", f"due to :{str(es)}", parent=self.root)


# ************************ fetch data **************


    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", user="root", password="2412", database="face_rec")
        my_curser = conn.cursor()
        my_curser.execute("select * from dataset")
        data = my_curser.fetchall()

        if len(data) != 0:
            self.dataset_table.delete(*self.dataset_table.get_children())
            for i in data:
                self.dataset_table.insert("", END, values=i)
            conn.commit()
        conn.close()

# ****** get update *************
    def get_cursor(self, event=""):
        cursor_focus = self.dataset_table.focus()
        content = self.dataset_table.item(cursor_focus)
        data = content["values"]

        self.var_name.set(data[1]),
        self.var_id.set(data[2]),
        self.var_email.set(data[3]),
        self.var_mobileNo.set(data[4]),
        self.var_gender.set(data[5]),
        self.var_dob.set(data[6]),
        self.var_age.set(data[7]),
        self.var_address.set(data[8]),
        self.var_radio1.set(data[9])


# update button

    def update_data(self):
        if self.var_name.get() == "" or self.var_id.get() == "" or self.var_email.get() == "":
            messagebox.showerror(
                "error", "all field are reqired", parent=self.root)
        else:
            try:
                update = messagebox.askyesno(
                    "update", "DO you want to update update", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", user="root", password="2412", database="face_rec")
                    my_curser = conn.cursor()
                    my_curser.execute("update dataset set name='" + self.var_name.get() + "',email='" + self.var_email.get() + "',mobileNo='" + self.var_mobileNo.get() + "',gender='" + self.var_gender.get(
                    ) + "',dob='" + self.var_dob.get() + "',age='" + self.var_age.get() + "',address='" + self.var_address.get() + "',photosample='" + self.var_radio1.get() + "' where id='" + self.var_id.get() + "'")

                else:
                    if not update:
                        return
                messagebox.showinfo(
                    "success", "details updated successfully !", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "error", f"due To{str(es)}", parent=self.root)


# delete button fuction ........

    def delete_data(self):
        if self.var_id == "":
            messagebox.showerror(
                "Error", "id must be rrequired", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "delete data", "Do you want yo delete thissa data", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", user="root", password="2412", database="face_rec")
                    my_curser = conn.cursor()
                    my_curser.execute(
                        "delete from dataset where id='" + self.var_id.get() + "'")

                else:
                    if not delete:
                        return
                messagebox.showinfo(
                    "success", "details delated successfully !", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror(
                    "error", f"due To{str(es)}", parent=self.root)

 # ************** RESET ********************

    def reset_data(self):
        self.var_name.set("")
        self.var_id.set("")
        self.var_email.set("")
        self.var_mobileNo.set("")
        self.var_gender.set("select gender")
        self.var_dob.set("")
        self.var_age.set("")
        self.var_address.set("")
        self.var_radio1.set("")


# ********* Genrate data set or take photo sampoles *****************

    def genrate_dataset(self):
        if self.var_name.get() == "" or self.var_id.get() == "" or self.var_email.get() == "":
            messagebox.showerror(
                "error", "all field are reqired", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="2412", database="face_rec")
                my_curser = conn.cursor()
                my_curser.execute("select * from dataset")
                myresult = my_curser.fetchall()
                id =  self.var_id.get()
                
                my_curser.execute("update dataset set name='" + self.var_name.get() + "',email='" + self.var_email.get() + "',mobileNo='" + self.var_mobileNo.get() + "',gender='" + self.var_gender.get(
                ) + "',dob='" + self.var_dob.get() + "',age='" + self.var_age.get() + "',address='" + self.var_address.get() + "',photosample='" + self.var_radio1.get() + "' where id='" + self.var_id.get() + "'")
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

          # load predifined data on face
                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scalling fctor = 1.3
                    # minimum neighbor = 5

                    for(x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + \
                            str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("cropped face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo(
                    "successs", "data taken succefully", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    "error", f"due To{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Dataset(root)
    root.mainloop()
