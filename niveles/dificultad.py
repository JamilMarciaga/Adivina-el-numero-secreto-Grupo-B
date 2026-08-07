def seleccionar_dificultad():
    """Permite al usuario elegir el nivel de dificultad y retorna el límite superior."""
    print("\n--- SELECCIONA EL NIVEL DE DIFICULTAD ---")
    print("1. Fácil (1 al 10)")
    print("2. Medio (1 al 20)")
    print("3. Difícil (1 al 50)")
    
    while True:
        try:
            opcion = int(input("Elige una opción (1-3): "))
            if opcion == 1:
                return 10
            elif opcion == 2:
                return 20
            elif opcion == 3:
                return 50
            else:
                print("Opción inválida. Selecciona 1, 2 o 3.")
        except ValueError:
            print("Error: Ingresa un número válido.")