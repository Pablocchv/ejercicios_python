#Escribir un programa en el que se pregunte al usuario por una frase y una letra,
#y muestre por pantalla el número de veces que aparece la letra en la frase y el número total de caracteres de la frase sin espacios en blanco.


frase=str(input("Escribe una frase"))
caracter=str(input("Escribe el caracter a buscar"))

numc=frase.count(caracter)
sine=frase.replace(' ','')
tam=len(sine)
print(" el caracter ",caracter , "aparece un total de",numc,"el tamaño de la cadena es de ",tam)


