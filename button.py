from tkinter import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
buttonPin=11

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

win = Tk()

def ledON():
    while True:
        if GPIO.input(11) == 1:
            ledButton["bg"] = "green"
        else:
            ledButton["bg"] = "red"

#I tried to use button widget in DISABLED state as a Indicator
ledButton = Button(win, text = " ON  ", command = ledON,state=DISABLED, height = 2, width =8,bg="red")
ledButton.pack()

mainloop()
