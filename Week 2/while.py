#B
i = 1
while True:
    user_input = input(f"{i} - Yozing (yoki 'yakun' deb yozing to'xtatish uchun): ")
    if user_input.lower() == 'yakun':
        break
    i += 1
#C
import math
i = 1
while i<=50:
    if math.isqrt(i) ** 2 == i:
        print(i)
    i += 1

#D
nums = []
while True:
    num = int(input("Son kiriting (to'xatsh uchun 0): "))
    nums.append(num)
    if num == 0:
        print(f"Average number is: {sum(nums) / len(nums[:-1])}")
        print(nums)
        break

#E
i = 1
even = []
odd = []
while i<=10:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
    i+=1
print(f"Even numbers are: {even}")
print(f"Odd numbers are: {odd}")

#F
names = []
while True:
    name = input("Enter a name(to stop enter 'yakun'): ")
    if name.lower() == 'yakun':
        break
    names.append(name)
for i in names:
    print(i.capitalize())

#G
i = 10
while i >= 1: 
    print(i)
    i-=1

#H
i = 1
while i <= 100:
    if i%5 == 0:
        print(i)
    i+=1

#I
num_list = [1,2,3,4,5,6,7,8,9,10]
i = len(num_list) - 1
while i>=0:
    print(num_list[i])
    i-=1

#J
matn = input("Enter a word: ")
while True:
    if len(matn) >= 5:
        print(matn)
    else:
        print("Matn has less than 5 letters")
    break

#K
while True:
    password = input("Enter a password: ")
    answer = "cm7student"
    if password.lower() == answer:
        break
print("Welcome to the course!")

#L(for loop)
fourth = []
for i in range(1, 51, 4):
    fourth.append(i)
print(fourth)

#(while loop)
f = []
i = 1
while i <=50:
    f.append(i)
    i+=4

print(f)

#M
fruits = ['apple', 'banana', 'grape']
prices = [5000, 12000,7000]
while True:
    for fruit, price in zip(fruits, prices):
        print(f"{fruit.capitalize()}-ning narxi {price} won")
    break

#N
import random
nums = []
i = 0
while i<=10:
    num = random.randint(0,100)
    nums.append(num)
    i+=1
print(f" Eng katta son {max(nums)}\n 
            Eng kichik son {min(nums)}\n 
            O'rtacha son {sum(nums)/len(nums)}\n 
            10ta random son ro'yxati {nums}")

#O Shunga Hint berib yuborsangiz  
list_words = ['salom', 'stul', 'qashqadaryo', 'universitet', 'pul'] 


