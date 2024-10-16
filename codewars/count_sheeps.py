"""
Counting sheeps
Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example,
"""
[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
"""
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined
"""

# Solución:

from typing import List

def count_sheeps(array_of_sheeps: List[bool]) -> int:
    return sum(1 for sheep in array_of_sheeps if sheep)


print(count_sheeps(
  [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True])
) # 17


# Otras soluciones:

def count_sheeps(array_of_sheeps:List[bool]) -> int:
  return array_of_sheeps.count(True)


def count_sheeps(array_of_sheeps:List[bool]) -> int:
  return len([x for x in array_of_sheeps if x])


def count_sheeps(array_of_sheeps:List[bool]) -> int:
  count = 0
  for sheep in array_of_sheeps:
      if sheep:
          count += 1 
  return count


def count_sheeps(array_of_sheeps: List[bool]) -> int:
    i = 0
    s = 0
    while i < len(array_of_sheeps):
        if array_of_sheeps[i]:
            s+=1
        i+=1
    return s