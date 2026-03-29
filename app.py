import customtkinter as ctk
from tkinter import filedialog
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

selected_files = []

def select_images():
    global selected_files
    files = filedialog.askopenfilenames(
        filetypes=[("Images", "*.jpg *.jpeg *.png")]
    )

    if files:
        selected_files = list(files)
        update_list()
        status_label.configure(text="Images selected ✅")

def update_list():
    listbox.delete(0, "end")
    for file in selected_files:
        listbox.insert("end", file.split("/")[-1])

def convert_to_pdf():
    if not selected_files:
        status_label.configure(text="No images selected ❌")
        return

    images = []
    for file in selected_files:
        img = Image.open(file).convert("RGB")
        images.append(img)

    save_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")]
    )

    if save_path:
        images[0].save(save_path, save_all=True, append_images=images[1:])
        status_label.configure(text="PDF Created Successfully 🎉")

# UI Window
app = ctk.CTk()
app.title("Image to PDF Pro")
app.geometry("600x500")

# Title
title = ctk.CTkLabel(app, text="📄 Image to PDF Converter",
                     font=("Arial", 20, "bold"))
title.pack(pady=15)

# Buttons Frame
frame = ctk.CTkFrame(app)
frame.pack(pady=10)

select_btn = ctk.CTkButton(frame, text="Select Images",
                           command=select_images)
select_btn.grid(row=0, column=0, padx=10)

convert_btn = ctk.CTkButton(frame, text="Convert to PDF",
                            command=convert_to_pdf)
convert_btn.grid(row=0, column=1, padx=10)

# Listbox (Selected Images)
listbox = ctk.CTkTextbox(app, height=150, width=500)
listbox.pack(pady=10)

# Status
status_label = ctk.CTkLabel(app, text="")
status_label.pack(pady=10)

app.mainloop()