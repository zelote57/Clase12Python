#definir el diccionario para almacenar los valores por usuario
usuarios = {}
#definir datos de prueba (mocks)
usuarios["gustavo"] = 400.00
usuarios["carlos"] = 200.00

def registrar_usuario():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        print("El usuario ya esta registrado")
    else:    
        usuarios[nombre] = 0.00
        print(f"usuario {nombre} agregado correctamente")

def depositar():
    nombre = input("Introduce el nombre del usuario: ")
    
    if nombre in usuarios:
        monto =  float(input("Introduce el monto a depositar: "))
        usuarios[nombre] += monto
    else:
        print(f"Usuario {nombre} no existe")

def retirar():
   nombre = input("Ingrese el nombre del usuario: ") 
   
   if nombre in usuarios:
       retiro = float(input("Ingrese el monto de retiro: "))
       if retiro > usuarios[nombre]:
           print("Saldo insuficiente para retirar")
       else:
           usuarios[nombre] -= retiro
       
   else:
       print("Usuario no existente en el sistema")

       
    

print(usuarios)
retirar()
print(usuarios)


