#!/usr/bin/env python3
"""Checks wheter two sentences are anagrams or not"""


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

    text = "".join(text_original.lower().split())
    text_prepared =  "".join(sorted(text))
    return text_prepared


def anagram(text_original1, text_original2, text_prepared1, text_prepared2):
    """checks whether the inputs are anagrams or not"""
    if text_prepared1 == text_prepared2:
        print(f"{text_original1} and {text_original2} are anagrams :)")
    else:
        print(f"{text_original1} and {text_original2} are not anagrams :(")
    return text_prepared1 == text_prepared2


def main():
    text_original1 = get_text()
    text_original2 = get_text()
    text_prepared1 = prepare_text(text_original1)
    text_prepared2 = prepare_text(text_original2)
    anagram(text_original1, text_original2, text_prepared1, text_prepared2)


if __name__ == "__main__":
    main()
