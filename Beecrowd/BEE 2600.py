n = int(input())

for c in range(n):
    n1 = int(input())
    n2,n3,n4,n5 = map(int, input().split())
    n6 = int(input())
    v1 = [n1, n2, n3,n6,n4,n5]
    

    if (min(v1)<1 or 6 < max(v1)) :
        print('NAO')
    
    else:
        cont = 0
        for c in range(3):
            if v1.count(v1[c]) > 1: 
                break 

            elif v1[c] + v1[c+3] == 7:
                cont += 1
            else: 
                break
        if cont == 3:
            print('SIM')
        else:
            print('NAO')

