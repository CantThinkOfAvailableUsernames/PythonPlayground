import random
import string
import tkinter as tk
from tkinter import filedialog

def replace_letter(text):
    symbol = "█"
    letter = random.choice(string.ascii_lowercase)
    return text.replace(letter, symbol)

def main():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("Text files", "*.txt"), ("all files", "*.*")))
    with open(file_path, "r") as f:
        text = f.read()

    corrupted_text = replace_letter(text)
    print("⚠️ WARNING: This document might be corrupted ⚠️")
    print(corrupted_text)

if __name__ == "__main__":
    main()
