# we are going to ceate a caeser cipher project using python , which involves fucntions, loops and so on 


# def greet_with_name(name):
#     print(f"Hello dear {name}, how are you ?")



# greet_with_name("Angela")

import art
print(art.logo)

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



# we creat a function called encrypt() that takes original text and shift-amount as 2 inputs 



# def encrypt(original_text,shift_amount):
#     cipher_text=""

#     for letter in original_text:
#         shifted_position=alphabet.index(letter) +shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]

#     print(f"here is the encoded result :{cipher_text}")


# # encrypt(original_text=text,shift_amount=shift)





# def decrypt(original_text,shift_amount):
#     output_text=""
#     for letter in original_text:
#         shifted_position=alphabet.index(letter)-shift_amount
#         shifted_position %=len(alphabet)
#         output_text +=alphabet[shifted_position]


#     print(f" Here is ther encoded result :{output_text}")







def caeser(original_text,shift_amount,encode_or_decode):
    output_text=""
    if encode_or_decode =="decode":
                shift_amount *=-1
    for letter in original_text:
        
        if letter not in alphabet:
            output_text +=letter


        else:
           
            shifted_position=alphabet.index(letter)+shift_amount
            shifted_position %=len(alphabet)
            output_text +=alphabet[shifted_position]


    print(f" Here is ther {encode_or_decode}d result :{output_text}")




should_continue=True


while should_continue:
    direction=input("Type 'encode' to encrypt,type 'decode' to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))

    caeser(text,shift,direction)
    restart=input("Type 'yes' if you want to go again. Otherwise, type 'no' .\n").lower()

    if restart =="no":
        should_continue=False
        print("Good Bye mfs ")






