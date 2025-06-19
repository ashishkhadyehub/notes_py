import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First GUI")
root.geometry("300x150")  # Width x Height

# Define a function to run on button click
def say_hello():
    label.config(text="Hello, Tkinter!")

# Add a label and a button
label = tk.Label(root, text="Click the button")
label.pack(pady=10)

button = tk.Button(root, text="Click Me", command=say_hello)
button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
