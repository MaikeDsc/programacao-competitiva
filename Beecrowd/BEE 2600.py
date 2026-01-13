n = int(input())

for c in range(n):
    top = int(input())

    others = list(map(int, input().split()))
    base = int(input())

    
    if top + base == 7 and (0 <top<7) and (0 <base<7):
        if ((others[0] + others[2] == 7) and (0<others[0]<7) and (0<others[2]<7) ) and ((others[1] + others[3] == 7) and (0<others[1]<7) and (0<others[3]<7)):
            print('SIM')
        else:
            print('NAO')
    else:
        print('NAO') 
