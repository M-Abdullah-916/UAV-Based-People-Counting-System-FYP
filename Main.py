import tkinter
import time
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
import Image_Stitching

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

def splashScreen():

    progressBar.start(20)
    for x in range(5):
        progressBar['value'] += 20
        splashWindow.update_idletasks()
        time.sleep(1)

def mainWindow():
    splashWindow.destroy()
    main = Tk()
    main.title('UAV-BASED PEOPLE COUNTING SYSTEM')
    main.iconbitmap('Logo.ico')
    main.minsize(1000, 700)
    main.maxsize(1000, 700)
    main.geometry('1000x700')

    main.configure(background='#0FB5DA')

    logo = Image.open('Logo.PNG')
    resized_logo = logo.resize((310, 130))
    logo = ImageTk.PhotoImage(resized_logo)
    logo_label = Label(main, image=logo, background='#0FB5DA')
    logo_label.pack(pady=(10, 10))

    text_logo = Label(main, text='UAV-Based People Counting System', fg='white', bg='#0FB5DA')
    text_logo.config(font=('verdana', 24))
    text_logo.pack()

    add_image_button = Button(main, text='Add Images', command=addImage, bg='white', fg='black', width=30, height=2)
    add_image_button.pack(pady=(15, 5))

    manage_drone_button = Button(main, text='Provide Coordinates to Drone', command=manageDrone, bg='white', fg='black', width=30, height=2)
    manage_drone_button.pack(pady=(5, 5))

    collate_image_button = Button(main, text='Collate Images', command=imageCollation, bg='white', fg='black', width=30,
                                  height=2)
    collate_image_button.pack(pady=(5, 5))

    history_button = Button(main, text='Check History', command=checkHistory, bg='white', fg='black', width=30,
                            height=2)
    history_button.pack(pady=(5, 5))

    exit_button = Button(main, text='Exit', command=main.destroy, bg='white', fg='black', width=30, height=2)
    exit_button.pack(pady=(5, 5))

    main.mainloop()

def selectFolder():
    folder_name = filedialog.askdirectory(initialdir="/", title="Select a Folder")
    if folder_name != "":
        stitching_object = Image_Stitching.stichImages(folder_name)
        stitching_object.stiching()


def imageCollation():
    collate = tkinter.Toplevel()
    collate.title('UAV-BASED PEOPLE COUNTING SYSTEM')
    collate.iconbitmap('Logo.ico')
    collate.minsize(1000, 700)
    collate.maxsize(1000, 700)
    collate.geometry('1000x700')

    collate.configure(background='#0FB5DA')

    logo = Image.open('Logo.PNG')
    resized_logo = logo.resize((310, 130))
    logo = ImageTk.PhotoImage(resized_logo)
    logo_label = Label(collate, image=logo, background='#0FB5DA')
    logo_label.pack(pady=(10, 10))

    text_logo = Label(collate, text='UAV-Based People Counting System', fg='white', bg='#0FB5DA')
    text_logo.config(font=('verdana', 24))
    text_logo.pack()

    folder_label = Label(collate, text='Open a Folder', bg='#0FB5DA', fg='black')
    folder_label.config(font=('verdana', 16))
    folder_label.pack(pady=(20, 10))
    browse_button = Button(collate, text='Browse a Folder', command=selectFolder, bg='white', fg='black', width=20, height=2)
    browse_button.pack(pady=(5, 5))

    exit_button = Button(collate, text='Exit', command=collate.destroy, bg='white', fg='black', width=20, height=2)
    exit_button.pack(pady=(5, 5))

    collate.mainloop()

def addImage():
    print("TBD")

def manageDrone():
    print("TBD")

def checkHistory():
    print("TBD")

def exitSystem():
    print("TBD")


if __name__ == '__main__':
    splashScreen()
    splashWindow.after(3500, mainWindow)
    mainloop()

