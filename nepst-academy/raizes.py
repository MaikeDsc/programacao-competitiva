n = int(input())

numeros = list(map(float, input().split()))

for c in range (0, n):
    raiz = numeros[c] **(1/2)
    print(f"{raiz:.4f}")