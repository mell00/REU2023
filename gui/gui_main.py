import tkinter as tk
from PIL import Image, ImageTk
import subprocess

def create_canvas():
    global canvas  # Declare the canvas variable as global
    canvas = tk.Canvas(window, width=450, height=500)
    canvas.pack()

window = tk.Tk()
window.title("DNA Image Recognition")
ico = Image.open('dnaicon.jpg')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)

def nav_to_loading():
    subprocess.run(["python", "gui_loadingbar.py"])

def create_buttons():
    window.geometry("450x350")

    button1 = tk.Button(window, text="Loading", command=nav_to_loading)
    button1.place(x=25, y=100)

    button2 = tk.Button(window, text="button2")
    button2.place(x=100, y=25)

    button3 = tk.Button(window, text="button3")
    button3.place(x=175, y=100)

create_canvas()

# Load the image
front_image = ImageTk.PhotoImage(file="3dmodel.jpg")

# Add the image to the canvas
canvas.create_image(0, 0, anchor="nw", image=front_image)

create_buttons()
window.mainloop()
