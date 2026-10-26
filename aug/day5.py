def get_spoken_duration(seconds):
    h, rest = divmod(seconds, 3600)
    m, s = divmod(rest, 60)

    parts = []
    for n, unit in [(h, "hour"), (m, "minute"), (s, "second")]:
        if n:
            parts.append(f"{n} {unit}{'s' if n != 1 else ''}")

    return " and ".join(", ".join(parts).rsplit(", ", 1))
