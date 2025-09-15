# # starting from variables to  advance concept 


# # adding \n  will print in new line in pytho n programm
# print("Hello world \nThis is my first program")




#  string concatination in python




# print("my name is Ghanshyam " + "bhattarai")






# print("Notes from Day 1")
# print("The print statement is used to output strings")
# print("Strings are strings of characters")
# print("String Concatenation is done with the + sign")
# print("New lines can be created with a \ and the letter n")
      



# we used input function to take input from user , store in user variable  and print it 
# name=input(("what is you name ?"))


# print(f"my name is {name}")




# print("welcome to the tip calculator")
# bill=float(input("what was the total bill?"))


# tip=float(input("HOW MUCH YOU WANNA GIVE TIP?"))

# p=int(input("how many people to split the bill?"))


# total_bill_with_tip=bill+(bill*tip/100)

# bill_per_person=total_bill_with_tip/p

# print(f"EACH PERSON SHOUL PAY :{bill_per_person}")



#modulo operator 

#it will return the remainder after divison value 
# a=10%3

# print(a)






# thsi code is to check whether a number is even or odd
# num=float(input("Enter a number:"))


# if num%2==0:
#     print("the number is even")



# else:
#     print("the number is odd")



#Nested if/else
# this is the example of nested if/else condition 

# height=float(input("enter your Height:"))


# if height>=120:
#     print("you can ride the rollercoaster")

#     age=int(input("enter your age:"))
#     if age<=18:
#         print("you need to pay 7$")


#     else:
#         print("you need to pay 12$")




# else:
#     print("you cannot ride rollercoaster")




# PIZZA ORDER PRGRAM


print("welcome to pizza delivery")



size=input("what size of pizza do you want ? (S,M,L:)")


pepperoni=input("do you want pepperoni ? (Y/N):")


extra_cheese=input("do you want extra cheese?(Y/N):")




bill=0

if size=="S":
    bill+=15

elif size=="M":
    bill+=20

elif size=="L":
    bill+=25


else:
    print("you typed wrong inputs")




if pepperoni=="Y":
    if size=="S":
        bill+=2

    else:
        bill+=3


if extra_cheese=="Y":
    bill+=1



print(f"your final bill is :{bill}")




















