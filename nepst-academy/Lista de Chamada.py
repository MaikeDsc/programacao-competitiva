n, k = map(int, input().split())

nomes = [str(input()) for c in range (n)]
nomes.sort()
print(nomes[k-1])
