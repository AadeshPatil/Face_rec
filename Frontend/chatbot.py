from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import time
import datetime
import pyttsx3
from threading import Thread
import requests
from bs4 import BeautifulSoup
import pyttsx3

class Chatbot:
    def __init__(self , root):
        self.root=root
        self.root.title("Chat Bot")
        self.root.config(bg="white")
        self.root.iconbitmap('icon.ico')   
        self.root.geometry("1360x690+-5+0")

      
      
      #BACKGROUND

        # bottom frmae 
        btm_frame=Frame(self.root,bg="#0b002e")
        btm_frame.place(x=0,y=0,relwidth=1,relheight=1)

        
        img4=Image.open(r"img\home_icon.png")
        img4=img4.resize((40,40),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(self.root,image=self.photoimg4,bd=0,cursor="hand2", command=root.destroy)
        b1.place(x=20,y=15)

      # frames 
        
        #right frame
        main_frame2=Frame(btm_frame,bd=2)
        main_frame2.place(x=10,y=10,width=705,height=650)

        img=Image.open("img/chatbot-image.PNG")
        img=img.resize((700,600),Image.ANTIALIAS)  
        self.photoimg1=ImageTk.PhotoImage(img)

        frmae1=Label(main_frame2,image=self.photoimg1,bd=5)
        frmae1.place(x=0,y=0,width=700,height=590)

       
        #left frame
        
        main_frame=Frame(btm_frame,bg="powder blue",)
        main_frame.place(x=730,y=10,width=630,height=500)

        self.srcoll_y=Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=100,height=35,bd=3,bg="powder blue",relief=RAISED,font=('Candara Light', -20,'bold italic'),yscrollcommand=self.srcoll_y)
        self.srcoll_y.pack(side=RIGHT,fill=Y)

        self.text.pack()

        button_frm=Frame(btm_frame,bg="white",width=630)
        button_frm.place(x=730,y=510)

        label_1=Label(button_frm,text="Type Something..",font=('arial',14,'bold'),fg="green",bg="white")
        label_1.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        
        self.entry=StringVar()
        self.entry_box=ttk.Entry(button_frm,textvariable=self.entry,width=18,font=('Candara Light', -25,'bold italic'))
        self.entry_box.grid(row=0,column=1,padx=5,sticky=W)

        self.send_btn=Button(button_frm,text="Send",width=9,command=self.send,font=('arial',15,"bold"),bg="blue",fg="white")
        self.send_btn.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        self.clear_btn=Button(button_frm,text="Clear Data",command=self.clear,width=15,font=('arial',15,"bold"),bg="red",fg="white")
        self.clear_btn.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        self.help_btn=Button(button_frm,text="Options",command=self.help,width=15,font=('arial',15,"bold"),bg="dark blue",fg="white")
        self.help_btn.grid(row=1,column=1,padx=20,pady=5,sticky=W)

        self.msg=""
        self.bot=Label(btm_frame,text=self.msg,font=('Candara Light', -25,'bold italic'),fg="white",bg="#0b002e")
        self.bot.place(x=800, y=620)


        # ******************   function *******************

    def help(self):
        self.entry.set("help")
        self.send()


    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set("")


    def send(self):
            send= '\t\t\t'+ 'You :' + self.entry.get()
            self.text.insert(END,'\n'+send)
            self.text.yview(END)

            if (self.entry.get() == ''):
                self.msg='Please Enter Some Input'
                self.bot.config(text=self.msg,fg='red')

            else :
                self.msg = ''
                self.bot.config(text=self.msg,fg='red')


            if (self.entry.get() == "hello"):
                self.text.insert(END,'\n\n'+ 'Bot: hii, how can i help you ' )
 
            elif (self.entry.get()== "hii"):
                self.text.insert(END,'\n\n'+ 'Bot: hello, how can i help you ' )

            elif (self.entry.get()== "How are you ?"):
                self.text.insert(END,'\n\n'+ 'Bot: Fine , what about you .? ' )

            elif (self.entry.get()== "Fantastic"):
                self.text.insert(END,'\n\n'+ 'Bot: nice to here ' )

            elif (self.entry.get()== "what is your name ?"):
                self.text.insert(END,'\n\n'+ 'Bot: you can call me anything' )
            
            elif (self.entry.get() == "help"):
                self.text.insert(END,'\n\n'+ 'Bot: What kind of help do you need ?, please chose the below option .\nHow to handle system ? \nWhat is in Dataset tab ?\nWhat is in Train Data tab ?\nWhat is in recognize tab ?\nHow record tab work ?')

            elif (self.entry.get()== "How to handle system ?"):
                self.text.insert(END,'\n\n'+ "Bot:  step 1: Crate an database of your employees. & capture their images\n step 2: Now go to Train Data tab and train the image .\n step 3: Hurreyyy...! its done now , just goto recognized tab and see the result.\n step 4: You can check the record in Record tab ." )

            elif (self.entry.get()== "What is in Dataset tab ?"):
                self.text.insert(END,'\n\n'+ "Bot: Its take an details with photos of your emplyee and store them in database ."  )

            elif (self.entry.get()== "What is in  Train Data tab ?"):
                self.text.insert(END,'\n\n'+ "Bot: Its convert the images into an easy alogorithm that computer can easily understad and recognised your face " )

            elif (self.entry.get()== "What is in  recognize tab ?"):
                self.text.insert(END,'\n\n'+ "Bot: After Training data the system make an alogorithm of your face , with the help of that alogorithm system recognise the correct face " )

            elif (self.entry.get()== "How record tab work ?"):
                self.text.insert(END,'\n\n'+ "Bot: When employee succefully recognised by alogorithm , its take the details of the emplye and store it in excel sheet with date and time .")


            elif (self.entry.get()== "Bye"):
                self.text.insert(END,'\n\n'+ 'Bot: Thank your reaching toward us 😊. Feel free to ask anything ' )
                
            else :
                self.text.insert(END, "\n\n" + " Bot : sorry i didn't get it ")




if __name__ =="__main__":
        root = Tk()
        obj=Chatbot(root)
        root.mainloop()
