def verifica_numeros(numero):
    if numero >= 0 and numero <= 100:
        return True
    else:
        return False
    def main():
        numero1 = int(input())
        numero2 = int(input())
        numero3 = int(input())

        if verifica_numeros(numero1) == True and verifica_numeros(numero2) == True and verifica_numeros(numero3):
            promedio = (numero1 + numero2 + numero3) / 3
            print("el promedio de los numeros es ", promedio)
        else:
            print("todos los numeros  deben ser valores entre 0 y 100")

    main()