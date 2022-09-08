# Tablas de multiplicar.

# Imprime todas las tablas del 1 al 10:
tabla = 1
x = 10
while(tabla<=x):
    print(f"\nTABLA DEL {tabla}:")
    i = 1
    while(i <= x):
        print(f"{tabla} x {i} = {tabla * i}")
        i+=1
    tabla+=1


# Permite ingresar hasta que tabla se va mostrar y hasta q numero multiplicar: 
t = 1
x = int(input("Mostrar hasta la tabla del: "))
n = int(input("Multiplicar hasta el número: "))
while(t<=x):
    print(f"\nTABLA DEL {t}:")
    i = 1
    while(i <= n):
        print(f"{t} x {i} = {t * i}")
        i+=1
    t+=1



