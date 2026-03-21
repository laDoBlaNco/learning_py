# task3.py

# Caeser Cipher
# alphabet = [chr(letter) for letter in range(97, 123)]
# Angela used this list of the alphabet, but I just used the ascii codes

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type yoru message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1 - create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2
# inputs.

# TODO-2 - Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the
# alphabet by the shift amount and print the encrypted text.

# TODO-3 - Call the 'encrypt()' function and pass in the user inputs.

# TODO-4 - What happens if we try to shift z forwards by 9? Can we fix the code?

# TODO-5 - Create a function called 'decrypt()' that thakes 'origina_text' and 'shift_amount' 

# TODO-6 - Inside 'decrypt()', shift each letter of the 'original_text' *backwards* by the shift
#   amount and print the decrypted word.

# TODO-7 - Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()' 
#   Using the value of the user in 'direction' to determine which function to run

def encrypt(original_text:str,shift_amount:int):
    res = []
    for letter in original_text:
        if letter==' ':
            res.append(' ')
        elif ord(letter)+shift_amount > 122:
            res.append(chr(ord(letter)+shift_amount-26))
        else:
            res.append(chr(ord(letter)+shift_amount))
    print(''.join(res))

def decrypt(original_text:str,shift_amount:int):
    res = []
    for letter in original_text:
        if letter==' ':
            res.append(' ')
        elif ord(letter)-shift_amount < 97:
            res.append(chr(ord(letter)-shift_amount+26))
        else:
            res.append(chr(ord(letter)-shift_amount))
    print(''.join(res))


def caesar(original_text:str,shift_amount:int,dir:str):
    if dir == 'encode':
        encrypt(original_text,shift_amount)
    elif dir == 'decode':
        decrypt(original_text,shift_amount)

caesar(text,shift,direction)