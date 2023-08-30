import os
import pygame
import tkinter as tk
from tkinter import BooleanVar
from tkinter.ttk import Checkbutton

import random  # Import the random module

# Initialize Tkinter
root = tk.Tk()
root.title("Icon Bouncer Options")

# Fullscreen variable and resolution toggle
fullscreen_var = tk.IntVar()
native_res_var = BooleanVar()
native_res_var.set(False)

# Option to run in fullscreen
fullscreen_checkbox = tk.Checkbutton(root, text="Launch in Fullscreen", variable=fullscreen_var)
fullscreen_checkbox.pack()

# Option to run in native resolution
native_res_checkbox = Checkbutton(root, text="Run in Native Resolution (Fullscreen)", variable=native_res_var)
native_res_checkbox.pack()

# Start button callback
def start_game():
    root.destroy()  # Close the options window

# Start button
start_button = tk.Button(root, text="Start", command=start_game)
start_button.pack()

root.mainloop()

# Initialize Pygame
pygame.init()

# Set up screen
screen_width = 800
screen_height = 600

if fullscreen_var.get():
    if native_res_var.get():
        info = pygame.display.Info()
        screen_width = info.current_w
        screen_height = info.current_h
        screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
    else:
        screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((screen_width, screen_height))

# Set the window title
pygame.display.set_caption("Windows XP Icon Screen Saver (DVD style)")

# Specified folder containing icons
icon_folder = r"K:\Stuff\Windows XP High Resolution Icon Pack\Windows XP Icons"  # Replace with your folder path
icon_files = [f for f in os.listdir(icon_folder) if f.endswith(".png") or f.endswith(".jpg")]

# Load and filter icons, resizing to fit within the screen dimensions
icons = []
for file in icon_files:
    icon = pygame.image.load(os.path.join(icon_folder, file))
    icon = pygame.transform.scale(icon, (icon.get_width() // 4, icon.get_height() // 4))  # Scale down by a factor
    icons.append(icon)

# Choose a random icon and initial position
current_icon = random.choice(icons)
icon_size = current_icon.get_size()
icon_x = random.randint(0, screen_width - icon_size[0])
icon_y = random.randint(0, screen_height - icon_size[1])

# Initial velocity
velocity_x = 5
velocity_y = 3

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # Update icon position
    icon_x += velocity_x
    icon_y += velocity_y

    # Bounce off the screen edges
    if icon_x <= 0 or icon_x >= screen_width - icon_size[0]:
        velocity_x = -velocity_x
    if icon_y <= 0 or icon_y >= screen_height - icon_size[1]:
        velocity_y = -velocity_y

    screen.fill((0, 0, 0))  # Clear the screen

    # Blit the icon at the updated position
    screen.blit(current_icon, (icon_x, icon_y))

    pygame.display.flip()
    clock.tick(30)  # Adjust the frame rate as needed

pygame.quit()
