import tkinter as tk
import time
import pygame
import requests
from io import BytesIO

# Function to download a sound from a URL
def download_sound(url):
    response = requests.get(url)
    return BytesIO(response.content)

# Function to set the alarm and trigger sound
def set_alarm():
    # Get the alarm time from the entry field
    alarm_time = entry.get()

    # Keep checking the current time until it matches the alarm time
    while time.strftime("%H:%M") != alarm_time:
        # Update the displayed time
        time_label.config(text=time.strftime("%H:%M"))
        root.update()
        time.sleep(1)

    # Play the alarm sound when the alarm time is reached
    play_alarm_sound()

# Function to play the alarm sound
def play_alarm_sound():
    pygame.mixer.init()

    # URL to the sound file
    sound_url = "http://david.guerrero.free.fr/Effects/WeaponHoming.wav"
    sound_data = download_sound(sound_url)

    # Load and play the sound indefinitely
    pygame.mixer.music.load(sound_data)
    pygame.mixer.music.play(-1)

# Function to stop the alarm sound
def stop_alarm_sound():
    pygame.mixer.music.stop()

# Create the main application window
root = tk.Tk()
root.title("Simple Alarm Clock")

# Create a canvas for the window
canvas = tk.Canvas(root, width=300, height=250, bg="#F0F0F0")
canvas.pack()

# Create a frame within the canvas
frame = tk.Frame(root, bg="#F0F0F0")
frame.place(relwidth=1, relheight=1)

# Create a label to display "Current Time:"
current_time_label = tk.Label(frame, text="Current Time:", font=("Helvetica", 14, "bold"), bg="#F0F0F0")
current_time_label.pack(pady=(20, 0))

# Create a label to display the current time
time_label = tk.Label(frame, text="", font=("Helvetica", 24), bg="#F0F0F0")
time_label.pack()

# Create an entry field for setting the alarm time
entry = tk.Entry(frame, font=("Helvetica", 16))
entry.pack(pady=10)

# Create a button to set the alarm
set_button = tk.Button(frame, text="Set Alarm", command=set_alarm, font=("Helvetica", 12), bg="#FF4C4C", fg="white")
set_button.pack()

# Create a button to stop the alarm sound
stop_button = tk.Button(frame, text="Stop Alarm", command=stop_alarm_sound, font=("Helvetica", 12), bg="#FF4C4C", fg="white")
stop_button.pack()

# Start the main event loop
root.mainloop()
