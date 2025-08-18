quant = int(input())

todasomas = []
for c in range(1, quant+1):
    n1, n2 = map(int, input().split())
    sub = n1 - n2
    somatorio  = 0

    if sub > 0:
        for cont in range(n2 + 1, n1):
            if cont % 2 == 1:
                somatorio += cont

    elif sub < 0:
        for ct in range(n1 +1, n2):
            if ct % 2 == 1: 
                somatorio += ct

    elif sub == 0:
        somatorio += 0            

    todasomas.append(somatorio)

for c in range (0, quant):
    print(todasomas[c])
               
    