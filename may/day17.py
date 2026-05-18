import datetime


def mongo_id_to_date(s):
    return datetime.datetime.utcfromtimestamp(int(s[:8], 16)).strftime("%Y-%m-%dT%H:%M:%S.000Z")
