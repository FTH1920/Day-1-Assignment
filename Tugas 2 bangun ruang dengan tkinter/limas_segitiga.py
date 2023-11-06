import tkinter
from tkinter import END


def calculate():

    luas_limas_entry.delete(0, END)
    volume_limas_entry.delete(0, END)

    try:
        tinggi_segitiga = float(tinggi_segitiga_entry.get())
        tinggi_limas = float(tinggi_limas_entry.get())
        alas = float(alas_entry.get())

        luas_segitiga = (1/2) * alas * tinggi_segitiga
        luas_limas = luas_segitiga + luas_segitiga + luas_segitiga + luas_segitiga
        volume = (1/6) * alas * tinggi_segitiga * tinggi_limas

        luas_limas_entry.insert(0, round(luas_limas, 2))
        volume_limas_entry.insert(0, round(volume, 2))
    except ValueError:
        pass

# print(f"luas limas segitiga : {round(luas_limas)}")
# print(f"volume limas segitiga : {round(volume)}")

# ----------------------------- UI ------------------------------------- #


window = tkinter.Tk()
window.minsize(400, 400)
window.title("Limas segitiga")
window.config(padx=10, pady=10)

# Label
title_label = tkinter.Label(text="Limas Segitiga")
tinggi_segitiga_label = tkinter.Label(text="Tinggi segitiga")
tinggi_limas_label = tkinter.Label(text="Tinggi limas")
alas_label = tkinter.Label(text="Alas")
hasil_label = tkinter.Label(text="Hasil")
luas_limas_label = tkinter.Label(text="Luas limas segitiga")
volume_limas_label = tkinter.Label(text="Volume")

title_label.grid(row=0, column=1, columnspan=2)
tinggi_segitiga_label.grid(row=1, column=0, sticky=tkinter.W, padx=5)
tinggi_limas_label.grid(row=2, column=0, sticky=tkinter.W, padx=5)
alas_label.grid(row=3, column=0, sticky=tkinter.W, padx=5)
hasil_label.grid(row=4, column=1, columnspan=2)
luas_limas_label.grid(row=5, column=0, sticky=tkinter.W, padx=5)
volume_limas_label.grid(row=6, column=0, sticky=tkinter.W, padx=5)

# Entry
tinggi_segitiga_entry = tkinter.Entry(width=40)
tinggi_limas_entry = tkinter.Entry(width=40)
alas_entry = tkinter.Entry(width=40)
luas_limas_entry = tkinter.Entry(width=40)
volume_limas_entry = tkinter.Entry(width=40)

tinggi_segitiga_entry.grid(row=1, column=1, columnspan=2)
tinggi_limas_entry.grid(row=2, column=1, columnspan=2)
alas_entry.grid(row=3, column=1, columnspan=2)
luas_limas_entry.grid(row=5, column=1, columnspan=2)
volume_limas_entry.grid(row=6, column=1, columnspan=2)

# Button
calculate_button = tkinter.Button(
    text="Calculate", width=10, height=8, command=calculate)
calculate_button.grid(row=1, column=3, rowspan=8, padx=5)

window.mainloop()
