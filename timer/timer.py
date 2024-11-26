from tkinter import *
import time
from tkinter import messagebox

root=Tk()
root.geometry("600x500")
root.title("Timer")

hour=StringVar()
hour.set("00")

minute=StringVar()
minute.set("00")

second=StringVar()
second.set("00")

def submit():
    try:
        temp=(int(hour.get())*3600) + (int(minute.get())*60) + (int(second.get()))
    except:
        print("Plz input the right value")
    while temp>-1:
        mins,secs=divmod(temp,60)
        hours=00
        if mins>60:
            hours,mins=divmod(mins,60)

        hour.set("{00:2d}".format(hours))
        minute.set("{00:2d}".format(mins))
        second.set("{00:2d}".format(secs))

        root.update()
        time.sleep(1)

        if(temp==00):
            messagebox.showinfo("Time Countdown","Time's up")

        temp -=1    

def reset():
    pass

#homework

hourEntry=Entry(root,width=3,font=("Arial",36,"bold"),textvariable=hour)
hourEntry.place(x=80,y=20)

minuteEntry=Entry(root,width=3,font=("Arial",36,"bold"),textvariable=minute)
minuteEntry.place(x=160,y=20)

secondEntry=Entry(root,width=3,font=("Arial",36,"bold"),textvariable=second)
secondEntry.place(x=240,y=20)

button=Button(root,text="Set Time Countdown",bd="7",command=submit)
button.place(x=114,y=180)

subway=Button(root,text="Reset Timer",bd="5",command=reset)
subway.place(x=114,y=220)



root.mainloop()