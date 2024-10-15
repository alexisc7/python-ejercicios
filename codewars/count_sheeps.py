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


def count_sheeps(sheeps):
    i = 0
    s = 0
    while(i < len(sheeps)):
        if (sheeps[i] != None):
            if (sheeps[i] == True):
                s+=1
        i+=1
    return s


print(count_sheeps(
  [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True])
) # 17


# Otras soluciones:

def count_sheeps(array_of_sheeps):
  count = 0
  for sheep in array_of_sheeps:
      if sheep:
          count += 1 
  return count


def count_sheeps(array_of_sheeps):
  return array_of_sheeps.count(True)


def count_sheeps(sheeps):
  return len([x for x in sheeps if x])