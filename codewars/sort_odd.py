""""
Sort the odd 6kyu

Task
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""

def sort_array(source_array):
    odd = sorted([num for num in source_array if num % 2 != 0])
    result = []
    i = 0
    for num in source_array:
        if num % 2 == 0:
            result.append(num)
        else:
            result.append(odd[i])
            i += 1
    return result

print(sort_array([7, 1])) #[1, 7]
print(sort_array([5, 8, 6, 3, 4])) #[3, 8, 6, 5, 4]
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) #[1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


# otras soluciones:

def sort_array(source_array):
    result = sorted([l for l in source_array if l % 2 == 1])
    for index, item in enumerate(source_array):
        if item % 2 == 0:
            result.insert(index, item)
    return result


def sort_array(source_array):
    odd = sorted(list(filter(lambda x: x % 2, source_array)))
    l, c = [], 0
    for i in source_array:
        if i in odd:
            l.append(odd[c])
            c += 1
        else:
            l.append(i)    
    return l


def sort_array(source_array):
    odds = iter(sorted(elem for elem in source_array if elem % 2 != 0))
    return [next(odds) if el % 2 != 0 else el for el in source_array]
