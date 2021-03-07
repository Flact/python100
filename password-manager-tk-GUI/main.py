import json
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(8, 10))]

    # This will work exactly above 👇
    # password_list = [choice(letters) for _ in range(randint(8, 10))]
    # password_list += [choice(symbols) for _ in range(randint(8, 10))]
    # password_list += [choice(numbers) for _ in range(randint(8, 10))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    if txt_password.get():
        txt_password.delete(0, END)
        txt_password.insert(0, password)
    else:
        txt_password.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = txt_website.get()
    email = txt_email.get()
    password = txt_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website and password:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are thee details entered:\nEmail: {email}"
        #                                                       f"\nPassword: {password}\nIs it ok to save?")
        #
        # if is_ok:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Update old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            clean_fields()
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = txt_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No data file found!")
    else:
        # try:
        #     msg = f"Email: {data[website]['email']}\nPassword: {data[website]['password']}"
        #     messagebox.showinfo(title=website.title(), message=msg)
        # except KeyError:
        #     messagebox.showinfo(title="Oops", message="No details for the website exists!")
        #
        if website in data:
            msg = f"Email: {data[website]['email']}\nPassword: {data[website]['password']}"
            messagebox.showinfo(title=website.title(), message=msg)
            clean_fields()
        else:
            messagebox.showinfo(title="Oops", message=f"No details for the '{website.title()}' exists!")
            clean_fields()


# ---------------------------- CLEAN ENTRIES ------------------------------- #
def clean_fields():
    txt_website.delete(0, END)
    txt_password.delete(0, END)
    txt_website.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Label
lbl_website = Label(text="Website:")
lbl_website.grid(row=1, column=0)

lbl_email = Label(text="Email/Username:")
lbl_email.grid(row=2, column=0)

lbl_password = Label(text="Password:")
lbl_password.grid(row=3, column=0)

# Entry
txt_website = Entry(width=40)
txt_website.grid(row=1, column=1)
txt_website.focus()

txt_email = Entry(width=40)
txt_email.grid(row=2, column=1)
txt_email.insert(0, "anushka@gmail.com")

txt_password = Entry(width=40)
txt_password.grid(row=3, column=1)

# Button
btn_gen_passwd = Button(text="Search", width=15, command=find_password)
btn_gen_passwd.grid(row=1, column=2)

btn_gen_passwd = Button(text="Generate Password", width=15, command=generate_password)
btn_gen_passwd.grid(row=3, column=2)

btn_add = Button(text="Add", width=50, command=save)
btn_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
