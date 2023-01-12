from tkinter import *

def show_config(widget):
    config_dict = widget.configure()
    if config_dict is not None:
        print(f"Configuration for {widget.winfo_class()}")
        for key, value in config_dict.items():
            if len(value) > 2:
                print(f"    {key}:  default: {value[3]}   currently: {value[4]}")
            else:
                print(f"    {key}:  synonym for: {value[1]}")
    else:
        print("No configuration info available")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
background_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=background_img)
show_config(canvas)
canvas.grid(row=0, column=1)

# labels
web_label = Label(text="Website:", bg="white")
web_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:",  bg="white")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:",  bg="white")
password_label.grid(row=3, column=0)

# User Text entries
web_entry = Entry(width=51)
web_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=51)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# buttons
gen_pass = Button(text="Generate Password", bg="white")
gen_pass.grid(row=3, column=2)

add_pass = Button(text="Add", width=43, bg="white")
add_pass.grid(row=4, column=1, columnspan=2)

window.mainloop()