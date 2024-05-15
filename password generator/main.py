import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip
from PIL import Image, ImageTk

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.bind("<Configure>", self.resize_background)

        # Background image
        self.background_image = Image.open("download.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Variables
        self.length_var = tk.IntVar(value=12)
        self.complexity_var = tk.StringVar(value="Medium")
        self.password_var = tk.StringVar()

        # Create a custom style for buttons
        self.button_style = ttk.Style()
        self.button_style.configure("Custom.TButton", font=("Arial", 14))

        # UI Elements
        ttk.Label(root, text="Password Length:", background="white", font=("Arial", 16)).place(relx=0.5, rely=0.4, anchor="center")
        self.length_entry = ttk.Entry(root, textvariable=self.length_var, font=("Arial", 14))
        self.length_entry.place(relx=0.5, rely=0.45, anchor="center")

        ttk.Label(root, text="Complexity:", background="white", font=("Arial", 16)).place(relx=0.5, rely=0.5, anchor="center")
        self.complexity_combobox = ttk.Combobox(root, values=["Low", "Medium", "High"], textvariable=self.complexity_var, state="readonly", font=("Arial", 14))
        self.complexity_combobox.place(relx=0.5, rely=0.55, anchor="center")

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password, style="Custom.TButton")
        self.generate_button.place(relx=0.5, rely=0.6, anchor="center")

        self.password_entry = ttk.Entry(root, textvariable=self.password_var, state="readonly", font=("Arial", 14))
        self.password_entry.place(relx=0.5, rely=0.65, anchor="center")

        self.copy_button = ttk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard, style="Custom.TButton")
        self.copy_button.place(relx=0.5, rely=0.7, anchor="center")
        self.copy_button.config(state="disabled")

        # Add spacing between elements
        self.add_spacing(root, 0.73)

        # Set window size
        self.root.geometry(f"{self.background_image.width}x{self.background_image.height}")

    def add_spacing(self, root, rely):
        ttk.Label(root, text="", background="white").place(relx=0.5, rely=rely, anchor="center")

    def generate_password(self):
        length = self.length_var.get()
        complexity = self.complexity_var.get()

        if complexity == "Low":
            characters = string.ascii_letters + string.digits
        elif complexity == "Medium":
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            characters = string.ascii_letters + string.digits + string.punctuation + "£$%^&*()_+~`|}{[]\:;?><,./-="

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)
        self.copy_button.config(state="normal")

    def copy_to_clipboard(self):
        password = self.password_var.get()
        pyperclip.copy(password)
        messagebox.showinfo("Info", "Password copied to clipboard!")

    def resize_background(self, event):
        width = event.width
        height = event.height
        resized_image = self.background_image.resize((width, height), Image.ANTIALIAS)
        self.background_photo = ImageTk.PhotoImage(resized_image)
        self.background_label.configure(image=self.background_photo)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
