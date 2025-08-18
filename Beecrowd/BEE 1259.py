linhas = int(input())

numeros = []
pares = []
impares = []
for c in range (linhas):
    numeros.append(int(input()))
    if numeros[c] % 2 == 0:
        pares.append(numeros[c])
    elif numeros[c] %2 == 1:
        impares.append(numeros[c])


pares.sort()
impares.sort(reverse = True)



for cp in range (len(pares)):
    print(pares[cp])

for ci in range (len(impares)):
    print(impares[ci])
    