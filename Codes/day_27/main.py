# import tkinter
from tkinter import *

window = Tk()
window.title("The GUI Python")
window.minsize(width=400, height=250)
window.config(padx=100, pady=150)

# Label
my_label = Label(text="A Label", font=("Consolas", 24, "italic"))
# my_label.pack(side="left")
# my_label.place(x=100, y=0)
my_label.grid(column=0, row=0)
my_label["text"] = "The new TEXT"  # Using dictionary key
my_label.config(text="From .config")
my_label.config(padx=15, pady=15)


# Button
def button_clicked():
    # print("Button Clicked")
    my_label["text"] = "Button got Clicked"
    # my_label.config(text="Button got Clicked")
    # my_label.config(text=input_field.get())


button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=0, row=2)

# Entry
input_field = Entry(width=15)
# input_field.pack()
input_field.grid(column=0, row=3)


window.mainloop()
