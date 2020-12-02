letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
'v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
'v','w','x','y','z']

def encrypt(message, shift_val):
    encrypted_message = ''

    for letter in message:
        if letter != ' ':
            encrypted_message += letters[letters.index(letter) + shift_val]
        else:
            encrypted_message += ' '
    
    return encrypted_message

def decrypt(message, shift_val):
    decrypted_message = ''

    for letter in message:
        if letter != ' ':
            decrypted_message += letters[letters.index(letter) - shift_val]
            # print("index: ", letters.index(letter))
        else:
            decrypted_message += ' '
    
    return decrypted_message


# print(encrypt('bmj', 1))      
# print(decrypt('ali', 1))  

while True:

    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

    if choice == 'encode':
        message = input("Enter message to encrypt: ")
        shift_val = int(input("Enter shift value: "))
        print("Encoded message: ", encrypt(message, shift_val))
    elif choice == 'decode':
        message = input("Enter message to decrypt: ")
        shift_val = int(input("Enter shift value: "))
        print("Decoded message: ", decrypt(message, shift_val))