import smtplib
from email.message import EmailMessage
from tkinter import messagebox
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import re
import requests

cred = credentials.Certificate("app.json")
firebase_admin.initialize_app(cred)
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

processed_emails = set()

async def sign_in_async(email, password, on_success, on_failure):
    try:
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, authenticate_user, email, password, on_success, on_failure)
    except Exception as e:
        on_failure(e)



def send_reset_password_email():
        email = entry_1.get()

        if not is_valid_email(email):
            messagebox.showerror("Error", "Invalid email address. Please check for typos.")
            return

        api_key = "AIzaSyCTSmGbgaO8OLIpFwZaU7OnMeBIG3U7S70"
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={api_key}"
        data = {
            "requestType": "PASSWORD_RESET",
            "email": email
        }

        response = requests.post(url, json=data)

        if response.status_code == 200:
            messagebox.showinfo("Success", "Password reset email has been sent.")
            window.destroy()
        else:
            error_message = response.json().get("error", {}).get("message", "Unknown error")
            messagebox.showerror("Error", f"Failed to send password reset email. {error_message}")
            



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Forget")
window.geometry("481x235")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 235,
    width = 481,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("resume.png"))
entry_bg_1 = canvas.create_image(
    297.0,
    81.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font =("Inter Bold",16,"bold")
)
entry_1.place(
    x=138.0,
    y=62.0,
    width=315.0,
    height=33.0
)

canvas.create_text(
    16.0,
    68.0,
    anchor="nw",
    text="EMAIL :",
    fill="#000000",
    font=("Inter", 20 * -1,"bold")
)

button_image_1 = PhotoImage(
    file=relative_to_assets("resey.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=send_reset_password_email,
    relief="flat"
)
button_1.place(
    x=155.0,
    y=124.0,
    width=168.0,
    height=65.0
)
window.resizable(False, False)
window.mainloop()
