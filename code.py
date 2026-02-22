import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
# print(lista)
password_list = []
for letra in range(0, nr_letters):
    password_list.append(random.choice(letters))
# print(simbolos)
nr_symbols = int(input(f"How many symbols would you like?\n"))
for letra in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
# print(numeros)
nr_numbers = int(input(f"How many numbers would you like?\n"))
for letra in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)

# SERIE
password = ""
for carac in password_list:
    password += carac + ""

print(f"Your easy password is: {password}")

# SHUFFLE
password = ""
random.shuffle(password_list)
for carac in password_list:
    password += carac + ""

print(f"Your difficult password is: {password}")
