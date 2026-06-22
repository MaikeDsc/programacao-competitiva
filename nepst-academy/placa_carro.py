placa = str(input())

padrao_antigo = True
padrao_atual = True

if 7 <= len(placa) <= 8 :

    cont = 0
    while padrao_antigo == True and cont < len(placa) and len(placa) == 8:
        if cont <= 2 and not(placa[cont].isupper()):

            padrao_antigo = False
            
        elif cont == 3 and not(placa[cont] == '-'):
            padrao_antigo = False
            
        elif cont >3 and not(placa[cont].isdigit()):
            
            padrao_antigo = False
        
        cont += 1

    #padrao atual 
    cont = 0
    while (padrao_atual == True) and (cont < len(placa)) and len(placa) == 7:
        if cont < 3 and not(placa[cont].isupper()):

            padrao_atual = False
            
        elif cont == 3 and not(placa[cont].isdigit()):
            padrao_antigo = False
            
        elif cont == 4 and not(placa[cont].isupper()):
            
            padrao_antigo = False
        elif cont > 4 and not(placa[cont].isdigit()):
            padrao_antigo = False
        cont += 1

    if padrao_antigo:
        print(1)
    elif padrao_atual:
        print(2)
    else:
        print(0)

else:
    print(0)