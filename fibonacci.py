# método iterativo:
from typing import List, Union

def main():
    while True:
        try:
            n = int(input("Términos a calcular: "))
            if n <= 0:
                 print("Ingrese un número entero mayor que 0.")
            else:
                f = fibo_sequence(n)
                print(f)
                break
        except ValueError:
            print("Solo se aceptan valores numéricos.")
            c = input("Continuar: 1\nSalir: 0")
            if c.isnumeric():
                if c == '0':
                    break
            else:
                print("Opción inválida.")
                break


def fibo_sequence(terminos: int) -> Union[List[int], str]:
    fibo = [0, 1]
    if terminos == 1:
        return f"primer término de la sucesión de fibonacci:\n{[0]}"
    else:
        for _ in range(terminos - 2):
            fibo.append(fibo[-1] + fibo[-2])
        return fibo


if __name__ == "__main__":
    main()



# con funcion recursiva
posicion = 8
def fibonacci_recursivo(posicion):
    if posicion < 2:
        return posicion
    return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)

posicion = int(input("Ingresa el término a calcular: ")) 
print(fibonacci_recursivo(posicion)) #21  



# implementación recursiva con memorización:
def fibonacci_memoization(posicion, memo={}):
    if posicion < 2:
        return posicion

    if posicion in memo:
        return memo[posicion]

    resultado = fibonacci_memoization(posicion - 1, memo) + fibonacci_memoization(posicion - 2, memo)
    memo[posicion] = resultado
    return resultado


n = int(input("Ingresa el término a calcular: ")) 
result = fibonacci_memoization(n)
print(result)