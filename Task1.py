# Задать строку из набора чисел. Найти большее и меньшее число. Разделитель - пробел.

def check(line):
    array = line.split()
    for i in array:
        if i.strip("-").isdigit():
            return[]
    return array

def min_max(arr):
    if arr: 
        return min(arr, key=int), max(arr, key=int)
    return []



q = check("2 78 -73 90")
print(min_max(q))       
