from tkinter import *
import tkmacosx
from datetime import datetime
import re

# 1 start 
root = Tk()

root.geometry('500x500')
head = Frame(root)
head.pack()

entry = Frame(root)
entry.pack()

# vars and consts 
var = StringVar()
error_message = StringVar()
gender_message = StringVar()
age_message = StringVar()


# submit button + fields checker + print the filed fields on the CLI 

# get the values of the vars and assign it here 
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    civil_id = civil_entry.get()
# check if the fileds are filled or not 
    if not name or not email or not civil_id or not var.get():
        error_message.set("All fields must be filled in.")
        return

    if not validate_email(email):
        error_message.set("Invalid email address.")
        return
     # clear the error message if all fields are filled
    else:
        error_message.set("") 


# Check gender and display message
    check_gender()  
# print the enterd values on the cli 
    print("Name:", name)
    print("Email:", email)
    print("Civil ID:", civil_id)
    print("Gender:", var.get())
    print_numbers(civil_id)
    check_age(civil_id)



    
# function to check if the enterd email is valid or not, if not " enter a valid email "
# const function for checking the valdation 
def validate_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex,email):
        return True
    else:
        return False

# function to check the gender if male blue, if female pink.

def check_gender():
    # here to get the gender that the user entered 
    gender = var.get()
    if gender == "male":
        gender_message.set("Thank you 💙")
    elif gender == "female":
        gender_message.set("Thank you 🩷")
    else:
        gender_message.set("Please select a gender.")


# function to limit the civil id to be maximum 12 nums 
# const function to check the len of somthing entered 
def check_civil_id_length(new_text):
    if len(new_text) > 12:
        return False
    return True
vcmd = (root.register(check_civil_id_length), '%P')

# function to take the second and the third nums from L, and print them on the CLI 
def print_numbers(civil_id):
    if len(civil_id) >= 3:
        second_number = civil_id[1] # 2
        third_number = civil_id[2] # 3 
        print(f"Second number: {second_number}, Third number: {third_number}")
    else:
        print("The civil ID must contain at least three numbers.")


# funtion to check the age of the user 
def check_age(civil_id):
    if len(civil_id) >= 3:
        # slice the civli id and add to 2000 to check the age 
        birth_year = int(civil_id[1:3]) + 2000
        print(birth_year)

        # calling form datetime lib to use the current year 
        current_year = datetime.now().year
        age = current_year - birth_year

        # the requested conditions
        if age < 13:
            age_message.set("Sorry kid, maybe next time.")
        elif age > 18:
            age_message.set("It's for kids only!")
        else:
            age_message.set(f"Welcome! You are {age} years old.")
    else:
        age_message.set("The civil ID must contain at least three digits.")





heading = Label(head, text="Welcome to Kuwait Codes, Let's start", font='Helvetica 25 bold', pady=10).pack()

# name entry and label
name_label = Label(entry, text='Name\t', font='Helvetica 20 bold', pady=5)
name_entry = Entry(entry, width=30, font='Helvetica 20')
# email entry and labe;
email_label = Label(entry, text='Email\t', font='Helvetica 20 bold', pady=5)
email_entry = Entry(entry, width=30, font='Helvetica 20')
# civil id entry and label 
civil_label = Label(entry, text='Civil ID\t', font='Helvetica 20 bold', pady=5)
civil_entry = Entry(entry, width=30, font='Helvetica 20', validate="key", validatecommand=vcmd)
# gender radi button and label 
gender_label = Label(entry, text='Gender\t', font='Helvetica 20 bold', pady=5)
male = Radiobutton(entry, text='Male', variable=var, value='male')
female = Radiobutton(entry, text='Female', variable=var, value='female')
# submit button + submit function
submit_button = Button(entry, text="Submit", command=submit_form, font='Helvetica 20')
submit_button.grid(row=5, column=2, pady=10)




# placing the elements using grid 
# name grid
name_label.grid(row=1, column=1)
name_entry.grid(row=1, column=2)
# email grid
email_label.grid(row=2, column=1)
email_entry.grid(row=2, column=2)
# civil id grid 
civil_label.grid(row=3, column=1)
civil_entry.grid(row=3, column=2)
# gender gird
gender_label.grid(row=4, column=1)
male.grid(row=4, column=2, sticky="nsew")
female.grid(row=4, column=3, sticky="nsew")





# labels  for the functions 
age_label = Label(entry, textvariable=age_message, font='Helvetica 15 bold')
age_label.grid(row=6, column=1, columnspan=4)
# error message 
error_label = Label(entry, textvariable=error_message, font='Helvetica 15 bold', fg='red')
error_label.grid(row=7, column=1, columnspan=4)
# gender message + heart 
gender_msg_label = Label(entry, textvariable=gender_message, font='Helvetica 15 bold', fg='white')
gender_msg_label.grid(row=8, column=1, columnspan=4)

root.title("Kuwait Codes Application Form")
root.mainloop()


