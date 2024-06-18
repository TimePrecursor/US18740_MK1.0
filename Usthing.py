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
placeholder_pin = StringVar()

placeholder_user = StringVar()

placeholder_user_lower = (placeholder_user.get()).lower()

global file_path
file_path = 'secrets.txt'


def sign_in_Step1():
    with open(file_path, 'r') as file:
        x_pin = str(placeholder_pin.get())
        x_user = str(placeholder_user.get())
        linesnum = file.readlines()
        print(linesnum)
        indexlol = 0
        for count, element in enumerate(linesnum):
            print(count,element)
            if x_user in element and (x_pin in element):
                print(f"{x_pin} is the right password for {placeholder_user.get()}")
                login_user2(x_user)
        
            # if x in element:
            #     print(f"{x} is the right password for {placeholder_user.get()}")
            # else:
            #     messagebox.showerror("Error", "Invalid pin for this user.") 


def read_file(): 
    global content
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        f = open("secrets.txt", "x")
        f.close()


def writeto_file():
    read_file()
    user_info = (f" User: {placeholder_user_lower} | Pin: {placeholder_pin.get()}")
    content_to_uplaod = (f"{content}\n{user_info}")
    try:
        with open(file_path, 'w') as file:
            file.write(content_to_uplaod)
    except FileNotFoundError:
        print("File can't be made.")


# Password and Username functions

def check_username():
    # writeto_file()
    try:
        with open(file_path, 'r') as file:
            x = placeholder_user.get()
            linesnum = file.readlines()
            for count, element in enumerate(linesnum):
                if x in element:
                    print(f"FOUND YA {x}, YOU WERE IN LINE {count}")
                    check_pin()
                else:
                    messagebox.showerror("Error", "User not found!") 
    except:
        print("ez")


def check_pin():
    x = placeholder_pin.get()
    print(x)
    try:
        y = int(x)+2
        # y2 = str(x).split()
        # print(len(y2))
        # if len(y2) != 4:
        #     raise Exception(TypeError)
    except:
        messagebox.showerror("Error", "Invalid pin type.") 
    else:
        sign_in_Step1()
        
        # boolx = len(str(x)) != 4
        # if boolx == True:
        #     messagebox.showerror("error", "Please enter a valid pin (four digits)") 
        # elif boolx == False:
        #     check_username()


# the actual login function that splits the user to two different databases
def login_user2(username):
    if username == "Lou" or "lou":
        pass
        
    elif username == "Lewis" or "lewis":    
        pass
        

# Score





# Percentage






# Threshold






# Average Percentage





# FINAL set up UI
userlabel = Label(window, text = 'Username:', font = ('calibre',10,'bold')).pack(pady=10)
userwentry = Entry(window, textvariable = placeholder_user).pack()

passlabel = Label(window, text = 'Pin:', font = ('calibre',10,'bold')).pack(pady=10)
passwentry = Entry(window, textvariable = placeholder_pin).pack()


signin_btn = Button(window, text = 'Sign in', command = check_pin).pack(pady=20)




# Mainloop
window.mainloop()