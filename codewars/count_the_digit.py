"""
Count the Digit

Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.

Square all numbers k (0 <= k <= n) between 0 and n.

Count the numbers of digits d used in the writing of all the k**2.

Implement the function taking n and d as parameters and returning this count.

Examples:
n = 10, d = 1 
the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
We are using the digit 1 in: 1, 16, 81, 100. The total count is then 4.

The function, when given n = 25 and d = 1 as argument, should return 11 since
the k*k that contain the digit 1 are:
1, 16, 81, 100, 121, 144, 169, 196, 361, 441.
So there are 11 digits 1 for the squares of numbers between 0 and 25.
Note that 121 has twice the digit 1.



==========================================================================================================

Cuenta el dígito
Tome un entero n (n >= 0) y un dígito d (0 <= d <= 9) como un entero.

Eleve al cuadrado todos los números k (0 <= k <= n) entre 0 y n.

Cuente la cantidad de dígitos d utilizados en la escritura de todos los k**2.

Implemente la función tomando n y d como parámetros y devolviendo este recuento.

Ejemplos:
n = 10, d = 1
los k*k son 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
Estamos usando el dígito 1 en: 1, 16, 81, 100. El recuento total es entonces 4.

La función, cuando se le da n = 25 y d = 1 como argumento, debe devolver 11 ya que
los k*k que contienen el dígito 1 son:
1, 16, 81, 100, 121, 144, 169, 196, 361, 441.
Por lo tanto, hay 11 dígitos 1 para los cuadrados de los números entre 0 y 25.
Ten en cuenta que 121 tiene el doble del dígito 1.
"""


def nb_dig(n, d):
    d_str = str(d)
    count = 0
    
    for k in range(n+1):
        square = k**2
        count += str(square).count(d_str)
        
    return count  
    

print(nb_dig(10,1)) # 4
print(nb_dig(25,1)) # 11   
print(nb_dig(5,1)) # 2
print(nb_dig(14,4)) # 5 
print(nb_dig(5750, 0)) # 4700
print(nb_dig(11011, 2)) # 9481



# solución 2
def nb_dig(n, d):
    cad_dig = ""
    for k in range(n+1):
        cad_dig += str(k**2)
        
    return cad_dig.count(str(d))   


# solución 3
def nb_dig(n, d):
    count = 0
    for k in range(n + 1):
        square = k * k
        while square > 0:
            if square % 10 == d:
                count += 1
            square //= 10
    return count+1 if d==0 else count