import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import pygame
import keyboard
import sys
import time

class AnimatedGif(tk.Label):
    def __init__(self, master=None, **kw):
        self._anim = None
        self._frame = None
        self._delay = None
        self._callback_id = None
        self._idx = 0
        self._images = []

        super().__init__(master, **kw)

    def load(self, gif_path):
        self._anim = Image.open(gif_path)
        try:
            self._delay = self._anim.info['duration']
        except KeyError:
            self._delay = 100

        for frame in range(0, self._anim.n_frames):
            self._anim.seek(frame)
            self._images.append(ImageTk.PhotoImage(self._anim.copy()))

        self._frame = self._images[0]
        self.config(image=self._frame)

    def start_animation(self):
        self._idx = 0
        self._animate()

    def _animate(self):
        self.config(image=self._images[self._idx])
        self._idx += 1
        if self._idx == len(self._images):
            self._idx = 0
        self._callback_id = self.after(self._delay, self._animate)

    def stop_animation(self):
        if self._callback_id is not None:
            self.after_cancel(self._callback_id)
            self._callback_id = None

def move_window(window):
    x = random.randint(0, window.winfo_screenwidth() - window.winfo_reqwidth())
    y = random.randint(0, window.winfo_screenheight() - window.winfo_reqheight())
    window.geometry("+{}+{}".format(x, y))
    window.after(2000, move_window, window)  # Update position every 2 seconds

def clone_window():
    play_music()
    def on_close_clone():
        clone_window()
        clone_window()

    def on_minimize_clone():
        clone_window()

    new_window = tk.Toplevel()
    new_window.title("Clone Window")
    new_window.bind("<Escape>", check_keys)
    
    # Load GIF and get its dimensions
    gif_image = Image.open("C:/Users/29JHANNI/OneDrive - Davis School District/Documents/PythonIdiots/Idiot.gif")
    gif_width, gif_height = gif_image.size

    # Set geometry to match GIF size
    new_window.geometry("{}x{}".format(gif_width, gif_height))
    
    new_window.resizable(False, False)  # Prevent resizing
    
    # Load and display GIF
    gif_widget = AnimatedGif(new_window)
    gif_widget.pack()
    gif_widget.load("./Idiot.gif")
    gif_widget.start_animation()

    move_window(new_window)  # Start moving the clone

    # Bind close event
    new_window.protocol("WM_DELETE_WINDOW", on_close_clone)

    # Bind minimize event
    new_window.protocol("WM_ICONIFY", on_minimize_clone)

def on_close():
    clone_window()
    clone_window()
    pygame.mixer.music.stop()  # Stop playing the music
def on_delete_window():
    messagebox.showinfo("Information", "To close the script in the future, use the provided close button.")

def play_music():
    pygame.mixer.music.load("./idiot.mp3")
    pygame.mixer.music.play(-1)  # Loop the music indefinitely
    
#Check if failsafe is activated
def check_keys(event):
    if event.keysym == "Escape":
        print("Terminating process...")
        sys.exit(0)
        
def force_focus():
    root.focus_set()
        
# Main loop for creating and managing Tkinter windows
root = tk.Tk()
root.overrideredirect(True)  # Remove window decorations (title bar, etc.)
root.attributes("-topmost", True)  # Keep window on top


# Load GIF and get its dimensions
gif_image = Image.open("C:/Users/29JHANNI/OneDrive - Davis School District/Documents/PythonIdiots/Idiot.gif")
gif_width, gif_height = gif_image.size

# Set geometry to match GIF size
root.geometry("{}x{}".format(gif_width, gif_height))

# Load and display GIF for root window
root_gif_widget = AnimatedGif(root)
root_gif_widget.pack()
root_gif_widget.load("C:/Users/29JHANNI/OneDrive - Davis School District/Documents/PythonIdiots/Idiot.gif")
root_gif_widget.start_animation()

close_button = tk.Button(root, text="X", command=on_close, bg="red", fg="white", relief="flat", activebackground="darkred", activeforeground="white", width=2, height=1)
close_button.place(relx=1, rely=0, anchor="ne")

clone_button = tk.Button(root, text="Clone!", command=clone_window)
clone_button.pack()

move_window(root)  # Start moving the root window

root.protocol("WM_DELETE_WINDOW", on_delete_window)  # Bind function to window close event

root.after(100, force_focus)

root.bind("<Escape>", check_keys)

# Initialize pygame mixer
pygame.mixer.init()

# Play the music
play_music()

root.mainloop()



while True:
    force_focus()  # Force focus to root window
    root.update()  # Update the Tkinter window
    time.sleep(0.1)  # Sleep for a short duration to avoid high CPU usage
