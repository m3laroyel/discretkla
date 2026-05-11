from itertools import *
from math import *

n = int(input("Введите N: "))
k = int(input("Введите K: "))

arr = list(range(1, n+1))

p = list(permutations(arr, k))
print("\n")
print("Размещения:", p)
print("Подсчет:", len(p))
print("По формуле:", perm(n, k))

c = list(combinations(arr, k))
print("\n")
print("Сочетания:", c)
print("Подсчет:", len(c))
print("По формуле:", comb(n, k))