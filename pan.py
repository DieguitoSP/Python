barras = int(input("Cuantas barras frescas has vendido hoy: "))
precio = 3.49
descuento = 0.6
coste = barras * precio * (1 - descuento)
print ("el coste de la barra fresca es " + str(precio) + "Euros")
print ("el descuento de la barra no fresca es " + str(descuento * 100) + "%" )
print ("El coste final es de " + str(round(coste, 2)) + "Euros")