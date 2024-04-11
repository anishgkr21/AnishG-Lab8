
#This is Anish Gaonkar's main.py file


def encode(password):
    encoded_password = ""
    for i in password:
        i += 3
        i = str(i)
        encoded_password += i
    return encoded_password

def decode(encoded_password):
    decoded_password = encoded_password[::-1]
    return decoded_password

if __name__ == '__main__':
    while True:
        print("Menu \n -------------- \n 1. Encode \n 2. Decode \n 3.Quit")

        choice = int(input("Please enter an option: "))

        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print(encoded_password)



