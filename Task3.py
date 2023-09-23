import random
import string
from customtkinter import *
import pyperclip

root = CTk()
root.title('Password Generator')
root.geometry('350x380')

frame = CTkFrame(root)
frame.pack(pady=20, padx=20, fill='both', expand=True)

label = CTkLabel(master=frame, text='Password Generator', font=('Times', 30), text_color='#00FF41')
label.place(x=35, y=25)

entry = CTkEntry(root, placeholder_text='Enter Length')
entry.place(x=110, y=120)

generated_password = ""

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(int(entry.get())))
    return password

def gen():
    global generated_password
    try:
        x = int(entry.get())
        if x <= 0:
            print("Password length must be greater than 0.")
            entry.delete(0, 'end')
        else:
            generated_password = generate_password(entry.get())
            label1 = CTkLabel(frame, text=f'Generated Password is {generated_password}', font=('Times', 20), text_color='red')
            label1.place(x=30, y=230)

            copy_button = CTkButton(root, text='Copy Password to Clipboard', command=copy_to_clipboard)
            copy_button.place(x=90, y=310)

            entry.delete(0, 'end')
    except ValueError:
        label1 = CTkLabel(frame, text='Invalid input. Please enter a valid number', font=('Times', 15), text_color='red')
        label1.place(x=25, y=230)
        entry.delete(0, 'end')

def copy_to_clipboard():
    global generated_password
    pyperclip.copy(generated_password)


button = CTkButton(root, text='Generate Password', command=gen)
button.place(x=110, y=185)

root.mainloop()


