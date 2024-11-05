# DATA STRUCTURES
from PIL.DdsImagePlugin import item1

# Lists

shopping_list = ["Apple", "Juice", "Ball", "Book"]
shopping_list.append("Water") #elemanı liste sonuna ekler
print(shopping_list)
shopping_list.insert(2, "Banana") #2 indexli olan elemandan sonraya ekler
print(shopping_list)
shopping_list.remove("Apple") #listeden eleman silme
print(shopping_list)
shopping_list[3] = "Strawberry"
print(shopping_list)


number_list = [1,2,3,4,5]
square_list = []
for num in number_list:
    square_list.append(num**2)
print(square_list)

"""
Lists=Mutable  Tuples=Immutable
Listeler değişitirilebilir tuples'lar değiştirilemez
tuples da köşeli değil normal parantez kullanılır.
"""

# Tuples

shopping_list2 = ("Apple", "Juice", "Ball", "Book")

item1, item2, item3, item4 = shopping_list2
print(item1)
print(item2)
print(item3)
print(item4)

print(shopping_list[1:3])

# Dictionaries  key-value  süslü parantez kullılır
phone_book = {'Aslı Kaya' : "+90 505 123 4567", 'Selin Demir' : "+90 569 345 9723", "Reyhan Yanık" : "+90 529 876 1234"}
print(phone_book)
print(phone_book["Aslı Kaya"])

#ürün ve stok sayısını tutan ve kendimiz tek tek eklediğimiz bir dic
inventory = dict()
inventory["bananas"] = 25
inventory["apples"] = 102
inventory["oranges"] = 54
inventory["watermelons"] = 4
print(inventory)
print(inventory.keys())
print(inventory.values())
print(inventory.items())

#her ürünün stoğunu 100 artırmak istersek
for key in inventory:
    inventory[key] += 100

print(inventory)

#200 den az ve çok ürünlerimizi yazdıralım
for key, value in inventory.items():
    if value > 200:
        print('Too many', key)
    else:
        print("Enough", key)

