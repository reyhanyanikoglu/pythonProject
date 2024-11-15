def divide(number1, number2):
    try:
        number1_integer = int(number1)
        number2_integer = int(number2)
        return number1_integer / number2_integer

    except ValueError:
        return "only integers are allowed! try again."
    except ZeroDivisionError:
        return "you cannot divide any number by zero"

number1 = input("Please provide a number1: ")
number2 = input("Please provide a number2: ")

print(divide(number1, number2))
