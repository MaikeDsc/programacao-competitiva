dd, mm =  map(int, input().split('/'))

if mm == 3:
    if dd >= 21:
        print('aries')
    elif dd <= 20:
        print('peixes')

elif mm == 4: 
    if dd <= 20:
        print('peixes')
    if dd >=21:
        print('touro')

elif mm ==  5:
    if dd <=20:
        print('touro')
    if dd >= 21:
        print('gemeos')

if mm == 6:
    if dd <= 20:
        print('gemeos')
    if  dd >= 21:
        print('cancer')


