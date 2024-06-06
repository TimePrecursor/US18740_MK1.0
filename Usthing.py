# Import all needed modules
import tkinter.ttk as ttk
from tkinter import *


# set up UI
window = Tk()
window.config(bg='lightgrey')
window.title("Calculator")
window.geometry('500x500')
window.resizable(0,0)



# Setup / constants / small functions
placeholder_pin = IntVar()

placeholder_user = StringVar()



def sign_in():
    pass


def read_file(): 
    global content, file_path
    file_path = 'secrets.txt'
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        f = open("secrets.txt", "x")
        f.close()


def writeto_file():
    read_file()
    user_info = (f"Pin: {placeholder_pin.get()} | User: {placeholder_user.get()}")
    content_to_uplaod = (f"{content}\n{user_info}")
    try:
        with open(file_path, 'w') as file:
            file.write(content_to_uplaod)
    except FileNotFoundError:
        print("File can't be made.")


# Password and Username functions


def check_username():
    writeto_file()
    try:
        with open(file_path, 'r') as file:
            x = "lol"
            linesnum = file.readlines()
            for count, element in enumerate(linesnum):
                if x in element:
                    print(f"FOUND YA {x}, YOU WERE IN LINE {count}")
    except:
        print("lol")
# Score





# Percentage






# Threshold






# Average Percentage





# FINAL set up UI


passlabel = Label(window, text = 'Pin:', font = ('calibre',10,'bold')).pack(pady=10)
passwentry = Entry(window, textvariable = placeholder_pin, show = '*').pack()

userlabel = Label(window, text = 'Username:', font = ('calibre',10,'bold')).pack(pady=10)
userwentry = Entry(window, textvariable = placeholder_user).pack()

signin_btn = Button(window, text = 'Sign in', command = check_username).pack(pady=20)




# Mainloop
window.mainloop()