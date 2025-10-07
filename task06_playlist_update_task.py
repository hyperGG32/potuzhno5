
"""
🎵 TASK 6 — Playlist Update
Topic: dict of lists (mutations) + loops

Playlist: {"rock": ["Queen", "AC/DC"], "pop": ["Adele"], "jazz": []}
Add one new artist to each genre list, then print all genres and artists.

"""
# Starter:
playlist = {"rock": ["Queen", "AC/DC"], "pop": ["Adele"], "jazz": []}
# TODO: append one artist per genre; then print genre -> list
playlist["rock"].append("DJ Montagem")
playlist["pop"].append("DJ Spoiler")
playlist["jazz"].append("Garik")
for genre in playlist:
    print(genre.capitalize() + ": ", end='')
    l = playlist[genre]
    for i in l:
        if i == l[-1]:
            print(i, end='.\n')
            continue
        print(i, end=", ")