print("Programa para calcular Factorial de n, donde n es un número natural.")

def factorial(n: int) -> int:
    result = 1
    secuencia = list(range(1,n+1))
    
    for n in secuencia:
        result *= n
    
    return result

def main():
    try: 
        num = int(input("ingresa un número: "))

        if num < 0:
            print("Debe ingresar un número natural.")
        
        while num >= 0:
            print(f"{num}! = {factorial(num)}")
            num-=1
 
    except ValueError:
        print("Asegúrese de ingresar un número natural.")
        
if __name__ == '__main__':
    main()


# solucion recursiva
def factorial_recursivo(n):
    if n <= 1:
        return 1
    return n * factorial_recursivo(n-1)

print(factorial_recursivo(5))


# Usando la función math.factorial:
# La biblioteca estándar de Python proporciona la función factorial en el módulo math:

import math

n = 7
result = math.factorial(n)
