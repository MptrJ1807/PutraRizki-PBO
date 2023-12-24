print("konversi suhu Kelvin")

#Entry
suhu = input("Masukkan suhu dalam Kelvin")

#rumus
R = (4/5 * (float(suhu) - 273))
F = (5/9 * (float(suhu) - 273)) + 32
C = float(suhu) - 273

#print
print(suhu + "Kelvin sama dengan")
print(str(R) + "Reamur")
print(str(F) + "Fahrenheit")
print(str(C) + "Celcius")
