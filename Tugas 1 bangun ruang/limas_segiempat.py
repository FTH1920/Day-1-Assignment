print("Limas Segiempat\n")

T = 5
p = 7

luas_segitiga = (1/2) * p * T
luas_alas = p**2
luas_limas = luas_segitiga + luas_segitiga + luas_segitiga + luas_segitiga + luas_alas
volume = (1/3) * luas_alas * T

print(f"luas limas segiempat : {round(luas_limas, 2)}")
print(f"volume limas segiempat : {round(volume, 2)}")
