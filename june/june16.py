import re

def british_to_american(sentence):
    # Mapping of base British words to American words
    mapping = {
        "colour": "color",
        "flavour": "flavor",
        "honour": "honor",
        "neighbour": "neighbor",
        "labour": "labor",
        "humour": "humor",
        "centre": "center",
        "fibre": "fiber",
        "defence": "defense",
        "offence": "offense",
        "organise": "organize",
        "recognise": "recognize",
        "analyse": "analyze",
    }
    
    # Suffix translation patterns
    suffix_rules = [
        (r'([a-z]+)our(ful|ous|ing|ed|s|or)?\b', r'\1or\2'),
        (r'([a-z]+)is(e|ed|ing|er|ers|es)\b', r'\1iz\2'),
        (r'([a-z]+)ys(e|ed|ing|er|ers|es)\b', r'\1yz\2'),
        (r'([a-z]+)re(s)?\b', r'\1er\2'),
        (r'([a-z]+)ence(s)?\b', r'\1ense\2')
    ]

    def match_case(original, target):
        """Helper to match the casing of the original word string."""
        if original.isupper():
            return target.upper()
        if original.istitle() or (original and original[0].isupper()):
            return target.capitalize()
        return target.lower()

    def replace_word(match):
        original_word = match.group(0)
        word_lower = original_word.lower()
        
        # 1. Check exact base word matches first
        if word_lower in mapping:
            return match_case(original_word, mapping[word_lower])
            
        # 2. Apply general suffix rules for derived words (e.g., unrecognised, colourful)
        for br_pattern, am_sub in suffix_rules:
            if re.match(br_pattern, word_lower):
                transformed = re.sub(br_pattern, am_sub, word_lower)
                return match_case(original_word, transformed)
                
        return original_word

    # Match any sequence of letters to catch whole words (ignoring punctuation boundaries)
    return re.sub(r'[A-Za-z]+', replace_word, sentence)
