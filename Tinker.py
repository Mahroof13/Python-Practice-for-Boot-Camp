import tkinter as tk

def say_hello():
    print("Hello, World!")

window = tk.Tk()
window.title("My GUI")

label = tk.Label(window, text="Welcome to my GUI!")
label.pack()

button = tk.Button(window, text="Click me!", command=say_hello)
button.pack()

window.mainloop()

# Entry box widget
import tkinter as tk
window = tk.Tk()
window.title("GUI")
window.geometry('350x200')
label = tk.Label(window, text="Hello", font=("arial bold", 20))
label.grid(column=0, row=0)
text = tk.Entry(window, width=10)
text.grid(column=1, row=1)
def clicked1():
    res = "Welcome to " + text.get()
    label.configure(text=res)
button = tk.Button(window, text="Enter", command=clicked1, bg="red", fg="black")
button.grid(column=2, row=1)
window.mainloop()

# combobox widget

import tkinter as tk
from tkinter.ttk import Combobox

# Initialize the main window
window = tk.Tk()

# Set the title of the window
window.title("GUI")

# Set the size of the window
window.geometry('350x200')

# Create and place the combobox using the grid method
combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Text")
combo.current(3)  # Set the default selected item
combo.grid(column=0, row=0)

# Start the Tkinter event loop
window.mainloop()

# Check button

import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Checkbutton Example")

# Set the size of the window
window.geometry('350x200')

# Create a BooleanVar and set it to True
check_state = tk.BooleanVar()
check_state.set(True)

# Create a Checkbutton widget
check = tk.Checkbutton(window, text="Select", variable=check_state)
check.grid(column=0, row=0)

# Start the Tkinter event loop
window.mainloop()

# Radio Button Example

import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Radio Button Example")

# Set the size of the window
window.geometry('350x200')

# Create a StringVar to hold the value of the selected radio button
selection = tk.StringVar()

# Create radio buttons and bind them to the selection variable
radio1 = tk.Radiobutton(window, text="BMW", variable=selection, value="BMW")
radio2 = tk.Radiobutton(window, text="Mercedes Benz", variable=selection, value="Mercedes Benz")
radio3 = tk.Radiobutton(window, text="Audi", variable=selection, value="Audi")

# Grid placement for the radio buttons
radio1.grid(column=0, row=0)
radio2.grid(column=1, row=0)
radio3.grid(column=2, row=0)

# Run the application
window.mainloop()

# Scrolled Text

import tkinter as tk
from tkinter import scrolledtext

# Create the main window
window = tk.Tk()
window.title("ScrolledText Example")

# Create a ScrolledText widget
text = scrolledtext.ScrolledText(window, width=40, height=10)
text.pack(padx=10, pady=10)

# Insert some text into the ScrolledText widget
text.insert(tk.INSERT, "Hello Python")

# Run the Tkinter event loop
window.mainloop()

# Message box widget

import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Message Box Widget example")

# Set the size of the window
window.geometry('350x200')

# Function to be called when the button is clicked
def clicked2():
    messagebox.showinfo("GUI", "Graphical user interface (GUI) is an interface that is drawn on the screen for the user to interact with.")

# Create the button and assign the function to be called on click
button = tk.Button(window, text="ENTER", command=clicked2)
button.pack(pady=20)  # Adds some padding to position the button

# Start the Tkinter event loop
window.mainloop()

# Spinbox Widget

import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Spinbox widget example")

# Create the Spinbox widget
spin = tk.Spinbox(window, from_=0, to=100, width=5)
spin.pack(pady=10)  # Adds some padding to position the Spinbox

# Start the Tkinter event loop
window.mainloop()
