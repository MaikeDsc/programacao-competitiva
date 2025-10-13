n = int(input())

for c in range(n):
    idades = list(map(int, input().split()))
    meio = (len(idades) // 2) 
    print(f'Case {c+1}: {idades[meio]}')
    