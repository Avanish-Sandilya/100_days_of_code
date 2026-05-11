alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

user_input = input("Do you want to encode or decode? ").lower()
user_word = input("Enter the text: ").lower()
shift_pos = int(input("Enter the shift position: "))


def encrypt(word, shift):
    encrypted_text = ""

    for char in word:

        # Ignore spaces
        if char == " ":
            encrypted_text += " "
            continue

        shifted_position = alphabets.index(char) + shift
        shifted_position %= len(alphabets)

        encrypted_text += alphabets[shifted_position]

    print(f"The encrypted text is: {encrypted_text}")


def decrypt(word, shift):
    decrypted_text = ""

    for char in word:

        # Ignore spaces
        if char == " ":
            decrypted_text += " "
            continue

        shifted_position = alphabets.index(char) - shift
        shifted_position %= len(alphabets)

        decrypted_text += alphabets[shifted_position]

    print(f"The decrypted text is: {decrypted_text}")


if user_input == "encode":
    encrypt(user_word, shift_pos)

elif user_input == "decode":
    decrypt(user_word, shift_pos)

else:
    print("Invalid choice")