from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    #password_list = []
    #
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password = "".join(password_list)

    #print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if not website or not email or not password:
        messagebox.showerror(title="Error", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                  f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("password_data.txt", "a") as password_data:
                password_data.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

#---Labels---#
website_label = Label(text="Website:", font="bold", bg="white")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:", font="bold", bg="white")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font="bold", bg="white")
password_label.grid(column=0, row=3)

#---Entries---#
website_entry = Entry(width=35, highlightthickness=1)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_username_entry= Entry(width=35, highlightthickness=1)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "example@gmail.com")

password_entry = Entry(width=21, highlightthickness=1)
password_entry.grid(column=1, row=3)

#---Buttons---#
generate_password_button = Button(text="Generate Password", bg="white", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", bg="white", width=30, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()