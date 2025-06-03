import re

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value 

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(val, str):
            self._value = val
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        sentences = re.split(r'[.!?]', self.value)
        return len([s for s in sentences if s.strip()])