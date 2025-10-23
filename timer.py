import time
import winsound
from tkinter import *

root = Tk()
root.title("Remind Me After")

frame1 = Frame(root)
frame1.pack()
myTimeLabel = Label(frame1, text="Enter the time in second: ", width=20, anchor="e")
myTimeInput = Entry(frame1)
myTimeLabel.pack(side="left")
myTimeInput.pack(side="left")

frame2 = Frame(root)
frame2.pack()
taskLabel = Label(frame2, text="Enter task to do: ",width=20, anchor="e")
taskInput = Entry(frame2)
taskLabel.pack(side="left")
taskInput.pack(side="left")

# Label for countdown and task
countdownLabel = Label(root, text="", font=(20))
timesUpLabel = Label(root, text="")
countdownLabel.pack()
timesUpLabel.pack()

def Timer():
    myTime = int(myTimeInput.get())
    task = taskInput.get().upper()

    for i in range(myTime, 0, -1):
        seconds = i % 60
        mins = int(i / 60) % 60
        hours = int(i / 3600)
        
        countdownLabel.config(text=f"{hours:02}:{mins:02}:{seconds:02}")
        root.update()
        time.sleep(1)

    timesUpLabel.config(text=f"IT'S TIME TO {task} NOW!!!")
    root.update()
    # winsound.PlaySound('alarm-clock.wav', winsound.SND_FILENAME)

button0 = Button(root, text="OK", command=Timer).pack()

root.mainloop()
