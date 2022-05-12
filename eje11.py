#Escribir una función que calcule el total de una factura tras aplicarle el IVA.
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura.
# Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%

def factura (preciosi, vat=21):
    preciosi=float(input("Escribe el precio de la factura sin IVA"))
    iva=float(input("Escribe el % de IVA a aplicar"))
    return preciosi+preciosi*iva/100  #para devolver el valor de la funcio que se crea

print(factura((100,4)))
print(factura(100))