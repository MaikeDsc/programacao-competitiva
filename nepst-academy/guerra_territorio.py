n = int(input())

tamanhos = list(map(int, input().split()))

acum_k = 0
acum_n = 0
somask = []
somasn = []
for c in range (0, n):
   acum_k += tamanhos[c]
   somask.append(acum_k)

   acum_n += tamanhos[n-c - 1]
   somasn.append(acum_n)

print(somask)
print(somasn)
for c in range(0, n-1):
   if somask[c] == somasn[n-2 - c ]:
      res = c + 1
print(res)
