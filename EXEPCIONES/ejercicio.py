try:
    x =float(input("ingrese un numero:"))
    y =float(input("ingrese un numero:"))
    z=x/y
    print("respuesta",z)
except ValueError:
    print("no se acepta")
except ZeroDivisionError:
    print("el cero no se puede dividir")
except:
    print("nada sirve gracias :)")     
#x =float(input("ingrese un numero:"))
#y =float(input("ingrese un numero:"))
while x>0:
    print("la divicion es:",x,y)