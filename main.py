from niveles.dificultad import seleccionar_dificultad
from juego.adivinanza import generar_numero_secreto, evaluar_intento
from estadisticas.control import verificar_intentos


def jugar():
    print("Bienvenido a 'Adivina el Número'")
    jugar_nuevamente = "s"

    while jugar_nuevamente.lower() == "s":
        # 1. Obtener dificultad
        limite = seleccionar_dificultad()
        numero_secreto = generar_numero_secreto(limite)

        # 2. Inicializar variables del juego
        intentos_realizados = 0
        max_intentos = 5
        adivinado = False

        print(
            f"\nHe pensado en un número entre 1 y {limite}. "
            f"¡Tienes {max_intentos} intentos para adivinarlo!"
        )

        # 3. Bucle de intentos
        while intentos_realizados < max_intentos and not adivinado:
            try:
                intento_usuario = int(
                    input(
                        f"\nIntento #{intentos_realizados + 1} "
                        "- Ingresa tu número: "
                    )
                )

                if intento_usuario < 1 or intento_usuario > limite:
                    print(
                        f"Por favor, ingresa un número dentro del "
                        f"rango permitido (1 a {limite})."
                    )
                    continue

                intentos_realizados += 1

                # Evaluar si acertó
                adivinado = evaluar_intento(
                    numero_secreto,
                    intento_usuario
                )

                if not adivinado:
                    verificar_intentos(
                        intentos_realizados,
                        max_intentos
                    )

            except ValueError:
                print(
                    "Error: Por favor, ingresa un número entero válido."
                )

        if not adivinado:
            print(f"El número secreto era: {numero_secreto}")

        # 4. Preguntar si quiere jugar otra vez
        jugar_nuevamente = input(
            "\n¿Quieres jugar otra vez? (s/n): "
        ).strip()

    print("\n¡Gracias por jugar! Hasta luego.")


if __name__ == "__main__":
    jugar()