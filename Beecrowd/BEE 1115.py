loop = True 
quadr = []
cont = 0
while loop == True: 
    cont += 1
    x, y = map(float, input().split())

    if x > 0 and y > 0:
        quadr.append('primeiro')
    elif x < 0 and y > 0:
        quadr.append('segundo')
    elif x < 0 and y < 0:
        quadr.append('terceiro')
    elif x > 0 and y < 0:
        quadr.append('quarto')
    elif x == 0 or y == 0:
        loop = False
    
for c in range (cont-1):
    print(quadr[c])
