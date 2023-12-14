import tkinter
from tkinter import W, END


class KonversiReamur:
    def __init__(self, root) -> None:
        self.window = root
        root.title("Konverter reamur")
        root.minsize(250, 200)
        self.buatUI()
        pass

    def buatUI(self):
        self.labelSuhu = tkinter.Label(
            root, text="Reamur:").grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.labelC = tkinter.Label(
            root, text="Celcius:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.labelF = tkinter.Label(
            root, text="Kelvin:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.labelR = tkinter.Label(root, text="Fahrenheit:").grid(
            row=4, column=0, sticky=W, padx=5, pady=5)

        self.entrySuhu = tkinter.Entry(root)
        self.entrySuhu.grid(row=0, column=1, sticky=W, padx=5, pady=5)
        self.entryC = tkinter.Entry(root)
        self.entryC.grid(row=2, column=1, sticky=W, padx=5, pady=5)
        self.entryK = tkinter.Entry(root)
        self.entryK.grid(row=3, column=1, sticky=W, padx=5, pady=5)
        self.entryF = tkinter.Entry(root)
        self.entryF.grid(row=4, column=1, sticky=W, padx=5, pady=5)

        self.buttonKonversi = tkinter.Button(root, text="konversi", command=self.convert).grid(
            row=1, column=1, sticky=W, padx=5, pady=5)

    def convert(self):
        try:
            suhu = int(self.entrySuhu.get())
            C = (5/4)*suhu
            K = (5/4)*suhu + 273
            F = (9/4)*suhu + 32

            self.entryC.delete(0, END)
            self.entryC.insert(0, str(round(C, 2)))

            self.entryK.delete(0, END)
            self.entryK.insert(0, str(round(K, 2)))

            self.entryF.delete(0, END)
            self.entryF.insert(0, str(round(F, 2)))
        except ValueError:
            pass


if __name__ == "__main__":
    root = tkinter.Tk()
    konverter = KonversiReamur(root)
    root.mainloop()
