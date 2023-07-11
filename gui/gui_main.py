import tkinter as tk
from PIL import Image, ImageTk
import subprocess
from uploadgui import *
from convert_gui import *


class KnotVision(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Set up the main application window
        self.title("DNA Image Recognition")
        self.geometry('500x300')
        self.minsize(682, 383)  # Set the minimum width and height
        self.maxsize(683, 384)  # Set the maximum width and height

        ico = Image.open('dnaicon.ico')
        photo = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, photo)

        self.frame = None
        self.switch_frame(MainPage)

    def switch_frame(self, target_frame):
        new_frame = target_frame(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.pack()


class MainPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master  # Store the master for later use

        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill="both", expand=True)

        # Load the image
        self.front_image = Image.open("DNAVision.png")

        # Add the original image to the canvas
        self.image_tk = ImageTk.PhotoImage(self.front_image)
        self.image_canvas = self.canvas.create_image(0, 0, anchor="nw", image=self.image_tk)

        # Bind the event handler to the canvas resize event
        self.canvas.bind("<Configure>", self.resize_and_reposition_elements)

        self.create_buttons()

    def resize_and_reposition_elements(self, event=None):
        self.resize_image()
        self.update_button_positions()

    def resize_image(self, event=None):
        # Get the current canvas size
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # Check if canvas dimensions are non-zero and not minimized
        if canvas_width > 1 and canvas_height > 1:
            # Get the original image dimensions
            original_width, original_height = self.front_image.size

            # Calculate the scaling factor
            width_ratio = canvas_width / original_width
            height_ratio = canvas_height / original_height

            # Choose the smaller ratio as the scaling factor
            scaling_factor = min(width_ratio, height_ratio)

            # Calculate the new dimensions
            new_width = int(original_width * scaling_factor)
            new_height = int(original_height * scaling_factor)

            # Resize the image
            front_image_resized = self.front_image.resize((new_width, new_height), Image.LANCZOS)

            # Convert the resized PIL image into a Tkinter-compatible photo image
            self.image_tk = ImageTk.PhotoImage(front_image_resized)
            
            # Remove the old image and add the new one
            self.canvas.delete(self.image_canvas)
            self.image_canvas = self.canvas.create_image(0, 0, anchor="nw", image=self.image_tk)
            
            # Call the method to update the button positions
            self.update_button_positions()


    def update_button_positions(self):
        # Get the current canvas size
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # Calculate new button positions
        button1_x = canvas_width * 0.9  # 90% from left
        button1_y = canvas_height * 0.6  # 60% from top

        button2_x = canvas_width * 0.7  # 70% from left
        button2_y = canvas_height * 0.8  # 80% from top

        button3_x = canvas_width * 0.9  # 90% from left
        button3_y = canvas_height * 0.8  # 80% from top

        # Move buttons to new positions
        self.button1.place(x=button1_x, y=button1_y)
        self.button2.place(x=button2_x, y=button2_y)
        self.button3.place(x=button3_x, y=button3_y)



    def nav_to_loading(self):
        subprocess.run(["python", "gui_loadingbar.py"])

    def create_buttons(self):
        self.button1 = tk.Button(self, text="Run", height=2, width=5, command=self.nav_to_loading)
        self.button1_window = self.canvas.create_window(0, 0, window=self.button1, anchor='nw')

        self.button2 = tk.Button(self, text="Quit", height=2, width=5, command=open_file)
        self.button2_window = self.canvas.create_window(0, 0, window=self.button2, anchor='nw')

        self.button3 = tk.Button(self, text="Help", height=2, width=5, command=select_directory_and_convert)
        self.button3_window = self.canvas.create_window(0, 0, window=self.button3, anchor='nw')


class RunPage(tk.Frame):
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


