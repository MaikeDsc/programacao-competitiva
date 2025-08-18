nump = int(input())

pedido = []
quant = []
soma = 0
for c in range (nump):
    ped, qt = map(int, input().split())
    pedido.append(ped)
    quant.append(qt)

    if pedido[c] == 1001:
        soma += quant[c]*1.50
    elif pedido[c] == 1002:
        soma += quant[c]*2.5
    elif pedido[c] == 1003:
        soma+= quant[c]*3.5
    elif pedido[c] == 1004:
        soma += quant[c]*4.5
    elif pedido[c] == 1005:
        soma += quant[c]*5.5
   
print (f'{soma:.2f}')  