alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

user_input = input("Do you want to encode or decode")
user_word = input("Enter the text")
shift_pos = int(input("Enter the shift position"))


def encrypt(word, shift):
    encrypted_text = ""

    for char in word:
        shifted_position = alphabets.index(char)+shift
        shifted_position %= len(alphabets)
        encrypted_text += alphabets[shifted_position]

    print(f"The encrypted text is : {encrypted_text}")
