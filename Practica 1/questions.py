import random
import string
words = [
    ["python", "programa", "variable"],
    ["funcion", "bucle"],
    ["cadena", "entero", "lista"]
]

num_category = int(input("""Elija una categoria para empezar:
    (1) Categoria X
    (2) Categoria logica
    (3) Categoria tipo de dato 
    """)) - 1
category = random.sample(words[num_category], len(words[num_category]))

guessed = []
attempts = 6

score = 0

print("¡Bienvenido al Ahorcado!")
print()

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
        print(f"Tu Puntaje fue de {score} puntos")
        if len(category) == 0: break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")

    if (letter not in string.ascii_letters) | (len(letter) > 1):
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
else:
    print(f"¡Perdiste! La palabra era: {word}")
    score = 0
    print(f"Tu Puntaje es de {score} puntos")
