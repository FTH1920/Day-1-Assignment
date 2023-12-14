# import tkinter


# class Celcius:
#     def __init__(self, satuan) -> None:
#         self.window = tkinter.Tk()
#         self.window.title("Konversi Celcius")
#         self.window.minsize(200, 200)
#         self.satuan = satuan
#         self.window.aturKomponen
#         self.window.mainloop
#         pass

#     def aturKomponen(self):
#         self.labelSuhu = tkinter.Label(
#             self.window, text="Masukan suhu:").grid(row=0, column=0)
#         self.labelHasil = tkinter.Label(
#             self.window, text="Hasil").grid(row=2, column=0)

#         self.entrySuhu = tkinter.Entry(
#             self.window, width=20).grid(row=0, column=1)
#         self.entryHasil = tkinter.Entry(
#             self.window, width=20).grid(row=2, column=1)

#         self.buttonKonversi = tkinter.Button(
#             self.window, text="Konversi").grid(row=1, column=1)

#     def ubah_fahrenheit(self):
#         self.fahrenheit = ((9/5)*self.satuan) + 32
#         print(f"Suhu dalam fahrenheit : {round(self.fahrenheit, 2)}")

#     def ubah_reamur(self):
#         self.reamur = (4/5)*self.satuan
#         print(f"Suhu dalam reamur : {round(self.reamur, 2)}")

#     def ubah_kelvin(self):
#         self.kelvin = self.satuan + 273
#         print(f"Suhu dalam kelvin : {round(self.kelvin, 2)}")


# window = Celcius(23)


from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W


class FrmSuhu:
    def __init__(self, parent, title):
        self.parent = parent
        # self.parent.geometry("400x400")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # pasang Label
        Label(mainFrame, text='Celcius:').grid(row=0, column=0,
                                               sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Fahrenheit:").grid(row=2, column=0,
                                                  sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Reamur:").grid(row=3, column=0,
                                              sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Kelvin:").grid(row=4, column=0,
                                              sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtCelcius = Entry(mainFrame)
        self.txtCelcius.grid(row=0, column=1, padx=5, pady=5)
        self.txtFahrenheit = Entry(mainFrame)
        self.txtFahrenheit.grid(row=2, column=1, padx=5, pady=5)
        self.txtReamur = Entry(mainFrame)
        self.txtReamur.grid(row=3, column=1, padx=5, pady=5)
        self.txtKelvin = Entry(mainFrame)
        self.txtKelvin.grid(row=4, column=1, padx=5, pady=5)

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
                                command=self.onHitung)
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)

    # fungsi "onHitung" berfungsi untuk menghitung luas persegi panjang

    def onHitung(self):
        C = int(self.txtCelcius.get())
        value_F = (9/5 * C)+32
        value_R = (4/5)*C
        value_K = C + 273

        self.txtFahrenheit.delete(0, END)
        self.txtFahrenheit.insert(END, str(round(value_F, 2)))

        self.txtReamur.delete(0, END)
        self.txtReamur.insert(END, str(round(value_R, 2)))

        self.txtKelvin.delete(0, END)
        self.txtKelvin.insert(END, str(round(value_K, 2)))

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()


if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmSuhu(root, "Program Konversi Suhu")
    root.mainloop()
