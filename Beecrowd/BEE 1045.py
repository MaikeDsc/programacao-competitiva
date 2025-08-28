a, b, c = map(float, input().split())

nums = [a,b,c]
nums.sort()
nums = nums[::-1]
a = nums[0]
b = nums[1]
c = nums[2]

if a >= (b+c):
    print('NAO FORMA TRIANGULO')

else:
    if (a**2) == ((b**2) + (c**2)):
        print('TRIANGULO RETANGULO')
        if a == b == c:
            print('TRIANGULO EQUILATERO')

        elif (a == b) or (a == c) or (b == c):
            print('TRIANGULO ISOSCELES') 


    elif (a**2) > ((b**2) + (c**2)):
        print('TRIANGULO OBTUSANGULO')

        if a == b == c:
            print('TRIANGULO EQUILATERO')

        elif (a == b) or (a == c) or (b == c): 
            print('TRIANGULO ISOSCELES') 

    elif (a**2) < ((b**2) + (c**2)):
        print('TRIANGULO ACUTANGULO')

        if a == b == c:
            print('TRIANGULO EQUILATERO')

        elif (a == b) or (a == c) or (b == c):
            print('TRIANGULO ISOSCELES') 
