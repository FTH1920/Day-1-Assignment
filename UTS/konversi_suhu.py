import tkinter as tk
from tkinter import ttk

def konversi_suhu():
    try:
        suhu = float(suhu_entry.get())
        initial_unit = initial_combobox.get()
        target_unit = target_combobox.get()

        # Fahrenheit awal
        if initial_unit == "Fahrenheit" and target_unit == "Celcius":
            hasil = (5/9)*(suhu-32)
        elif initial_unit == "Fahrenheit" and target_unit == "Reamur":
            hasil = (4/9)*(suhu-32)
        elif initial_unit == "Fahrenheit" and target_unit == "Kelvin":
            hasil = (5/9)*(suhu-32) + 273

        # Celcius awal
        elif initial_unit == "Celcius" and target_unit == "Fahrenheit":
            hasil = ((9/5)*suhu) + 32
        elif initial_unit == "Celcius" and target_unit == "Reamur":
            hasil = (4/5)*suhu
        elif initial_unit == "Celcius" and target_unit == "Kelvin":
            hasil = suhu + 273

        # Reamur awal
        elif initial_unit == "Reamur" and target_unit == "Fahrenheit":
            hasil = (9/4)*suhu + 32
        elif initial_unit == "Reamur" and target_unit == "Celcius":
            hasil = (5/4)*suhu
        elif initial_unit == "Reamur" and target_unit == "Kelvin":
            hasil = (5/4)*suhu + 273

        # Kelvin awal
        elif initial_unit == "Kelvin" and target_unit == "Fahrenheit":
            hasil = (9/5)*(suhu-273) + 32
        elif initial_unit == "Kelvin" and target_unit == "Celcius":
            hasil = suhu - 273
        elif initial_unit == "Kelvin" and target_unit == "Reamur":
            hasil = (4/5)*(suhu-273)

        hasil_label.config(text=f"Hasil konversi:\n{round(hasil, 2)} {target_unit}")

    except ValueError:
        hasil_label.config(text="Tolong Masukkan Angka!")


window = tk.Tk()
window.minsize(300, 350)
window.title("Konverter Suhu")

style = ttk.Style()
style.configure('TButton', padding=5, width=15)

title_label = tk.Label(text="Konverter Suhu", font=('Helvetica', 16, 'bold'))
title_label.pack(pady=10)

# Satuan suhu awal
initial_label = tk.Label(text="Satuan Awal:")
initial_label.pack()

initial_units = ["Fahrenheit", "Celcius", "Reamur", "Kelvin"]
initial_combobox = ttk.Combobox(window, values=initial_units)
initial_combobox.set(initial_units[0]) 
initial_combobox.pack(pady=5)

suhu_label = tk.Label(text="Masukkan Suhu:")
suhu_label.pack()

suhu_entry = tk.Entry()
suhu_entry.pack(pady=5)

# Satuan suhu target
target_label = tk.Label(text="Satuan Target:")
target_label.pack()

target_units = ["Fahrenheit", "Celcius", "Reamur", "Kelvin"]
target_combobox = ttk.Combobox(window, values=target_units)
target_combobox.set(target_units[1]) 
target_combobox.pack(pady=5)

konversi_button = ttk.Button(text="Konversi", command=konversi_suhu)
konversi_button.pack(pady=10)

hasil_label = tk.Label(text="", font=('Helvetica', 12, 'italic'))
hasil_label.pack()

window.mainloop()
