diccionario_espanol_ingles = {}
diccionario_ingles_espanol = {}

def agregar_palabra(diccionario_espanol_ingles, diccionario_ingles_espanol):
    palabra_espanol = input("Ingrese la palabra en español: ")
    palabra_ingles = input("Ingrese la palabra en inglés: ")
    diccionario_espanol_ingles[palabra_espanol] = palabra_ingles
    diccionario_ingles_espanol[palabra_ingles] = palabra_espanol
    print("Palabras agregadas exitosamente.")

def traducir_palabra(diccionario_espanol_ingles, diccionario_ingles_espanol):
    palabra = input("Ingrese la palabra a traducir: ")
    if palabra in diccionario_espanol_ingles:
        traduccion = diccionario_espanol_ingles[palabra]
        print("Traducción:", traduccion)
    elif palabra in diccionario_ingles_espanol:
        traduccion = diccionario_ingles_espanol[palabra]
        print("Traducción:", traduccion)
    else:
        print("La palabra no se encuentra en el diccionario.")

def mostrar_menu():
    print("1. Agregar palabra al diccionario")
    print("2. Traducir palabra")
    print("3. Salir")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_palabra(diccionario_espanol_ingles, diccionario_ingles_espanol)
        elif opcion == "2":
            traducir_palabra(diccionario_espanol_ingles, diccionario_ingles_espanol)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

ejecutar_menu()
