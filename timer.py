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

frame1 = Frame(root)
frame1.pack()
myTimeLabel = Label(frame1, text="Enter the time (HH:MM:SS)", width=25, anchor="e")
myTimeInputH = ttk.Combobox(frame1, values=varH, width=2, validate="key", validatecommand=(validate, "%P"))
myTimeInputH.current(0)
myTimeInputMin = ttk.Combobox(frame1, values=varMin, width=2, validate="key", validatecommand=(validate, "%P"))
myTimeInputMin.current(0)
myTimeInputSec = ttk.Combobox(frame1, values=varSec, width=2, validate="key", validatecommand=(validate, "%P"))
myTimeInputSec.current(0)

myTimeLabel.pack(side="left")
myTimeInputH.pack(side="left")
myTimeInputMin.pack(side="left")
myTimeInputSec.pack(side="left")

frame2 = Frame(root)
frame2.pack()
taskLabel = Label(frame2, text="Enter task to do",width=25, anchor="e")
taskInput = Entry(frame2)
taskLabel.pack(side="left")
taskInput.pack(side="left")

# Label for countdown and task
countdownLabel = Label(root, text="", font=(20))
timesUpLabel = Label(root, text="")
countdownLabel.pack()
timesUpLabel.pack()


button0 = Button(root, text="OK", command=Timer).pack()

root.mainloop()
