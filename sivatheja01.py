def caesar_cipher(text, shift, encrypt=True):
    result_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                offset = 65  # ASCII value for 'A'
            else:
                offset = 97  # ASCII value for 'a'

            shift_direction = shift if encrypt else -shift
            shifted_char = chr((ord(char) - offset + shift_direction) % 26 + offset)
            result_text += shifted_char
        else:
            result_text += char

    return result_text

def encrypt_message(text, shift):
    return caesar_cipher(text, shift, encrypt=True)

def decrypt_message(text, shift):
    return caesar_cipher(text, shift, encrypt=False)

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? ").lower()
        if choice in ['e', 'd']:
            text = input("Enter your message: ")
            shift = int(input("Enter the shift value: "))
            if choice == 'e':
                processed_text = encrypt_message(text, shift)
                print("Encrypted text:", processed_text)
            else:
                processed_text = decrypt_message(text, shift)
                print("Decrypted text:", processed_text)
        else:
            print("Invalid choice! Please select 'e' for encryption or 'd' for decryption.")

        continue_choice = input("Do you want to continue? (yes/no): ").lower()
        if continue_choice != 'yes':
            break

if __name__ == "__main__":
    main()
