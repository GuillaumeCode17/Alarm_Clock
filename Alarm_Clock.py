import time
import threading
from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from pygame import mixer

root = Tk()
root.title("YTD(-Youtube-) 📺 Downloader 📺")
root.geometry("700x900")  # set window
root.columnconfigure(0, weight=1)  # set all content in center.
root.config(background="black")
# root.iconbitmap("Youtube.ico")
root.resizable(False, False)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
LINKED_STARTED = True
mixer.init()


def clock():
    clock_time = time.strftime("%H:%M:%S %p")
    current_time.config(
        text=f"Current Time : {clock_time}", font="Times 17")
    current_time.after(500, clock)


def th():
    t1 = threading.Thread(target=a, args=())
    t1.start()
    
def a():
    a = AlarmSet.get()
    if a == "":
        msg = messagebox.showerror(
            'Invalid data', 'Please enter valid time | Example ( 15:45 )')
    else:
        Alarmtime = a
        CurrentTime = time.strftime("%H:%M")

        while Alarmtime != CurrentTime:
            CurrentTime = time.strftime("%H:%M")

        if Alarmtime == CurrentTime:
            mixer.music.load('Bird01.mp3')
            mixer.music.play()
            msg = messagebox.showinfo('It is time', f'{amsg.get()}')
            if msg == 'ok':
                mixer.music.stop()


# Labels Zone ==========================================================|

# Top Image
first_img = PhotoImage(file="./Images/Alarm01.png")
my_img = Label(root, image=first_img, width=800, height=300, bg="black")
my_img.grid(row=0, column=0, pady=(10, 0), padx=5)


# btn to set alarm time
SetTime = Button(root, width=10, bg="red", fg="white",
                 text="Set Time", command=th, padx=10, pady=5, cursor="hand2")
SetTime.grid(row=5, column=0, padx=10, pady=10)

AlarmSet = Entry(root, insertbackground="white", font=("comic sans", 20),
                 width=5, bg="black", fg="white", border=10)
AlarmSet.grid(row=6, column=0, padx=10, pady=10)


try:  # Pop up confirmation alarm warning
    amessage = Label(root, text="Message", font=(
        'comic sans', 20), bg="black", fg="white")
    amessage.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    amsg = Entry(root, font=('comic sans', 15),
                 width=25, bg="black", fg="white", insertbackground="white", border=10)
    amsg.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
except:
    pass

try:  # Current Time Label and # developer Label
    # Current Time Label
    current_time = Label(root, font="arial 15 bold",
                         text="", fg="white", bg="black", padx=5)
    current_time.grid(row=1, column=0, pady=10)

    # developer Label
    developerlabel = Label(root, text="This App was build by Guillaume", font=(
        "jost", 15), bg="black", fg="white", padx=10, pady=5)
    developerlabel.grid(row=12, column=0, padx=10, pady=10)
except:
    pass

clock()
root.mainloop()
