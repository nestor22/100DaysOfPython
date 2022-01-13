import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['1','2','3','4','5','6','7','8','9','0']

simbols = ['!', '#', '$', '%','&','(',')','*','+']

print("Welcome to the password generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("how many symbols would you like?\n"))
nr_numbers = int(input("how many numbers would you like?\n"))

passwords = []

for char in range(1, nr_letters+1):
    passwords+=random.choice(letters)

for char in range(1, nr_numbers+1):
    passwords+=random.choice(numbers)

for char in range(1, nr_symbols+1):
    passwords+=random.choice(simbols)

random.shuffle(passwords)
final_pass = ""

for char in passwords:
    final_pass += char

print(final_pass)
