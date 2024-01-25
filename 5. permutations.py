#input is N
n = int(input())

if(n == 1):
    print("1")

elif(n < 4):
    print("NO SOLUTION")

else:
    #result string of length N
    res_e = []
    res_o = []
    nat = []
    
    #even places
    pos = 1
    while pos < n + 1:
        if pos % 2 == 0:
            res_e.append(pos)
        else:
            res_o.append(pos)
        pos += 1

    res = res_e + res_o
    stres = ""
    for x in res:
        stres += (str(x) + " ")
    print(stres)
    
