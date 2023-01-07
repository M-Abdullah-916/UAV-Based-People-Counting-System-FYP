from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import bcrypt
import Main

# Temporary Database
registered_users_emails = []
registered_users_passwords = []
registered_users_hashed_passwords = []
user_index = 0


class Registration:
    def __init__(self):
        self.confirm_password_entry = None
        self.main = None
        self.password_entry = None
        self.email_entry = None
        self.credentials = [0, 0]

    def registration_screen(self):
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
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password == confirm_password:
            # PASSWORD ENCRYPTION
            byte_password = password.encode('utf-8')
            salt = bcrypt.gensalt()
            pwd_hash = bcrypt.hashpw(byte_password, salt)
            password = password.encode('utf-8')
            registered_users_emails.insert(user_index, email)
            registered_users_passwords.insert(user_index, password)
            registered_users_hashed_passwords.insert(user_index, pwd_hash)
            messagebox.showinfo("Message", "Successfully Registered!")
            login_screen = Login()
            self.main.destroy()
            login_screen.login_screen()
        else:
            messagebox.showinfo("Message", "Password Does Not Match!")


class Login:
    def __init__(self):
        self.main = None
        self.password_entry = None
        self.email_entry = None
        self.credentials = [0, 0]

    def login_screen(self):
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

        if email == registered_users_emails.pop() and bcrypt.checkpw(registered_users_passwords.pop(), registered_users_hashed_passwords.pop()):
            self.main.destroy()
            Main.main_window()


if __name__ == '__main__':
    mainloop()