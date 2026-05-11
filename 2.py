from itertools import *
from math import *

n = int(input("Введите N: "))
k = int(input("Введите K: "))

arr = list(range(1, n + 1))

p_rep = list(product(arr, repeat=k))
print('')
print("Размещения с повторениями:", p_rep)
print("Подсчет:", len(p_rep))
print("По формуле:", n ** k)

c_rep = list(combinations_with_replacement(arr, k))
print("")
print("Сочетания с повторениями:", c_rep)
print("Подсчет:", len(c_rep))
print("По формуле:", comb(n + k - 1, k))
