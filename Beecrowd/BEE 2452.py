comp, sementes = map(int, input().split())

pos = list(map(int, input().split()))

diasborda = []

if pos[0] > 1:
    diasborda.append(pos[0] - 1)
if pos[sementes-1] < comp:
    diasborda.append(comp  - pos[-1])

diasmeio = []

for c  in range(sementes-1):
    intervalo  = pos[c+1] - 1 - pos[c]

    if intervalo % 2 == 0:
        diasmeio.append(intervalo//2)
    else:
        diasmeio.append((intervalo//2) + 1)

todos = list()
todos.extend(diasmeio)
todos.extend(diasborda)

print(max(todos))



