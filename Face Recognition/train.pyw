import tkinter
from tkinter  import*
from tkinter import ttk
from  PIL import Image,ImageTk
import os 
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
from playsound import playsound 


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train dataset")
        self.root.iconbitmap('icon.ico')
    

        title_lbl=Label(self.root,text="Train Data Set",font=("times new romen",25,"bold"),bg="black",fg='white')
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img4=Image.open(r"img\home_icon.png")
        img4=img4.resize((40,40),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(title_lbl,image=self.photoimg4,bd=0,cursor="hand2", command=root.destroy)
        b1.place(x=5,y=0)

        # background image
        img=Image.open(r"img\train_bg.jpg")
        img=img.resize((1530,745),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=45,width=1530,height=745)



        img8=Image.open(r"img\train.png")
        img8=img8.resize((440,440),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        
        # button 
        train_data=Button(bg_img,command=self.train_classifier,bd=0,image=self.photoimg8)
        train_data.place(x=500,y=50,width=440,height=440)

        train_data2=Button(bg_img,command=self.train_classifier,bd=0,text="TRAIN DATA",font=("regular 400",25,"bold"),bg="black",fg='white')
        train_data2.place(x=600,y=490)



    def train_classifier(self):
                data_dir=("data")
                path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

                faces=[]
                ids=[]

                for image in path:
                    img=Image.open(image).convert("L") #gray scale image
                    imageNp=np.array(img,'uint8')
                    id=int(os.path.split(image)[1].split('.')[1])

                    faces.append(imageNp)
                    ids.append(id)
                    cv2.imshow("Training",imageNp)
                    cv2.waitKey(1)==13  # press enter to close window
                
                # Train the claassifier and save *

                clf=cv2.face.LBPHFaceRecognizer_create()
                clf.train(faces,np.array(ids))
                clf.write("classifier.xml")
                cv2.destroyAllWindows()
                messagebox.showinfo("result","Training Dataset completed !!",parent=self.root)
            
      





if __name__ =="__main__":
        root = Tk()
        obj=Train(root)
        root.mainloop()