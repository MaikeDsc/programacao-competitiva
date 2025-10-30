n = int(input())
cargas = [0]
car = list(map(int,input().split()))
cargas.extend(car)
cargas.sort()

resp = True
for c in range(n-1):
    if cargas[c+1] - cargas[c] >= 8:
        resp = False
        break
print('S' if resp == True else 'N')

