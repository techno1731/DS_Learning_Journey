#!/usr/bin/env python3

# Caesar cipher


def get_text():
    while True:
        text = input("Enter your message: ")
        if len(text) > 0:
            break
        print("You must type a message to continue...")
    return text


def get_value():
    while True:
        value = input("Enter a shift value in the range [1 - 25]: ")
        try:
            value_int = int(value)
            if (value_int >= 1 and value_int <= 25):
                break
            else:
                print(f"{value_int} is not in range, please try again...")
        except ValueError:
            print(f"{value} is not an integer, try again...")
    return value_int


def cipherize(text, value_int):
    cipher = ''
    for char in text:
        if not char.isalpha():
            if char ==' ' or char.isnumeric():
                cipher += char
        else:
            if char.isupper():
                upper = True
            else:
                upper = False
                char = char.upper()
            code = ord(char) + value_int
            if code > ord('Z'):
                code = code - 26
            char_c = chr(code)
            if upper:
                cipher += char_c
            else:
                cipher += char_c.lower()
    print(f"Your message is: {cipher}")


def main():
    text = get_text()
    value = get_value()
    cipherize(text, value)


if __name__ == "__main__":
    main()
