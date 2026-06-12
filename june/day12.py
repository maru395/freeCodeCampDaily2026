import re

def extract_content(html):
    # 1. Strip out all HTML tags entirely
    # <[^>]*> matches '<', followed by anything that isn't '>', followed by '>'
    clean_text = re.sub(r'<[^>]*>', '', html)
    
    # 2. Fix formatting issues (turn multiple spaces or newlines into a single space)
    clean_text = re.sub(r'\s+', ' ', clean_text)
    
    # 3. Clean up any trailing/leading whitespace
    return clean_text.strip()
