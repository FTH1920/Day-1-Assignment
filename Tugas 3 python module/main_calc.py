import tkinter
from tkinter import W
import balok
import bola
import kerucut
import kubus
from limas_segiempat import limas_segiempat
from limas_segitiga import limas_segitiga
from prisma_segitiga import prisma_segitiga
from silinder_tabung import silinder_tabung

# def list_bangun_ruang():
#     print("[1] Balok")
#     print("[2] Bola")
#     print("[3] Kerucut")
#     print("[4] Kubus")
#     print("[5] Limas Segiempat")
#     print("[6] Limas Segitiga")
#     print("[7] Prisma Segitiga")
#     print("[8] Silinder Tabung")
#
# is_on = True
#
# print("*KALKULATOR BANGUN RUANG*")
# print("==========================")
#
# while is_on:


def choose():
    window.destroy()
    chose = x.get()

    if chose == 1:
        balok.balok()
    elif chose == 2:
        bola.bola()
    elif chose == 3:
        kerucut.kerucut()
    elif chose == 4:
        kubus.kubus()
    elif chose == 5:
        limas_segiempat()
    elif chose == 6:
        limas_segitiga()
    elif chose == 7:
        prisma_segitiga()
    elif chose == 8:
        silinder_tabung()

    # next_iteration = input("Lanjut Menggunakan? [Y/N]\n").lower()
    # if next_iteration == "n":
    #     # is_on = False
    #     print("THANK FOR USING")


window = tkinter.Tk()
window.minsize(400, 400)
window.title("Kalkulator Bangun Ruang")
window.config(pady=15, padx=15)

x = tkinter.IntVar()

# Radio
# male_button = tkinter.Radiobutton(window, text="Male", variable=x, value=0)
# female_button = tkinter.Radiobutton(window, text="Female", variable=x, value=1)

# Label
title_label = tkinter.Label(text="Kalkulator\nBangun Ruang")
balok_label = tkinter.Radiobutton(window, text="1.Balok", variable=x, value=1)
bola_label = tkinter.Radiobutton(window, text="2.Bola", variable=x, value=2)
kerucut_label = tkinter.Radiobutton(window, text="3.Kerucut", variable=x, value=3)
kubus_label = tkinter.Radiobutton(window, text="4.Kubus", variable=x, value=4)
limasempat_label = tkinter.Radiobutton(window, text="5.Limas Segiempat", variable=x, value=5)
limastiga_label = tkinter.Radiobutton(window, text="6.Limas Segitiga", variable=x, value=6)
prismatiga_label = tkinter.Radiobutton(window, text="7.Prisma Segitiga", variable=x, value=7)
silinder_label = tkinter.Radiobutton(window, text="8.Silinder Kubus", variable=x, value=8)
pilihan_label = tkinter.Label(text="PILIHAN")

title_label.grid(row=0, column=1, columnspan=2)
balok_label.grid(row=2, column=1, sticky=W, padx=15)
bola_label.grid(row=3, column=1, sticky=W, padx=15)
kerucut_label.grid(row=4, column=1, sticky=W, padx=15)
kubus_label.grid(row=5, column=1, sticky=W, padx=15)
limasempat_label.grid(row=2, column=2, sticky=W, padx=15)
limastiga_label.grid(row=3, column=2, sticky=W, padx=15)
prismatiga_label.grid(row=4, column=2, sticky=W, padx=15)
silinder_label.grid(row=5, column=2, sticky=W, padx=15)
pilihan_label.grid(row=1, column=1, columnspan=2)

# Entry
# pilihan_entry = tkinter.Entry(width=35)
# pilihan_entry.grid(row=6, column=1, columnspan=2, sticky=W)

# Button
confirm_button = tkinter.Button(width=40, text="Confirm", command=choose)
confirm_button.grid(row=7, column=1, columnspan=2, sticky=W, pady=20)

window.mainloop()
