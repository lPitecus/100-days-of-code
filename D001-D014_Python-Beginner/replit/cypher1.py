alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text_p, shift_p):
    
    print(f"The input text is {text_p}")
    output_text = ""
    for letter in text_p:
        position = alphabet.index(letter)
        new_position = position + shift_p
        if new_position > 25:
            new_position -= 25
        output_text += alphabet[new_position]

    print(f"The encoded text is {output_text}")

    
encrypt(text, shift)