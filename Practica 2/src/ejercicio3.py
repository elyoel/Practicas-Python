def spoiler ():
    review = """La película sigue a un grupo de astronautas que
    viajan a Marte
    en una misión de rescate. El capitán Torres lidera al equipo
    a través
    de tormentas solares y fallos en el sistema de navegación. Al
    llegar
    a Marte descubren que la base está abandonada y los
    suministros
    destruidos. Torres decide sacrificar la nave nodriza para
    salvar
    al equipo y logran volver a la Tierra en una cápsula de
    emergencia.
    El final revela que Torres sobrevivió gracias a un pasaje
    secreto."""

    words = input('Ingrese las palabras spoiler (separadas por coma): ').split(', ')
    words_review = review.split()

    words_review = ['*' * len(word) if word in words else word for word in words_review]

    words_review = ' '.join(words_review)
    print(words_review)