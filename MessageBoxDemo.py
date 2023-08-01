import tkinter.messagebox as msgbox

msgbox.showinfo("ERROR", "Hi!")
msgbox.showinfo("mmmm yum", "chicken nugget")
msgbox.showwarning("ERROR","That's What I Had To Say.")
msgbox.showerror("ERROR", "ERROR")

for i in range(21, -1, -1):
    msgbox.showerror("ERROR", str(i))

msgbox.showerror("ERROR", "This Causes An Error!")
msgbox.showerror("ERROR", "ERROR")
msgbox.showerror("ERROR", "Told Ya.")
msgbox.showinfo("ERROR","I learned a new trick today.")
msgbox.askquestion("ERROR?", "Do you know it?")
msgbox.askretrycancel("I changed!", "It didn't work.")
msgbox.askyesno("ERROR", "What should I do next?")
