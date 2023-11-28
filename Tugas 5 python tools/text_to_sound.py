from gtts import gTTS 
from playsound import playsound
import tkinter


def textsound():

    mytext = entry_text.get()
    language = 'id'
    myobj = gTTS(text=mytext, lang=language, slow=False) 

    myobj.save("textsound/soundobj.mp3") 
    playsound("textsound/soundobj.mp3", True)

# ----------------------------- UI -------------------------------- #

window = tkinter.Tk()
window.minsize(400, 200)
window.title("Text to Sound")

label_title = tkinter.Label(text="Text --> Sound", font=("Arial", 24, "bold"))
label_title.pack(pady=15)

label_insert = tkinter.Label(text="Masukan text:")
label_insert.pack()

entry_text = tkinter.Entry(width=30)
entry_text.pack()

button_confirm = tkinter.Button(text="Confirm", command=textsound, width=25)
button_confirm.pack()

window.mainloop()