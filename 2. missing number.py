n = int(input()) 
ns = input()

ns_str = ns.split()
ns = list(map(int,ns_str))

sumfirstn = (n*(n+1)/2)
result = int(sumfirstn - sum(ns))

print(result)