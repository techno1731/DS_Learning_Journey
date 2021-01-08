#!/usr/bin/env python3


def get_value():
    while True:
        value = input("Enter your birthdate in the format YYYYMMDD or DDMMYYYY: ")
        try:
            value_int = int(value)
            if len(value) == 8:
                break
            else:
                print(f"{value} is not a proper date, please try again...")
        except ValueError:
            print(f"{value} is not a date, try again...")
    return value


def suma(value):
    suma = 0
    for char in value:
        suma += int(char)
    while suma > 9:
        valor = str(suma)
        suma = 0
        for char in valor:
            suma += int(char)
    return suma


def main():
    value = get_value()
    digitoflife = suma(value)
    print(f"Your digit of life is {digitoflife}")


if __name__ == "__main__":
    main()

