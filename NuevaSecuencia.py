# Escribe un programa que le solicite al usuario 
# un número entero y muestre todos los números 
# correlativos entre el 1 y el número 
# ingresado por el usuario.

numero = int(input("Ingrese un valor: "))
numero_limite = range(1,numero+1)

for indice in numero_limite:
    print(indice)
   
# numero_entero=""
# for indice in numero_limite:
#     numero_entero+= str(indice)+" "
    
# print(numero_entero)

