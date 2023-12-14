import tkinter
from tkinter import W, END


class KonversiKelvin:
    def __init__(self, root) -> None:
        self.window = root
        root.title("Konverter kelvin")
        root.minsize(250, 200)
        self.buatUI()
        pass

    def buatUI(self):
        self.labelSuhu = tkinter.Label(
            root, text="Kelvin:").grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.labelC = tkinter.Label(
            root, text="Celcius:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.labelF = tkinter.Label(
            root, text="Fahrenheit:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.labelR = tkinter.Label(root, text="Reamur:").grid(
            row=4, column=0, sticky=W, padx=5, pady=5)

        self.entrySuhu = tkinter.Entry(root)
        self.entrySuhu.grid(row=0, column=1, sticky=W, padx=5, pady=5)
        self.entryC = tkinter.Entry(root)
        self.entryC.grid(row=2, column=1, sticky=W, padx=5, pady=5)
        self.entryF = tkinter.Entry(root)
        self.entryF.grid(row=3, column=1, sticky=W, padx=5, pady=5)
        self.entryR = tkinter.Entry(root)
        self.entryR.grid(row=4, column=1, sticky=W, padx=5, pady=5)

        self.buttonKonversi = tkinter.Button(root, text="konversi", command=self.convert).grid(
            row=1, column=1, sticky=W, padx=5, pady=5)

    def convert(self):
        suhu = int(self.entrySuhu.get())
        C = suhu - 273
        F = (9/5)*(suhu-273) + 32
        R = (4/5)*(suhu-273)

        self.entryC.delete(0, END)
        self.entryC.insert(0, str(round(C, 2)))

        self.entryF.delete(0, END)
        self.entryF.insert(0, str(round(F, 2)))

        self.entryR.delete(0, END)
        self.entryR.insert(0, str(round(R, 2)))


if __name__ == "__main__":
    root = tkinter.Tk()
    konverter = KonversiKelvin(root)
    root.mainloop()
