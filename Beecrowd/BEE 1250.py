n = int(input())

for c in range(0, n):
    q_tiros = int(input())
    alturas = list(map(int, input().split()))
    movimentos = str(input())

    acum_dano = 0
    for i in range(0, q_tiros):
        
        if alturas[i] <= 2 and movimentos[i] == "S" :
            acum_dano += 1
            
        elif alturas[i] > 2 and movimentos[i] == "J":
            acum_dano += 1
    print(acum_dano)    
