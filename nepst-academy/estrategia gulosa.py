# notas: 1 5 10 25 50 100

notas = [100, 50, 25, 10, 5]

valor = int(input())
q = 0
for c in range(5):
    aux = valor
    q += aux//notas[c]
    valor = aux%notas[c]
print(q+valor)

"""
valor =  int(input())

c1 = valor//100
rc1 = valor%100

c2 = rc1//50
rc2 = rc1%50

c3 = rc2//25
rc3 = rc2%25

c4 = rc3//10
rc4 = rc3%10

c5 = rc4//5
rc5 = rc4%5

print(c1+c2+c3+c4+c5+rc5)

"""