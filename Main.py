import tkinter
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

import Add_Images_From_Video
import Image_Stitching
from tkinter import messagebox


def main_window():
    main = Tk()
    main.title('UAV-BASED PEOPLE COUNTING SYSTEM')
    main.iconbitmap('Logo.ico')
    main.minsize(1000, 700)
    main.maxsize(1000, 700)
    main.geometry('1000x700')
    custom_font = ("Times", 14, 'bold')

    main.configure(background='#0FB5DA')

    logo = Image.open('Logo.PNG')
    resized_logo = logo.resize((310, 130))
    logo = ImageTk.PhotoImage(resized_logo)
    logo_label = Label(main, image=logo, background='#0FB5DA')
    logo_label.pack(pady=(10, 10))

    text_logo = Label(main, text='UAV-Based People Counting System', fg='black', bg='#0FB5DA')
    text_logo.config(font=('verdana', 24))
    text_logo.pack()

    add_image_button = Button(main, text='Add Images', font=custom_font, command=add_image, bg='black', fg='white',
                              width=30, height=2)
    add_image_button.pack(pady=(45, 5))

    manage_drone_button = Button(main, text='Provide Coordinates to Drone', font=custom_font, command=manage_drone,
                                 bg='black', fg='white', width=30, height=2)
    manage_drone_button.pack(pady=(5, 5))

    collate_image_button = Button(main, text='Collate Images', font=custom_font, command=image_collation, bg='black',
                                  fg='white', width=30, height=2)
    collate_image_button.pack(pady=(5, 5))

    history_button = Button(main, text='Check History', font=custom_font, command=check_history, bg='black', fg='white',
                            width=30, height=2)
    history_button.pack(pady=(5, 5))

    exit_button = Button(main, text='Exit', command=main.destroy, font=custom_font, bg='black', fg='white', width=30,
                         height=2)
    exit_button.pack(pady=(5, 5))

    main.mainloop()


def select_video():
    extracting_images = Add_Images_From_Video.ExtractImages()
    extracting_images.extraction()


def select_images():
    folder_name = filedialog.askdirectory(initialdir="/", title="Select a Folder")
    if folder_name != "":
        stitching_object = Image_Stitching.ImageCollation(folder_name)
        stitching_object.stitching()
    else:
        return 0


def image_collation():
    collate = tkinter.Toplevel()
    collate.title('UAV-BASED PEOPLE COUNTING SYSTEM')
    collate.iconbitmap('Logo.ico')
    collate.minsize(1000, 700)
    collate.maxsize(1000, 700)
    collate.geometry('1000x700')
    custom_font = ("Times", 14, 'bold')

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
    folder_label.pack(pady=(50, 10))
    browse_button = Button(collate, text='Browse a Folder', command=select_images, font=custom_font, bg='black',
                           fg='white', width=20, height=2)
    browse_button.pack(pady=(5, 5))

    exit_button = Button(collate, text='Exit', command=collate.destroy, font=custom_font, bg='black', fg='white',
                         width=20, height=2)
    exit_button.pack(pady=(15, 5))

    collate.mainloop()


def add_image():
    extract = tkinter.Toplevel()
    extract.title('UAV-BASED PEOPLE COUNTING SYSTEM')
    extract.iconbitmap('Logo.ico')
    extract.minsize(1000, 700)
    extract.maxsize(1000, 700)
    extract.geometry('1000x700')
    custom_font = ("Times", 14, 'bold')

    extract.configure(background='#0FB5DA')

    logo = Image.open('Logo.PNG')
    resized_logo = logo.resize((310, 130))
    logo = ImageTk.PhotoImage(resized_logo)
    logo_label = Label(extract, image=logo, background='#0FB5DA')
    logo_label.pack(pady=(10, 10))

    text_logo = Label(extract, text='UAV-Based People Counting System', fg='white', bg='#0FB5DA')
    text_logo.config(font=('verdana', 24))
    text_logo.pack()

    folder_label = Label(extract, text='Extract Images from Video', bg='#0FB5DA', fg='black')
    folder_label.config(font=('verdana', 16))
    folder_label.pack(pady=(50, 10))
    browse_button = Button(extract, text='Click to Start Process', command=lambda: [select_video(), extract.destroy()],
                           font=custom_font, bg='black', fg='white', width=20, height=2)
    browse_button.pack(pady=(5, 5))

    exit_button = Button(extract, text='Exit', command=extract.destroy, font=custom_font, bg='black', fg='white',
                         width=20, height=2)
    exit_button.pack(pady=(15, 5))

    extract.mainloop()


def manage_drone():
    messagebox.showinfo("Message", "Functionality Under Development.")


def check_history():
    messagebox.showinfo("Message", "Functionality Under Development.")


if __name__ == '__main__':
    mainloop()
