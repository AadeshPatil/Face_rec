import tkinter
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog

class face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face_recognition")
        self.root.iconbitmap('icon.ico')

        title_lbl = Label(self.root, text="Face Recognition", font=(
            "times new romen", 25, "bold"), bg="darkblue", fg='white')
        title_lbl.place(x=0, y=0, width=1530, height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('digital-7 mono', 30, 'bold'),
                    bg="darkblue", fg='white')
        lbl.place(x=70, y=0)
        time()

        img4 = Image.open(r"img\home_icon.png")
        img4 = img4.resize((40, 40), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(title_lbl, image=self.photoimg4, bd=0,
                    cursor="hand2", command=root.destroy)
        b1.place(x=5, y=0)

        # background image
        img = Image.open(r"img\fr.jpg")
        img = img.resize((1530, 700), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=45, width=1530, height=700)

        rec = Button(bg_img, text="By Camera", command=self.face_recog, font=(
            "times new romen", 20, "bold"), bg="white", fg="blue")
        rec.place(x=160, y=145, width=350, height=60)
        photo = Button(bg_img, text="By Photo", command=self.face_recog_from_image, font=(
            "times new romen", 20, "bold"), bg="white", fg="blue")
        photo.place(x=600, y=145, width=350, height=60)

# **Atttendance
    def my_attendnce(self, i, n, e, a):
        with open("record.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split((","))
                nameList.append(entry[0])
            if((i not in nameList) and (n not in nameList) and (e not in nameList) and (a not in nameList)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{e},{dtString},{d1}")

    # face recognition function

    def face_recog_from_image(self):
        def drow_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="localhost", user="root", password="2412", database="face_rec")
                my_curser = conn.cursor()

                my_curser.execute("select name from dataset where id=" + str(id))
                n = my_curser.fetchone()
                n = "+".join(n)

                my_curser.execute("select email from dataset where id=" + str(id))
                e = my_curser.fetchone()
                e = "+".join(e)

                my_curser.execute("select age from dataset where id=" + str(id))
                a = my_curser.fetchone()
                a = "+".join(a)

                my_curser.execute("select id from dataset where id=" + str(id))
                i = my_curser.fetchone()
                i = "+".join(i)

                if confidence > 60:
                    cv2.putText(img, f"ID: {i}", (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 25, 255), 1)
                    cv2.putText(img, f"Name: {n}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 25, 255), 1)
                    cv2.putText(img, f"Email: {e}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 25, 255), 1)
                    cv2.putText(img, f"Age: {a}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 25, 255), 1)
                    self.my_attendnce(i, n, e, a)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 1)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = drow_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades, "haarcascade_frontalface_default.xml"))
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        # image_path = input("Enter the path to the image file: ")
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open Image",filetypes=(("open Image","*.jpg"),("All file","*.*")),parent=self.root)
        if fln:
            with open(fln) as myfile:
                file_path = myfile.name
                img = cv2.imread(file_path)
                # img = cv2.imread("image.jpg")
                height, width, _ = img.shape
                if img is not None:
                    original_height, original_width, _ = img.shape
                    aspect_ratio = original_width / original_height
                    max_display_width = 800  # Maximum allowed width for the displayed image
                    max_display_height = 600  # Maximum allowed height for the displayed image

                    # Calculate new width and height while maintaining the aspect ratio
                    display_width = min(original_width, max_display_width)
                    display_height = int(display_width / aspect_ratio)
                    if display_height > max_display_height:
                        display_height = max_display_height
                        display_width = int(display_height * aspect_ratio)

                    img = recognize(img, clf, faceCascade)
                    resized_img = cv2.resize(img, (display_width, display_height))
                    cv2.imshow("FACE RECOGNITION", resized_img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                else:
                    print("Invalid image file.")


    def face_recog(self):
        def drow_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    host="localhost", user="root", password="2412", database="face_rec")
                my_curser = conn.cursor()

                my_curser.execute("select name from dataset where id="+str(id))
                n = my_curser.fetchone()
                n = "+".join(n)

                my_curser.execute(
                    "select email from dataset where id="+str(id))
                e = my_curser.fetchone()
                e = "+".join(e)

                my_curser.execute("select age from dataset where id="+str(id))
                a = my_curser.fetchone()
                a = "+".join(a)

                my_curser.execute("select id from dataset where id="+str(id))
                i = my_curser.fetchone()
                i = "+".join(i)

                if confidence > 80:
                    cv2.putText(
                        img, f"ID:{i}", (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 25, 255), 1)
                    cv2.putText(
                        img, f"Name:{n}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 25, 255), 1)
                    cv2.putText(
                        img, f"Email:{e}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 25, 255), 1)
                    cv2.putText(
                        img, f"Age:{a}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 25, 255), 1)
                    self.my_attendnce(i, n, e, a)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown", (x, y-55),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 1)

                coord = [x, y, w, h]

            return coord

        def recogize(img, clf, faceClasscade):
            coord = drow_boundray(img, faceClasscade, 1.1,
                                  10, (255, 25, 255), "Face", clf)
            return img

        faceClasscade = cv2.CascadeClassifier(os.path.join(
            cv2.data.haarcascades, "haarcascade_frontalface_default.xml"))
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while True:
            ret, img = video_cap.read()
            img = recogize(img, clf, faceClasscade)
            cv2.imshow("FACE RECOGNITION", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = face_recognition(root)
    root.mainloop()
