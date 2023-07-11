import tkinter as tk
from PIL import Image, ImageTk
import subprocess
from uploadgui import *
from convert_gui import *

class SettingsPage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.create_canvas()
        self.create_buttons()

    def create_canvas(self):
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill="both", expand=True)
        self.front_image = Image.open("settings.png")
        self.canvas.bind("<Configure>", self.resize_image)
        image_tk = ImageTk.PhotoImage(self.front_image)
        self.image_canvas = self.canvas.create_image(0, 0, anchor="nw", image=image_tk)

    def resize_image(self, event=None):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        if canvas_width > 0 and canvas_height > 0:
            max_width = canvas_width
            max_height = canvas_height
            original_width = self.front_image.width
            original_height = self.front_image.height
            width_ratio = max_width / original_width
            height_ratio = max_height / original_height
            scaling_factor = min(width_ratio, height_ratio)
            new_width = int(original_width * scaling_factor)
            new_height = int(original_height * scaling_factor)
            front_image_resized = self.front_image.resize((new_width, new_height), Image.LANCZOS)
            image_tk = ImageTk.PhotoImage(front_image_resized)
            self.canvas.itemconfig(self.image_canvas, image=image_tk)
            self.canvas.image = image_tk

    def create_buttons(self):
        self.geometry("450x350")
        button1 = tk.Button(self, text="Run", height=2, width=5, command=lambda: self.controller.show_page("Loading"))
        button1.place(x=420, y=192)

        button2 = tk.Button(self, text="Select file", height=2, width=5, command=open_file)
        button2.place(x=341, y=267)


if __name__ == "__main__":
    app = MyApp()
window.mainloop()