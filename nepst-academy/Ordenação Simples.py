numeros = [int(input()) for c in range (10)]
numeros.sort()
print(' '.join(map(str,numeros)))
numeros.sort(reverse=True)
print(' '.join(map(str, numeros)))



