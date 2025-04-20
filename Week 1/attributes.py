string  = "Sun'iy Intelekt"
print(len(string))
print(string.upper())
print(string.lower())


for i in range(len(string)):
    if string[i]  == "'":
        print("tutuq belgisi", string[i])
    elif string[i] == "y":
        print("y harfi", string[i])


matn = input("Matn kiriting: ")
if len(matn) > 5:
    print("Matn 5da harfdan ko'p, matn uzunligi:", len(matn))
else:
    print("Matn 5ta harfdan kam, matn uzunligi:", len(matn))


matn = input("Matn kiriting: ")
for i in range(len(matn)):
    if matn[i] == 'a':
        print("matnda 'a' harfi bor")


matn = input("'Son' yoki 'Matn'ni tanlang: ")
if matn.lower() == 'son':
    son  = int(input("Son kiriting: "))
    if son > 0:
        print(f"{son} soni musbot son!")
    else:
        print(f"{son} soni manfiy son!")
elif matn.lower() == 'matn':
    matn = input("Matn kiriting: ")
    if len(matn) / 2:
        print(f"'{matn}' matn uzunligi juft son")
    else:
        print(f"'{matn}' matn uzunligi toq son")

matn = input("Matn kiriting: ")
print(f"Matnning uzunligi: {len(matn)}")

#k,l,m,n,o 남았다
#(K) Teskari matn
matn = "Mening ismim Muhammadjon"
for i in range(len(matn)-1, -1, -1):
    print(matn[i], end="")
print()

#(L) Name, surname Capitalize
name = input("Ismingizni kiriting: ")
surname = input("Familiyangizni kiriting: ")
print(f"sizning to'liq ismingiz: {name.capitalize()} {surname.capitalize()}")

#(M) square a,b
l = int(input("Length: "))
print(f"To'rtburchakning yuzi: {l*l}")
print(f"To'rtburchakning perimetri: {l*4}")

#(N) S,I kichik harf
string = "Sun'iy Intelekt"
print(string.replace("I", "i"))
print(string.replace("S", "s"))

#(O)
string = "Sun'iy Intelekt"
ism = "Muhammadjon"
print(f"{ism} {string}ni yaxshi ko'radi!")