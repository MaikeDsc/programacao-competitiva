n = int(input())

alturas = list(map(int, input().split()))
limite = n//2
soma = [0 for c in range(limite)]

for c in range(limite):
    soma[c]  = alturas[c] + alturas[n-1-c]

if n%2 == 0:
    print('S' if soma.count(soma[0]) == len(soma) else 'N')

else:
    print('S' if soma.count(soma[0]) == len(soma) == alturas[(n//2)+1] else 'N') 
