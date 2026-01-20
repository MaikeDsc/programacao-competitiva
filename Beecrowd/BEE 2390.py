n = int(input())
segundos = [int(input()) for c in range (n) ]

segs = 0
intervalos = 0
for c in range(n-1):
    
    if segundos[c+1] - segundos[c] > 10:
        intervalos += segundos[c+1] - segundos[c] - 10

print(segundos[-1] + 10 - segundos[0] - intervalos)
    
5
5
10
17
20
30