import os
def add_songs(*tuples_):
    songs = {}
    for t in tuples_:
        if t[0] not in songs:
            songs[t[0]] = []
        songs[t[0]].extend(t[1])
    print(songs)
    result = []
    for song_title, song_lyrics in songs.items():
        result.append('- ' + song_title)
        if song_lyrics:
            result.extend(song_lyrics)
    return os.linesep.join(result)

print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
