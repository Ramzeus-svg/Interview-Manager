from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



cred = credentials.Certificate("app.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def update_meeting():
    full_name = entry_1.get()
    new_date = entry_2.get()

    if full_name and new_date:
        doc_ref = db.collection('interviews').document("name&date")
        doc_ref.update({'interview_date': new_date})
        print(f"Meeting {full_name} updated with new date: {new_date}")
    else:
        print("Missing meeting ID or new date.")

def delete_meeting():
    full_name = entry_3.get()

    if full_name:
        doc_ref = db.collection('interviews').document("name&date")
        doc_ref.delete()
        print(f"Meeting {meeting_id} deleted.")
    else:
        print("Missing meeting ID.")



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("476x577")
window.title("Admin Actions")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 577,
    width = 476,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("ac1.png"))
entry_bg_1 = canvas.create_image(
    258.0,
    121.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#78D2EE",
    highlightthickness=0,
    font=("Inter Bold", 16 , "bold")
)
entry_1.place(
    x=165.0,
    y=105.0,
    width= 180.0,
    height=27.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("ac2.png"))
entry_bg_2 = canvas.create_image(
    258.0,
    189.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#78D2EE",
    highlightthickness=0,
    font=("Inter Bold", 16 , "bold")
)
entry_2.place(
    x=165.0,
    y=169.0,
    width= 180.0,
    height=27.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("ac3.png"))
entry_bg_3 = canvas.create_image(
    258.0,
    406.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#78D2EE",
    highlightthickness=0,
    font=("Inter Bold", 16 , "bold")
)
entry_3.place(
    x=171.0,
    y=387.0,
    width= 180.0,
    height=27.0
)

canvas.create_text(
    13.0,
    106.0,
    anchor="nw",
    text="Meeting ID :",
    fill="#000000",
    font=("Inter", 16 * -1,"bold")
)

canvas.create_text(
    13.0,
    174.0,
    anchor="nw",
    text="Enter New Date :",
    fill="#000000",
    font=("Inter", 16 * -1,"bold")
)

canvas.create_text(
    13.0,
    391.0,
    anchor="nw",
    text="Meeting ID :",
    fill="#000000",
    font=("Inter", 16 * -1,"bold")
)

button_image_1 = PhotoImage(
    file=relative_to_assets("delt.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=delete_meeting,
    relief="flat"
)
button_1.place(
    x=185.0,
    y=476.0,
    width=103.0,
    height=43.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("ed.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=update_meeting,
    relief="flat"
)
button_2.place(
    x=185.0,
    y=272.0,
    width=103.0,
    height=48.0
)
window.resizable(False, False)
window.mainloop()
