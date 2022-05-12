#En una determinada empresa, sus productos son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores opiniones.
# Los puntos que pueden conseguir los productos pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.
# A continuación, se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de reputación conseguida en cada nivel es de 1.5 puntos multiplicada por la puntuación del nivel.
#Mal producto: 0.0
#Aceptable: 0.4
#Reseñable: 0.6 o más
#Escribir un programa que lea la puntuación del producto e indique su nivel de evaluación, así como la reputación del producto.
puntuacion = float(input("Escribe la puntuacion"))
malp=float(0.0)
acept=float(0.4)
rese=float(0.6)
val=float(1.5)

#while puntuacion != malp or acept or rese:
#    puntuacion=float(input("Escribe un producto dentro de los valores "))
if puntuacion ==malp:
    val=puntuacion*val
    print ("la puntuacion es de",val)
elif puntuacion==acept:
    val=puntuacion*val
    print("la puntuacion es de", val)
elif puntuacion==rese:
    val=puntuacion*val
    print("la puntuacion es de", val)


