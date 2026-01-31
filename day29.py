import re

def separate_letters_and_numbers(text):
    #  Find a Letter followed by a Digit
    text = re.sub(r'([a-zA-Z])(\d)', r'\1-\2', text)
    
    # Find a Digit followed by a Letter
    text = re.sub(r'(\d)([a-zA-Z])', r'\1-\2', text)
    
    return text
