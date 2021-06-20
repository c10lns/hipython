from functools import reduce

print(reduce(lambda x, y: x * 10 + y, [1, 2, 3]))
print(list(map(lambda x: x * x, [1, 2, 3])))
print(reduce(lambda x, y: x * 10 + y, map(lambda x: x * x, [1, 2, 3])))



