def parse_url_query(url):
    query = url.split("?")[1]
    parameters = query.split("&")
    result = {}
    for parameter in parameters:
        key, value = parameter.split("=")
        result[key] = value
    return result
