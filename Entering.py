from pathlib import Path
import time
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import subprocess
import os
import json
import sys



if getattr(sys, 'frozen', False):
    # If the script is running as an executable, use the executable's directory
    app_json_path = os.path.join(sys._MEIPASS, 'app.json')
else:
    # If the script is running in the Python interpreter, use the script's directory
    app_json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app.json')


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"


def request():
    subprocess.Popen(["python", 'Request.py'])



def exit(window):
    for opacity in range(100, -1, -5):
        window.attributes('-alpha', opacity / 100)
        window.update()
        time.sleep(0.05)
    window.destroy()


def open_second_window():
    subprocess.Popen(["python", 'Login.py'])
    for opacity in range(100, -1, -5):
        window.attributes('-alpha', opacity / 100)
        window.update()
        time.sleep(0.04)
    window.destroy()


def schedule():
    subprocess.Popen(["python", r"C:\Users\Administrator\Desktop\Interview design\Schedule\build\schedule.py"])

def admin():
    subprocess.Popen(["python", r"C:\Users\Administrator\Desktop\Interview design\Admin Pass\build\Admin.py"])



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)





window = Tk()
window.title("WELCOME")
width = 1083
height = 560
x_offset = 100
y_offset = 100
window.geometry(f"{width}x{height}+{x_offset}+{y_offset}")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 560,
    width = 1083,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("Main.png"))
image_1 = canvas.create_image(
    541.0,
    280.0,
    image=image_image_1
)

canvas.create_text(
    287.0,
    0.0,
    anchor="nw",
    text="WELCOME TO THE JOURNEY",
    fill="#FFFFFF",
    font=("IM_FELL_Great_Primer_SC", 40 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("Admin.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=admin,
    relief="flat"
)
button_1.place(
    x=13.0,
    y=125.0,
    width=155.0,
    height=50.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("Login.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_second_window,
    relief="flat"
)
button_2.place(
    x=916.0,
    y=125.0,
    width=150.0,
    height=45.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("Exit.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: exit(window),
    relief="flat"
)
button_3.place(
    x=473.0,
    y=480.0,
    width=135.0,
    height=45.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("Schedule.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=schedule,
    relief="flat"
)
button_4.place(
    x=11.0,
    y=242.0,
    width=154.0,
    height=47.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("request.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=request,
    relief="flat"
)
button_5.place(
    x=911.0,
    y=254.0,
    width=145,
    height=43.0
)
window.resizable(False, False)
window.mainloop()
