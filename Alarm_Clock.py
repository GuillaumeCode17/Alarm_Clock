import time
import threading
from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from pygame import mixer

try:  # Initialization of the labels ( root=Tk... )
    root = Tk()
    root.title("Alarm Clock Version 1 Beta")
    root.geometry("700x900")  # set window
    root.columnconfigure(0, weight=1)  # set all content in center.
    root.config(background="black")
    # root.iconbitmap("Youtube.ico")
    root.resizable(False, False)
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    mixer.init()
    Current_Alarm_State = True
except:
    pass

# Functions Zone =======================================================|


def motion(event):  # Function To Track Mouse Position for Devloppement only
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))


def Only_Two_Entry():  # Only two entry function for the Alarm's time setup
    if len(HourSet.get()) > 1:
        HourSet.delete(2, END)

    if len(MinuteSet.get()) > 1:
        MinuteSet.delete(2, END)

    if len(SecondSet.get()) > 1:
        SecondSet.delete(2, END)
    root.after(200, Only_Two_Entry)


def clock():  # Simple Clock Function
    clock_time = time.strftime("%H:%M:%S %p")
    current_time.config(
        text=f"Current Time : {clock_time}", font="Times 17")
    current_time.after(500, clock)


def th():  # Set Alarm Function into Threading
    t1 = threading.Thread(target=a, args=())
    t1.start()


def a():  # Set Alarm Function
    Current_Alarm_State = False
    AlarmTime = ""
    a = (HourSet.get()+":"+MinuteSet.get()+":"+SecondSet.get())
    if a == "":
        msg = messagebox.showerror(
            'Invalid data', 'Please enter valid time | Example ( 15:45 )')
    else:
        AlarmTime = a
        CurrentTime = time.strftime("%H:%M:%S %p")
        SetTime.config(bg="green")
        AlarmSetLabel.config(text="Time's Set to : \n" +
                             AlarmTime+" ⏰", fg="green")
        Current_Alarm_State = True

        if AlarmTime != CurrentTime:
            while Current_Alarm_State:
                CurrentTime = time.strftime("%H:%M:%S")
                if AlarmTime == CurrentTime:
                    mixer.music.load("./Alarm01.mp3")
                    mixer.music.play(loops=2)
                    msg = messagebox.showinfo('Time is up !', f'{amsg.get()}')
                    if msg == 'ok':
                        mixer.music.stop()
                        SetTime.config(bg="red")
                        AlarmSetLabel.config(text="")
                        Current_Alarm_State = False


# Labels Zone ==========================================================|
# Top Image
first_img = PhotoImage(file="./Images/Alarm01.png")
my_img = Label(root, image=first_img, width=800, height=300, bg="black")
my_img.grid(row=0, column=0, pady=(10, 0), padx=5)

try:  # Pop up confirmation alarm warning
    amessage = Label(root, text="Message", font=(
        'comic sans', 20), bg="black", fg="white")
    amessage.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    amsg = Entry(root, font=('comic sans', 15),
                 width=25, bg="black", fg="white", insertbackground="white", border=10)
    amsg.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
except:
    pass

# btn to set alarm time
SetTime = Button(root, width=10, bg="red", fg="white",
                 text="Set Time", command=th, padx=10, pady=5, cursor="hand2")
SetTime.grid(row=5, column=0, padx=10, pady=10)

AlarmSetLabelMsg = Label(root, text="Enter Alarm's Time \n Format e.g. \n(15:45:15) = 15 Heures 45 Minutes and 15 Secondes",
                         fg="white", font=("Times", 20), bg="black")
AlarmSetLabelMsg.grid(row=8, column=0, pady=10)

try:  # Alarm Time Set by User
    HourSet = Entry(root, insertbackground="white", font=("comic sans", 20),
                    width=2, bg="black", fg="white", border=10)
    HourSet.place(x=202, y=665)

    TwoPointsLabel = Label(root, text=':', fg="red",
                           font=("comic sans", 20), bg="black")
    TwoPointsLabel.place(x=282, y=670)

    MinuteSet = Entry(root, insertbackground="white", font=("comic sans", 20),
                      width=2, bg="black", fg="white", border=10)
    MinuteSet.place(x=322, y=665)

    TwoPointsLabel = Label(root, text=':', fg="red",
                           font=("comic sans", 20), bg="black")
    TwoPointsLabel.place(x=402, y=670)

    SecondSet = Entry(root, insertbackground="white", font=("comic sans", 20),
                      width=2, bg="black", fg="white", border=10)
    SecondSet.place(x=442, y=665)
except:
    pass

AlarmSetLabel = Label(root, text="", bg="black",
                      fg="white", font=("Times", 20))
AlarmSetLabel.place(x=510, y=430)

try:  # Current Time Label and # developer Label
    # Current Time Label
    current_time = Label(root, font="arial 15 bold",
                         text="", fg="white", bg="black", padx=5)
    current_time.grid(row=1, column=0, pady=10)

    # developer Label
    developerlabel = Label(root, text="This App was build by Guillaume.\n\n Made WIth Python3", font=(
        "jost", 14), bg="black", fg="white", padx=10, pady=5)
    developerlabel.grid(row=12, column=0, padx=10, pady=(100, 10))
except:
    pass

Only_Two_Entry()
clock()
root.bind('<Motion>', motion)
root.mainloop()
