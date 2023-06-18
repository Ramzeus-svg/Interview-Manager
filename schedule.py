from tkinter import messagebox
from pathlib import Path
import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import auth
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"

cred = credentials.Certificate("app.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def search_interview():
    full_name = entry_1.get()

    if not full_name:
        messagebox.showerror("Error", "Please enter a full name.")
        return

    # Search Firestore for an interview with the given full name
    existing_interview_ref = db.collection('interviews').where('full_name', '==', full_name).get()

    if existing_interview_ref:
        interview_date = existing_interview_ref[0].to_dict()['interview_date']
        messagebox.showinfo("Interview Date", f"Interview date for {full_name}: {interview_date}")
        window.destroy()
    else:
        messagebox.showerror("Error", "No interview found for the provided Name.")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Schedule")
window.geometry("559x202")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 202,
    width = 559,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    10.0,
    62.0,
    anchor="nw",
    text="Full Name :",
    fill="#000000",
    font=("Inter", 20 * -1, "bold ")
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("sec.png"))
entry_bg_1 = canvas.create_image(
    322.5,
    77.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font = ("Inter Bold" , 15 , "bold")
)
entry_1.place(
    x=168.0,
    y=56.0,
    width=305.0,
    height=35.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("ser.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=search_interview,
    relief="flat"
)
button_1.place(
    x=196.0,
    y=117.0,
    width=200.0,
    height=65.0
)
window.resizable(False, False)
window.mainloop()
