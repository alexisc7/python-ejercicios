# Programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

#con while:
num = float(input("ingresa un numero: "))
if(num == int(num) and num > 0):
    i = 0
    while(num >= i):
        if(i % 2 != 0):
            print(i, end=", ")
        i+=1
elif(num != int(num)):
    print("ingrese un numero entero positivo")

elif(num <= 0 ):
    print("ingrese un numero positivo") 
    

# haciendo mas validaciones
num = float(input("ingrese un numero: "))
if(num == int(num) and num > 0):
    i = 0
    while(num >= i):
        if(i % 2 != 0):
            print(f"{i}",end=", ")
        i+=1
elif(num != int(num)):
    print("ingrese un numero entero y positivo")

elif(num <= 0 ):
    print("ingrese un numero positivo")



#con for:
num = float(input("ingresa un numero: "))

if(num == int(num) and num > 0):
    for x in range(int(num)+1):
    	if(x % 2 != 0):
        	print(x, end=", ")
else:
    print("ingrese un numero entero y positivo") 