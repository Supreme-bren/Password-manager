from tkinter import *
from tkinter import messagebox
from passwordgen import passwordgenerator
import pyperclip
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
    if len(web) != 0 and len(email) !=0 and len(pw) !=0:
        is_okay = messagebox.askokcancel(title=web, message=
        f"These are the details entered:\nEmail: {email} \nPassword: {pw} \nIs it okay to save?")
        if is_okay:
            with open("data.txt", 'a') as file:
                file.write(f"{web} | {email} | {pw}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)
    else:
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty")



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
website_input = Entry(width=35)
email_input = Entry(width=35)
password_input = Entry(width=21)



website.grid(column=0,row=1)
email_username.grid(column=0,row=2)
generate_password.grid(column=2,row=3)
website_input.grid(column=1,row=1,columnspan=2)
website_input.focus()
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(0,"bio5@pitt.edu")
password_input.grid(column=1,row=3)
add.grid(column=1,row=4,columnspan=2)



window.mainloop()