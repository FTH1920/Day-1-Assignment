from googletrans import Translator
import tkinter
from tkinter import END


def id_to_en():

    entry_result.delete(0, tkinter.END)    

    text = entry_text.get()
    translator = Translator()
    translation = translator.translate(text=text, src='id', dest='en')
    
    entry_result.insert(0, translation.text)


def en_to_id():

    entry_result.delete(0, tkinter.END)    

    text = entry_text.get()
    translator = Translator()
    translation = translator.translate(text=text, src='en', dest='id')
    
    entry_result.insert(0, translation.text)


# ---------------------------------- UI ----------------------------------------- #

window = tkinter.Tk()
window.title("Google Translate")
window.minsize(400, 250)

label_title = tkinter.Label(text="Google Translate", font=("Arial", 20, "bold"))
label_title.pack(pady=10)

label_text = tkinter.Label(text="Insert Text:")
label_text.pack()

entry_text = tkinter.Entry(width=25)
entry_text.pack()

button_id_en = tkinter.Button(text="id to en", command=id_to_en)
button_id_en.pack()

button_en_id = tkinter.Button(text="en to id", command=en_to_id)
button_en_id.pack()

label_result = tkinter.Label(text="Result:")
label_result.pack()

entry_result = tkinter.Entry(width=25)
entry_result.pack()

window.mainloop()
