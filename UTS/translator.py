from googletrans import Translator
import tkinter as tk
from tkinter import ttk, END

def translate_text():
    entry_result.delete(0, END)
    
    text = entry_text.get()
    src_lang = src_language.get()
    dest_lang = dest_language.get()

    translator = Translator()
    translation = translator.translate(text=text, src=src_lang, dest=dest_lang)

    entry_result.insert(0, translation.text)


# ---------------------------------- UI ----------------------------------------- #

window = tk.Tk()
window.title("Google Translate")
window.geometry("500x350") 
window.resizable(False, False) 

# Set background color
window.configure(bg='#EFEFEF') 

label_title = tk.Label(window, text="Google Translate", font=("Arial", 20, "bold"), bg='#EFEFEF')
label_title.pack(pady=10)

label_text = tk.Label(window, text="Insert Text:", bg='#EFEFEF')
label_text.pack()

entry_text = tk.Entry(window, width=35) 
entry_text.pack()

src_language_label = tk.Label(window, text="From Language:", bg='#EFEFEF')
src_language_label.pack()

src_languages = ["id", "en", "jv", "su"]  
src_language = tk.StringVar()
src_language.set(src_languages[0])  

src_language_menu = ttk.OptionMenu(window, src_language, *src_languages)
src_language_menu.pack()

dest_language_label = tk.Label(window, text="To Language:", bg='#EFEFEF')
dest_language_label.pack()

dest_languages = ["en", "id", "jv", "su"]  
dest_language = tk.StringVar()
dest_language.set(dest_languages[0])  

dest_language_menu = ttk.OptionMenu(window, dest_language, *dest_languages)
dest_language_menu.pack()


translate_button = tk.Button(window, text="Translate", command=translate_text)

label_result = tk.Label(window, text="Result:", bg='#EFEFEF')
label_result.pack()

entry_result = tk.Entry(window, width=35) 
entry_result.pack()

window.mainloop()

