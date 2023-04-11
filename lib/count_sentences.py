#!/usr/bin/env python3
import ipdb;

class MyString:
    def __init__(self, value=""):
        self.value = value

    def get_value(self):
        return self._value
    
    def set_value(self, value):
      if (type(value) == str):
        self._value = value
      else:
        print("The value must be a string.")
    
    value = property(get_value, set_value)

    def is_sentence(self):
      if self.value.endswith("."):
         return True
      else:
         return False
      
    def is_question(self):
      if self.value.endswith("?"):
         return True
      else:
         return False
      
    def is_exclamation(self):
      if self.value.endswith("!"):
         return True
      else:
         return False
      
    def count_sentences(self):
      value = self.value
      for punc in ['!','?']:
        value = value.replace(punc, '.')
    
      sentences = [sentence for sentence in value.split('.') if sentence]
    
      return len(sentences)
        


    # def test_value_string(value):
    #
    #  if (type(value) != str):
    #       print("The value must be a string.")