n = int(input())
r = 5**(1/2)

fib = ( ( ((1+r)/2)**n ) - ( ((1-r)/2)**n ) ) / r
print(f'{fib:.1f}')
