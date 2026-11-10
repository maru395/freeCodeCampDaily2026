def favorite_songs(playlist):

    return list(map(lambda s: s["title"], sorted(playlist, key=lambda s: s["plays"], reverse=True)[:2]))
