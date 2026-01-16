n = int(input())

for c in range(n):

    a, b = map(int, input().split())
    if a % b == 0:
        print(0)
    else:
        rest = int(a % b)
        dist = abs(rest - b)
        print(dist)
