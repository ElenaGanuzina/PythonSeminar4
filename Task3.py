# Задать 2 числа. Найти их наименьшее общее кратное.

from math import gcd

a = int(input())
b = int(input())

print((a * b) // gcd(a, b))