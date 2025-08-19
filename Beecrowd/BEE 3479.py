dd, mm =  map(int, input().split('/'))

if mm == 1:
    if dd <= 19:
        print('capricornio')
    elif dd >= 20:
        print('aquario')

elif mm == 2:
    if dd <= 18:
        print('aquario')
    elif dd >= 19:
        print('peixes')

if mm == 3:
    if dd <= 20:
        print('peixes')
    elif dd >= 21:
        print('aries')
    
elif mm == 4: 
    if dd <= 20:
        print('aries')
    elif dd >=21:
        print('touro')

elif mm ==  5:
    if dd <=20:
        print('touro')
    elif dd >= 21:
        print('gemeos')

elif mm == 6:
    if dd <= 20:
        print('gemeos')
    elif dd >= 21:
        print('cancer')

elif mm == 7:
    if dd <= 22:
        print('cancer')
    elif dd >= 23:
        print('leao')

elif mm == 8:
    if dd <= 22:
        print('leao')
    elif dd >= 23:
        print('virgem')

elif mm == 9:
    if dd <= 22:
        print('virgem')
    elif dd >= 23:
        print('libra')

elif mm == 10:
    if dd <= 22:
        print('libra')
    elif dd >= 23:
        print('escorpiao')

elif mm == 11:
    if dd <= 21:
        print('escorpiao')
    elif dd >= 22:
        print('sagitario')

elif mm == 12:
    if dd <= 21:
        print('sagitario')
    elif dd >= 22:
        print('capricornio')
