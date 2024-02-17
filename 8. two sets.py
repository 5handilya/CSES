n = int(input())
sum = (n*(n+1))/2
if sum % 2 == 1:
    print("NO")
else:
    print("YES")
    halfsum = sum//2
    A = []
    B = []
    for i in range(n, 0, -1):
        if (i <= halfsum):
            halfsum -= i
            A.append(i)
        else:
            B.append(i)
    print(len(A))
    print(*A)
    print(len(B))
    print(*B)