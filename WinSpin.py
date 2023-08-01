import tkinter as tk
import math

R = 0
x1 = 0.1
y1 = 0.05
x2 = 0.25
y2 = 0.24
x3 = 1.6
y3 = 0.24
x4 = 300
y4 = 200
x5 = 300
y5 = 200

root = tk.Tk()
root.geometry("400x400")

windows = []
for i in range(12):
    window = tk.Toplevel(root)
    window.geometry("100x100")
    windows.append(window)

def update_windows():
    global R
    for i, window in enumerate(windows):
        x = int(math.sin(R*x1 + i*x2 + x3) * x4 + x5)
        y = int(math.cos(R*y1 + i*y2 + y3) * y4 + y5)
        window.geometry("+{}+{}".format(x, y))
    R += 1
    root.after(5, update_windows)

update_windows()
root.mainloop()
