from tkinter import *
import time
from tkinter import messagebox

root = Tk()
root.geometry("600x500")
root.title("Timer")

hour = StringVar()
hour.set("00")

minute = StringVar()
minute.set("00")

second = StringVar()
second.set("00")

yeah = 0
oh_hello = False 

def submit():
    global yeah, oh_hello
    try:
        yeah = (int(hour.get()) * 3600) + (int(minute.get()) * 60) + int(second.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")
        return

    oh_hello = True

    while yeah > -1 and oh_hello:
        mins, secs = divmod(yeah, 60)
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        hour.set(f"{hours:02d}")
        minute.set(f"{mins:02d}")
        second.set(f"{secs:02d}")
        
        root.update()

        time.sleep(1)

        if yeah == 0 and oh_hello: 
            messagebox.showinfo("Time Countdown", "Time's up")
            break

        yeah -= 1

def reset():
    global yeah, oh_hello
    yeah = 0 
    oh_hello = False  
    hour.set("00")
    minute.set("00")
    second.set("00")

hourEntry = Entry(root, width=3, font=("Arial", 36, "bold"), textvariable=hour)
hourEntry.place(x=80, y=20)

minuteEntry = Entry(root, width=3, font=("Arial", 36, "bold"), textvariable=minute)
minuteEntry.place(x=160, y=20)

secondEntry = Entry(root, width=3, font=("Arial", 36, "bold"), textvariable=second)
secondEntry.place(x=240, y=20)

button = Button(root, text="Set Time Countdown", bd="7", command=submit)
button.place(x=114, y=180)

subway = Button(root, text="Reset Timer", bd="5", command=reset)
subway.place(x=114, y=220)

root.mainloop()
