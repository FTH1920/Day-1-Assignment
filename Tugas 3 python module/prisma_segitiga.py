import tkinter
from tkinter import END


def prisma_segitiga():
    def calculate():

        ls_entry.delete(0, END)
        lp_entry.delete(0, END)
        volume_prisma_entry.delete(0, END)

        try:
            tinggi_segitiga = float(tinggi_segitiga_entry.get())
            tinggi_prisma = float(tinggi_prisma_entry.get())
            alas = float(alas_entry.get())

            keliling_segitiga = alas**3
            ls = keliling_segitiga * tinggi_prisma
            lp = ls + alas * tinggi_segitiga
            volume = (1/2) * alas * tinggi_segitiga * tinggi_prisma

            ls_entry.insert(0, str(round(ls, 2)))
            lp_entry.insert(0, str(round(lp, 2)))
            volume_prisma_entry.insert(0, str(round(volume, 2)))
        except ValueError:
            pass

    # T = 8
    # t = 5
    # a = 5

    # keliling_segitiga = a**3
    # Ls = keliling_segitiga * T
    # Lp = (keliling_segitiga * T) + (a * t)
    # volume = (1/2) * a * t * T

    # print(f"Ls : {Ls}")
    # print(f"Lp : {Lp}")
    # print(f"volume : {round(volume, 2)}")

# ------------------------------------ UI ---------------------------------------- #

    window = tkinter.Tk()
    window.minsize(400, 400)
    window.title("Prisma Segitiga")
    window.config(padx=10, pady=10)

    # Label
    title_label = tkinter.Label(text="Prisma Segitiga")
    tinggi_segitiga_label = tkinter.Label(text="Tinggi segitiga")
    tinggi_prisma_label = tkinter.Label(text="Tinggi prisma")
    alas_label = tkinter.Label(text="Alas")
    hasil_label = tkinter.Label(text="Hasil")
    ls_label = tkinter.Label(text="Ls")
    lp_label = tkinter.Label(text="Lp")
    volume_prisma_label = tkinter.Label(text="Volume")

    title_label.grid(row=0, column=1, columnspan=2)
    tinggi_segitiga_label.grid(row=1, column=0, sticky=tkinter.W, padx=5)
    tinggi_prisma_label.grid(row=2, column=0, sticky=tkinter.W, padx=5)
    alas_label.grid(row=3, column=0, sticky=tkinter.W, padx=5)
    hasil_label.grid(row=4, column=1, columnspan=2)
    ls_label.grid(row=5, column=0, sticky=tkinter.W, padx=5)
    lp_label.grid(row=6, column=0, sticky=tkinter.W, padx=5)
    volume_prisma_label.grid(row=7, column=0, sticky=tkinter.W, padx=5)

    # Entry
    tinggi_segitiga_entry = tkinter.Entry(width=40)
    tinggi_prisma_entry = tkinter.Entry(width=40)
    alas_entry = tkinter.Entry(width=40)
    ls_entry = tkinter.Entry(width=40)
    lp_entry = tkinter.Entry(width=40)
    volume_prisma_entry = tkinter.Entry(width=40)

    tinggi_segitiga_entry.grid(row=1, column=1, columnspan=2)
    tinggi_prisma_entry.grid(row=2, column=1, columnspan=2)
    alas_entry.grid(row=3, column=1, columnspan=2)
    ls_entry.grid(row=5, column=1, columnspan=2)
    lp_entry.grid(row=6, column=1, columnspan=2)
    volume_prisma_entry.grid(row=7, column=1, columnspan=2)

    # Button
    calculate_button = tkinter.Button(
        text="Calculate", width=10, height=9, command=calculate)
    calculate_button.grid(row=1, column=3, rowspan=9, padx=5)

    window.mainloop()
