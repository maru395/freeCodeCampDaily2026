def migrate_record(template, record):
    result = dict(record) # approach, copy record because it already has values
    for key, value in template.items():
        if key not in result:
            result[key] = value
    return result
