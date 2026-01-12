import math

voltas, placas = map(int, input().split())

total_placas = voltas * placas

porc = 0
result = []
for c in range(9):
    porc += 0.1
    mult = (total_placas * porc)
    result.append(math.ceil(mult))

print(' '.join(map(str, result)))
