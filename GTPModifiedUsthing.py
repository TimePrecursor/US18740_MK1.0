from tkinter import *
from tkinter import Tk
from tkinter import DISABLED
from tkinter import messagebox
import sys
import random

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
def set_new_scores():
    filelines1 = []
    user = str(placeholder_user.get())
    file_path1 = f"students_{user}.txt"
    with open(file_path1, 'r') as f:
        for line1 in f.readlines():
            x = line1.replace("scores", f"{random.randint(0, 100)}")
            filelines1.append(x)
    with open(file_path1, 'w') as f:
        for y in filelines1:
            f.write(f"{y}")
    filelines1.clear()



def averg_percentages():
    percent = []
    num = 0
    user = str(placeholder_user.get())
    file_path1 = f"students_{user}.txt"
    with open(file_path1, 'r') as file:
        for line in file.readlines():
            x = line.split("|")
            percent.append(x[2])
    for x in percent:
        y = x.replace("%", "", 2)
        num += int(y)
    return num/len(percent)

def averg_scores():
    score = []
    num = 0
    user = str(placeholder_user.get())
    file_path1 = f"students_{user}.txt"
    with open(file_path1, 'r') as file:
        for line in file.readlines():
            x = line.split("|")
            score.append(x[1])
    for x in score:
        num += int(x)
    return num/len(score)


# Percentage
def set_new_percentages():
    filelines1 = []
    user = str(placeholder_user.get())
    file_path1 = f"students_{user}.txt"
    with open(file_path1, 'r') as f:
        for line1 in f.readlines():
            x = line1.replace("percent", f"%{random.randint(0, 100)}%")
            filelines1.append(x)
    with open(file_path1, 'w') as f:
        for y in filelines1:
            f.write(f"{y}")
    filelines1.clear()



def check_threshholds_2(x):
    if x < 60:
        return str("Not Achieved")
    elif x >= 60:
        return str("Achieved")

def check_threshholds():
    filelines1 = []
    user = str(placeholder_user.get())
    file_path1 = f"students_{user}.txt"
    with open(file_path1, 'r') as f:
        for line1 in f.readlines():
            percent1 = line1.split("%")
            int_x = percent1[1].replace("%","")
            percent1 = int(int_x)
            x = line1.replace("thresh", f'{check_threshholds_2(percent1)}')
            filelines1.append(x)
    with open(file_path1, 'w') as f:
        for y in filelines1:
            f.write(f"{y}")
    filelines1.clear()

# Student search functions

def student_search_window(name, type):
    searchwindow = Toplevel()
    searchwindow.config(bg='lightgrey')
    searchwindow.title("Student Search Window")
    searchwindow.geometry('800x500')
    searchwindow.resizable(0,1)
    if type == "1":
        search_label = Label(searchwindow, text=f"Student Scores:\n {name}", font=('calibre', 15))
        search_label.pack()
    elif type == "2":
        search_label = Label(searchwindow, text=f"Student Percentages:\n {name}", font=('calibre', 15))
        search_label.pack()
    elif type == "3":
        search_label = Label(searchwindow, text=f"Student Thresholds:\n {name}", font=('calibre', 15))
        search_label.pack()
    elif type == 0:
        search_label = Label(searchwindow, text=f"Student(s) Found:\n {name}", font=('calibre', 15))
        search_label.pack()



def student_search(type):
    score = []
    percent = []
    thresh = []
    search = str(student_search_entry.get())
    user = str(placeholder_user.get())
    student_list = []
    students = []
    file_path = f"students_{user}.txt"

    with open(file_path, 'r') as file:
        for line in file.readlines():
            x = line.split("|")
            students.append(f"{x[0]}")
            score.append(f"{x[0]}{(x[1])}")
            percent.append(f"{x[0]}{(x[2])}")

        if type == 0:
            for count,stud in enumerate(students):
                if search in stud:
                    if search in students[count]:
                        student_list.append(students[count])
                elif search not in stud:
                    pass

        if type == 5:
            for line in file.readlines():
                x = line.split("|")
                score.append(x[1])


        if type == 5:
            for line in file.readlines():
                x = line.split("|")
                percent.append(x[2])
            for count,stud in enumerate(percent):
                if search in stud:
                    if search in students[count]:
                        student_list.append(students[count])
                elif search not in stud:
                    pass


    lololo = '\n'.join(students)
    lololo1 = '\n'.join(score)
    lololo2 = '\n'.join(percent)
    lololo3 = '\n'.join(thresh)

    if type == 1:
        student_search_window(lololo1, "1")
    elif type == 2:
        student_search_window(lololo2, "2")
    elif type == 3:
        student_search_window(lololo3, "3")
    else:
        student_search_window(lololo, 0)
            
            
            
            

       

# Second window set up UI
student_search_entry = StringVar()
def secondindowUI(current_user):
    #scores setup
    scores_label = Label(window2, text='Student Scores:', font=('calibre', 15)).grid(column=1, row=1, pady=10, padx=5)
    scores_btn = Button(window2, text='Show', command=lambda: student_search(1)).grid(column=1, row=2, padx=10, pady=5)
    avg_percentage_label = Label(window2, text=f'Average Score: {averg_scores()}', font=('calibre', 10)).grid(column=1, row=8, pady=5, padx=5)
    #scores_btn2 = Button(window2, text='Gen Rand Scores (ADMIN)', command=set_new_scores).grid(column=1, row=50, padx=10, pady=5)
    
    #percentage setup
    percentage_label = Label(window2, text='Student Percentages:', font=('calibre', 15)).grid(column=4, row=1, pady=10, padx=5)
    percentage_btn = Button(window2, text='Show', command=lambda: student_search(2)).grid(column=4, row=2, padx=10, pady=5)
    avg_percentage_label = Label(window2, text=f'Average Percentage: {averg_percentages()}', font=('calibre', 10)).grid(column=4, row=8, pady=5, padx=5)
    #percentage_btn2 = Button(window2, text='Gen Rand Percentages (ADMIN)', command=set_new_percentages).grid(column=4, row=50, padx=10, pady=5)
    #percentage_btn3 = Button(window2, text='Set Passed or not (ADMIN)', command=check_threshholds).grid(column=4, row=60, padx=10, pady=5)
    file_path2 = f"students_{current_user}.txt"
    with open(file_path2, 'r') as file:
        number_of_students = len(file.readlines())
    
    #student search
    scores_label = Label(window2, text='Student Search:', font=('calibre', 15)).grid(column=8, row=1, pady=10, padx=5)
    scores_label = Label(window2, text=f"Number of students: {number_of_students}", font=('calibre', 10)).grid(column=8, row=2, pady=10, padx=5)
    scoressearch_entry = Entry(window2, textvariable=student_search_entry).grid(column=8, row=3)
    scoressearch_btn = Button(window2, text='Search', command= lambda: student_search(0)).grid(column=8, row=4)
    

    
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