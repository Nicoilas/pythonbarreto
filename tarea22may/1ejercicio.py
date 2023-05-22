def obtener_valor_tipo(diccionario, clave):
    if clave in diccionario:
        valor = diccionario[clave]
        tipo_dato = type(valor).__name__
        return valor, tipo_dato
    else:
        return "La clave no existe en el diccionario", None

diccionario_ejemplo = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "activo": True
}


valor, tipo_dato = obtener_valor_tipo(diccionario_ejemplo, "edad")
print("Valor:", valor)
print("Tipo de dato:", tipo_dato)


resultado = obtener_valor_tipo(diccionario_ejemplo, "apellido")
print(resultado)
Valor: 30

('La clave no existe en el diccionario', None)
