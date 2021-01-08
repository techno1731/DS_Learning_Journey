#!/usr/bin/env python3
"""Checks wheter a sentende/word is a palindrome or not"""


def get_text():
    """Gets a non blank input from the user"""
    while True:
        text_original = input("Enter your message: ")
        if len(text_original) > 0:
            break
        print("You must type a message to continue...")
    return text_original


def prepare_text(text_original):
    """Removes all white spaces and makes all chars lowercase """

    text_prepared = "".join(text_original.lower().split())
    return text_prepared


def palindrome(text_original, text_prepared):
    """Reverse the text and checks wheter it is a palindrome or not"""
    print(f"Texto original: {text_original}\nTexto preparado: {text_prepared}")
    txet = text_prepared[::-1]  # One liner for string inversion
    if text_prepared == txet:
        print(f"{text_original} is a palindrome! :)")
    else:
        print(f"{text_original} is not a palinfrome :(")
    return text_prepared == txet


def main():
    text_original = get_text()
    text_prepared = prepare_text(text_original)
    palindrome(text_original, text_prepared)


if __name__ ==  "__main__":
    main()

