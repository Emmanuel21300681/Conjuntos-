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

#Función que saca la cardinalidad de los conjuntos A y B
def cardinalidad(A: list, B: list):
    cardA = len(set(A))
    cardB = len(set(B))
    print(f"Cardinalidad de A: {cardA}")
    print(f"Cardinalidad de B: {cardB}")

def interseccion(A: list, B: list) -> list:
    interseccion = A & B
    return interseccion

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
    print("1. Intersección de A B")
    print("2. Unión de A B")
    print("3. Diferencia A - B")
    print("4. Diferencia B - A")
    print("5. Diferencia simétrica A B")
    print("6. Complemento A")
    print("7. Complemento B")
    print("8. Producto cartesiano A x B")
    print("9. Producto cartesiano B x A")
    print("10. Producto cartesiano A x A")
    print("11. Producto cartesiano B x B")
    print("12. Conjunto potencia P(A)")
    print("13. Conjunto potencia P(B)")
    print("14. Cardinalidad |A|")
    print("15. Cardinalidad |B|")
    print("16. Análisis de propiedades (reflexiva, simétrica, transitiva) del producto cartesiano A x B")
    print("17. Análisis de propiedades (reflexiva, simétrica, transitiva) del producto cartesiano B x A")
    print("18. Análisis de propiedades (reflexiva, simétrica, transitiva) del producto cartesiano A x A")
    print("19. Análisis de propiedades (reflexiva, simétrica, transitiva) del producto cartesiano B x B")
    print("0. Volver al menú principal\n")

    while True:
        try:
            opcion = int(input("Elige una opción: "))
            if opcion in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19):
                return opcion
            print("Opción no válida. Elige un número entre 0 y 19.")
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

                while True:
                    opcion_submenu = menu_operaciones_aleatorias()

                    match opcion_submenu:
                        case 1:
                            print("La intersección de A y B es: ", interseccion(set(A), set(B)))
                        case 2:
                            print("[Esqueleto] Aquí va la lógica de la opción 2.")
                        case 3:
                            print("[Esqueleto] Aquí va la lógica de la opción 3.")
                        case 4:
                            print("[Esqueleto] Aquí va la lógica de la opción 4.")
                        case 0:
                            print("Regresando al menú principal...")
                            break


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
                            print("La intersección de A y B es: ", interseccion(A, B))
                        case 2:
                            print("[Esqueleto] Aquí va la lógica de la opción 2.")
                        case 3:
                            print("[Esqueleto] Aquí va la lógica de la opción 3.")
                        case 4:
                            print("[Esqueleto] Aquí va la lógica de la opción 4.")
                        case 0:
                            print("Regresando al menú principal...")
                            break



if __name__ == "__main__":
    main()