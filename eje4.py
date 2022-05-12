#Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n.
suma=0
num=int(input("Escribe un numero"))
for i in range (1,num+1):
    print(i)
    suma=suma+i
#suma2=0
#cont=0
#while num>0 and cont<=num:
 #   suma2=suma+num
  #  cont=cont+1