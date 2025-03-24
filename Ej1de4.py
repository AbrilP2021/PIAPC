import random

# Lista de palabras para el juego
palabras = ['auricular', 'casa', 'perro', 'sebastian', 'mate']
palabra_oculta = random.choice(palabras)  # Selecciona una palabra al azar
letras_adivinadas = ['_'] * len(palabra_oculta)
errores = 0
max_errores = 6

print("¡Juega al ahorcado!")
print(' '.join(letras_adivinadas))

# Bucle principal del juego
while errores < max_errores and '_' in letras_adivinadas:
    letra = input("\nIngresa una letra: ").lower()

    if letra in palabra_oculta:
        # Si la letra está en la palabra, revelar las posiciones
        for i in range(len(palabra_oculta)):
            if palabra_oculta[i] == letra:
                letras_adivinadas[i] = letra
        print("Tu letra esta en la palabra")
    else:
        # Si la letra no está, aumentar el contador de errores
        errores += 1
        print(f" Letra incorrecta. Te quedan {max_errores - errores} intentos.")

    # Mostrar progreso actual
    print(' '.join(letras_adivinadas))

# Verificar si ganó o perdió
if '_' not in letras_adivinadas:
    print("\n¡Felicidades! Has adivinado la palabra correctamente. ")
else:
    print(f"\n ¡Perdiste! La palabra era: {palabra_oculta}.")
