import random
import string
list_words= {
    "conceptos_generales": ["python", "programa", "variable"],
    "logica_control": ["funcion", "bucle"],
    "tipos_datos": ["cadena", "entero", "lista"]
}
category = list(list_words.keys())

guessed = []
attempts = 6
score = 0

print("¡Bienvenido al Ahorcado!")
print()

#While para seguir jugando al juego hasta que pierda o elija opcion de finalizar
while attempts > 0:
    #Muestra las opciones para las categorias y se ingresa un numero de categoria
    print("Elija categoria")
    for i, cat in enumerate(category):
        print(f'  - ({i}) {cat}')
    print(f'  - ({len(category)}) para finalizar')
    selection = int(input('Elija un numero: '))
    
    if selection == len(category): 
        #Muestro el puntaje final al terminar el juego
        print(f"Tu Puntaje fue de {score} puntos")
        break

    #Guardo en 'words' la lista de palabras que tiene la categoria seleccionada
    #Genero una lista aleatoria con las palabras de la categoria
    words = list_words[category[selection]]
    random_words = random.sample(words, len(words))

    for word in random_words:
        while attempts > 0:
            # Mostrar progreso: letras adivinadas y guiones para las que faltan
            progress = ""
            for letter in word:
                if letter in guessed:
                    progress += letter + " "
                else:
                    progress += "_ "
            print(progress)

            # Verificar si el jugador ya adivinó la palabra completa
            if "_" not in progress:
                score += 6
                guessed.clear()

                print("¡Ganaste!")
                print()
                break
            
            print(f"Intentos restantes: {attempts}")
            print(f"Letras usadas: {', '.join(guessed)}")

            letter = input("Ingresá una letra: ")

            if not letter.isalpha() | (len(letter) > 1):
                print("Entrada no valida")
            elif letter in guessed:
                print("Ya usaste esa letra.")
            elif letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
            else:
                guessed.append(letter)
                attempts -= 1
                score -= 1
                print("Esa letra no está en la palabra.")
            print()
        if attempts == 0:
            print(f"¡Perdiste! La palabra era: {word}")
            score = 0
            print(f"Tu puntaje queda en {score}")
            break
