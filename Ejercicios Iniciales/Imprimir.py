palabra= input("Introduzca una palabra")

# palabra_reverse = list (palabra)
# palabra_reverse.reverse()

palabra_reverse = palabra[::-1]

for letra in palabra_reverse:
     print(letra)