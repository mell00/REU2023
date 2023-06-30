import tkinter as tk
from PIL import Image, ImageTk
import subprocess
from uploadgui import *
from convert_gui import *

def create_canvas():
    global canvas  # Declare the canvas variable as global
    canvas = tk.Canvas(window, width=450, height=500)
    canvas.place(x=0, y=0)  # Use place instead of pack

window = tk.Tk()
window.title("DNA Image Recognition")
ico = Image.open('dnaicon.jpg')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)
window.geometry('500x300')

def nav_to_loading():
    subprocess.run(["python", "gui_loadingbar.py"])

def create_buttons():
    window.geometry("450x350")

    button1 = tk.Button(window, text="Loading", command=nav_to_loading)
    button1.place(x=25, y=100)

    button2 = tk.Button(window, text="Upload Sample Image", command=open_file)
    button2.place(x=100, y=25)

    button3 = tk.Button(window, text="Convert Image(s)", command=select_directory_and_convert)
    button3.place(x=175, y=100)

create_canvas()

# Load the image
front_image = Image.open("3dmodel.jpg")
canvas_width = 300
canvas_height = 300

# Resize the image to fit the canvas while maintaining aspect ratio
image_ratio = front_image.width / front_image.height
canvas_ratio = canvas_width / canvas_height

if image_ratio > canvas_ratio:
    new_width = canvas_width
    new_height = int(new_width / image_ratio)
else:
    new_height = canvas_height
    new_width = int(new_height * image_ratio)

front_image = front_image.resize((new_width, new_height), Image.ANTIALIAS)
front_image = ImageTk.PhotoImage(front_image)

# Add the image to the canvas
canvas.create_image(canvas_width/2, canvas_height/2, anchor="center", image=front_image)

create_buttons()
window.mainloop()
