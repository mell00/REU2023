import tkinter as tk
import pystray
from PIL import Image

# Create a Tkinter window
root = tk.Tk()
root.title("Toolbar Icon Example")

# Load the icon image
icon = Image.open("dnaicon.png")

# Define a function to quit the application
def quit_app():
    root.destroy()

# Create the system tray icon
menu = (
    pystray.MenuItem("Exit", quit_app),
)
tray_icon = pystray.Icon("my_app", icon, "My App", menu)

# Start the system tray
tray_icon.run()

# Start the Tkinter event loop
root.mainloop()


