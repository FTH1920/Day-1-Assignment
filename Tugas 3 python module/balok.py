import tkinter
from tkinter import messagebox
import random

luas = ""
volume = ""


def balok():

    def fill_result_entry(ll, vv):
        luas_entry.insert(0, ll)
        volume_entry.insert(0, vv)

    def clear_entry():
        panjang_entry.delete(0, tkinter.END)
        lebar_entry.delete(0, tkinter.END)
        tinggi_entry.delete(0, tkinter.END)

    def clear_result_entry():
        luas_entry.delete(0, tkinter.END)
        volume_entry.delete(0, tkinter.END)

    def clear_all():
        clear_entry()
        clear_result_entry()

    def autofill():

        clear_entry()

        panjang_entry.insert(0, str(random.randint(1, 20)))
        lebar_entry.insert(0, str(random.randint(1, 20)))
        tinggi_entry.insert(0, str(random.randint(1, 20)))

    def calculate():

        global luas
        global volume

        try:
            panjang = int(panjang_entry.get())
            lebar = int(lebar_entry.get())
            tinggi = int(tinggi_entry.get())
            luas = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)
            volume = (panjang*lebar*tinggi)

            clear_result_entry()
            fill_result_entry(ll=luas, vv=volume)

        except ValueError:
            messagebox.showerror(title="ERROR", message="Please input a number")
            pass

    luas = "n/a"
    volume = "n/a"

    # ------------------------------------- UI SETUP ------------------------------------------ #

    window = tkinter.Tk()
    window.title("Block Calculator")
    window.config(padx=25, pady=25)
    window.minsize(400, 250)

    # label

    title_text = tkinter.Label(text="Block Calculator", font=("Arial", 15, "normal"))
    panjang_text = tkinter.Label(text="Panjang :")
    lebar_text = tkinter.Label(text="Lebar :")
    tinggi_text = tkinter.Label(text="Tinggi :")
    result_text = tkinter.Label(text="RESULT", font=("Arial", 15, "normal"))
    luas_text = tkinter.Label(text="Luas", font=("Arial", 15, "normal"))
    volume_text = tkinter.Label(text="Volume", font=("Arial", 15, "normal"))

    title_text.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
    panjang_text.grid(row=1, column=0, sticky=tkinter.W)
    lebar_text.grid(row=2, column=0, sticky=tkinter.W)
    tinggi_text.grid(row=3, column=0, sticky=tkinter.W)
    result_text.grid(row=4, column=1, columnspan=2, pady=10)
    luas_text.grid(row=5, column=0, columnspan=2)
    volume_text.grid(row=5, column=2, columnspan=2)

    # entry

    panjang_entry = tkinter.Entry(width=40)
    lebar_entry = tkinter.Entry(width=40)
    tinggi_entry = tkinter.Entry(width=40)
    luas_entry = tkinter.Entry(width=31)
    volume_entry = tkinter.Entry(width=31)

    panjang_entry.grid(row=1, column=1, columnspan=2)
    lebar_entry.grid(row=2, column=1, columnspan=2)
    tinggi_entry.grid(row=3, column=1, columnspan=2)
    luas_entry.grid(row=6, column=0, columnspan=2)
    volume_entry.grid(row=6, column=2, columnspan=2)

    # button

    calculate_button = tkinter.Button(
        text="Calculate", width=10, height=2, command=calculate)
    calculate_button.grid(row=2, column=3, rowspan=2)

    autofill_button = tkinter.Button(text="Autofill", width=10, command=autofill)
    autofill_button.grid(row=1, column=3)

    clear_all_button = tkinter.Button(text="Clear All", width=53, command=clear_all)
    clear_all_button.grid(row=7, column=0, columnspan=4)

    panjang_entry.focus()

    window.mainloop()
