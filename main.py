from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

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

txt_password = Entry(width=21)
txt_password.grid(row=3, column=1)

# Button
btn_gen_passwd = Button(text="Generate Password")
btn_gen_passwd.grid(row=3, column=2)

btn_add = Button(text="Add", width=36, command=save)
btn_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
