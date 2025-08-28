qroupas = int(input())


lmin, lmax = map(int, input().split())
smin, smax = map(int, input().split())
cont =0

if (lmin <= qroupas <= lmax) and (smin <= qroupas <= smax):
    print('possivel')

else:
    print('impossivel')
    