from tkinter import *
from tkinter import Tk
from tkinter import DISABLED
from tkinter import messagebox
import sys

# set up UI
global active_window_list
active_window_list = []
window = Tk()
window.config(bg='lightgrey')
window.title("Login")
window.geometry('500x500')
window.resizable(0,0)
active_window_list.append("window")

# Setup / constants / small functions
global placeholder_pin
placeholder_pin = IntVar()
placeholder_user = StringVar()



global file_path
file_path = 'secrets.txt'

def closeapplication1():
    try:
        if window.winfo_exists():    
            window.destroy()
            active_window_list.pop(0)
    except:
        print("error1")
    try:
        if window2.winfo_exists():    
            window2.destroy()
            indexlol = active_window_list.index("window2")
            active_window_list.pop(indexlol)
    except:
        print("error2")
    sys.exit()
    
def closeapplication2():
    pass
    
def mainpage_window():
    global signin_btn
    signin_btn.config(state=DISABLED)
    global window2
    active_window_list.append("window2")
    window2 = Toplevel()
    window2.config(bg='lightgrey')
    window2.title("MainPage")
    window2.geometry('800x500')
    window2.resizable(0,0)
    window.withdraw()  # Close the login window
    secondindowUI(placeholder_user.get())

# signing in process
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
            elif indexthing == 3:
                messagebox.showerror("Error", "Wrong username or password!")
            else:
                print("an error occurred")

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
    user_info = (f" User: {placeholder_user.get().lower()} | Pin: {placeholder_pin.get()}")
    content_to_upload = (f"{content}\n{user_info}")
    try:
        with open(file_path, 'w') as file:
            file.write(content_to_upload)
    except FileNotFoundError:
        print("File can't be made.")

# Password and Username functions
def check_username():
    try:
        with open(file_path, 'r') as file:
            y = placeholder_user.get()
            linesnum = file.readlines()
            for count, element in enumerate(linesnum):
                if y in element:
                    print(f"FOUND YA {y}, YOU WERE IN LINE {count}")
                    check_pin()
                elif y not in element:
                    messagebox.showerror("Error", "User not found!") 
    except:
        print("ez")



def convert_to_int(x=placeholder_pin.get()):
    try:
        string_value = x  # Get the value from the StringVar
        int_value = int(string_value)    # Convert the string value to an integer
        if len(str(x)) != 4:
            raise TypeError
        return False
    except ValueError:
        return True

def check_pin():
    global placeholder_pin
    x = placeholder_pin.get()
    print(x)
    lol2 = True
    while lol2:     
        try:
            if convert_to_int(x) is True:
                raise TypeError
            elif convert_to_int(x) is False:
                pass
        except:
            messagebox.showerror("Error", "Invalid pin type.")
            break
        else:
            lol2 = False
            sign_in_Step1()

# the actual login function that splits the user to two different databases
def login_user_step2(username):
    if username.lower() in ["lou", "lewis"]:
        messagebox.showinfo("Hello", f"Welcome {username}. You have been logged in!") 
        mainpage_window()
    else:
        messagebox.showerror("Error", "Invalid username!")

# Score
def show_scores():
    pass

def scoressearch():
    pass

# Percentage
def show_percentages():
    pass

# Student search function
def student_search():
    student_id = "?"
    student_Lname = "?"
    search = str(student_search_entry.get())
    user = str(placeholder_user.get())
    file_path = f"students_{user}.txt"
    with open(file_path, 'r') as file:
        students = file.readlines()
        students = [student.strip() for student in students]  # Remove any leading/trailing whitespace
        if search not in students:
            messagebox.showerror("Error", "Invalid student name or ID")
        elif search in students:
            for count,element in enumerate(students):
                if search in students[count]:
                    messagebox.showinfo("Student Found!", f"ID: {student_id}\n Last Name: {student_Lname}")
                    continue
            
            
            
            
            

       

# Second window set up UI
student_search_entry = StringVar()
def secondindowUI(current_user):
    avg_percent = 10
    #scores setup
    scores_label = Label(window2, text='Student Scores:', font=('calibre', 15)).grid(column=1, row=1, pady=10, padx=5)
    scores_btn = Button(window2, text='Show', command=show_scores).grid(column=1, row=2, padx=10, pady=5)
    
    #percentage setup
    percentage_label = Label(window2, text='Student Percentages:', font=('calibre', 15)).grid(column=4, row=1, pady=10, padx=5)
    percentage_btn = Button(window2, text='Show', command=show_percentages).grid(column=4, row=2, padx=10, pady=5)
    avg_percentage_label = Label(window2, text=f'Average Percentage: {avg_percent}', font=('calibre', 10)).grid(column=4, row=8, pady=5, padx=5)
    
    file_path2 = f"students_{current_user}.txt"
    with open(file_path2, 'r') as file:
        number_of_students = len(file.readlines())
    
    #student search
    scores_label = Label(window2, text='Student Search:', font=('calibre', 15)).grid(column=8, row=1, pady=10, padx=5)
    scores_label = Label(window2, text=f"Number of students: {number_of_students}", font=('calibre', 10)).grid(column=8, row=2, pady=10, padx=5)
    scoressearch_entry = Entry(window2, textvariable=student_search_entry).grid(column=8, row=3)
    scoressearch_btn = Button(window2, text='Search', command=student_search).grid(column=8, row=4)
    

    
    #Menu
    menubar = Menu(window2)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New Student")
    filemenu.add_command(label="Leaving Student")
    filemenu.add_command(label="Close", command=lambda: closeapplication1())
    menubar.add_cascade(label="Edit", menu=filemenu)
    helpmenu = Menu(menubar, tearoff=0)
    window2.config(menu=menubar)

    window2.protocol("WM_DELETE_WINDOW", lambda: closeapplication1())

# FINAL set up UI

#Menu
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Close", command=lambda: closeapplication1())
menubar.add_cascade(label="Edit", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
window.config(menu=menubar)

#Main UI
userlabel = Label(window, text='Username:', font=('calibre', 10, 'bold')).pack(pady=10)
userwentry = Entry(window, textvariable=placeholder_user).pack()
passlabel = Label(window, text='Pin:', font=('calibre', 10, 'bold')).pack(pady=10)
passwentry = Entry(window, textvariable=placeholder_pin)
passwentry.pack()
global signin_btn
signin_btn = Button(window, text='Sign in', command=check_pin)
signin_btn.pack(pady=20)
# Ensure the main window closes properly
window.protocol("WM_DELETE_WINDOW", lambda: closeapplication1())

# Mainloop
mainloop()