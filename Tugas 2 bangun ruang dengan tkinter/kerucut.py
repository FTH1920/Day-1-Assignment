import tkinter
from tkinter import END
from math import pi

def calculate():

    luas_selimut_entry.delete(0, END)
    luas_permukaan_entry.delete(0, END)
    volume_entry.delete(0, END)

    try:
        garis = float(garis_entry.get())
        tinggi = float(tinggi_entry.get())
        jari = float(jari_entry.get())

        luas_selimut = pi * jari * garis
        luas_permukaan = luas_selimut + pi * jari**2
        volume = ((1/3) * pi * jari**2 * tinggi)

        luas_selimut_entry.insert(0, round(luas_selimut, 2))
        luas_permukaan_entry.insert(0, round(luas_permukaan, 2))
        volume_entry.insert(0, round(volume, 2))
    except ValueError:
        pass

# garis_pelukis_S = 5
# t = 7
# r = 9

# luas_selimut = PI * r * s
# luas_permukaan = (PI * r * s) + (PI * r**2)
# volume = ((1/3) * PI * r**2 * t)

# print(f"luas_selimut : {luas_selimut}")
# print(f"luas_permukaan : {luas_permukaan}")
# print(f"volume : {volume}")

# ------------------------------- UI ---------------------------------- #

window = tkinter.Tk()
window.title("KERUCUT")
window.minsize(400, 400)
window.config(padx=10, pady=10)

# LABEL
title_label = tkinter.Label(text="Kerucut")
garis_label = tkinter.Label(text="Garis pelukis")
tinggi_label = tkinter.Label(text="Tinggi")
jari_label = tkinter.Label(text="Jari-jari")
hasil_label = tkinter.Label(text="Hasil")
luas_selimut_label = tkinter.Label(text="Luas selimut")
luas_permukaan_label = tkinter.Label(text="Luas permukaan")
volume_label = tkinter.Label(text="Volume")

title_label.grid(row=0, column=1, columnspan=2)
garis_label.grid(row=1, column=0)
tinggi_label.grid(row=2, column=0)
jari_label.grid(row=3, column=0)
hasil_label.grid(row=4, column=1, columnspan=2)
luas_selimut_label.grid(row=5, column=0)
luas_permukaan_label.grid(row=6, column=0)
volume_label.grid(row=7, column=0)

# ENTRY
garis_entry = tkinter.Entry(width=40)
tinggi_entry = tkinter.Entry(width=40)
jari_entry = tkinter.Entry(width=40)
luas_selimut_entry = tkinter.Entry(width=40)
luas_permukaan_entry = tkinter.Entry(width=40)
volume_entry = tkinter.Entry(width=40)

garis_entry.grid(row=1, column=1, columnspan=2)
tinggi_entry.grid(row=2, column=1, columnspan=2)
jari_entry.grid(row=3, column=1, columnspan=2)
luas_selimut_entry.grid(row=5, column=1, columnspan=2)
luas_permukaan_entry.grid(row=6, column=1, columnspan=2)
volume_entry.grid(row=7, column=1, columnspan=2)

# BUTTON
calculate_button = tkinter.Button(text="calculate", width=10, height=9, command=calculate)
calculate_button.grid(row=1, column=3,rowspan=9)

window.mainloop()
