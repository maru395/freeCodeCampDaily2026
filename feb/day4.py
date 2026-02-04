def truncate_text(text):
    if len(text) < 21:
        return text
    else:
        trunc_text = text[:17] 
        return f"{trunc_text}..."
