n = int(input())

numeros = [int(input()) for c in range(n)]

numeros.sort()

results  = {}

for num in numeros:

    results[num] = results.get(num, 0) + 1

for c in results:

    print(f'{c} aparece {results[c]} vez(es)')
