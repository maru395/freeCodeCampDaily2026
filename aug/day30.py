def find_duplicates(arr):
    seen = set()
    duplicates = []
    for n in arr:
        if n in seen and n not in duplicates:
            duplicates.append(n)
        seen.add(n)

    return sorted(duplicates)
