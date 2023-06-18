from google.cloud import storage
from pathlib import Path
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tkinter import filedialog
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Toplevel,messagebox
import os
from datetime import datetime, timedelta
import random
from tkinter.ttk import Progressbar





OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"

service_account_json = ("app.json")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_json

# Create a client
client = storage.Client.from_service_account_json(service_account_json)

# Access your bucket
bucket = client.get_bucket('database-for-python.appspot.com')

cred = credentials.Certificate(service_account_json)
firebase_admin.initialize_app(cred, {
    'storageBucket': 'gs://database-for-python.appspot.com'
})

db = firestore.client()




def generate_interview_date():
    # Generate a random number of days between 7 and 14
    random_days = random.randint(7, 14)
    
    # Calculate the interview date by adding the random number of days to the current date
    interview_date = datetime.now() + timedelta(days=random_days)

    return interview_date



cv_file = None

def select_cv():
    global cv_file
    cv_file = filedialog.askopenfilename(title="Select CV", filetypes=[("PDF Files", "*.pdf")])
    
    if cv_file:
        print(f"CV selected: {cv_file.encode('utf-8')}")
    else:
        print("No CV selected.")

def upload_cv():
    global cv_file

    full_name = entry_1.get()
    age = entry_2.get()

    # Check if an interview already exists for the user
    existing_interview_ref = db.collection('interviews').where('full_name', '==', full_name).where('age', '==', age).get()

    if existing_interview_ref:
        messagebox.showerror("Error", "Already have an interview meeting.")
        return

    if cv_file:
        # Create a loading popup
        loading_popup = Toplevel(window)
        loading_popup.title("Uploading")
        loading_popup.geometry("200x100")
        loading_popup.configure(bg="#FFFFFF")

        # Create a progress bar in indeterminate mode
        progress = Progressbar(loading_popup, mode="indeterminate", length=150)
        progress.pack(pady=20)
        progress.start()

        # Display a loading message
        loading_label = Text(loading_popup, height=1, width=20)
        loading_label.pack()
        loading_label.insert("end", "Uploading CV...")

        # Update the UI and disable the main window
        window.withdraw()
        loading_popup.update()
        window.after(100, window.update())

        # Generate a unique file name based on the full name and age
        full_name = entry_1.get()
        age = entry_2.get()
        file_name = f"{full_name}-{age}.pdf"

        try:
            # Upload the CV to Firebase Storage
            blob = bucket.blob(cv_file)
            with open(cv_file, 'rb') as f:
                blob.upload_from_file(f)
            print(f"CV uploaded: {file_name}")

            # Generate an interview date and save it to Firestore
            interview_date = generate_interview_date()
            doc_ref = db.collection('interviews').document("name&date")
            doc_ref.set({
                'full_name': full_name,
                'age': age,
                'cv_file_name': file_name,
                'interview_date': interview_date
            })
            print(f"Interview date for {full_name} saved: {interview_date}")

            # Close the loading popup and show a success message with the interview date
            loading_popup.destroy()
            window.deiconify()
            formatted_date = interview_date.strftime("%Y-%m-%d %H:%M:%S")
            messagebox.showinfo("Success", f"CV uploaded successfully.\nInterview Date: {formatted_date} .\n Your Meeting ID is :{full_name}")
        except Exception as e:
            print(f"Error: {e}")
            # Close the loading popup and show a failure message
            loading_popup.destroy()
            window.deiconify()
            messagebox.showerror("Error", "Failed to upload CV.")
    else:
        print("No CV selected.")
        messagebox.showerror("Error", "No CV selected.")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("CV")
window.geometry("681x296")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 296,
    width = 681,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("name.png"))
entry_bg_1 = canvas.create_image(
    349.5,
    69.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font = ("Inter Bold", 16 , "bold")
)
entry_1.place(
    x=219.0,
    y=51.0,
    width=261.0,
    height=33.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("CV.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=select_cv,
    relief="flat"
)
button_1.place(
    x=210.0,
    y=169.0,
    width=140.0,
    height=48.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("age.png"))
entry_bg_2 = canvas.create_image(
    349.5,
    129.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font = ("Inter Bold", 16 , "bold")
)
entry_2.place(
    x=219.0,
    y=111.0,
    width=261.0,
    height=33.0
)

canvas.create_text(
    13.0,
    54.0,
    anchor="nw",
    text="Full Name :",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    13.0,
    175.0,
    anchor="nw",
    text="CV :",
    fill="#000000",
    font=("Inter", 20 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("sub.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=upload_cv,
    relief="flat"
)
button_2.place(
    x=215.0,
    y=236.0,
    width=130.0,
    height=50.0
)

canvas.create_text(
    13.0,
    114.0,
    anchor="nw",
    text="Age :",
    fill="#000000",
    font=("Inter", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
