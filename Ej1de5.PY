#REVISAR

import random

# Namespace para almacenar datos y funciones relacionadas con el juego
class JuegoAdivinarPrecio:
    def __init__(self):
        self.precio_real = random.randint(1, 100)
        self.apuestas = {}  # Diccionario para almacenar las apuestas
    
    def registrar_apuesta(self):
        nombre = input("Introduce tu nombre: ").strip()
        while True:
            try:
                apuesta = float(input(f"{nombre}, ¿cuánto crees que cuesta el producto?: "))
                break
            except ValueError:
                print("Por favor, introduce un número válido.")
        
        # Guardar en el diccionario usando el nombre como clave
        self.apuestas[nombre] = apuesta
    
    def determinar_ganador(self):
        if not self.apuestas:
            print("\nNadie hizo una apuesta. ¡Juego cancelado!\n")
            return
        
        # Encontrar el ganador (menor diferencia con el precio real)
        ganador = min(self.apuestas, key=lambda nombre: abs(self.apuestas[nombre] - self.precio_real))
        apuesta_ganadora = self.apuestas[ganador]
        diferencia = abs(apuesta_ganadora - self.precio_real)
        
        # Mostrar resultados
        print("\n¡Resultados!")
        print(f"Precio real: ${self.precio_real:.2f}")
        print(f"{ganador} apostó ${apuesta_ganadora:.2f} (diferencia de ${diferencia:.2f})")
        print(f" ¡El ganador es {ganador}! \n")

    def jugar(self):
        print("\n¡Bienvenidos al juego de adivinar el precio!\n")
        
        while True:
            continuar = input("¿Quieres hacer una apuesta? (sí/no): ").strip().lower()
            if continuar != 'sí':
                break
            
            self.registrar_apuesta()
        
        self.determinar_ganador()

# Crear un objeto dentro del namespace y ejecutar el juego
if __name__ == "__main__":
    juego = JuegoAdivinarPrecio()
    juego.jugar()