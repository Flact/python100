from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
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

    if website or password:
        is_ok = messagebox.askokcancel(title=website, message=f"These are thee details entered:\nEmail: {email}"
                                                              f"\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")
            txt_website.delete(0, END)
            txt_password.delete(0, END)
            txt_website.focus()
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")


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
txt_website = Entry(width=35)
txt_website.grid(row=1, column=1, columnspan=2)
txt_website.focus()

txt_email = Entry(width=35)
txt_email.grid(row=2, column=1, columnspan=2)
txt_email.insert(0, "anushka@gmail.com")

txt_password = Entry(width=40)
txt_password.grid(row=3, column=1)

# Button
btn_gen_passwd = Button(text="Generate Password", command=generate_password)
btn_gen_passwd.grid(row=3, column=2)

btn_add = Button(text="Add", width=36, command=save)
btn_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
