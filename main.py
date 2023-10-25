def encode(password):
    encoded = ''
    for digit in password:
        encoded_digit = (str(int(digit) + 3) % 10)
        encoded += encoded_digit
        return encoded


def decode(password):
    decoded = ''
    for digit in password:
        encoded_digit = (str(int(digit) - 3) % 10)
        decoded += encoded_digit
        return decoded


def main():
    encoded = None

    while True:
        print("Menu")
        print("------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")
        print()

        menu_selection = int(input("Please enter an option: "))
        if menu_selection == 1:
            password = input("Please enter your password to encode:")
            encoded = encode(password)
            print("Encoded password is " + encoded)

        elif menu_selection == 2:
            encoded = input("")
            decoded = decode(encoded)
            print("Decoded password is " + decoded)

        elif menu_selection == 3:
            break


if __name__ == "__main__":
    main()