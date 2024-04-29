import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
user_letters = int(input("how many letters you need..?"))
user_numbers = int(input("how many letters you need..?"))
user_symbols = int(input("how many symbols you need..?"))
# easy password generator
password = ""
for char in range(1,user_letters+1):
    password += random.choice(letters)
for num in range(1,user_numbers+1):
    password += random.choice(numbers)
for symb in range(1,user_symbols+1):
    password += random.choice(symbols)
print(f"we have generated an easy password for you and that is {password}")

#hard  password generator
password_list = []
for char in range(1,user_letters+1):
    password_list+=(random.choice(letters))
for num in range(1,user_numbers+1):
    password_list += random.choice(numbers)
for symb in range(1,user_symbols+1):
    password_list+= random.choice(symbols)
random.shuffle(password_list)
f_password = ""
for char in password_list:
    f_password +=char
    
print(f"we have generated a safe password for you and that is {f_password}")