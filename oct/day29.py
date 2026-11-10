def sort(emails):
    def key(email):
        user, domain = email.split("@")
        return (domain.lower(), user.lower())

    return sorted(emails, key=key)
