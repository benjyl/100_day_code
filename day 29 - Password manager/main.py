from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# https://tkdocs.com/tutorial/widgets.html#entry - tkinter tutorials


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
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(choice(letters)) for i in range(randint(8, 10))]
    [password_list.append(choice(numbers)) for i in range(randint(2, 4))]
    [password_list.append(choice(symbols)) for i in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)
    pyperclip.copy(password) # saves password to clipboard
    messagebox.showinfo(message="Password saved to clipboard")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_pd_vals():
    """obtains website, email and password used
    """
    web = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    return web, email, password


def save_pd():

    web, email, password = get_pd_vals()
   
    # check for empty fields
    if web == "" or password=="":
        messagebox.showinfo("Error!", message="You must fill in all fields")
    else:
        # check if password info ok
        yes = messagebox.askyesno(message=f"web: {web}\nemail: {email}\npassword: {password}\nAre these correct?")
        if yes:  
            with open("password.txt", "a") as file:
                file.write(f"{web} | {email} | {password}\n")
            messagebox.showinfo(message="Password information stored")
            web_entry.delete(0, "end")
            email_entry.delete(0, "end")
            email_entry.insert(0, "benjy.lovat@gmail.com") # go back to original input
            password_entry.delete(0, "end")
        else:
            messagebox.showinfo(message="No password information stored")
        
        
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
background_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=background_img)
# show_config(canvas)
canvas.grid(row=0, column=1)

# labels
web_label = Label(text="Website:", bg="white")
web_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

# User Text entries
web_entry = Entry(width=51)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()  # gets cursor into web_entry on start up

email_entry = Entry(width=51)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)
email_entry.insert(0, "benjy.lovat@gmail.com")

# buttons
gen_pass = Button(text="Generate Password", bg="white", command=gen_password)
gen_pass.grid(row=3, column=2)

add_pass = Button(text="Add", width=43, bg="white", command=save_pd)
add_pass.grid(row=4, column=1, columnspan=2)

window.mainloop()
