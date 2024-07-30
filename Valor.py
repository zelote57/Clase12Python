#referencia en memoria
numeros = [1]
enteros = numeros
enteros.append(2)
print(numeros)
print(enteros)

#copia individual
numerosIndividuales = [1]
enterosIndividuales = numerosIndividuales[:]
enterosIndividuales.append(2)
print(numerosIndividuales)
print(enterosIndividuales)