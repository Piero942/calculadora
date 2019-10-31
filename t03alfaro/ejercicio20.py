#Algoritmo para sacar la potencia
potencia,masa,tiempo,longitud=0.0,0.0,0.0,0.0

#asignacion de valores
masa,tiempo,longitud=7.8,8.9,2.9

#calculo
potencia=masa*longitud**2/tiempo**3

#mostrar valores
print("la masa es",masa)
print("el tiempo es",tiempo)
print("la longitud es",longitud)
print("la potencia es", potencia)
