def format(seconds):
    hours, rem = divmod(seconds, 3600)
    minutes, secs = divmod(rem, 60)

    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"
