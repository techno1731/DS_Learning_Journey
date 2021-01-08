#!/usr/bin/env python3
"""Finds a word in a sequence of letters can be together or separated but the
order must be right"""


def get_text():
    """Gets the user to input a valid word/text"""
    while True:
        text = input("Enter your message: ")
        if len(text) > 0:
            break
        print("You must type a message to continue...")
    return text


def findword(word, text):
    position = []
    start = 0
    for char in word:
        if text.find(char, start) == -1:
            print(f"{word} is not in {text}")
            break
        position.append(text.find(char,start))
        start = text.find(char,start)


    if len(position) == len(word):
        print(f"{word} is in {text} :)")
    return len(position) == len(word)


def main():
    word = get_text()
    text = get_text()
    findword(word, text)


if __name__ == "__main__":
    main()

