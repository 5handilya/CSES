#input is N
n = int(input())

if(n == 1):
    print("1")
elif(n == 4):
    print("2 4 1 3")
elif(n < 4):
    print("NO SOLUTION")

else:
    #result string of length N
    res = []
    i = 0
    while i < n:
        res.append(None)
        i += 1
    
    #even places
    pos = 0
    i = 1
    while pos < n:
        res[pos] = i
        i += 1
        pos += 2
    
    #odd places
    pos = 1
    while pos < n:
        res[pos] = i
        i += 1
        pos += 2

    stres = ""
    for x in res:
        stres += (str(x) + " ")
    print(stres)
    
