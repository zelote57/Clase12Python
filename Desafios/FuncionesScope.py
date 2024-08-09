#Scope (o alcance) de variables
# 1. Scope Global

valor_numerico = 80

#función con alcance global
def PresentaValorNumerico():
    print(valor_numerico)
    
#función con alcance global    
def PresentaValorNumericoConMensajeAdicional():
    print("El valor es:", valor_numerico)

#función con alcance global    
def PresentaUnNuevoValor():
    print(100)
    
    #variable con scope (alcance) local
    mensajeHolaMundo = "Hola Mundo"
    
    #funcion con scope (alcance) local
    def MuestraHolaMundo():
        print("Esta es una ejecución desde la función interna")
        print(mensajeHolaMundo)
        
    MuestraHolaMundo()
    print(mensajeHolaMundo)
    
PresentaValorNumerico()
PresentaValorNumericoConMensajeAdicional()

