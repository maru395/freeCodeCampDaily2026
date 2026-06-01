def is_valid_schema(obj):
    # Get key independently
    first_key = next(iter(obj))
    # Get value independently
    first_value = next(iter(obj.values()))
    return isinstance(first_key, str) and isinstance(first_value, str)
