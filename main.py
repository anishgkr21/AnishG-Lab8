
#This is Anish Gaonkar's main.py file


def encode(password):
    encoded_password = "" # Empty string for shifted password
    for char in password:
        # Goes through each character and shifts it by 3
        encoded_char = chr(ord(char)+3)
        encoded_password += encoded_char
    return encoded_password

def decode(encoded_password):
    decoded_password = ""
    for i in encoded_password:
        i = int(i)
        i -= 3
        if i < 0:
            i += 10
        i = str(i)
        decoded_password += i
    return decoded_password

if __name__ == '__main__':
    # Main menu loop
    while True:
        print(" Menu \n -------------- \n 1. Encode \n 2. Decode \n 3. Quit")

        choice = int(input("Please enter an option: "))

        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored")

        if choice ==2:
            print(f"Your encoded password is {encoded_password}, and the original password is: {decode(encoded_password)}")
        if choice ==3:
            break




