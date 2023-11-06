import tkinter
from tkinter import END


def calculate():

    luas_limas_entry.delete(0, END)
    volume_entry.delete(0, END)

    try:
        tinggi_limas = float(tinggi_entry.get())
        panjang_alas = float(panjang_entry.get())

        luas_segitiga = (1/2) * panjang_alas * tinggi_limas
        luas_alas = panjang_alas**2
        luas_limas = luas_segitiga + luas_segitiga + luas_segitiga + luas_segitiga + luas_alas
        volume = (1/3) * luas_alas * tinggi_limas

        luas_limas_entry.insert(0, round(luas_limas, 2))
        volume_entry.insert(0, round(volume, 2))
    except ValueError:
        pass

# print("Limas Segiempat\n")

# tinggi limas = 5
# panjang alas = 7

# luas_segitiga = (1/2) * p * T
# luas_alas = p**2
# luas_limas = luas_segitiga + luas_segitiga + luas_segitiga + luas_segitiga + luas_alas
# volume = (1/3) * luas_alas * T

# print(f"luas limas segiempat : {round(luas_limas, 2)}")
# print(f"volume limas segiempat : {round(volume, 2)}")

# ----------------------------- UI ------------------------------------ #

window = tkinter.Tk()
window.title("Limas Segiempat")
window.minsize(400, 400)
window.config(padx=10, pady=10)

# LABEL
title_label = tkinter.Label(text="Limas Segiempat")
tinggi_label = tkinter.Label(text="Tinggi Limas")
panjang_label = tkinter.Label(text="Panjang Alas")
hasil_label = tkinter.Label(text="Hasil")
luas_limas_label = tkinter.Label(text="Luas Limas")
volume_label = tkinter.Label(text="Volume")

title_label.grid(row=0, column=1, columnspan=2, pady=10)
tinggi_label.grid(row=1, column=0, padx=5, sticky=tkinter.W)
panjang_label.grid(row=2, column=0, padx=5, sticky=tkinter.W)
hasil_label.grid(row=3, column=1, columnspan=2, pady=10)
luas_limas_label.grid(row=4, column=0, padx=5, sticky=tkinter.W)
volume_label.grid(row=5, column=0, padx=5, sticky=tkinter.W)

# ENTRY
tinggi_entry = tkinter.Entry(width=40)
panjang_entry = tkinter.Entry(width=40)
luas_limas_entry = tkinter.Entry(width=40)
volume_entry = tkinter.Entry(width=40)

tinggi_entry.grid(row=1, column=1, columnspan=2)
panjang_entry.grid(row=2, column=1, columnspan=2)
luas_limas_entry.grid(row=4, column=1, columnspan=2)
volume_entry.grid(row=5, column=1, columnspan=2)

# BUTTON
calculate_button = tkinter.Button(text="calculate", width=10, height=8, command=calculate)
calculate_button.grid(row=1, column=3, rowspan=8, padx=5)



window.mainloop()
