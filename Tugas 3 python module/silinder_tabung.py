import tkinter
from tkinter import END
from math import pi


def silinder_tabung():
    def calculate():

        luas_selimut_entry.delete(0, END)
        luas_permukaan_entry.delete(0, END)
        volume_entry.delete(0, END)

        try:
            tinggi = float(tinggi_entry.get())
            jari = float(jari_entry.get())
            luas_selimut = 2 * pi * jari * tinggi
            luas_permukaan = (2 * jari * tinggi) + (2 * pi * jari**2)
            volume = pi * jari**2 * tinggi

            luas_selimut_entry.insert(0, str(round(luas_selimut, 2)))
            luas_permukaan_entry.insert(0, str(round(luas_permukaan, 2)))
            volume_entry.insert(0, str(round(volume, 2)))
        except ValueError:
            pass

    # print("Silinder Tabung\n")

    # PI = 3.14

    # T = 5
    # r = 7

    # luas_selimut = 2 * PI * r * T
    # luas_permukaan = (2 * r * T) + (2 * PI * r**2)
    # volume = PI * r**2 *T

    # print(f"Luas selimut : {round(luas_selimut, 2)}")
    # print(f"Luas permukaan: {round(luas_permukaan, 2)}")
    # print(f"Volume : {round(volume, 2)}")

# ---------------------------- UI ----------------------------------- #

    window = tkinter.Tk()
    window.title("Silinder Tabung")
    window.minsize(400, 400)
    window.config(padx=10, pady=10)

    # LABEL
    title_label = tkinter.Label(text="Silinder Tabung")
    tinggi_label = tkinter.Label(text="Tinggi")
    jari_label = tkinter.Label(text="Jari-jari")
    hasil_label = tkinter.Label(text="Hasil")
    luas_selimut_label = tkinter.Label(text="Luas Selimut")
    luas_permukaan_label = tkinter.Label(text="Luas Permukaan")
    volume_label = tkinter.Label(text="Volume")

    title_label.grid(row=0, column=1, columnspan=2, pady=10)
    tinggi_label.grid(row=1, column=0, padx=5, sticky=tkinter.W)
    jari_label.grid(row=2, column=0, padx=5, sticky=tkinter.W)
    hasil_label.grid(row=3, column=1, columnspan=2, pady=1)
    luas_selimut_label.grid(row=4, column=0, padx=5, sticky=tkinter.W)
    luas_permukaan_label.grid(row=5, column=0, padx=5, sticky=tkinter.W)
    volume_label.grid(row=6, column=0, padx=5, sticky=tkinter.W)

    # ENTRY
    tinggi_entry = tkinter.Entry(width=40)
    jari_entry = tkinter.Entry(width=40)
    luas_selimut_entry = tkinter.Entry(width=40)
    luas_permukaan_entry = tkinter.Entry(width=40)
    volume_entry = tkinter.Entry(width=40)

    tinggi_entry.grid(row=1, column=1, columnspan=2)
    jari_entry.grid(row=2, column=1, columnspan=2)
    luas_selimut_entry.grid(row=4, column=1, columnspan=2)
    luas_permukaan_entry.grid(row=5, column=1, columnspan=2)
    volume_entry.grid(row=6, column=1, columnspan=2)

    # BUTTON
    calculate_button = tkinter.Button(text="Calculate", width=10, height=8, command=calculate)
    calculate_button.grid(row=1, column=3, rowspan=8, padx=5)

    window.mainloop()
