#B
nums = []
for i in range(1,11):
    nums.append(i**2)
print(nums)

#C
nums = []
for i in range(1,11):
    nums.append(i**3)
print(sum(nums))

#D
import math
nums = []
for i in range(1,11):
    nums.append(math.isqrt(i))
print(nums)

#E
karrali_sonlar = []
for i in range(0,21):
    if i%5 == 0:
        karrali_sonlar.append(i)
print(karrali_sonlar)

#F, G
names = []
for i in range(5):
    name = input(f"{i+1} foydalanuvchi ismini kiriting: ")
    names.append(name.capitalize())
print(names)

for name in names:
    print(f"{name} Salom!")

#H
nums= [12,5,45,9,11,1]
for i in nums:
    if i >= 10:
        print(i)

#I
even = []
odd = []
for i in range(5):
    son = int(input(f"{i+1}chi sonni kiriting: "))
    if son%2 == 0:
        even.append(son)
    else:
        odd.append(son)

print(even)
print(odd)

#J
nums = []
for i in range(1,11):
    nums.append(i*2)
print(nums)

#K
nums = []
for i in range(1,21):
    if i%3 == 0 and i%4 == 0:
        nums.append(i)
print(nums)

nums = []
for i in range(1,21):
    if i%3 == 0:
        nums.append(i)
    elif i%4 == 0:
        nums.append(i)
print(nums)

#L
products = ['non', 'sut', 'yog', 'olma', 'nok', 'banan', 'shakar']
for word in products:
    if len(word) > 3:
        print(word)

#M
names = ['muhammad', 'ulugbek', 'oybek', 'samandar']
for name in names:
    print(f"{name.capitalize()}-ning uzunligi {len(name)} harf")

#N
nums = []
for i in range(5):
    son = int(input(f"{i+1}chi sonni kiriting: "))
    nums.append(son)
print(f"{nums}-ning o'rtacha soni {sum(nums)/len(nums)}")

#O 
prices = [10000,25000,30000,15000,5000]
new_prices = []
for price in prices:
    new_prices.append(price + (price*15/100))
print(new_prices)

#P
for i in range(1,11):
    print(f"3*{i}={3*i}")

#Q
for i in range(1,10):
    print(f"1*{i}={1*i}")

#R
for i in range(5):
    word = input(f"{i+1}-chi so'zni kiriting: ")
    print(word.upper())

#S
for num in range(0,11):
    if num > 0:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)

#T 
for i in range(1,101):
    if i%7 == 0 and i%5!=0:
        print(i)




