from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(decision, original_text, shift_amount):

    def encrypt(original_text, shift_amount):
        cipher_text = ""
        for letter in original_text:
            if letter not in alphabet:
                cipher_text += letter
            else:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
        print(f"Here is the encoded result: {cipher_text}")

    def decrypt(original_text, shift_amount):
        cipher_text = ""
        for letter in original_text:
            if letter not in alphabet:
                cipher_text += letter
            else:
                shifted_position = alphabet.index(letter) - shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
        print(f"Here is the decoded result: {cipher_text}")

    if decision == "encode":
        encrypt(original_text, shift_amount)
    elif decision == "decode":
        decrypt(original_text, shift_amount)


keep_going = True

while keep_going is True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(decision=direction, original_text=text, shift_amount=shift)

    go_again = input("Type 'yes' if you want to go again. Otherwise, type 'no'.")
    if go_again == "no":
        keep_going = False
