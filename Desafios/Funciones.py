# función sin parámetros
def MostrarMensaje():
    "Muestra un mensaje de prueba"
    
    print("Hola Mundo")
    return

# función con parámetros (argumentos)
def MostrarMensajeConParametros(nombre):
    "Muestra un mensaje de prueba"
    
    print("Hola", nombre)    
    return

# funcion sin parámetros(argumentos) que retornan un valor
def MostrarMensajeNueva():
    print("Hola Clase")
    return True

# funcion con parámetros(argumentos) que retornan un valor
def MostrarMensajeNuevaConParametros(nombre):
    mensaje = "Hola " + nombre
    print(mensaje)
    return mensaje

mensaje_devuelto = MostrarMensajeNuevaConParametros("Gustavo")

print(mensaje_devuelto, "segunda ejecución")