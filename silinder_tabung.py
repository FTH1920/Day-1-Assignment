print("Silinder Tabung\n")

PI = 3.14

T = 5
r = 7

luas_selimut = 2 * PI * r * T
luas_permukaan = (2 * r * T) + (2 * PI * r**2)
volume = PI * r**2 *T

print(f"Luas selimut : {round(luas_selimut, 2)}")
print(f"Luas permukaan: {round(luas_permukaan, 2)}")
print(f"Volume : {round(volume, 2)}")
