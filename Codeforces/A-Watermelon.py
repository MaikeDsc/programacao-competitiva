kg = int(input())

for c in range(0, kg, 2):
    sub = kg - c
    if sub % 2 == 0 and c != 0:
        result = "YES"
        
    else:
        result = "no"
    
print(result)