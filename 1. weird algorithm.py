n = int(input())
printarray=[]

##even div by 2 odd times 3 plus 1

def check(m):
    printarray.append(m)
    if (m==1):
        pass
    elif (m%2==0):
        m = int(m/2)
        check(m)
    else:
        m = m*3 + 1
        check(m)
check(n)
ops = ""
for i in printarray:
    ops += (" " + str(i))
print(ops)