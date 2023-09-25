from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json



def generation_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_insert.insert(0, password)


def save():
    
    website_save = web_insert.get()
    user_save = user_insert.get()
    password_save = password_insert.get()
    new_data = {
        website_save: { 
            "email": user_save,
            "password": password_save 
        }
    }

    if len(website_save) == 0 or len(password_save) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            data_file = open("data.json", "r")
        except:
            data_file = open("data.json", "w")
            json.dump(new_data, data_file, indent=4)
        else:
            data = json.load(data_file)
            data.update(new_data)
            data_file = open("data.json", "w")
            json.dump(data, data_file, indent=4)
        finally:
            web_insert.delete(0, END)
            password_insert.delete(0, END)
            
def find_password():
    try:
        data_file = open("data.json", "r")
    except:
        messagebox.showinfo(title= "Error", message="No Data File Found")
        return
    data = json.load(data_file)
    website_save = web_insert.get()
    if website_save in data:
        password_search = data[website_save]["password"]
        email_search = data[website_save]["email"]
        messagebox.showinfo(title=website_save, message=f"Email: {email_search}\n Password: {password_search}")
        web_insert.delete(0, END)
        password_insert.delete(0, END)
        return
    else:
        messagebox.showinfo(message=f"No details for the {website_save} exists.")
        web_insert.delete(0, END)
        password_insert.delete(0, END)

            
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)

web_insert = Entry(width=21)
web_insert.grid(column=1, row=1)
web_insert.focus()
email = Label(text="Email/Username:")
email.grid(column=0, row=2)

user_insert = Entry(width=35)
user_insert.grid(column=1, row=2, columnspan=2)
user_insert.insert(0, "kamil@gmail.com")

password = Label(text="Password:")
password.grid(column=0, row=3)

password_insert = Entry(width=21)
password_insert.grid(column=1, row=3)

generate_password = Button(text="Generate Password", command=generation_password)
generate_password.grid(column=2, row=3)

search = Button(text="Search",width=15, command=find_password)
search.grid(column=2, row=1)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()