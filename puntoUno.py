#Elabore un programa para la Universidad de Florida que calcule los primeros 100 números de la siguiente serie 5, 8, 13, 21, ... sin mostrar el 13, y muestre la lista del resultado de los números.


# INICIAMOS CON LOS DOS PRIMEROS NUMEROS DE SERIE
a, b = 5, 8
resultado = []

# 100 PRIMEROS NUMEROS DE LA SERIE GENERADOS
for _ in range(100):
    if a != 13:  # PARA QUE NO SALGA EL NUMERO 13
        resultado.append(a)
    # AVANCE EN LA SERIE
    a, b = b, a + b

# IMPRIMIMOS RST DE LA SERIE
print("Los primeros 100 numeros de la serie (sin el 13):")
print(resultado)
