m, n, a = map(int, input().split())

heighth = 0
width = 0

heighth_total = m/a
width_total = n/a

if heighth_total > m//a:
    heighth = (m//a) + 1
else: 
    heighth = m // a

if width_total > n // a:
    width = (n // a) + 1
else:
    width = n//a

print(width * heighth)