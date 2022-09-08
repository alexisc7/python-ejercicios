#Dado un número natural x, determinar si es capicua.

x = int(input("ingresa un numero: "))

def invertirNumero(n):
    numero = 0
    while n != 0:
        numero = 10*numero+n % 10
        n //= 10
    return numero
    
numero_invertido = invertirNumero(x)

if(x == numero_invertido):
    print(f"{x} es capicua")
else:
    print(f"{x} no es capicua")