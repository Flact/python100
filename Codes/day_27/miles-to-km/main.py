from tkinter import Label, Button, Entry, Tk, END

# Creating a new window and configurations
window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)
window.minsize(width=200, height=100)

# Entry
user_input = Entry(width=10)
user_input.insert(END, string="0")

# Labels
miles = Label(text="Miles")
zero = Label(text="0")
is_eq = Label(text="Is equal to:")
km = Label(text="Km")


# Buttons
def action():
    in_km = round(float(user_input.get()) * 1.609, 2)
    zero.config(text=in_km)


button = Button(text="Click Me", command=action)

# Grid alignment
user_input.grid(column=1, row=0)
miles.grid(column=3, row=0)
is_eq.grid(column=0, row=1, padx=10)
zero.grid(column=1, row=1)
km.grid(column=3, row=1)
button.grid(column=1, row=2)

window.mainloop()
