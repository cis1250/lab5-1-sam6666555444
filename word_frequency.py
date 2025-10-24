#!/usr/bin/env python3

import re

# This is pre-written — DO NOT modify this function
def is_sentence(text):
    if not isinstance(text, str) or not text.strip():
        return False
    if not text[0].isupper():
        return False
    if not re.search(r'[.!?]$', text):
        return False
    if not re.search(r'\w+', text):
        return False
    return True

def get_sentence():
    while True:
        sentence = input("Enter a sentence: ")
        if is_sentence(sentence):
            return sentence
        else:
            print("Invalid sentence. Make sure it starts with a capital letter and ends with '.', '!' or '?'.")

def calculate_frequencies(sentence):
    words = sentence[:-1].split() 
    word_list = []
    frequency_list = []

    for word in words:
        word = word.lower() 
        if word in word_list:
            index = word_list.index(word)
            frequency_list[index] += 1
        else:
            word_list.append(word)
            frequency_list.append(1)

    return word_list, frequency_list

def print_frequencies(words, frequencies):
    print("\nWord Frequencies:")
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")

def main():
    sentence = get_sentence()
    words, frequencies = calculate_frequencies(sentence)
    print_frequencies(words, frequencies)

if __name__ == "__main__":
    main()

