import re

EMAIL_RE = re.compile(
    r"[A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*"   # local part
    r"@"
    r"(?:[^@\s.]+\.)+[A-Za-z]{2,}"           # domain part
)

def validate(email):

    return EMAIL_RE.fullmatch(email) is not None
