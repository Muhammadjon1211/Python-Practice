converter = input("Choose converter(kg/pound/celcius/fahrenheit): ")
if converter.lower() == "kg":
    kg = int(input("Kg: "))
    print(f"{kg} kg = {kg*2.20462} pound")
elif converter.lower() == "pound":
    pound = int(input("Pound: "))
    print(f"{pound} pound = {pound/2.20462} kg")
elif converter.lower() == "celcius":
    celcius = int(input("Celcius: "))
    print(f"{celcius} Celcius = {celcius*9/5 + 32} Fahrenheit")
elif converter.lower() == "fahrenheit":
    fahrenheit = int(input("Fahrenheit: "))
    print(f"{fahrenheit} Fahrenheit = {(fahrenheit-32)*5/9} Celcius")


currency_converter = input("Pul birligini tanlang (USD/KRW/RBL): ")
if currency_converter.lower() == 'usd':
    dollar = float(input("Dollarni kiriting: "))
    print(f"{dollar} dollar = {dollar * 12950} so'm")
elif currency_converter.lower() == 'krw':
    won = float(input("Korean wonni kiriting: "))
    print(f"{won} Korean won = {won * 9.08} so'm")
elif currency_converter.lower() == 'rbl':
    ruble = float(input("Rublni kiriting: "))
    print(f"{ruble} rubl = {ruble * 82.08} so'm")

weight_converter = int(input("Kg kiriting: "))
if weight_converter>0:
    tonna = weight_converter / 1000
    print(f"{weight_converter} kg = {tonna} tonna")
elif weight_converter>0:
    gram = weight_converter * 1000
    print(f"{weight_converter} kg = {gram} gram")
elif weight_converter>0:
    milligram = weight_converter * 1000000
    print(f"{weight_converter} kg = {milligram} milligram")

measure_converter = int(input("CM uzunligini kiriting: "))
if measure_converter>0:
    cm = measure_converter
    print(f"{cm} cm = {cm / 100} m")
    print(f"{cm} cm = {cm / 1000} km")
    print(f"{cm} cm = {cm * 10} mm")
    print(f"{cm} cm = {cm * 0.01} yard")

score = 92
if score >= 90:
    print("A")
elif score >= 80 and score < 90:
    print("B")
elif score >= 70 and score < 80:
    print("C")
elif score >= 60 and score < 70:
    print("D")
elif score < 60:
    print("Fail")

year = int(input("Yilni kiriting: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} yili kabisat yili")
else:
    print(f"{year} yili kabisat yili emas")


prime_number = int(input("Sonni kiriting: ")