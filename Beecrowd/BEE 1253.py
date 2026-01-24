n = int(input())

for c in range(n):

    criptografado  = str(input())
    deslocamento = int(input())
    c_separado = [ord(c) for c in criptografado]

    desc_separado = [((c-65-deslocamento)%26 + 65) for c in c_separado]
    desc_letras = [chr(c) for c in desc_separado]
    print(''.join(desc_letras))
