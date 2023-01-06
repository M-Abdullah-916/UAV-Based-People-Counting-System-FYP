import string
import tkinter
import time
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

splashWindow = Tk()
splashWindow.configure(background='#0FB5DA')

appWidth = 720
appHeight = 680
screenWidth = splashWindow.winfo_screenwidth()
screenHeight = splashWindow.winfo_screenheight()

xCoordinates = (screenWidth / 2) - (appWidth / 2)
yCoordinates = (screenHeight / 2) - (appHeight / 2)

splashWindow.overrideredirect(True)
splashWindow.geometry(f'{appWidth}x{appHeight}+{int(xCoordinates)}+{int(yCoordinates)}')
splashBackground = PhotoImage(file="Logo.png")
pictureLabel = Label(splashWindow, image=splashBackground, bg='#0FB5DA')
pictureLabel.place(x=0, y=0, relwidth=1, relheight=1)

progressBar = ttk.Progressbar(splashWindow, orient=HORIZONTAL, length=300, mode='determinate')
progressBar.place(x=170, y=450, relwidth=0.5, relheight=0.05)


def progress():
    progressBar.start(20)
    for x in range(5):
        progressBar['value'] += 20
        splashWindow.update_idletasks()
        time.sleep(1)


if __name__ == '__main__':
    print('Main Created')

