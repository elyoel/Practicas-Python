def spoiler ():
    review = """    La película sigue a un grupo de astronautas que viajan a Marte
    en una misión de rescate. El capitán Torres lidera al equipo
    a través de tormentas solares y fallos en el sistema de navegación. Al llegar
    a Marte descubren que la base está abandonada y los suministros
    destruidos. Torres decide sacrificar la nave nodriza para salvar
    al equipo y logran volver a la Tierra en una cápsula de emergencia.
    El final revela que Torres sobrevivió gracias a un pasaje secreto."""

    spoiler_words = input('Ingrese las palabras spoiler (separadas por coma): ').lower().split(', ')
    review_words = review.split('\n')


    for i, line in enumerate(review_words):
        new_line = line
        for word in line.split():
            if word.lower().strip('. ') in spoiler_words:
                new_line = new_line.replace(word, '*' * len(word))
        review_words[i] = new_line

    review_words = '\n'.join(review_words)
    print(review_words)