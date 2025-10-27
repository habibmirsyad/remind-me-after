import time
import winsound
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Remind Me After")

def OnlyNum(timeInput):
    return timeInput.isdigit() or timeInput == ""

validate = root.register(OnlyNum)

def Timer():
    myTime = int(myTimeInputH.get())*3600 + int(myTimeInputMin.get())*60 + int(myTimeInputSec.get())
    task = taskInput.get().upper()

    if myTime <= 0:
        timesUpLabel.config(text="Timer must be greater than 0!")
    else:
        timesUpLabel.config(text="")
        for i in range(myTime, -1, -1):
            seconds = i % 60
            mins = int(i / 60) % 60
            hours = int(i / 3600)
            
            countdownLabel.config(text=f"{hours:02}:{mins:02}:{seconds:02}")
            root.update()
            time.sleep(1)

        if task == "":
            timesUpLabel.config(text="TIME'S UP!!!")
        else:
            timesUpLabel.config(text=f"IT'S TIME TO {task} NOW!!!")
        root.update()
        # winsound.PlaySound('alarm-clock.wav', winsound.SND_FILENAME)


varSec = [f"{i:02d}" for i in range(60)]
varMin = [f"{i:02d}" for i in range(60)]
varH = [f"{i:02d}" for i in range(24)]

frame = Frame(root)
frame.pack()
myTimeInput = Frame(frame)
myTimeInput.grid(row=0, column=1, padx=20, pady=10)

myTimeLabel = Label(frame, text="Enter the time (HH:MM:SS)",width=25)
myTimeInputH = ttk.Combobox(myTimeInput, values=varH, width=3, validate="key", validatecommand=(validate, "%P"))
myTimeInputH.current(0)
myTimeInputMin = ttk.Combobox(myTimeInput, values=varMin, width=3, validate="key", validatecommand=(validate, "%P"))
myTimeInputMin.current(0)
myTimeInputSec = ttk.Combobox(myTimeInput, values=varSec, width=3, validate="key", validatecommand=(validate, "%P"))
myTimeInputSec.current(0)

myTimeLabel.grid(row=0, column=0)
myTimeInputH.pack(side="left")
myTimeInputMin.pack(side="left")
myTimeInputSec.pack(side="left")

taskLabel = Label(frame, text="Enter task to do",width=25)
taskInput = Entry(frame)
taskLabel.grid(row=1, column=0)
taskInput.grid(row=1, column=1)

# Label for countdown and task
countdownLabel = Label(root, text="", font=(20))
timesUpLabel = Label(root, text="")
countdownLabel.pack()
timesUpLabel.pack()


button0 = Button(root, text="OK", command=Timer).pack()

root.mainloop()
