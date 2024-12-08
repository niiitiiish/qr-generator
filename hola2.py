import qrcode
from PIL import Image, ImageTk
import os

import tkinter as tk
from tkinter import filedialog, messagebox

# Function to generate and display QR code
def generate_qr():
    url = entry_url.get()
    name = entry_name.get()

    if not url or not name:
        messagebox.showerror("Input Error", "Please enter both URL and name.")
        return

    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    # Add the URL data to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image with custom colors
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image with the specified name
    file_path = os.path.join(os.getcwd(), f"qr{name}.png")
    img.save(file_path)

    # Display the image in the GUI
    img_display = Image.open(file_path)
    img_display = img_display.resize((250, 250))  # Resize for display in GUI
    img_display = ImageTk.PhotoImage(img_display)

    label_image.config(image=img_display)
    label_image.image = img_display  # Keep reference to avoid garbage collection

    # Show success message
    messagebox.showinfo("Success", f"QR code saved as: {file_path}")

# Create the main application window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x450")  # Set window size

# Create and place widgets
label_url = tk.Label(root, text="Enter URL:")
label_url.pack(pady=10)
entry_url = tk.Entry(root, width=40)
entry_url.pack(pady=5)

label_name = tk.Label(root, text="Enter Name:")
label_name.pack(pady=10)
entry_name = tk.Entry(root, width=40)
entry_name.pack(pady=5)

button_generate = tk.Button(root, text="Generate QR Code", command=generate_qr)
button_generate.pack(pady=20)

# Label to display the generated QR code
label_image = tk.Label(root)
label_image.pack(pady=10)

# Run the application
root.mainloop()
