import tkinter
from tkinter import END

def calculate():

    luas_entry.delete(0, END)
    volume_entry.delete(0, END)

    try:
        rusuk = float(rusuk_entry.get())
        luas = 6 * rusuk**2
        volume = rusuk**3

        luas_entry.insert(0, round(luas, 2))
        volume_entry.insert(0, round(volume, 2))
    except ValueError:
        pass


# print("Kubus\n")

# rusuk = int(input("Panjang rusuk : "))

# luas = 6 * rusuk**2
# volume = rusuk**3

# print(f"Luas kubus : {luas}")
# print(f"Volume kubus :{volume}")

# ------------------------ UI --------------------------- #
window = tkinter.Tk()
window.title("KUBUS")
window.minsize(400, 400)
window.config(padx=10, pady=10)

# LABEL
title_label = tkinter.Label(text="Kubus")
rusuk_label = tkinter.Label(text="Rusuk")
hasil_label = tkinter.Label(text="Hasil")
luas_label = tkinter.Label(text="Luas")
volume_label = tkinter.Label(text="Volume")

title_label.grid(row=0, column=1, columnspan=2, pady=5)
rusuk_label.grid(row=1, column=0, padx=10, sticky=tkinter.W)
hasil_label.grid(row=2, column=1, columnspan=2, pady=5)
luas_label.grid(row=3, column=0, padx=10, sticky=tkinter.W)
volume_label.grid(row=4, column=0, padx=10, sticky=tkinter.W)

# ENTRY
rusuk_entry = tkinter.Entry(width=40)
luas_entry = tkinter.Entry(width=40)
volume_entry = tkinter.Entry(width=40)

rusuk_entry.grid(row=1, column=1, columnspan=2)
luas_entry.grid(row=3, column=1, columnspan=2)
volume_entry.grid(row=4, column=1, columnspan=2)

# BUTTON
calculate_button = tkinter.Button(text="Calculate", height=5, width=10, command=calculate)
calculate_button.grid(row=1, column=3, rowspan=5, padx=5)

window.mainloop()
