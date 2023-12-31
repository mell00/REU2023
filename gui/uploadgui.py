import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import subprocess

def open_file():
    filepath = filedialog.askopenfilename(
        initialdir="/",
        title="Select Image File",
        filetypes=(("Image files", "*.jpg *.jpeg *.png *.gif"), ("All files", "*.*"))
    )
    if filepath:
        save_image(filepath)

def save_image(filepath):
    image = Image.open(filepath)
    save_path = "path/to/save/directory/image.jpg"  # Set the desired save path
    image.save(save_path)
    print("Image saved successfully!")

def create_canvas():
    global canvas  # Declare the canvas variable as global
    canvas = tk.Canvas(window, width=450, height=500)
    canvas.place(x=0, y=0)  # Use place instead of pack

