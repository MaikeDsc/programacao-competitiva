#primeiro discionário  de Andy
#ainda farei com ascii 

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

texto = ''
while True:

    try:
        texto += input().lower()
        texto += " "
    except:
        break

n = len(texto)

for c in range(n):
    aux = texto[c]
    if aux not in alfabeto:
        texto = texto.replace(aux, "0")

palavras = list(texto.split('0'))   

selecionadas = set()
np = len(palavras)

for c in range(np):

    selecionadas.add(palavras[c])

pa = sorted(selecionadas)

del pa[0]
print('\n'.join(pa))
