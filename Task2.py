# Найти корни квадратного уравнения Ax**2 + Bx + C = 0 с помощью модуля. 
# Запросить значения A, B, C 3 раза. Уравнения и корни записать в файл.

from math import sqrt
def abc(a, b, c):
    discrim = b ** 2 - 4 * a * c
    with open('result.txt', 'a' encoding='utf-8') as my_f:
        my_f.write(f"{a}x^2 + {b}x + {c} = 0")
        if discrim > 0 and a:
            my_f.write(str((-b + sqrt(discrim))/(2*a)) + "\n")
            my_f.write(str((-b - sqrt(discrim))/(2*a)) + "\n")
        elif discrim == 0 and b:
            my_f.write(str(-b/(2*a))+ "\n")
        else:
            my_f.write("Корней нет"+ "\n")

for i in range(3):
    abc(int(input()), int(input()), int(input()))
