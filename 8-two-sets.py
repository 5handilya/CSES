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
        print("I",i)

        # Halfsum will accomodate descending members of set N (1 to N) in A until halfsum < next N member
        # then, min(A) - halfsum is, of course, in N and thus guaranteed to be in the iteration
        # thus, exhaustion of halfsum by set A is guaranteed, ie set A and B are correctly computed

        if (i <= halfsum):
            print("HS",halfsum)
            halfsum -= i
            print("HS-", halfsum)
            print("A add:", i)
            A.append(i)
        else:
            print("HS",halfsum)
            print("B add: ",i)
            B.append(i)
    print(len(A))
    print(*A)
    print(len(B))
    print(*B)