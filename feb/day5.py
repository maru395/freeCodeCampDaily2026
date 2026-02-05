def count_change(change):
    total = sum(change) / 100
    return f"${total:.2f}"

print(count_change([25, 10, 5, 1, 25, 10, 25, 1, 1, 10, 5, 25]))
