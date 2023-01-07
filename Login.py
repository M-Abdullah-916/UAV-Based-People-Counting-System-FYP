from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import bcrypt
import time
import Main

# Temporary Database
registered_users_emails = []
registered_users_passwords = []

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


def splash_screen():
    progressBar.start(20)
    for x in range(5):
        progressBar['value'] += 20
        splashWindow.update_idletasks()
        time.sleep(1)


class Registration:
    def __init__(self):
        self.confirm_password_entry = None
        self.main = None
        self.password_entry = None
        self.email_entry = None
        self.credentials = [0, 0]

    def registration_screen(self):
        splashWindow.destroy()
        self.main = Tk()
        self.main.title('UAV-BASED PEOPLE COUNTING SYSTEM')
        self.main.iconbitmap('Logo.ico')
        self.main.minsize(1000, 700)
        self.main.maxsize(1000, 700)
        self.main.geometry('1000x700')

        self.main.configure(background='#0FB5DA')

        logo = Image.open('Logo.PNG')
        resized_logo = logo.resize((310, 130))
        logo = ImageTk.PhotoImage(resized_logo)
        logo_label = Label(self.main, image=logo, background='#0FB5DA')
        logo_label.pack(pady=(10, 10))

        text_logo = Label(self.main, text='UAV-Based People Counting System', fg='white', bg='#0FB5DA')
        text_logo.config(font=('verdana', 24))
        text_logo.pack()

        email_label = Label(self.main, text='Enter your Email', fg='black', bg='#0FB5DA')
        email_label.config(font=('verdana', 20))
        email_label.pack(pady=(60, 10))

        self.email_entry = Entry(self.main)
        self.email_entry.config(width=50)
        self.email_entry.pack()

        password_label = Label(self.main, text='Enter your Password', fg='black', bg='#0FB5DA')
        password_label.config(font=('verdana', 20))
        password_label.pack(pady=(30, 10))

        self.password_entry = Entry(self.main)
        self.password_entry.config(width=50)
        self.password_entry.pack()

        password_label = Label(self.main, text='Confirm your Password', fg='black', bg='#0FB5DA')
        password_label.config(font=('verdana', 20))
        password_label.pack(pady=(30, 10))

        self.confirm_password_entry = Entry(self.main)
        self.confirm_password_entry.config(width=50)
        self.confirm_password_entry.pack()

        add_image_button = Button(self.main, text='Register', command=self.add_user, bg='white', fg='black',
                                  width=30,
                                  height=2)
        add_image_button.config(font=('verdana', 11), border=10)
        add_image_button.pack(pady=(60, 5))

        self.main.mainloop()

    def add_user(self):
        print("TEMP")


class Login:
    def __init__(self):
        self.main = None
        self.password_entry = None
        self.email_entry = None
        self.credentials = [0, 0]

    def login_screen(self):
        splashWindow.destroy()
        self.main = Tk()
        self.main.title('UAV-BASED PEOPLE COUNTING SYSTEM')
        self.main.iconbitmap('Logo.ico')
        self.main.minsize(1000, 700)
        self.main.maxsize(1000, 700)
        self.main.geometry('1000x700')

        self.main.configure(background='#0FB5DA')

        logo = Image.open('Logo.PNG')
        resized_logo = logo.resize((310, 130))
        logo = ImageTk.PhotoImage(resized_logo)
        logo_label = Label(self.main, image=logo, background='#0FB5DA')
        logo_label.pack(pady=(10, 10))

        text_logo = Label(self.main, text='UAV-Based People Counting System', fg='white', bg='#0FB5DA')
        text_logo.config(font=('verdana', 24))
        text_logo.pack()

        email_label = Label(self.main, text='Enter your Email', fg='black', bg='#0FB5DA')
        email_label.config(font=('verdana', 20))
        email_label.pack(pady=(80, 10))

        self.email_entry = Entry(self.main)
        self.email_entry.config(width=50)
        self.email_entry.pack()

        password_label = Label(self.main, text='Enter your Password', fg='black', bg='#0FB5DA')
        password_label.config(font=('verdana', 20))
        password_label.pack(pady=(30, 10))

        self.password_entry = Entry(self.main)
        self.password_entry.config(width=50)
        self.password_entry.pack()

        add_image_button = Button(self.main, text='Login', command=self.check_credentials, bg='white', fg='black',
                                  width=30,
                                  height=2)
        add_image_button.config(font=('verdana', 11), border=10)
        add_image_button.pack(pady=(80, 5))

        self.main.mainloop()

    def check_credentials(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        # PASSWORD ENCRYPTION
        byte_password = password.encode('utf-8')
        salt = bcrypt.gensalt()
        pwd_hash = bcrypt.hashpw(byte_password, salt)
        password = password.encode('utf-8')

        if email == "yes" and bcrypt.checkpw(password, pwd_hash):
            self.main.destroy()
            Main.main_window()


if __name__ == '__main__':
    splash_screen()
    # login_object = Login()
    registration_object = Registration()
    splashWindow.after(3500, registration_object.registration_screen())
