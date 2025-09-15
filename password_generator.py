3# we are going to create password generator using python

# i have created threee variables for letters,numbers and symbools 

import random 
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']


print("Welcome to the pypasswrod generator")


nr_letters=int(input("how many letters would you like un your password ?\n"))
nr_symbols=int(input("how many symbols would like ?\n"))
nr_numbers=int(input("how many numbers would you like ?\n"))




# THIS IS EASY LEVEL PASSWORD GENERATOR 

password=""


for char in range(0,nr_letters):
    password+=random.choice(letters)



for char in range(0,nr_symbols):
    password+=random.choice(symbols)



for char in range(0,nr_numbers):
    password+=random.choice(numbers)



print(password)

