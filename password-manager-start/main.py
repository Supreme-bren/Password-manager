from tkinter import *
from tkinter import messagebox
from passwordgen import passwordgenerator
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():
    password_input.delete(0,END)
    new_password = passwordgenerator()
    pyperclip.copy(new_password)
    password_input.insert(0,new_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_input.get()
    email = email_input.get()
    pw = password_input.get()
    new_data = {
        web: {
            "email": email,
            "password": pw
        }
    }
    if len(web) != 0 and len(email) !=0 and len(pw) !=0:
        is_okay = messagebox.askokcancel(title=web, message=
        f"These are the details entered:\nEmail: {email} \nPassword: {pw} \nIs it okay to save?")
        if is_okay:
            try:
                with open("data.json", 'r') as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", 'w') as data_file:
                    # Saving updated data
                    json.dump(new_data, data_file, indent=4)
                website_input.delete(0, END)
                password_input.delete(0, END)
            else:
                # Updating old data with new data
                if web in data.keys():
                    del data[web]
                data.update(new_data)
                with open("data.json", 'w') as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
                website_input.delete(0, END)
                password_input.delete(0, END)

    else:
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty")

# ---------------------------- SEARCH ------------------------------- #
def search():
    try:
        with open("data.json", 'r') as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="No data file found")
    else:

        web = website_input.get()
        data_storage = {key:value for key,value in data.items() if key == web}
        if len(data_storage) ==0:
            messagebox.showerror(title="Error",message=f"No details for {web} exists")
        else:
            messagebox.showinfo(title=f"{web}",message=f"Email: {data_storage[web]["email"]}\npassword: {data_storage[web]["password"]}")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(column=1,row=0)

website = Label(text="Website:")
email_username = Label(text="Email/Username:")
password = Label(text="Password:")
password.grid(column=0,row=3)
generate_password = Button(text="Generate Password",command=create_password)
add = Button(text="Add", width=29, command=save)
search = Button(text="Search Password",command=search)
website_input = Entry(width=35)
email_input = Entry(width=35)
password_input = Entry(width=35)



website.grid(column=0,row=1)
email_username.grid(column=0,row=2)
generate_password.grid(column=3,row=3)
website_input.grid(column=1,row=1,columnspan=2)
website_input.focus()
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(0,"bio5@pitt.edu")
password_input.grid(column=1,row=3)
add.grid(column=1,row=4,columnspan=2)
search.grid(column=3,row=1)



window.mainloop()