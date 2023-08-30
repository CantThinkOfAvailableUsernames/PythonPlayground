import tkinter as tk
import random

def move_elements():
    for element in elements:
        dx = random.randint(-5, 5)
        dy = random.randint(-5, 5)
        canvas.move(element, dx, dy)
    window.after(100, move_elements)

def close_window(event):
    if event.keysym == '9' and event.state == 12:  # Ctrl+Shift+A+9
        window.destroy()

window = tk.Tk()
window.attributes('-fullscreen', True)
window.bind('<KeyPress>', close_window)

canvas = tk.Canvas(window, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# Create a random button
button_text = "Random Button"
button = tk.Button(window, text=button_text)
button_window = canvas.create_window(random.randint(50, window.winfo_screenwidth() - 150),
                                     random.randint(50, window.winfo_screenheight() - 150),
                                     window=button)

# Create a blue circle
circle = canvas.create_oval(random.randint(50, window.winfo_screenwidth() - 100),
                            random.randint(50, window.winfo_screenheight() - 100),
                            random.randint(100, window.winfo_screenwidth() - 50),
                            random.randint(100, window.winfo_screenheight() - 50),
                            fill="blue")

# Create the letter 'A'
element_text = "A"
element = canvas.create_text(window.winfo_screenwidth() // 2, window.winfo_screenheight() // 2,
                             text=element_text, font=("Arial", 20))

elements = [button_window, circle, element]
move_elements()

window.mainloop()
