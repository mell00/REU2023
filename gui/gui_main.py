import tkinter as tk

def create_canvas():
    canvas = tk.Canvas(window, width=450, height=500)
    canvas.pack()

window = tk.Tk()
window.title("DNA Image Recognition")

window.mainloop()
create_canvas()








