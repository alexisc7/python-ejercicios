# Programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

frase = input("frase: ")
letra = input("letra: ")

i = 0
n = len(frase) - 1
rep = 0
while(i <= n):
    if(frase[i]==letra[0]):
        rep+=1
    i+=1
print(f"La letra '{letra}' se repite {rep} veces")


# lo mismo solo q mostrando el recorrido de la frase:
frase = input("frase: ")
letra = input("letra: ")

i = 0
n = len(frase) - 1
rep = 0
while(i <= n):
    print(frase[i])
    if(frase[i]==letra[0]):
        rep+=1
    i+=1
print(f"La letra '{letra}' se repite {rep} veces")
