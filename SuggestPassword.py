import random
import string

print("Welcome to the Password Suggestor Project by KouMoh!")


numbers = [1,2,3,4,5,6,7,8,9]
uppercase_letters = list(string.ascii_uppercase)
lowercase_letters = list(string.ascii_lowercase)
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', ';', ':', ',', '.', '<', '>', '/', '?']

letters= uppercase_letters+lowercase_letters
password=[]



n_letters=random.randint(8,20)
n_numbers=random.randint(8,20)
n_symbols=random.randint(8,20)


for i in range(1,n_letters+1):
    char= random.choice(letters)
    password+=char

for i in range(1,n_numbers+1):
    char=str(random.choice(numbers))
    password+=char

for i in range(1,n_symbols+1):
    sym=random.choice(symbols)
    password+=sym

random.shuffle(password)
gen=''
for char in password:
    gen+=str(char)

print(f"Your strong password: {gen} ")

