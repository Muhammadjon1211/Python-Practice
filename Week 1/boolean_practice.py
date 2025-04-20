b1 = True
b2 = False
b3 = True

if b1>b2 and b3<b2:
    print("True")
elif b1<b2 or b3>b1:
    print("False")
elif not b2:
    print("True")


#(E) Voyaga yetganlikni aniqlash
def adult_age():
    age = int(input("Yoshingizni kiriting: "))
    if age >= 18:
        return f"Siz voyaga yetkansiz"
    else:   
        return f"Siz voyaga yetmagansiz"

print(adult_age())