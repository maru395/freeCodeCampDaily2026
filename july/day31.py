def decode_morse(code):
    morse_to_letter = {
        '.-': 'A', '-.': 'N', '-...': 'B', '---': 'O', '-.-.': 'C',
        '.--.': 'P', '-..': 'D', '--.-': 'Q', '.': 'E', '.-.': 'R',
        '..-.': 'F', '...': 'S', '--.': 'G', '-': 'T', '....': 'H',
        '..-': 'U', '..': 'I', '...-': 'V', '.---': 'J', '.--': 'W',
        '-.-': 'K', '-..-': 'X', '.-..': 'L', '-.--': 'Y', '--': 'M',
        '--..': 'Z'
    }
    
    morse_words = code.split("   ")
    
    decoded_words = []
    for word in morse_words:
        letters = word.split(" ")
        
        decoded_word = "".join(morse_to_letter[char] for char in letters)
        decoded_words.append(decoded_word)
        
    return " ".join(decoded_words)
