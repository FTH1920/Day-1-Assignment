print("Prisma Segitiga\n")

T = 8
t = 5
a = 5

keliling_segitiga = a**3
Ls = keliling_segitiga * T
Lp = (keliling_segitiga * T) + (a * t)
volume = (1/2) * a * t * T

print(f"Ls : {Ls}")
print(f"Lp : {Lp}")
print(f"volume : {round(volume, 2)}")
