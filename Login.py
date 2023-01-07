import tkinter
import time
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image


class Registration:
    def __init__(self):
        self.temp = "HELLO"


class Login:
    def __init__(self):
        self.temp = "HELLO"

    def login_screen(self):
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

        email_label = Label(main, text='Enter your Email', fg='black', bg='#0FB5DA')
        email_label.config(font=('verdana', 16))
        email_label.pack(pady=(20, 10))

        email_entry = Entry(main)
        email_entry.pack()

        password_label = Label(main, text='Enter your Password', fg='black', bg='#0FB5DA')
        password_label.config(font=('verdana', 16))
        password_label.pack(pady=(10, 10))

        password_entry = Entry(main)
        password_entry.pack()

        add_image_button = Button(main, text='Add Images', command=self.check_credentials, bg='white', fg='black', width=30,
                                      height=2)
        add_image_button.pack(pady=(15, 5))

        main.mainloop()

    def check_credentials(self):
        ds



if __name__ == '__main__':
    print("HELLO")
