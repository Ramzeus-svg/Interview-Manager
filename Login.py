import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from pathlib import Path
import time 
import subprocess
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import requests
from tkinter import messagebox


def forget():
    subprocess.Popen(["python", 'forget.py'])


# Open the CV.py file
def sign_up():
    subprocess.Popen(["python", 'Sign up.py'])

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"


cred = credentials.Certificate("app.json")
firebase_admin.initialize_app(cred)

def sign_in_with_email_and_password(email, password):
    api_key = 'AIzaSyCTSmGbgaO8OLIpFwZaU7OnMeBIG3U7S70'  # Replace with your Firebase API key
    request_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}"
    data = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    response = requests.post(request_url, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(response.json())

def login():
    email = entry_1.get("1.0", "end-1c")
    password = entry_2.get("1.0", "end-1c")
    
    try:
        # Sign in the user
        user = sign_in_with_email_and_password(email, password)
        print("Login successful")
        
        # Open the CV.py file
        subprocess.Popen(["python", 'CV.py'])

    except Exception as e:
        error_message = str(e)
        print("Error signing in:", error_message)
        
        if "EMAIL_NOT_FOUND" in error_message or "INVALID_PASSWORD" in error_message:
            messagebox.showerror("Error", "User not found or incorrect password.")
        else:
            messagebox.showerror("Error", "An error occurred while signing in.")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def show():
    subprocess.Popen(["python", 'Entering.py'])
    for opacity in range(100, -1, -5):
        window.attributes('-alpha', opacity / 100)
        window.update()
        time.sleep(0.04)
    window.destroy()


window = Tk()

window.geometry("1103x594")
window.title("Login")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 594,
    width = 1103,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("back.png"))
image_1 = canvas.create_image(
    300.0,
    315.0,
    image=image_image_1
)

canvas.create_text(
    668.0,
    63.0,
    anchor="nw",
    text="LOGIN",
    fill="#000000",
    font=("Baloo Regular", 40 * -1)
)

canvas.create_text(
    653.0,
    184.0,
    anchor="nw",
    text="EMAIL :",
    fill="#000000",
    font=("Baloo Regular", 24 * -1)
)

canvas.create_rectangle(
    649.0,
    124.0,
    812.0,
    125.0,
    fill="#030303",
    outline="")

canvas.create_text(
    646.0,
    232.0,
    anchor="nw",
    text="Password :",
    fill="#000000",
    font=("Baloo Regular", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("en1.png"))
entry_bg_1 = canvas.create_image(
    868.0,
    199.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D7D7D7",
    fg="#000716",
    highlightthickness=0,
    font=("Inter Bold",10,"bold")
)
entry_1.place(
    x=786.0,
    y=184.0,
    width=164.0,
    height=27.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("en2.png"))
entry_bg_2 = canvas.create_image(
    868.0,
    252.0,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Inter Bold",14,"bold")
)
entry_2.place(
    x=786.0,
    y=238.0,
    width=164.0,
    height=24.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("Sign in.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat"
)
button_1.place(
    x=773.0,
    y=329.0,
    width=190.0,
    height=50.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("signup.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=sign_up,
    relief="flat"
)
button_2.place(
    x=773.0,
    y=397.0,
    width=187.0,
    height=50.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("forget.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=forget,
    relief="flat"
)
button_3.place(
    x=773.0,
    y=460.0,
    width=185.0,
    height=50.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("back1.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command= show,
    relief="flat"
)
button_4.place(
    x=773.0,
    y=522.0,
    width=185.0,
    height=50.0
)
window.resizable(False, False)
window.mainloop()
