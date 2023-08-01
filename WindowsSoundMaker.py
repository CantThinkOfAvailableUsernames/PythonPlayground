import tkinter as tk
from winsound import PlaySound, SND_ASYNC

def play_error1():
    PlaySound("SystemHand", SND_ASYNC)

def play_error2():
    PlaySound("SystemAsterisk", SND_ASYNC)

def play_error3():
    PlaySound("WindowsLogon", SND_ASYNC)

def toggle_font(event):
    global font
    if font == "Calibri":
        font = "Segoe UI"
    elif font == "Segoe UI":
        font = "Comic Sans MS"
    elif font == "Comic Sans MS":
        font = "Arial"
    else:
        font = "Calibri"
    error1_button.config(font=(font, 20))
    error2_button.config(font=(font, 20))
    error3_button.config(font=(font, 20))

root = tk.Tk()
root.title("Windows Sound Maker")
root.geometry("450x200") #Resize the window to 450x200 pixels

#Create a frame to hold the buttons
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor='center')

font = "Calibri"

error1_button = tk.Button(frame, text="Error 1", command=play_error1, font=(font, 20))
error1_button.grid(row=0, column=0, padx=20, pady=20)

error2_button = tk.Button(frame, text="Error 2", command=play_error2, font=(font, 20))
error2_button.grid(row=0, column=1, padx=20, pady=20)

error3_button = tk.Button(frame, text="Sound 1", command=play_error3, font=(font, 20))
error3_button.grid(row=0, column=2, padx=20, pady=20)

root.bind("<Tab>", toggle_font)
root.mainloop()
