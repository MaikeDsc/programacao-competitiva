n = int(input())

tacos  = list(map(int, input().split())) 

spar = set()
cont = 0
for c in range(n):

    if tacos[c] in spar:
        spar.remove(tacos[c])
    elif tacos[c] not in spar:
        spar.add(tacos[c])
        cont += 2

print(cont)
    