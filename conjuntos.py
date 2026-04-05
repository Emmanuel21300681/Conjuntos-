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


def diferencia_simetrica(A: set, B: set):  #recibe dos conjuntos A y B
    return A ^ B  #elementos que están en A o en B pero no en ambos
#La diferencia simétrica devuelve los elementos que pertenecen a uno de los conjuntos pero no a los dos al mismo tiempo.

def complemento_A(A: set, B: set):  # complemento de A respecto a B
    return B - A  # devuelve los elementos que están en B pero no en A
#El complemento de A toma los elementos de B que no están en A.

def complemento_B(A: set, B: set):  
    return A - B  # Devuelve los elementos que están en A pero no en B
#El complemento de B toma los elementos de A que no están en B.


def producto_cartesiano(A: set, B: set):  # producto cartesiano entre los conjuntos A y B
    producto = set()  # Se crea un conjunto vacío donde se almacenarán los pares ordenados

    for a in A:  # Se recorre cada elemento de A
        for b in B:  # Por cada A se recorren todos los de B
            producto.add((a, b))  # Se crea un par ordenado (a,b) y se agrega al conjunto producto

    return producto  #devuelve conjunto con todos los pares ordenados 

'''
A = {1,2}
B = {3}
A × B = {(1,3),(2,3)}
'''



def analisis_propiedades(R, conjunto):  # r cumple ciertas propiedades 

    reflexiva = True  # Se asume que relación es reflexiva
    for a in conjunto:  # Se recorre cada elemento 
        if (a, a) not in R:  # Se verifica si el par (a,a) está en la relación
            reflexiva = False  # 
            break  

    simetrica = True  # Se asume que la relación es simétrica
    for (a, b) in R:  # Se recorren todos los pares ordenados de la relación
        if (b, a) not in R:  
            simetrica = False  
            break  

    transitiva = True  # Se asume que la relación es transitiva
    for (a, b) in R:  # Se recorre cada par de la relación
        for (c, d) in R:  # Se compara con todos los demás pares
            if b == c and (a, d) not in R:  
                transitiva = False  
                break  

    print("Reflexiva:", reflexiva) 
    print("Simétrica:", simetrica)  
    print("Transitiva:", transitiva)  

'''
Primero se genera el producto cartesiano para obtener la relación.
Luego la función analiza si la relación cumple tres propiedades matemáticas:
reflexiva, simétrica y transitiva, verificando las condiciones de cada una dentro de la relación.
'''

"""
En la función conjunto_potencia se recibe un conjunto y se genera su conjunto potencia P(C).
El conjunto potencia es una colección de todos los subconjuntos posibles de un conjunto dado, 
incluyendo el conjunto vacío y el conjunto mismo. Se inicia con una lista que contiene 
el conjunto vacío y se itera sobre cada elemento para ir generando las combinaciones.
"""
def conjunto_potencia(conjunto: set) -> list:
    lista_elementos = list(conjunto)
    potencia = [[]]  # Iniciamos con el conjunto vacío
    
    for elemento in lista_elementos:
        nuevos_subconjuntos = []
        for subconjunto in potencia:
            # Por cada subconjunto existente, creamos uno nuevo agregando el elemento actual
            nuevos_subconjuntos.append(subconjunto + [elemento])
        # Extendemos la lista original con los nuevos subconjuntos generados
        potencia.extend(nuevos_subconjuntos)
        
    # Convertimos las listas internas a tuplas para que puedan ser visualizadas 
    # de manera ordenada como elementos inmutables, simulando el comportamiento de subconjuntos.
    return [tuple(sub) for sub in potencia]

"""
La función cardinalidad_individual toma un conjunto y devuelve un número entero
que representa la cantidad de elementos únicos que lo conforman. 
Se utiliza la función integrada len() de Python sobre la estructura de datos set.
"""
def cardinalidad_individual(conjunto: set) -> int:
    cardinalidad = len(conjunto)
    return cardinalidad

"""
Esta función toma un conjunto original (que en el caso 19 será un producto cartesiano) 
y genera un subconjunto aleatorio del mismo.
Utiliza random.randint para determinar el tamaño del subconjunto y random.sample 
para extraer los elementos aleatoriamente.
"""
def subconjunto_aleatorio(conjunto_original: set) -> set:
    lista_elementos = list(conjunto_original)
    # Se define un tamaño aleatorio entre 0 y el total de elementos del conjunto original
    cantidad = random.randint(0, len(lista_elementos))
    # random.sample toma 'cantidad' elementos sin repetirlos
    subconjunto = random.sample(lista_elementos, cantidad)
    return set(subconjunto)

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
                            print("Diferencia simétrica:", diferencia_simetrica(set(A), set(B))) 
                        case 6:
                            print("Complemento de A:", complemento_A(set(A), set(B)))
                        case 7:
                            print("Complemento de B:", complemento_B(set(A), set(B)))
                        case 8:
                            print("Producto cartesiano A x B:", producto_cartesiano(set(A), set(B)))
                        case 9:
                            pass
                        case 10:
                            pass
                        case 11:
                            pass
                        case 12:
                            pass
                        case 13:
                            # Se llama a la función pasándole el conjunto B convertido en set
                            print("El conjunto potencia P(B) es: ", conjunto_potencia(set(B)))
                        case 14:
                            # Se calcula la cantidad de elementos del conjunto A
                            print("La cardinalidad de |A| es: ", cardinalidad_individual(set(A)))
                        case 15:
                            # Se calcula la cantidad de elementos del conjunto B
                            print("La cardinalidad de |B| es: ", cardinalidad_individual(set(B)))
                        case 16:
                           R = producto_cartesiano(set(A), set(B))
                           print("Relación A x B:", R)
                           analisis_propiedades(R, set(A))
                        case 17:
                            R = producto_cartesiano(set(B), set(A))
                            print("Relación B x A:", R)
                            analisis_propiedades(R, set(B))

                        case 18:
                            pass
                        case 19:
                            """
                            Para el análisis del subconjunto aleatorio de B x B:
                            1. Se obtiene el producto cartesiano completo de B x B.
                            2. Se extrae un subconjunto aleatorio de esa relación.
                            3. Se imprimen los datos y se mandan a la función de análisis.
                            """
                            producto_BxB = producto_cartesiano(set(B), set(B))
                            sub_relacion = subconjunto_aleatorio(producto_BxB)
                            print("Producto cartesiano completo B x B:", producto_BxB)
                            print(f"\nSubconjunto aleatorio a analizar (tamaño {len(sub_relacion)}):", sub_relacion)
                            print("\nAnálisis de propiedades para el subconjunto:")
                            # Se analiza el subconjunto generado contra el conjunto base B
                            analisis_propiedades(sub_relacion, set(B))
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
                            print("Diferencia simétrica:", diferencia_simetrica(set(A), set(B))) 
                        case 6:
                            print("Complemento de A:", complemento_A(set(A), set(B)))
                        case 7:
                            print("Complemento de B:", complemento_B(set(A), set(B)))
                        case 8:
                            print("Producto cartesiano A x B:", producto_cartesiano(set(A), set(B)))
                        case 9:
                            pass
                        case 10:
                            pass
                        case 11:
                            pass
                        case 12:
                            pass
                        case 13:
                            # Se llama a la función pasándole el conjunto B convertido en set
                            print("El conjunto potencia P(B) es: ", conjunto_potencia(set(B)))
                        case 14:
                            # Se calcula la cantidad de elementos del conjunto A
                            print("La cardinalidad de |A| es: ", cardinalidad_individual(set(A)))
                        case 15:
                            # Se calcula la cantidad de elementos del conjunto B
                            print("La cardinalidad de |B| es: ", cardinalidad_individual(set(B)))
                        case 16:
                           R = producto_cartesiano(set(A), set(B))
                           print("Relación A x B:", R)
                           analisis_propiedades(R, set(A))
                        case 17:
                            R = producto_cartesiano(set(B), set(A))
                            print("Relación B x A:", R)
                            analisis_propiedades(R, set(B))
                        case 18:
                            pass
                        case 19:
                            """
                            Para el análisis del subconjunto aleatorio de B x B:
                            1. Se obtiene el producto cartesiano completo de B x B.
                            2. Se extrae un subconjunto aleatorio de esa relación.
                            3. Se imprimen los datos y se mandan a la función de análisis.
                            """
                            producto_BxB = producto_cartesiano(set(B), set(B))
                            sub_relacion = subconjunto_aleatorio(producto_BxB)
                            print("Producto cartesiano completo B x B:", producto_BxB)
                            print(f"\nSubconjunto aleatorio a analizar (tamaño {len(sub_relacion)}):", sub_relacion)
                            print("\nAnálisis de propiedades para el subconjunto:")
                            # Se analiza el subconjunto generado contra el conjunto base B
                            analisis_propiedades(sub_relacion, set(B))
                        case 0:
                            print("Regresando al menú principal...")
                            break



if __name__ == "__main__":
    main()
