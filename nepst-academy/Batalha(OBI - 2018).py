a1 = int(input())
d1 = int(input())
a2 = int(input())
d2 = int(input())

if a1 == d2 and a2 == d1:
    print(-1)

elif a1 != d2 and a2 != d1:
    print(-1)
elif a1 != d2 and a2 == d1:
    print(1)
elif a1 == d2 and a2 != d1:
    print(2)
    