def time_playlist ():
    playlist = [
    {"title": "Bohemian Rhapsody", "duration": "5:55"},
    {"title": "Hotel California", "duration": "6:30"},
    {"title": "Stairway to Heaven", "duration": "8:02"},
    {"title": "Imagine", "duration": "3:07"},
    {"title": "Smells Like Teen Spirit", "duration": "5:01"},
    {"title": "Billie Jean", "duration": "4:54"},
    {"title": "Hey Jude", "duration": "7:11"},
    {"title": "Like a Rolling Stone", "duration": "6:13"},
    ]
    
    durations = [ music['duration'].split(':') for music in playlist ]
    durations = [int(mm) * 60 + int(ss) for mm, ss in durations]

    total = sum(durations)
    max_music = playlist[durations.index(max(durations))]
    min_music = playlist[durations.index(min(durations))]
    
    print(f'Duracion total: {total//60}m {total%60}s')
    print(f'Cancion más larga: "{max_music['title']}" ({max_music['duration']})')
    print(f'Cancion más corta: "{min_music['title']}" ({min_music['duration']})')