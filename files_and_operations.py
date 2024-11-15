import random
# file operations

# r=> read mode , w=> write mode
message_file = open("file_operations/message.txt", "r")

content = message_file.read()
message_file.close()

print(content)

hello_file = open("file_operations/hello.txt", "w") # eğer bu dosya yoksa kendi otomatik oluşturacak

hello_file.write("I'm 22")
hello_file.close()



"""
# 777 bulma algoritmasında tahmin ettiği sayıları dosyaya kaydetme
numbers_file = open("file_operations/number_history.txt", "w")
while True:
    random_number = random.randrange(1000)
    numbers_file.write(str(random_number))  # write metod sadece str tipi veriyi kabul ediyor
    numbers_file.write("\n") # her bir sayıyı altalta yazsın


    if random_number == 777:
        print("Found")
        numbers_file.close()
        break
"""

# dosyayı kapatmanın kısa yolu da var bloktan çıkınca python otomatik dosyayı kapatır
with open("file_operations/number_history.txt", "w") as numbers_file:
    while True:
        random_number = random.randrange(1000)
        numbers_file.write(str(random_number))  # write metod sadece str tipi veriyi kabul ediyor
        numbers_file.write("\n")  # her bir sayıyı altalta yazsın

        if random_number == 777:
            print("Found")
            break