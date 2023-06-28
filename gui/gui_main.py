import tkinter as tk
from PIL import Image, ImageTk

def create_canvas():
    canvas = tk.Canvas(window, width=450, height=500)
    canvas.pack()

window = tk.Tk()
window.title("DNA Image Recognition")
ico = Image.open('dnaicon.jpg')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)

window.mainloop()
create_canvas()








