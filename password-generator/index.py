import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = [ '0','1','2','3','4','5','6','7','8','9' ]
symbols = [ '!','@','$', '*','+' ,'%' ,'(',')']

print("welcome to the password generator")

n_letters = int(input("how many letters would you like in your password\n"))
n_symbols = int(input("how many symbols would you like\n"))
n_numbers = int(input("how many numbers would you like\n"))

password_list= [ ]

for char in range(1,n_letters+1):
    password_list.append(random.choice(letters))

for char in range(1,n_numbers+1):
    password_list.append(random.choice(numbers))

for char in range(1,n_symbols+1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
print(password_list)

password = " "
for char in password_list:
    password += char
print(f"your password is: {password}")



