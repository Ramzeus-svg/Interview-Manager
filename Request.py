from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("app.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"

def search_and_delete():
    full_name = entry_1.get()

    if not full_name:
        messagebox.showerror("Error", "Please enter a full name.")
        return

    # Search Firestore for a document with the given full name
    existing_docs = db.collection('interviews').where('full_name', '==', full_name).get()

    if existing_docs:
        doc = existing_docs[0]
        db.collection('interviews').document(doc.id).delete()
        messagebox.showinfo("Success", f"Deleted the document for {full_name}.")
    else:
        messagebox.showerror("Error", "No document found for the provided full name.")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Request")
window.geometry("407x289")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 289,
    width = 407,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("req1.png"))
entry_bg_1 = canvas.create_image(
    203.0,
    92.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Inter Bold", 16 * -1 , "bold")
)
entry_1.place(
    x=79.0,
    y=72.0,
    width=245.0,
    height=35.0
)

canvas.create_text(
    138.0,
    19.0,
    anchor="nw",
    text="MEETING ID : ",
    fill="#000000",
    font=("Inter Bold", 20 * -1,"bold")
)

button_image_1 = PhotoImage(
    file=relative_to_assets("delta.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=search_and_delete,
    relief="flat"
)
button_1.place(
    x=134.0,
    y=168.0,
    width=135.0,
    height=52.0
)
window.resizable(False, False)
window.mainloop()
