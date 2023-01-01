from caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', \
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', \
            'u', 'v', 'w', 'x', 'y', 'z']
cypher_loop = True

def caesar(text, shift_amount, cypher_direction):
    shift = shift_amount % len(alphabet)
    output_text = []
    if cypher_direction == "encode":
        for char in text:
            if char not in alphabet:
                output_text += char
            else:
                output_text += alphabet[alphabet.index(char) + shift]
    elif cypher_direction == "decode":
        for char in text:
            if char not in alphabet:
                output_text += char
            else:
                output_text += alphabet[alphabet.index(char) - shift]
    else:
        print("Please enter a valid operation: encode/decode")
        
    print("".join(output_text))

print(logo)

while cypher_loop == True:
    input_text = input("What is the text you'd like to use?\n")
    direction = input("Would you like to encode or decode?\n")
    shift_amount = int(input("Please enter the shift amount:\n"))
    
    caesar(input_text, shift_amount, direction)
    
    restart = input("Would you like to continue? Type 'yes'\n")
    if restart != 'yes':
        cypher_loop = False
