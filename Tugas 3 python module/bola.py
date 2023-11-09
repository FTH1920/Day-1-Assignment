import tkinter
from tkinter import END
from math import pi


def bola():

    def calculate():

        luas_lingkaran_entry.delete(0, END)
        luas_bola_entry.delete(0, END)
        volume_entry.delete(0, END)

        try:
            jari = float(jari_entry.get())
            luas_lingkaran = pi * jari**2
            luas_bola = 4 * luas_lingkaran
            volume = ((4/3) * pi * jari**3)

            luas_lingkaran_entry.insert(0, str(round(luas_lingkaran, 2)))
            luas_bola_entry.insert(0, str(round(luas_bola, 2)))
            volume_entry.insert(0, str(round(volume, 2)))
        except ValueError:
            pass


# ----------------------------- UI SETUP ------------------------------- #

    window = tkinter.Tk()
    window.title("Bola")
    window.minsize(400, 400)
    window.config(padx=10, pady=10)

    # LABEL
    title_label = tkinter.Label(text="Bola")
    jari_label = tkinter.Label(text="Jari-jari")
    luas_lingkaran_label = tkinter.Label(text="Luas lingkaran")
    hasil_label = tkinter.Label(text="Hasil")
    luas_bola_label = tkinter.Label(text="Luas bola")
    volume_label = tkinter.Label(text="Volume")

    title_label.grid(row=0, column=1, columnspan=2, pady=10)
    jari_label.grid(row=1, column=0, sticky=tkinter.W, padx=5)
    hasil_label.grid(row=3, column=1, columnspan=2, pady=10)
    luas_lingkaran_label.grid(row=4, column=0, sticky=tkinter.W, padx=5)
    luas_bola_label.grid(row=5, column=0, sticky=tkinter.W, padx=5)
    volume_label.grid(row=6, column=0, sticky=tkinter.W, padx=5)

    # ENTRY
    jari_entry = tkinter.Entry(width=40)
    luas_lingkaran_entry = tkinter.Entry(width=40)
    luas_bola_entry = tkinter.Entry(width=40)
    volume_entry = tkinter.Entry(width=40)

    jari_entry.grid(row=1, column=1, columnspan=2)
    luas_lingkaran_entry.grid(row=4, column=1, columnspan=2)
    luas_bola_entry.grid(row=5, column=1, columnspan=2)
    volume_entry.grid(row=6, column=1, columnspan=2)

    # BUTTON
    calculate_button = tkinter.Button(width=10, height=7, text="Calculate", command=calculate)
    calculate_button.grid(row=1, column=4, rowspan=7, padx=5)

    jari_entry.focus()

    window.mainloop()
