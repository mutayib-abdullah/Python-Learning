import math

c = int(input('Enter c:'))
b = int(input('Enter b:'))
a = int(input('Enter a:'))

root1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
root2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

print('root1:', root1)
print('root2:', root2)