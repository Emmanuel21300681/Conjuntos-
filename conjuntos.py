import random


def ingresar_conjunto(nombre: str) -> list:
    while True:
        try:
            longitud = int(input(f"¿Cuántos elementos tendrá el conjunto {nombre}? "))
            if longitud < 1:
                print("La longitud debe ser al menos 1.")
                continue
            break
        except ValueError:
            print("Ingresa un número entero válido.")

    elementos = []
    print(f"Ingresa los {longitud} elementos del conjunto {nombre}:")

    for i in range(longitud):
        while True:
            try:
                valor = int(input(f"  Elemento {i + 1}: "))
                elementos.append(valor)
                break
            except ValueError:
                print("  Ingresa un número entero válido.")

    return elementos


def generar_conjunto_aleatorio(cantidad: int = 5, rango: tuple = (1, 50)) -> list:
    return [random.randint(rango[0], rango[1]) for _ in range(cantidad)]


def mostrar_conjuntos(A: list, B: list):
    print(f"\nA = {A}")
    print(f"B = {B}\n")

def cardinalidad(A: list, B: list):
    cardA = len(A)
    cardB = len(B)
    print(f"Cardinalidad de A: {cardA}")
    print(f"Cardinalidad de B: {cardB}")


def menu_principal() -> int:
    print("\nMenú principal")
    print("1. Ingresar conjuntos manualmente")
    print("2. Generar conjuntos aleatorios")
    print("0. Salir\n")

    while True:
        try:
            opcion = int(input("Elige una opción: "))
            if opcion in (0, 1, 2):
                return opcion
            print("Opción no válida. Elige 0, 1 o 2.")
        except ValueError:
            print("Ingresa un número.")


def menu_operaciones_aleatorias() -> int:
    print("\nMenú de operaciones (esqueleto)")
    print("1. Opción 1")
    print("2. Opción 2")
    print("0. Volver al menú principal\n")

    while True:
        try:
            opcion = int(input("Elige una opción: "))
            if opcion in (0, 1, 2):
                return opcion
            print("Opción no válida. Elige 0, 1 o 2.")
        except ValueError:
            print("Ingresa un número.")


def main():
    while True:
        opcion = menu_principal()

        match opcion:
            case 0:
                print("\nHasta luego.")
                break

            case 1:
                print("\nIngreso manual\n")
                A = ingresar_conjunto("A")
                B = ingresar_conjunto("B")
                mostrar_conjuntos(A, B)
                cardinalidad(A, B)

            case 2:
                print("\nConjuntos aleatorios\n")
                A = generar_conjunto_aleatorio()
                B = generar_conjunto_aleatorio()
                mostrar_conjuntos(A, B)
                cardinalidad(A, B)

                while True:
                    opcion_submenu = menu_operaciones_aleatorias()

                    match opcion_submenu:
                        case 1:
                            print("[Esqueleto] Aquí va la lógica de la opción 1.")
                        case 2:
                            print("[Esqueleto] Aquí va la lógica de la opción 2.")
                        case 0:
                            print("Regresando al menú principal...")
                            break


if __name__ == "__main__":
    main()