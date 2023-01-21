import numpy as np
b =  [ 2, 2]
print(b)
a = []
for i in range(len(b)):
    a.append(i)

for i, j in zip(b,a):
    print(i,j)
print(a)