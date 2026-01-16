n = int(input())

for c in range(n):
    candies = int(input())

    if candies <= 2: 
        print(0)
    else:
        aux = (candies//2) + 1
        conbinations = candies - aux 
        print(conbinations)
        