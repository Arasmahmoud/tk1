from datetime import datetime , date
from tinydb import TinyDB ,Query
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import shutil
import time
text_bg = "darkblue"
text_color = "white"
text_font = 'tajawal','15','bold'

db = TinyDB("/home/aras/vscode/qamishlo/invoc.json")
current_time =str(date.today())




root = Tk()
root.title("shop")
root.config(bg="white")
root.geometry('850x500+270+120')
root.resizable('false', 'false')


s1 = Frame(root,width=850,height=150,bg="darkblue")
s1.pack(side="top")

saction_title = Label(s1,text="SHOP",bg="darkblue",fg="white",font=('tajawal','20','bold'))
saction_title.place(x=350,y=5)


id_label = Label(s1,text="TOTAL :",bg=text_bg,fg=text_color,font=(text_font))
id_label.place(x=5,y=70)
id_input = Entry(s1,justif='center')
id_input.place(x=105,y=74)

id_label2 = Label(s1,text="EXPENSES :",bg=text_bg,fg=text_color,font=(text_font))
id_label2.place(x=300,y=70)
id_input2 = Entry(s1,justif='center')
id_input2.place(x=450,y=74)


def send():
    all = int(id_input.get())
    used = int(id_input2.get())
    db.insert({"all":all,"used":used,"date":current_time})
    id_input.delete(0,END)
    id_input2.delete(0,END)




def total():
    num = 0
    num1 = 0
    res = db.all()
    for i in res :
        num = num + i["all"]
    for i in res :
        num1 = num1 + i["used"]

    m_total.config(text=f"Month Total : {num}")
    m_ex.config(text=f"Month Expen : {num1}")
    m_time.config(text=current_time)
    

def cleardb():
    shutil.copy("invoc.json",f"{current_time}.json")
    db.truncate()
    m_total.config(text="")
    m_ex.config(text="")
    m_time.config(text="")
    m_get['state'] = 'normal'
    



sub_bu = Button(s1,text="CONFIRM",width=14,bg="white",font=('tajawal','10','bold'),command=send)
sub_bu.place(x=670,y=70)

m1 = Label(root,text="Details of Month",bg="white",fg="darkblue",font=('tajawal','20','bold'))
m1.place(x=290,y=160)

m_total = Label(root,bg="white",fg="darkblue",font=(text_font))
m_total.place(x=300,y=250)

m_ex = Label(root,bg="white",fg="darkblue",font=(text_font))
m_ex.place(x=300,y=300)

m_time = Label(root,bg="white",fg="darkblue",font=(text_font))
m_time.place(x=340,y=350)

m_get = Button(root,text="GET",width=12,bg="darkblue",fg="white",font=('tajawal','12','bold'),command=total)
m_get.place(x=450,y=450)

m_cl = Button(root,text="CLEAR",width=12,bg="darkblue",fg="white",font=('tajawal','12','bold'),command=cleardb)
m_cl.place(x=250,y=450)


image1 = PhotoImage(file='logo.png')

mypic = Label(root,image=image1)
mypic.place(x=0,y=465)

root.mainloop()