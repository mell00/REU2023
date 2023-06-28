import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time
import subprocess
from gui_main import *


def start_loading():
    # Disable the button during loading
    start_button.config(state=tk.DISABLED)
    
    # Simulate loading process
    for i in range(101):
        progress_bar["value"] = i
        window.update_idletasks()
        time.sleep(0.03)
    
    # Re-enable the button after loading
    start_button.config(state=tk.NORMAL)

# Create the main window
window = tk.Tk()
window.title("DNA Image Recognition")
ico = Image.open('dnaicon.jpg')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)

# Create a progress bar
progress_bar = ttk.Progressbar(window, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=20)

# Create a button to start the loading process
start_button = tk.Button(window, text="Start Loading", command=start_loading)
start_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
