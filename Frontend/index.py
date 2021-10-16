from tkinter.ttk import Progressbar
from tkinter import *
from tkinter import ttk
import os
import login  


w=Tk()
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))


w.overrideredirect(1)

s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#00fc0d')
progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate')

# import main file
def new_win():
  os.system('python login.py')


# progress bar
def bar():
    loading_label=Label(w,text='Loading...',fg='white',bg=a,font=('Calibri (Body)',10)).place(x=18,y=210)

    import time
    r=0
    for i in range(100):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.03)
        r=r+1
    
    w.destroy()
    new_win()
        
    
progress.place(x=-10,y=235)


# Frame
a='#010240'
Frame(w,width=427,height=241,bg=a).place(x=0,y=0)  #249794
b1=Button(w,width=10,height=1,text='Get Started',command=bar,border=0,fg=a,bg='white').place(x=170,y=200)

# Labels

l1=Label(w,text='SUPERIOR SECURITY',fg='#fff',bg=a,font=('times new romen', 20,'bold')).place(x=50,y=80)
l2=Label(w,text='Face Recognition Based Security System ',fg='#fff',bg=a,font=('times new romen', 10,'bold italic')).place(x=70,y=110)

# close window
w.mainloop()