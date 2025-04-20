#B
prices = [11000,1500,26500,45600]
prices[0] = 13000
prices[2] = 11000
prices[3] = 2000
print(prices)

#C,D
fruits = ['apple' ,'banana', 'grape', 'tomato', 'cherry']
fruits.extend(['strawberry', 'orange', 'ananas', 'nuts'])
print(fruits)

fruits.remove('orange')
fruits.remove('tomato')
print(fruits)

#E
fruits = ['apple' ,'banana', 'grape', 'tomato']
prices = [11000,1500,26500,45600]
for fruit, price in zip(fruits, prices):
    print(f"{fruit.capitalize()}ning narxi {price} so'm")

#F,G
cars = ['bmw', 'mercedez benz', 'volvo', 'hyunadai', 'kia', 'general motors','tesla', 'audi']
print(cars)
print(sorted(cars))

cars2 = ['bmw', 'mercedez benz', 'volvo', 'hyunadai', 'kia', 'general motors','tesla', 'audi']
new_cars = []
for _ in range(3):
    car = cars2.pop(-1)
    new_cars.append(car)
print(new_cars)

H
"""List [1,3, "5", "name"]. list square brackets bilan ishlatiladi va tuple bilan eng katta va asosiy farqi esa list ustida biz turli xil amallar oshira olamiz(append, pop, insert, sort, replace, indexing), ammo biz tuple yarathanimizdan so'ng (12.2,56.8) unig ustidan amallar oshira olmaymiz va bu juda muhim data turi hisoblanadi sababi biz tuple da o'zgartirishimizni xoxlamaydigan malumotlarni saqlaymiz misol uchun Koordinatlar."""

#I
x = ('olma', 'banan', 'olcha')
y = list(x)
y[1] = 'kivi'
x = tuple(y)
print(y)

#J
a = ['a','b','c']
b = [1,2,3]
print(a+b)

#K
dic = {"ism":"Muhammad", "yosh":21, "vazn":80.9}
print(f"Ismim {dic['ism']}, yoshim {dic['yosh']}da va vaznim {dic['vazn']} kg")

#L,M,N,O
car = {"lacetti":"oq", "audi":"qora", "hyundai":"kulrang"}
car["kia"] = "qizil"
car["samsung"] = "ko'k"
car["bmw"] = "sariq"
car["voyah"] = "qora"

car["audi"] = "oq"
print(car)

for key, value in car.items():
    print(key,value)

for key in car.keys():
    if len(key) == 3:
        print(key.upper())

#P
countries = {
    "Uzbekistan":"Tashkent",
    "South Korea":"Seoul",
    "Japan":"Tokyo",
    "Malaysia":"Kuala Lumpur",
    "Spain":"Madrid"
}
for key in sorted(countries.keys()):
    print(key, "\n")
for value in sorted(countries.values()):
    print(value)

#Q,R
akam = {"ism":"Javohir", "yosh":27, "hobby":"stol tennis"}
ukam = {"ism":"Muhammad", "yosh":21, "hobby":"kitob o'qish"}
print(f"Akamning ismi {akam['ism'].capitalize()}, yoshlari {akam['yosh']}da, va qiziqishi {akam['hobby']}")
print(f"Ukamning ismi {ukam['ism'].capitalize()}, yoshlari {ukam['yosh']}da, va qiziqishi {ukam['hobby']}")



