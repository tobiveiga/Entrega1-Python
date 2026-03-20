import random

categorias = {
    "Programación": ["python", "programa", "variable", "funcion", "bucle", "cadena", "entero", "lista"],
    "Animales": ["perro", "gato", "lobo", "loro", "tortuga", "delfin", "aguila", "serpiente"],
    "Frutas": ["manzana", "banana", "naranja", "frutilla", "sandia", "durazno", "mandarina", "uva"],
}

print("Categorías disponibles:")
for i, categoria in enumerate(categorias, 1):
    print(f"{i}. {categoria}")

opcion = int(input("Elegí una categoría (número): "))
categoria_elegida = list(categorias.keys())[opcion - 1]
words = categorias[categoria_elegida]
word = random.choice(words)

guessed = []
attempts = 6

print("¡Bienvenido al Ahorcado!")
print()

puntaje = 0

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
        print("¡Ganaste!")
        puntaje = 6 - (6 - attempts)
        print(f"Puntaje: {puntaje}")
        break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ").lower()

    if len(letter) !=1 or not ("a" <= letter <= "z"):
        print("Entrada no válida.")
        continue

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        print("Esa letra no está en la palabra.")
    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
    print("Puntaje: 0")