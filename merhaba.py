import time

print("merhaba")

fav_number = 12
if fav_number <= 15:
    print("my favorite number smaller then 15")

#büyük harflere duyarlı
#değişkenlerde snake kullanımı var


def greeting(name):
    print("Hello "+name)
greeting("Reyhan")

"""
this is a long comment
"""

"""
numbers, lists, strings  data types
"""

print(type(fav_number))


store_items = ['Apple', 1.49, 'Banana', 1, 'Milk', 2.99] #list farklı veri türlerini bir arada tutar
print(store_items, type(store_items))

print(store_items[2])
print(store_items[0:4])
print(store_items[2:])
print(store_items[:2]) #ilk iki ögeyi ekrana yazdırır

store_items[2] = "Chocolate"
print(store_items)

#veri türünü değiştirme

age = "25"
age =  int(age)
print(age, type(age))


#contact with users
#input and output functions

sayi = 22
isim = "reyhan"
print(f"{isim} {sayi} yaşındadır")

"""
namee = input('Name: ')
print('Greetings',namee)
"""

"""
numberr = input("Number: ") #input dizi gibi alıyor
print(type(numberr))
numberr = int(numberr)
print(type(numberr),numberr+10)
"""

"""
python's modules
built-in
ready to use
"""

import math
floor_number = math.floor(3.45)
print(floor_number,type(floor_number))

import datetime
print(datetime.datetime.now())

#random module
import random
print(random.randint(1,6))

#operators
x = 5
x += 5 #x++ yok

num1 = 10
num2 = 5

print(num1, ">", num2, "=", num1>num2)

# && ve || komutu yok and ve or direkt yazılıyor

celcius = 32
if celcius > 30:
    print('Hot ☀️')
elif celcius > 20:
    print("Good 🌻")
else:
    print('Cold ❄️')


drivers_licence = True
age = 17
if age > 17:
    if drivers_licence:
        print("You can drive a car")
    else:
        print("You need t go to a driver licence course")
else:
    print("You need to get older")


#foor loop ve while loop var
comp_name = 'Ajfgbgkjshgk'
for i in comp_name:
    print(i)
print("loop is complated")


toplam = 0
for i in range(1,11): # 1 to 10
    toplam+= i  # toplam = toplam + i
print(toplam)

for i in range(1,101):
    if i % 5 == 0:
        print(i)
print("loop is complated")


celcius2 = 10
while celcius2 < 50:
    print("the current temperature is", celcius2)
    if celcius2 > 30:
        print("Hot")
    elif 30 >= celcius2 > 20:
        print("Good")
    elif -273 < celcius2 <= 20:
        print("cold")
    else:
        print("something went wrong")
    celcius2 += 5
    #time.sleep(1) #bir saniye bekle

"""
while True:
    random_number = random.randrange(1000)
    print(random_number)
    if random_number == 777:
        print("Found!")
        break
"""

names = ["Max","Felix","Deniz",26,"Sarah"]

for name in names:
    if type(name) != str:
        print("Found!")
        break
    else:
        print(name, "is a string")