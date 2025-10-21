import time
import winsound


myTime = int(input("Enter the time in second: "))
task = input("Enter task to do: ").upper()
for i in range(int(myTime), 0, -1):
    seconds = i % 60
    mins = int(i / 60) % 60
    hours = int(i / 3600)
    print(f"{hours:02}:{mins:02}:{seconds:02}")
    time.sleep(1)

print(f"IT'S TIME TO {task} NOW!!!")
winsound.PlaySound('alarm-clock.wav', winsound.SND_FILENAME)

# Buat GUI