import tkinter as tk
import subprocess
import random

def initiate_shutdown():
    subprocess.run(["shutdown", "/s", "/t", "60"])

def cancel_shutdown():
    subprocess.run(["shutdown", "/a"])

def get_random_message():
    messages = [
        "-" * 55 + "\n" +
        "            Windows has encountered an error\n" +
        "-" * 55 + "\n\n" +
        "To prevent further damage, Windows must shut down now.\n\n" +
        "Error Code: 0x0A4F2\n\n" +
        "Please save your work. Restart your computer after shutdown.\n\n" +
        "Contact our support for assistance if the issue persists.\n\n" +
        "Thank you.\n\n" +
        "- Windows Team\n" +
        "-" * 55,

        "-" * 55 + "\n" +
        "      Windows has encountered a critical issue\n" +
        "-" * 55 + "\n\n" +
        "To avoid system damage, Windows will now shut down.\n\n" +
        "Error Code: 0x8B19\n\n" +
        "Please save any unsaved work immediately.\n\n" +
        "For further help, contact our support team.\n\n" +
        "Thank you for your understanding.\n\n" +
        "- The Windows Team\n" +
        "-" * 55
    ]

    return random.choice(messages)

def main():
    root = tk.Tk()
    root.title("Error Simulator")

    message = get_random_message()

    label = tk.Label(root, text=message, padx=20, pady=20)
    label.pack()

    button_frame = tk.Frame(root)
    button_frame.pack()

    shutdown_button = tk.Button(button_frame, text="Shutdown", command=initiate_shutdown)
    shutdown_button.pack(side=tk.LEFT, padx=5)

    cancel_button = tk.Button(button_frame, text="Cancel", command=root.destroy)
    cancel_button.pack(side=tk.LEFT, padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()
