#declaramos un diccionario

opciones = {
    "izquierda":"Te encontraste con un dragón",
    "derecha":"Encontraste un Tesoro",
    "adelante":"Caíste en un pozo"
}

#solicitamos la opción al usuario
eleccion = input("Estás en un cruze. ¿Quieres ir a la derecha, izquierda o adelante?: ")

if eleccion in opciones:
    print("Respuesta: ",opciones[eleccion])
else:
    print("opción equivocada")
    
#Carpeta con nombre que diga Clase27
#tarea: considera que el jugador pueda escribir 
# las opciones tambien en Mayúsculas,
# Capital Case (cuando solo la primera letra es mayusculas)