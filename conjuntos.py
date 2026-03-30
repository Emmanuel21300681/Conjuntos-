import random


def ingresar_conjunto(nombre: str) -> list:
    while True:#Se usa un while true para que el usuario pueda ingresar el número de elementos del conjunto
        try:#Aquí se verifica que el usuario ingrese un número entero válido 
            longitud = int(input(f"¿Cuántos elementos tendrá el conjunto {nombre}? "))
            if longitud < 1:#Si la longitud es menor a 1, se muestra un error y se vuelve a pedir
                print("La longitud debe ser al menos 1.")
                continue
            break#Se sale del bucle si se ingresa un número válido
        except ValueError:
            print("Ingresa un número entero válido.")

    elementos = []#Aqui se crea una lista para almacenar los elementos del conjunto
    print(f"Ingresa los {longitud} elementos del conjunto {nombre}:")

    for i in range(longitud):#Se crea un bucle para que el usuario ingrese cada elemento del conjunto según la longitud de este
        while True:
            try:#Aqui como anteriormente se hace, se verifica que sea un número entero válido
                valor = int(input(f"  Elemento {i + 1}: "))#Aquí se ingresa el dato y se almacena en valor, y aumenta el contador de i
                elementos.append(valor)#Se agrega el valor a la lista de elementos del conjunto
                break
            except ValueError:
                print("  Ingresa un número entero válido.")

    return elementos#Finalmente se retorna la lista


def generar_conjunto_aleatorio(cantidad: int = 5, rango: tuple = (1, 100)) -> list:#Se generan dos conjuntos con números aleatorios
    #Usando la importación de random, se genera una lista de números aleatorios dentro del rango de (1-100)
    return [random.randint(rango[0], rango[1]) for _ in range(cantidad)]#Aquí se genera una lista de números aleatorios
    #Usando una comprensión de listas, se genera una lista de números aleatorios con la cantidad especificada y el rango dado
    #La comprensión de listas itera la cantidad de veces especificada y genera un número aleatorio en cada iteración, que se agrega a la lista resultante


def mostrar_conjuntos(A: list, B: list):
    print(f"\nA = {A}")
    print(f"B = {B}\n")

#Función que saca la cardinalidad de los conjuntos A y B
def cardinalidad(A: list, B: list):
    cardA = len(set(A))
    cardB = len(set(B))
    print(f"Cardinalidad de A: {cardA}")
    print(f"Cardinalidad de B: {cardB}")

"""
Función de intersección que utiliza los dos conjuntos A y B y 
hace la intersección de ambos conjuntos utilizando el operador &
y luego la retorna como resultado.
El operador & lo que hace es comparar ambos y solo tomar los elementos que están en los dos conjuntos,
"""
def interseccion(A: list, B: list) -> list:
    interseccion = A & B
    return interseccion


"""
Función de unión que de los dos conjuntos A y B usa el operador de |
que lo que hace es comparar los conjuntos y tomar los elementos que 
están en A, en B o en ambos y retona la union de ambos.
"""
def union(A: list, B: list) -> list:
    union = A | B
    return union

"""
En la función de diferencia se toman los dos conjuntos A y B y se utiliza 
el operador de - para obtener la diferencia, lo que hace el operador es comparar 
ambos conjuntos y tomar los elementos que están en A pero no en B, y luego se retorna la diferencia.
"""
def diferencia(A: list, B: list) -> list:
    diferencia = A - B
    return diferencia

def analisis16(A: list, B: list):
    pass

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
                A = ingresar_conjunto("A")#Se le llama a la función con el nombre de A para que la función pueda distinguir entre un conjunto y otro
                B = ingresar_conjunto("B")
                mostrar_conjuntos(A, B)
                cardinalidad(A, B)

                while True:
                    opcion_submenu = menu_operaciones_aleatorias()

                    match opcion_submenu:
                        case 1:
                            print("La intersección de A y B es: ", interseccion(set(A), set(B)))
                        case 2:
                            print("La unión de A y B es: ", union(set(A), set(B)))
                        case 3:
                            print("La diferencia de A - B es: ", diferencia(set(A), set(B)))
                        case 4:
                            print("La diferencia de B - A es: ", diferencia(set(B), set(A)))
                        case 5:
                            pass
                        case 6:
                            pass
                        case 7:
                            pass
                        case 8:
                            pass
                        case 9:
                            pass
                        case 10:
                            pass
                        case 11:
                            pass
                        case 12:
                            pass
                        case 13:
                            pass
                        case 14:
                            pass
                        case 15:
                            pass
                        case 16:
                            pass
                        case 17:
                            pass
                        case 18:
                            pass
                        case 19:
                            pass
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
                            print("La intersección de A y B es: ", interseccion(set(A), set(B)))
                        case 2:
                            print("La unión de A y B es: ", union(set(A), set(B)))
                        case 3:
                            print("La diferencia de A - B es: ", diferencia(set(A), set(B)))
                        case 4:
                            print("La diferencia de B - A es: ", diferencia(set(B), set(A)))
                        case 5:
                            pass
                        case 6:
                            pass
                        case 7:
                            pass
                        case 8:
                            pass
                        case 9:
                            pass
                        case 10:
                            pass
                        case 11:
                            pass
                        case 12:
                            pass
                        case 13:
                            pass
                        case 14:
                            pass
                        case 15:
                            pass
                        case 16:
                            pass
                        case 17:
                            pass
                        case 18:
                            pass
                        case 19:
                            pass
                        case 0:
                            print("Regresando al menú principal...")
                            break



if __name__ == "__main__":
    main()