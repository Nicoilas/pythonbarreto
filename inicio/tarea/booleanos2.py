def verifica_impuestos(impuestos):
    if impuestos >= 0 and (impuestos) <= 2000:
        return True
    else:
        return False
    def main():
        impuestos1 = int(input())
        impuestos2 = int(input())
    

        if verifica_impuestos(impuestos1) == True and verifica_impuestos(impuestos2):
            promedio = (impuestos1 + impuestos2 + impuestos3) / 3
            print("el promedio de los impuestos es ", promedio)
        else:
            print("todas los impuestos deben ser valores entre 0 y 2000")

    main() 