from tkinter import messagebox
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import firebase_admin
from firebase_admin import auth, credentials

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"

cred = credentials.Certificate("app.json")
firebase_admin.initialize_app(cred)


def create_user(email, password):
    try:
        user = auth.create_user(email=email, password=password)
        print(f"User created successfully: {user.uid}")
        messagebox.showinfo("Success", "User account created successfully!")
    except Exception as e:
        print(f"Error creating user: {e}")
        messagebox.showerror("Error", "An error occurred while creating the user account.")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("449x689")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 689,
    width = 449,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("backy1.png"))
image_1 = canvas.create_image(
    226.0,
    103.73580932617188,
    image=image_image_1
)

canvas.create_text(
    155.0,
    130.0,
    anchor="nw",
    text="SIGN UP",
    fill="#000000",
    font=("AdventPro Regular", 40 * -1)
)

canvas.create_text(
    12.0,
    334.0,
    anchor="nw",
    text="EMAIL :",
    fill="#000000",
    font=("AdventPro Regular", 28 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("mail1.png"))
entry_bg_1 = canvas.create_image(
    312.5,
    359.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#F2F2F2",
    
    highlightthickness=0,
    font=("Inter Bold",16)
)
entry_1.place(
    x=213.0,
    y=339.0,
    width=199.0,
    height=30.0
)

canvas.create_text(
    12.0,
    412.0,
    anchor="nw",
    text="PASSWORD :",
    fill="#000000",
    font=("AdventPro Regular", 28 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("pass1.png"))
entry_bg_2 = canvas.create_image(
    312.5,
    429.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#EFF0F1",
    
    highlightthickness=0,
    font=("Inter Bold",16)
)
entry_2.place(
    x=213.0,
    y=412.0,
    width=199.0,
    height=30.0
)

canvas.create_text(
    12.0,
    477.0,
    anchor="nw",
    text="CONFIRM :",
    fill="#000000",
    font=("AdventPro Regular", 28 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("pass2.png"))
entry_bg_3 = canvas.create_image(
    312.5,
    496.0,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#F3F3F3",
    
    highlightthickness=0,
    font=("Inter Bold",16)
)
entry_3.place(
    x=213.0,
    y=477.0,
    width=199.0,
    height=30.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("suby.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: create_user(entry_1.get("1.0", "end-1c"), entry_2.get()),
    relief="flat"
)
button_1.place(
    x=140.0,
    y=561.0,
    width=225.0,
    height=60.0
)
window.resizable(False, False)
window.mainloop()
