# Escriba un programa que, dado un número entero positivo, calcule y muestre su factorial. 
# El factorial de un número se obtiene multiplicando todos los números enteros positivos 
# que hay entre el 1 y ese número. El factorial de 0 es 1.

numero=int(input("Ingrese el numero a calcular: "))
factorial=1
for contador in range (1, numero+1):
    factorial=factorial*contador
    
print(factorial)
    
    