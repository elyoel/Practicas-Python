from collections import Counter

def hashtags_analysis ():
    posts = [ "Arrancando el lunes con energía #Motivación #NuevaSemana",
             "Terminé mi primer proyecto en Python #Python #Programación #OrgullosoDeMi",
             "No puedo creer el final de la serie #SinSpoilers #SerieAdicta",
             "Nuevo video en el canal sobre #InteligenciaArtificial y #Python",
             "Entrenamiento de hoy completado #Fitness #Motivación #NoPainNoGain",
             "Leyendo sobre #InteligenciaArtificial y el futuro del trabajo #Tecnología",
             "Arranqué a estudiar #Programación por mi cuenta #Python #Autodidacta",
             "Finde de lluvia, maratón de series #SerieAdicta #Relax",
             "Workshop de #InteligenciaArtificial en la universidad #Tecnología #Programación"
    ]
    hashtag_words = []
    for post in posts:
        hashtag_words.extend(filter(lambda word: word.startswith('#'), post.split()))
    
    hashtag_words = Counter(hashtag_words)
    
    print('Hashtags trending (más de una aparición): ')
    for key, value in hashtag_words.most_common():
        if value > 1:
            print(f'{key}: {value}')
    print(f'Total de hashtags únicos: {len(hashtag_words)}')
    
hashtags_analysis()