                                    #THIS IS A TEMPLATE
#----------------------------------------------------------------------------------------------

'''import tkinter as tk
from PIL import Image, ImageTk
import subprocess
from uploadgui import *
from convert_gui import *

def create_canvas():
    global canvas  # Declare the canvas variable as global
    canvas = tk.Canvas(window)
    canvas.pack(fill="both", expand=True)  # Use pack with fill and expand to fill the window

def resize_image(event=None):
    global front_image, canvas, image_canvas

    # Get the current canvas size
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    # Check if canvas dimensions are non-zero
    if canvas_width > 0 and canvas_height > 0:
        # Calculate the maximum size to fit within the canvas
        max_width = canvas_width
        max_height = canvas_height

        # Get the original image dimensions
        original_width = front_image.width
        original_height = front_image.height

        # Calculate the scaling factor
        width_ratio = max_width / original_width
        height_ratio = max_height / original_height

        # Choose the smaller ratio as the scaling factor
        scaling_factor = min(width_ratio, height_ratio)

        # Calculate the new dimensions
        new_width = int(original_width * scaling_factor)
        new_height = int(original_height * scaling_factor)

        # Resize the image
        front_image_resized = front_image.resize((new_width, new_height), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS

        # Add the resized image to the canvas
        image_tk = ImageTk.PhotoImage(front_image_resized)
        canvas.itemconfig(image_canvas, image=image_tk)
        canvas.image = image_tk  # Save a reference to prevent image garbage collection

window = tk.Tk()
window.title("DNA Image Recognition")
ico = Image.open('dnaicon.ico')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)
window.geometry('500x300')

# Set the minimum and maximum size for the window
window.minsize(682, 383)  # Set the minimum width and height
window.maxsize(683, 384)  # Set the maximum width and height

def nav_to_loading():
    subprocess.run(["python", "gui_loadingbar.py"])

def create_buttons():
    window.geometry("450x350")

    button1 = tk.Button(window, text="Run", height= 2, width=5, command=nav_to_loading)
    button1.place(x=420, y=192)

    button2 = tk.Button(window, text="Quit", height= 2, width=5, command=open_file)
    button2.place(x=341, y=267)

    button3 = tk.Button(window, text="Help", height= 2, width=5, command=select_directory_and_convert)
    button3.place(x=500, y=267)

create_canvas()

# Load the image
front_image = Image.open("DNAVision.png")

# Bind the event handler to the canvas resize event
canvas.bind("<Configure>", resize_image)

# Add the original image to the canvas
image_tk = ImageTk.PhotoImage(front_image)
image_canvas = canvas.create_image(0, 0, anchor="nw", image=image_tk)

create_buttons()
window.mainloop()


'''