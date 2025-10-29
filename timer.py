import os
import sys
import time
import winsound
from tkinter import *
from tkinter import ttk

stoped = False
currentTime = 0

root = Tk()
root.title("Remind Me After")

def OnlyNum(timeInput):
    return timeInput.isdigit() or timeInput == ""

validate = root.register(OnlyNum)

def StartTimer():
    global currentTime, stoped
    
    myTime = int(myTimeInputH.get())*3600 + int(myTimeInputMin.get())*60 + int(myTimeInputSec.get())
    task = taskInput.get().upper()

    
    if myTime == 0 and currentTime == 0:
        timesUpLabel.config(text="Timer must be greater than 0!")
    elif currentTime > 0:
        myTime = currentTime
    
    if myTime > 0:
        stoped = False
        startButton.config(state=DISABLED)
        stopButton.config(state=NORMAL)
        resetButton.config(state=NORMAL)
        timesUpLabel.config(text="")
        
        for i in range(myTime, -1, -1):
            if stoped == True:
                currentTime = i
                break
            
            seconds = i % 60
            mins = int(i / 60) % 60
            hours = int(i / 3600)
            
            countdownLabel.config(text=f"{hours:02}:{mins:02}:{seconds:02}")
            root.update()
            time.sleep(1)
            
            if task == "" and i == 0:
                timesUpLabel.config(text="TIME'S UP!!!")
                # winsound.PlaySound('alarm-clock.wav', winsound.SND_FILENAME)
                currentTime=0
            elif i == 0:
                timesUpLabel.config(text=f"IT'S TIME TO {task} NOW!!!")
                # winsound.PlaySound('alarm-clock.wav', winsound.SND_FILENAME)
                currentTime=0
        root.update()
        startButton.config(state=NORMAL)


def StopTimer():
    global stoped
    stopButton.config(state=DISABLED)
    startButton.config(state=NORMAL)
    stoped = True
    
    
def ResetTimer():
    os.execv(sys.executable, ['python'] + sys.argv)


varMinSec = [f"{i:02d}" for i in range(60)]
varH = [f"{i:02d}" for i in range(24)]

frame = Frame(root)
frame.pack()
myTimeInput = Frame(frame)
myTimeInput.grid(row=0, column=1, padx=20, pady=10)

myTimeLabel = Label(frame, text="Enter the time (HH:MM:SS)",width=25)
myTimeInputH = ttk.Combobox(myTimeInput, values=varH, width=3, validate="key", validatecommand=(validate, "%P"))
myTimeInputH.current(0)
myTimeInputMin = ttk.Combobox(myTimeInput, values=varMinSec, width=3, validate="key", validatecommand=(validate, "%P"))
myTimeInputMin.current(0)
myTimeInputSec = ttk.Combobox(myTimeInput, values=varMinSec, width=3, validate="key", validatecommand=(validate, "%P"))
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

buttonFrame = Frame(root)
buttonFrame.pack()
startButton = Button(buttonFrame, text="Start", command=StartTimer, width=10)
stopButton = Button(buttonFrame, text="Stop", command=StopTimer, width=10)
resetButton = Button(buttonFrame, text="Reset", command=ResetTimer, width=10)
startButton.grid(row=0, column=0)
stopButton.grid(row=0, column=1, padx=15, pady=10)
resetButton.grid(row=0, column=2)

stopButton.config(state=DISABLED)
resetButton.config(state=DISABLED)

root.mainloop()
