def generate_slug(text):
    cleaned = "".join(c for c in text.lower() if c.isalnum() or c.isspace())
    return "%20".join(cleaned.split())
