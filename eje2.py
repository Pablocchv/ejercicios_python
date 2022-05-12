#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34,
#y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato
#y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
#Además, debe reconocer el prefijo la comunidad autónoma.

tel=input("Escribe el numero en siguiente formato  +xx-xxxxxxxxx-xx:")
print("El numero de telefono es", tel[4:-3])

prefijo=tel[4:7]
prefijo2=tel[4:6]
prefijo=int(prefijo)
prefijo2=int(prefijo2)

if prefijo==980 or prefijo==981 or prefijo==982 or prefijo==986:
    print("Galicia")
elif prefijo==942:
    print("Cantabria")
elif prefijo==945 or prefijo==943 or prefijo==944:
    print("Pais Vasco")
elif prefijo==948:
    print("Comunidad Foral de Navarra")
elif prefijo==941:
    print("La rioja")
elif prefijo==920 or prefijo==947 or prefijo==987 or prefijo==979 or prefijo==923 or prefijo==921 or prefijo==975 or prefijo==983 or prefijo==980:
    print("Castilla y león")
elif prefijo==974 or prefijo==978 or prefijo==976:
    print("Aragon")
elif prefijo==965 or prefijo==966 or prefijo==964 or prefijo==960 or prefijo==961 or prefijo==962 or prefijo2==963:
    print("Comunidad Valenciana")
elif prefijo==972 or prefijo==973 or prefijo==977 or prefijo==93:
    print("Catalunya")
elif prefijo==968:
    print("Murcia")
elif prefijo2==91:
    print("Comunidad de Madrid")
elif prefijo==950 or prefijo==956 or prefijo==957 or prefijo==958 or prefijo==959 or prefijo==953 or prefijo==951 or prefijo==954 :
    print("Andalucia")
elif prefijo==924 or prefijo==927:
    print("Extremadura")
elif prefijo==926 or prefijo==969 or prefijo==949 or prefijo==925:
    print("Castilla la Mancha")
