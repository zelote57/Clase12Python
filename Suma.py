# Escribe un programa que solicite al usuario dos números y los almacene 
# en dos variables. En otra variable, almacená el resultado de la suma 
# de esos dos números y luego mostrá ese resultado en pantalla.
# A continuación, el programa debe solicitar al usuario que ingrese un 
# tercer número, el cual se debe almacenar en una nueva variable. 
# Por último, mostrá en pantalla el resultado de la multiplicación de 
# este nuevo número por el resultado de la suma anterior.

primerNumero = int(input("Escribe el primer numero: "))
segundoNumero = int(input("Escribe el segundo numero: "))

suma = primerNumero + segundoNumero 
print(suma)

tercerNumero = int(input("Escribe el tercero numero: "))

multi = suma * tercerNumero 
print(multi)
