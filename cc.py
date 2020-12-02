letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
'v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
'v','w','x','y','z']


def caesar(message, shift_val, mechanism):
    final_message = ''
    if mechanism  == 'decode':
        shift_val *= -1

    for letter in message:
        if letter != ' ':
            final_message += letters[letters.index(letter) + shift_val]
        else:
            final_message += ' '

    print(f"The {mechanism}d message is: {final_message}")



while True:

    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

    if choice == 'encode':
        message = input("Enter message to encrypt: ")
        shift_val = int(input("Enter shift value: "))
        caesar(message, shift_val, choice)
    elif choice == 'decode':
        message = input("Enter message to decrypt: ")
        shift_val = int(input("Enter shift value: "))
        caesar(message, shift_val, choice)

