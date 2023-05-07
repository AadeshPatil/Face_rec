import tkinter
from tkinter import*
from tkinter import ttk
import os
from PIL import Image, ImageTk
from train import Train
from dataset import Dataset
from unauthorised import Unautharise
from face_recognition import face_recognition
from attendance import Records
from chatbot import Chatbot
from tkinter import messagebox
import mysql.connector
from playsound import playsound
from time import strftime
from datetime import datetime
import datetime as dt


class Face_Recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Superior Security")
        self.root.iconbitmap('icon.ico')

        self.var = IntVar()
        # navbar img
 # img1
        img = Image.open(r"img\facialrecognition.jpeg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
# img2
        title_lbl = Label(self.root, text="SUPERIOR SECURITY", font=(
            "times new romen", 25, "bold"), bg="black", fg='white')
        title_lbl.place(x=450, y=0, width=500, height=130)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=("digital-7 mono",
                    30, "bold"), bg="black", fg='white')
        lbl.place(x=140, y=85)
        time()

# img3
        img2 = Image.open(r"img\facialrecognition - Copy.jpeg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=900, y=0, width=500, height=130)

# bg image
        bg_img = Label(self.root, bg="#0da697")
        bg_img.place(x=0, y=130, width=1530, height=710)


# dataset
        img4 = Image.open(r"img\dataset.jpg")
        img4 = img4.resize((220, 200), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, bd=0,
                    cursor="hand2", command=self.dataset)
        b1.place(x=100, y=10, width=220, height=200)

        b1 = Button(bg_img, text="Dataset", cursor="hand2", bd=0, command=self.dataset, font=(
            "times new romen", 15, "bold"), bg="#090954", fg="white")
        b1.place(x=100, y=200, width=220, height=40)

# detect face
        img5 = Image.open(r"img\face_detector.jpg")
        img5 = img5.resize((220, 200), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2",
                    bd=0, command=self.face_recognition)
        b1.place(x=400, y=10, width=220, height=200)

        b1 = Button(bg_img, text="Face Detecter", cursor="hand2", bd=0, command=self.face_recognition, font=(
            "times new romen", 15, "bold"), bg="#090954", fg="white")
        b1.place(x=400, y=200, width=220, height=40)

# REcords
        img6 = Image.open(r"img\records.jpeg")
        img6 = img6.resize((220, 200), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2",
                    bd=0, command=self.attendance)
        b1.place(x=700, y=10, width=220, height=200)

        b1 = Button(bg_img, text="Records", command=self.attendance, bd=0, cursor="hand2", font=(
            "times new romen", 15, "bold"), bg="#090954", fg="white")
        b1.place(x=700, y=200, width=220, height=40)


# help
        img7 = Image.open(r"img\help.jpg")
        img7 = img7.resize((220, 200), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, bd=0,
                    cursor="hand2", command=self.help_desk)
        b1.place(x=1000, y=10, width=220, height=200)

        b1 = Button(bg_img, text="Help Desk", cursor="hand2", bd=0, command=self.help_desk, font=(
            "times new romen", 15, "bold"), bg="#090954", fg="white")
        b1.place(x=1000, y=200, width=220, height=40)

# train
        img8 = Image.open(r"img\train_data.jpg")
        img8 = img8.resize((220, 200), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8,
                    command=self.train_data, bd=0, cursor="hand2")
        b1.place(x=100, y=300, width=220, height=200)

        b1 = Button(bg_img, text="Train Data", cursor="hand2", bd=0, command=self.train_data, font=(
            "times new romen", 15, "bold"), bg="#090954", fg="white")
        b1.place(x=100, y=500, width=220, height=40)

# Unauthorised Access
        img9 = Image.open(r"img\un_access.jpeg")
        img9 = img9.resize((220, 200), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, bd=0,
                    command=self.open_unaut, cursor="hand2")
        b1.place(x=400, y=300, width=220, height=200)

        b1 = Button(bg_img, text="Unauthorised Access", bd=0, cursor="hand2", command=self.open_unaut, font=(
            "times new romen", 15, "bold"), bg="#090954", fg="white")
        b1.place(x=400, y=500, width=220, height=40)

# Reset system
        img10 = Image.open(r"img\restart.jpeg")
        img10 = img10.resize((220, 200), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, bd=0,
                    command=self.Reset_system, cursor="hand2")
        b1.place(x=700, y=300, width=220, height=200)

        b1 = Button(bg_img, text="Restart System", bd=0, cursor="hand2", command=self.Reset_system, font=(
            "times new romen", 15, "bold"), bg="#090954", fg="white")
        b1.place(x=700, y=500, width=220, height=40)
# exit
        img11 = Image.open(r"img\exit.jpg")
        img11 = img11.resize((220, 200), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, bd=0,
                    command=self.exit, cursor="hand2")
        b1.place(x=1000, y=300, width=220, height=200)

        b1 = Button(bg_img, text="Exit", cursor="hand2", bd=0, command=self.exit, font=(
            "times new romen", 15, "bold"), bg="#090954", fg="white")
        b1.place(x=1000, y=500, width=220, height=40)

    def dataset(self):
        self.new_window = Toplevel(self.root)
        self.app = Dataset(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_recognition(self):
        self.new_window = Toplevel(self.root)
        self.app = face_recognition(self.new_window)

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Records(self.new_window)

    def help_desk(self):
        self.new_window = Toplevel(self.root)
        self.app = Chatbot(self.new_window)

    def open_unaut(self):
        self.new_window = Toplevel(self.root)
        self.app = Unautharise(self.new_window)

    def exit(self):
        yes = messagebox.askyesno(
            "exit", "Are You Sure You Want To Quit", parent=self.root)
        if yes > 0:
            self.root.destroy()

    def empty(self):
        dir = 'data'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))


# Reset system

    def Reset_system(self):
        self.root2 = Tk()
        self.root2.title("Restart System")
        self.root2.geometry("400x300+480+200")
        self.root2.config(bg="white")
        self.root2.focus_force()
        self.root2.grab_set()
        self.root2.iconbitmap('icon.ico')

        t = Label(self.root2, text="Restart System", font=(
            "times new romen", 20, "bold"), bg="white", fg="red").place(x=0, y=10, relwidth=1)

        # Username
        emial_name = Label(self.root2, text="Username  : ", font=(
            "times new romen", 15, "bold"), bg="white", fg="black").place(x=80, y=80)
        self.txt_anser = Entry(self.root2, font=(
            "times new romen", 15), bg="lightgray")
        self.txt_anser.place(x=80, y=120, width=250)

        # password
        password = Label(self.root2, text=" Password  : ", font=(
            "times new romen", 15, "bold"), bg="white", fg="black").place(x=80, y=160)
        self.password = Entry(self.root2, show="●", font=(
            "times new romen", 15), bg="lightgray")
        self.password.place(x=80, y=200, width=250)

        # pw_hide_show
        bt = Checkbutton(self.root2, command=self.mark,
                         offvalue=0, onvalue=1, variable=self.var)
        bt.place(x=335, y=200)

        # reset btn
        btn_reset = Button(self.root2, text="Restart System", command=self.forget_ps,
                           cursor="hand2", font=("times new romen", 12, "bold"), bg="green", fg="white")
        btn_reset.place(x=90, y=240, width=140)


# password hide show function


    def mark(self):

        if self.var.get() == 1:
            self.password.configure(show="")
        elif self.var.get() == 0:
            self.password.configure(show="●")

    def forget_ps(self):
        if self.txt_anser.get() == "" or self.password.get() == "":
            messagebox.showerror(
                "error", "plese enter email adrress & password", parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="2412", database="face_rec")
                my_curser = conn.cursor()
                my_curser.execute("select * from users where email= '" + self.txt_anser.get(
                ) + "' and password = '" + self.password.get() + "' ")
                row = my_curser.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Plese enter valid Email & Password to Restart your System !", parent=self.root2)

                else:

                    delete = messagebox.askyesno(
                        "Reset Data", "Do you want yo Delete Your Data ?", parent=self.root2)
                    if delete > 0:
                        conn = mysql.connector.connect(
                            host="localhost", user="root", password="2412", database="face_rec")
                        my_curser = conn.cursor()
                        my_curser.execute("TRUNCATE TABLE dataset")
                        messagebox.showinfo(
                            "Succefully", "Your system has been Reset succefully", parent=self.root2)
                        playsound("audio/restart_system.mp3")
                        conn.commit()
                        conn.close()
                        self.empty()
                        self.root2.destroy()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root2)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_system(root)
    root.mainloop()
