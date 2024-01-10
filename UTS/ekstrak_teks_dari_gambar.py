import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from pytesseract import pytesseract

class TextExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Extractor App")
        self.root.configure(bg="blueviolet")

        self.path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        self.path_to_image = None
        pytesseract.tesseract_cmd = self.path_to_tesseract

        self.create_widgets()

    def create_widgets(self):

        title_label = tk.Label(self.root, text="Ekstrak Text dari Gambar", bg="blueviolet", fg="azure1", font=("Areal", 25, "bold"))
        title_label.grid(row=0, column=0, padx=10, pady=10)

        choose_button = tk.Button(self.root, text="pilih gambar",font=("Arial", 10, "normal"), bg="azure1", fg="blueviolet", command=self.choose_image)
        choose_button.grid(row=1, column=0, padx=10, pady=10)

        try:
            if self.path_to_image:          
                img = Image.open(self.path_to_image)
                text = pytesseract.image_to_string(img)

                img.thumbnail((300, 300))
                img_tk = ImageTk.PhotoImage(img)
                image_label = tk.Label(self.root, image=img_tk)
                image_label.image = img_tk
                image_label.grid(row=2, column=0, padx=10, pady=10)

                text_label = tk.Label(self.root, text=f"Text yang diekstrak:\n{text}", bg="azure1", fg="blueviolet",font=("Areal", 10, "normal"))
                text_label.grid(row=3, column=0, padx=10, pady=10)

        except FileNotFoundError:
            error_label = tk.Label(self.root, text=f"File not found: {self.path_to_image}")
            error_label.grid(row=2, column=0, padx=10, pady=10)
        except Exception as e:
            error_label = tk.Label(self.root, text=f"Error: {str(e)}")
            error_label.grid(row=2, column=0, padx=10, pady=10)

    def choose_image(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.path_to_image = file_path
            self.create_widgets()

if __name__ == "__main__":
    root = tk.Tk()
    app = TextExtractorApp(root)
    root.mainloop()
