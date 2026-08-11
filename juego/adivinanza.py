import random


def _validar_entero(valor, nombre):
    """Verifica que un valor sea un número entero."""
    if not isinstance(valor, int) or isinstance(valor, bool):
        raise TypeError(f"{nombre} debe ser un número entero.")


def generar_numero_secreto(limite_superior):
    """Genera un número secreto entre 1 y el límite superior, ambos incluidos."""
    _validar_entero(limite_superior, "El límite superior")

    if limite_superior < 1:
        raise ValueError("El límite superior debe ser mayor o igual que 1.")

    return random.randint(1, limite_superior)


def evaluar_intento(numero_secreto, intento_usuario):
    """Muestra una pista y retorna True únicamente si el intento es correcto."""
    _validar_entero(numero_secreto, "El número secreto")
    _validar_entero(intento_usuario, "El intento del usuario")

    if intento_usuario < numero_secreto:
        print("El número secreto es MAYOR.")
        return False

    if intento_usuario > numero_secreto:
        print("El número secreto es MENOR.")
        return False

    print("¡Felicidades! Adivinaste el número secreto.")
    return True
