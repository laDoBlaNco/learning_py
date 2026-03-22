# task3.py
import art

print(art.logo)

# Caeser Cipher
alphabet = [chr(letter) for letter in range(97, 123)]
# Angela used this list of the alphabet, but I just used the ascii codes


# def encrypt(original_text, shift_amount):
#     cipher_text = ""

#     for letter in original_text:
#         shifted_pos = alphabet.index(letter) + shift_amount

#         shifted_pos %= len(alphabet)
#         cipher_text += alphabet[shifted_pos]

#     print(f"Here is the encoded result: {cipher_text}")


# def decrypt(original_text, shift_amount):
#     output_text = ""
#     for letter in original_text:
#         shifted_pos = alphabet.index(letter) - shift_amount

#         shifted_pos %= len(alphabet)
#         output_text += alphabet[shifted_pos]

#     print(f"Here is your decoded result: {output_text}")


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_pos = alphabet.index(letter) + shift_amount

            shifted_pos %= len(alphabet)
            output_text += alphabet[shifted_pos]

    print(f"Here is your {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # encrypt(original_text=text, shift_amount=shift)
    # decrypt(original_text=text, shift_amount=shift)
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise, type 'no'.\n"
    ).lower()

    if restart == "no":
        should_continue = False
        print("Goodbye")
