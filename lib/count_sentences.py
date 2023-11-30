#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=""):
        print("The value must be a string.")
        if not isinstance(value, str):
          print("The value must be a string.")
        else:
          self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Replace multiple punctuation marks with a single dot
        cleaned_text = re.sub(r'[.?!]+', '.', self.value)
        # Split the text using dot as the separator
        sentences = cleaned_text.split('.')
        # Filter out empty sentences (resulting from consecutive dots)
        valid_sentences = [sentence for sentence in sentences if sentence]
        return len(valid_sentences)

# Example usage:
# string = MyString("This is a string! It has three sentences. Right?")
# print(string.is_sentence())  # Output: True
# print(string.is_question())  # Output: False
# print(string.is_exclamation())  # Output: True
# print(string.count_sentences())  # Output: 3
