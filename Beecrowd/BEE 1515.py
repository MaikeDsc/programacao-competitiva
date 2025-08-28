
cont = 0
primeiras = []

while True:
    nomes = []
    chegada =[]
    planetas = int(input())

    if planetas == 0:
        break
    for c in range (planetas):
        nome, chegouterra, demora = input().split()
        nomes.append(nome)
        chegada.append(int(int(chegouterra) - int(demora)))

    cont += 1
    localprimeira = chegada.index(min(chegada))
    primeiras.append(nomes[localprimeira])
    
for c in range(cont):
    print(primeiras[c])
