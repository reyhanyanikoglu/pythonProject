from distutils.command.install import install


def function(number):
    number+=1
    print(number)

def sum_numbers(num1, num2):
    result = num1+num2
    print(result)

sum_numbers(3,2)

def argument_printer(arg_position1, arg_position2):
    print("Argument at position 1:", arg_position1)
    print("Argument at position 2:",arg_position2)

argument_printer("value 1", "value2")

def greetings(first_name,last_name,auto_correction = True): #default true dönecek
    if auto_correction == True:
        capitalized_first_name = first_name.capitalize()
        capitalized_last_name = last_name.capitalize()
        print("Hello", capitalized_first_name, capitalized_last_name)
    else:
        print("Hello",first_name, last_name)

greetings("reyhan","yanıkoğlu",True)
greetings("eDA","yIldırım")

def car(brand, model, colour):
    print("My favorite car is the", brand, model, 'in the colour', colour)
car(colour = "white", brand = "Mercedes", model="c200")

number = 13 #global value
def change_number():
    number=4 # local value
print(number)

number2 = 10
def change_number2():
    global number2
    number2 = 4

change_number2()
print(number2)

import seaborn as sns #veri görselleştirmede kullanılan bir kütüphane

data = [1,2,3,4,5,6,13]
sns.lineplot(x=range(7), y=data)  #çizgi grafiği oluşturuyor

