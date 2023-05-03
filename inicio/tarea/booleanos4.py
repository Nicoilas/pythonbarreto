def verifica_ingresos(ingresos):
    if ingresos >= 0 and ingresos <= 50000:
        return True
    else:
        return False
    def main():
        ingresos = int(input())
        ingresos = int(input())
        ingresos = int(input())

        if verifica_ingresos(ingresos1) == True and verifica_ingresos(ingresos2) == True and verifica_ingresos(ingresos3):
            promedio = (ingresos1 + ingresos2 + ingresos3) / 3
            print("el promedio de los ingresos es ", promedio)
        else:
            print("todos los ingresos deben ser valores entre 0 y 50000")

    main()