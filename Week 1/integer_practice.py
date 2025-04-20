#3ta musbato'zgaruvchilari
musbat1 = 1
musbat2 = 2
musbat3 = 3

#2ta manfiy o'zgaruvchilari
manfiy1 = -1
manfiy2 = -2

#(C) o'zgaruvchilarni qiymatini va turini chiqarish
print(musbat1, type(musbat1))
print(musbat2, type(musbat2))
print(musbat3, type(musbat3))
print(manfiy1, type(manfiy1))
print(manfiy2, type(manfiy2))

#(D) vazifalar
print(musbat1 + musbat3)
print(musbat2 - manfiy1)
print(musbat1 * manfiy2)
print(musbat2 / musbat1)

#(E) foydalanuvchidan input olish
num = int(input("Butun son kiriting: "))
if num > 0:
    print("Musbat son")
elif num < 0:
    print("Manfiy son")
elif num == 0:
    print("Bu nolga teng")
else:
    print("Bu son butun emas")

#(F) Katta yoki kichikligini aniqlash
num1 = int(input("Birinchi sonni kiring: "))
num2 = int(input("Ikkinchi sonni kring: "))
if num1>num2:
    print(f"Eng katta son: {num1}")
else:
    print(f"Eng katta son: {num2}")