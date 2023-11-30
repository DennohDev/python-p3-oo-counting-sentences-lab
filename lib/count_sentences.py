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
        cleaned_text = re.sub(r'[.?!]+', '.', self.value)
        sentences = cleaned_text.split('.')
        valid_sentences = [sentence for sentence in sentences if sentence]
        return len(valid_sentences)

