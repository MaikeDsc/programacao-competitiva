x = int(input())

if 0<x<6:
    result =1
else:
    result = x // 5
    if x % 5: 
        result += 1

print(result)