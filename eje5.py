#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente
#<c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario,
#y <c> y <r> son el cociente y el resto de la división entera respectivamente

n=int(input("Escribe un numero"))
m=int(input("Escribe un numero"))

divi=n/m
resto=n%m
print(n ,"entre" ,m,"da un conciente" ,divi,"y un resto", resto,"y ", n, m, "son los números introducidos por el usuarios,y", divi, "y" ,resto, "son el cociente y el resto de la división entera")

