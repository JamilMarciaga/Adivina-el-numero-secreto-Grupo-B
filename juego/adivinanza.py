# juego/adivinanza.py
import random

def generar_numero_secreto(limite_superior):
    """Genera un número aleatorio entre 1 y el límite superior indicado."""
    return random.randint(1, limite_superior)

def evaluar_intento(numero_secreto, intento_usuario):
    """Compara el número ingresado con el secreto y retorna una pista."""
    if intento_usuario < numero_secreto:
        print("El número secreto es MAYOR.")
        return False
    elif intento_usuario > numero_secreto:
        print("El número secreto es MENOR.")
        return False
    else:
        print("¡Felicidades! Adivinaste el número secreto.")
        return True
