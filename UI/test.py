import tkinter as tk

def on_button_click(param):
    print(f"Button clicked with parameter: {param}")

# Create the main window
root = tk.Tk()

# Create a Button and use a lambda to pass a parameter
button = tk.Button(root, text="Click Me", command=lambda: on_button_click("Hello, world!"))
button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
