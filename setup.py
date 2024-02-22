from cx_Freeze import setup, Executable
import sys

# Define executables and build options
executables = [
    Executable("./offiz.py", base="Win32GUI", icon="idiot.ico")  # Replace "icon.ico" with your custom icon file
]

# Specify other options, such as including additional files
options = {
    "build_exe": {
        "includes": ["pygame", "tkinter", "PIL", "random", "keyboard", "sys", "time"],  # Include any additional modules
        "include_files": ["./idiot.gif", "./idiot.mp3"]  # Include the GIF and MP3 files
    }
}

try:
    setup(
        name="Offiz",
        version="1.0",
        description="Python recreation of the infamous You are an idiot (offiz) malware from the early 2000s",
        options=options,
        executables=executables
    )
except Exception as e:
    print("An error occurred:", e)
    sys.exit(1)  # Exit with a non-zero status code to indicate failure