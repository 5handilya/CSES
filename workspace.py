import math
n = int(input())
n5factors = 0
while (n >= 5):
    n5factors += (n//5)
    n//=5    
print(n5factors)


