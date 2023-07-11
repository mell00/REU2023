import tkinter as tk
from PIL import Image, ImageTk
import subprocess
from uploadgui import *
from convert_gui import *
from gui_main import MainPage

import tkinter as tk
from PIL import Image, ImageTk

class KnotVision(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Set up the main application window
        self.title("DNA Image Recognition")
        self.geometry('500x300')
        self.minsize(682, 383)  # Set the minimum width and height
        self.maxsize(683, 384)  # Set the maximum width and height

        ico = Image.open('dnaicon.ico')
        photo = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, photo)

        self.frame = None
        self.switch_frame(Main)

    def switch_frame(self, target_frame):
        new_frame = target_frame(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.pack(fill="both", expand=True)

class Main(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master  # Store the master for later use

        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill="both", expand=True)

        # Load the image
        self.front_image = Image.open("blankpage.png")

        # Add the original image to the canvas
        self.image_tk = ImageTk.PhotoImage(self.front_image)
        self.image_canvas = self.canvas.create_image(0, 0, anchor="nw", image=self.image_tk)

        # Bind the event handler to the canvas resize event
        self.canvas.bind("<Configure>", self.resize_image)

        self.create_buttons()

    def resize_image(self, event=None):
        canvas_width = event.width
        canvas_height = event.height

        if canvas_width > 0 and canvas_height > 0:
            front_image_resized = self.front_image.resize((canvas_width, canvas_height), Image.LANCZOS)
            self.image_tk = ImageTk.PhotoImage(front_image_resized)
            self.canvas.itemconfig(self.image_canvas, image=self.image_tk)

    def create_buttons(self):
        button1 = tk.Button(self, text="Exit", height=2, width=5, command=self.results_to_nav)
        button1.place(relx=0.9, rely=0.6, anchor="center")

        button2 = tk.Button(self, text="Quit", height=2, width=5, command=open_file)
        button2.place(relx=0.7, rely=0.8, anchor="center")

        button3 = tk.Button(self, text="Help", height=2, width=5, command=select_directory_and_convert)
        button3.place(relx=0.9, rely=0.8, anchor="center")


    def results_to_nav(self):
        self.master.switch_frame(MainPage)  # Switch back to the main page of the application


class ExitPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text='This is the Run page').pack()
        tk.Button(self, text='Go back', command=lambda: master.switch_frame(MainPage)).pack()


class QuitPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text='This is the Quit page').pack()
        tk.Button(self, text='Go back', command=lambda: master.switch_frame(MainPage)).pack()


class HelpPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text='This is the Help page').pack()
        tk.Button(self, text='Go back', command=lambda: master.switch_frame(MainPage)).pack()


if __name__ == '__main__':
    app = KnotVision()
    app.mainloop()
