# Unaa pelota se deja caer desde una altura "h", y en cada rebote sube el -10% del anterior.
# Hacer el diagrama de flujo y el programa en python, que lea "h" y que calcule e imprima en cual rebote la pelota no alcanza a subir la quinta parte de la altura inicial

print("---------------------------------------------")
print("----------------REBOTE-PELOTA----------------")
print("---------------------------------------------")

#input
h = int(input("Digíta la altura en que se dejo caer la pelota: "))

#process
i = 0
h1 = h

while h1 > h*0.2:
    h1 = h1 - h1 * 0.1
    i = i + 1

else:
    print("La pelota fue lanzada a una altura de",h,"y despues de",i,"rebotes la altura fue inferior a 1/5 siendo de:",h1)