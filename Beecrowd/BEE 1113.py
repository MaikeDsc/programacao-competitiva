loop = True
cont = 0
ordens = []
while loop == True:
    n1, n2 = map(int, input(). split())
    cont += 1
    if n1 > n2:
        ordens.append('Decrescente')
    elif n2 > n1:
        ordens.append('Crescente')
    elif n1 == n2:
        loop = False

for c in range(cont-1):
    print(ordens[c])