def verifica_auto(auto):
    if auto >= 0 and (auto) <= 10:
        return True
    else:
        return False
    def main():
        auto1 = int(input())
        auto2 = int(input())
        auto3 = int(input())
    

        if verifica_auto(auto1) == True and verifica_auto(autoo2) == True and verifica_auto(auto3):
            promedio = (auto1 + auto2 + auto3) / 3
            print("el promedio del auto es ", promedio)
        else:
            print("todas los todos las autos estan calificdos de 0 a 10")

    main() 