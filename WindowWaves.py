import tkinter as tk
import math
import random

R = 0
x1 = 0.1
y1 = 0.05
x2 = 0.25
y2 = 0.24
x3 = 1.6
y3 = 0.24
x4 = 50
y4 = 50
x5 = 0
y5 = 100

root = tk.Tk()
root.withdraw()

windows = []
for i in range(20):
    window = tk.Toplevel(root)
    window.geometry("{}x100".format(root.winfo_screenwidth() // 20))
    window.overrideredirect(True)
    window.lift()
    windows.append(window)

def update_windows():
    global R
    for i, window in enumerate(windows):
        x = i * (root.winfo_screenwidth() // 20)
        y = int(math.sin(R*x1 + i*x2 + x3) * x4 + y5)
        window.geometry("+{}+{}".format(x, y))
    R += 0.1
    root.after(5, update_windows)

def change_color(event):
    for window in windows:
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        window.config(bg=color)

root.bind("<Tab>", change_color)

update_windows()
root.mainloop()
