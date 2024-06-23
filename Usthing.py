# Import all needed modules
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox

# set up UI
window = Tk()
window.config(bg='lightgrey')
window.title("Login")
window.geometry('500x500')
window.resizable(0,0)



# Setup / constants / small functions
placeholder_pin = StringVar()

placeholder_user = StringVar()

placeholder_user_lower = (placeholder_user.get()).lower()

global file_path
file_path = 'secrets.txt'


def mainpage_window():
    global window2
    window2 = Toplevel(window)
    window2.config(bg='lightgrey')
    window2.title("MainPage")
    window2.geometry('800x500')
    window2.resizable(0,0)
    window.destroy()
    secondindowUI()
    
    
    

#signing in process

def sign_in_Step1():
    with open(file_path, 'r') as file:
        x_pin = str(placeholder_pin.get())
        x_user = str(placeholder_user.get())
        indexthing = 0
        for count, element in enumerate(file.readlines()):
            print(count,element)
            indexthing += 1
            if x_user in str(element) and x_pin in str(element):
                print("The right password for lou has been entered")
                login_user_step2(x_user)
                break
            elif x_user in str(element) and x_pin in str(element):
                print("The right password for lewis has been entered")
                login_user_step2(x_user)
                break
            elif indexthing == 2:
                messagebox.showerror("Error", "Wrong username or password!")
            else:
                print("an error accured")
        
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
        x2 = x
        count = 0
        # while x2 != 0:
        #     x2 //= 10
        #     count += 1
        if len(str(x)) != 4:
            Exception(TypeError)
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


def login_user_step2(username):
    if username == "Lou" or "lou":
        messagebox.showinfo("Hello", f"Welcome {username}. You have been logged in!") 
        mainpage_window()
    elif username == "Lewis" or "lewis":    
        messagebox.showinfo("Hello", f"Welcome {username}. You have been logged in!") 
        mainpage_window()
        

# Score
def show_scores():
    pass

def scoressearch():
    pass


# Percentage
def show_percentages():
    pass






# Threshold






# Average Percentage



# Main Code!

#Student search function
def student_search():
    student_id = "?"
    student_Lname = "?"
    search = str(placeholder_user.get())
    user = str(placeholder_user.get())
    file_path = f"students_{user}.txt"
    with open(file_path, 'r') as file:
        linesnum = file.readlines()
        if str(search) not in file.read():
            messagebox.showerror("Error", "Invalid student name or ID")
        elif str(search) in file.read():
            for count,element in enumerate(linesnum):
                if search in linesnum[count]:
                    messagebox.showinfo("Student Found!", f"ID: {student_id}\n Last Name: {student_Lname}")
                    continue
    
                
                
# Second window set up UI
student_search_entry = StringVar()
def secondindowUI():
    avg_percent = 10
    #scores setup
    scores_label = Label(window2, text = 'Student Scores:', font = ('calibre',15)).grid(column=1,row=1, pady=10,padx=5)
    scores_btn = Button(window2, text = 'Show', command = show_scores).grid(column=1,row=2,padx=10,pady=5)
    
    #percentage setup
    percentage_label = Label(window2, text = 'Student Percentages:', font = ('calibre',15)).grid(column=4,row=1, pady=10,padx=5)
    percentage_btn = Button(window2, text = 'Show', command = show_percentages).grid(column=4,row=2,padx=10,pady=5)
    avg_percentage_label = Label(window2, text = f'Average Percentage: {avg_percent}', font = ('calibre',10)).grid(column=4,row=8, pady=5,padx=5)
    
    #student search
    scores_label = Label(window2, text = 'Student Search:', font = ('calibre',15)).grid(column=8,row=1, pady=10,padx=5)
    scoressearch_entry = Entry(window2, textvariable = student_search_entry).grid(column=8,row=2)
    scoressearch_btn = Button(window2, text = 'Search', command = student_search).grid(column=8,row=3)


# FINAL set up UI
userlabel = Label(window, text = 'Username:', font = ('calibre',10,'bold')).pack(pady=10)
userwentry = Entry(window, textvariable = placeholder_user).pack()
passlabel = Label(window, text = 'Pin:', font = ('calibre',10,'bold')).pack(pady=10)
passwentry = Entry(window, textvariable = placeholder_pin).pack()
signin_btn = Button(window, text = 'Sign in', command = check_pin).pack(pady=20)


# Mainloop
mainloop()