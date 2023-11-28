import tkinter


def konversi_suhu():
    try:
        suhu = float(suhu_entry.get())
        if choice.get() == 1:
            hasil = ((9/5) * suhu) +32
            satuan = "Fahrenheit"
        else:
            hasil = (5/9) * (suhu - 32)
            satuan = "Celcius"

        hasil_label.config(text=f"Hasil konversi:\n{round(hasil, 2)} {satuan}")

    except ValueError:
        hasil_label.config(text="Tolong Masukan Angka!")


# Membuat windowS
window = tkinter.Tk()
window.minsize(300, 200)
window.title("Konverter Suhu")

# Membuat label judul
title_label = tkinter.Label(text="Konverter Suhu")
title_label.pack()

# Membuat label
suhu_label = tkinter.Label(text="Masukan Suhu:")
suhu_label.pack()

# Membuat entry suhu
suhu_entry = tkinter.Entry()
suhu_entry.pack()

# Membuat pilihan konversi menggunakan radiobutton
choice = tkinter.IntVar()
celcius_radio = tkinter.Radiobutton(text="Celcius ke Fahrenheit", variable=choice, value=1)
fahrenheit_radio = tkinter.Radiobutton(text="Fahrenheit ke Celcius", variable=choice, value=2)

celcius_radio.pack()
fahrenheit_radio.pack()

# Membuat tombol konversi
konversi_button = tkinter.Button(text="Konversi", command=konversi_suhu)
konversi_button.pack()

# Membuat labeh hasil konversi
hasil_label = tkinter.Label(text="")
hasil_label.pack()

window.mainloop()
