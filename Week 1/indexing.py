string = "Sunniy Intelekt"
#(C) indekslarni musbat bo'lish
print(string[:6])
print(string[7:])
#(D) indekslarni manfiy bo'lish
print(string[:-9])
print(string[-8:])

#(E) 1chi va oxirgi harfini katta qilib chiqarish
word = "o'zbekistan"
print(word[0].upper() + word[1:] + word[-1].upper())

#(F) Matn, Index, Harf
matn = "o'zbekistan"
index = int(input("Index kiriting: "))
harf = input("Yangi harf kiriting: ")


print(f"Matn: {matn[:index]+harf+matn[index+1:]}")

#(G) 2chi harfni chiqarish 
matn = "Salom"
print(matn, matn[1])

#(I) jusft sonli indeksdagi harflarini chiqarish
matn = "Salom"
for i in range(1, len(matn), 2):
    print(matn[i])

#(I) oxirgi 3 ta harfini chiqarish
matn = "o'zbekistan"
print(matn[-3:])

