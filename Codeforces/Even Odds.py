n, k= map(int, input().split())

an = 0

if n % 2 == 0:
    if k > n/2:
        n = k - (n/2) 
        an = 2 + (n-1) * 2
        
    else:
        n = k 
        an = 1 +(n-1) * 2 
    print(int(an))

elif n % 2 != 0:
    if k > (n//2)+1:
        n = k - ((n//2) + 1)
        an = 2 + ( n-1)*2
    else:
        n = k
        an = 1 +(n-1) * 2 
    print(int(an))
