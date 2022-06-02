# Tuple: ordered, immutable, allows duplicate elementes
# Lists: ordered, mutable, allows duplicate elements

import sys
import timeit

my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)

print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")
print("Listas são dados mutaveis, porém ocupam mais espaço que tupla\n\n")

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
print("Listas demoram mais tempo para serem processadas")