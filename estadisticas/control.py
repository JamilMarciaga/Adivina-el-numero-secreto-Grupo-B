def verificar_intentos(intentos_realizados, max_intentos):
    """Muestra y retorna la cantidad de intentos disponibles."""
    if not isinstance(intentos_realizados, int) or isinstance(
        intentos_realizados, bool
    ):
        raise TypeError("Los intentos realizados deben ser un número entero.")

    if not isinstance(max_intentos, int) or isinstance(max_intentos, bool):
        raise TypeError("El máximo de intentos debe ser un número entero.")

    if max_intentos < 1:
        raise ValueError("El máximo de intentos debe ser mayor que cero.")

    if intentos_realizados < 0 or intentos_realizados > max_intentos:
        raise ValueError("La cantidad de intentos realizados no es válida.")

    intentos_restantes = max_intentos - intentos_realizados

    if intentos_restantes == 0:
        print("No te quedan más intentos.")
    elif intentos_restantes == 1:
        print("Te queda 1 intento.")
    else:
        print(f"Te quedan {intentos_restantes} intentos.")

    return intentos_restantes
