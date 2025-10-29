n = int(input())
fila = list(map(int, input().split()))

s = int(input())
sairam = list(map(int, input().split()))
for i in range(s):
    fila.remove(sairam[i])

print(' '.join(map(str, fila)))
