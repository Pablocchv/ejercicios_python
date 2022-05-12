#  Escribir un programa que pregunte el nombre completo del usuario (nombre y apellidos) en la consola
#  y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas,
#  otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
#  El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
nombre=(input("Escribe tu nombre"))
apellido=(input("Escribe tu apellido"))
apellidodos=(input("Escribe tu segundo apellido"))

for i in range (1,2):
    print(nombre.lower())
    print(apellido.lower())
    print(apellidodos.lower())
    print(nombre.upper())
    print(apellido.upper())
    print(apellidodos.upper())
    print(nombre.capitalize())
    print(apellido.capitalize())
    print(apellido.capitalize())


  