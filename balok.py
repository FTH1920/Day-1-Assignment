print("Balok\n")

panjang = int(input("Masukan panjang : "))
lebar = int(input("Masukan lebar : "))
tinggi = int(input("Masukan tinggi : "))

luas = (2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi)
volume = luas * lebar * tinggi

print(f"Luas balok : {luas}")
print(f"Volume balok : {volume}")
