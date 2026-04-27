 from itertools import *
from math import *

n = int(input("N: "))
k = int(input("K: "))

arr = list(range(1, n+1))
print("1 задание")
# Размещения (порядок важен)
p = list(permutations(arr, k))
print("Размещения:", p)
print("Подсчет:", len(p))
print("По формуле:", perm(n, k))

# Сочетания (порядок не важен)
c = list(combinations(arr, k))
print("\nСочетания:", c)
print("Подсчет:", len(c))
print("По формуле:", comb(n, k))
