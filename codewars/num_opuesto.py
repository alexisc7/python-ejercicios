# Muy simple, dado un número entero o un número de punto flotante, encuentre su opuesto.

def opposite(number):
    return number - (number*2)

print(opposite(2.5)) # -2.5

# otra solucion posible
def opposite(number):
    return -number
        
print(opposite(14)) # -14


# num = float(input("ingresa un numero: "))
# opuesto = num - (num*2)
# print(opuesto)