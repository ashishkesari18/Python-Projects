from art import logo
from dev import mark
print("Welcome to")
print(logo)
print(mark)
def caesar(start_text,shift_number,cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
            shift_number *=-1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position+shift_number
            end_text+=alphabet[new_position]
        else:
            end_text+=char

    print(f"The {cipher_direction}d text is {end_text}\n")
is_end = False
while not is_end:
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    direction = input( "For encryption type encode and for decryption type decode\n")
    text = input("type your message\n").lower()
    shift= int(input("please enter your shift number\n"))   
    shift = shift % 26
    caesar(start_text = text,shift_number = shift,cipher_direction = direction)
    result= input("Do you want to Continue..? type Yes for continue and No for stop\n").lower()
    if result == "no":
        is_end = True
print("Bye")
