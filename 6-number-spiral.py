############################
t = int(input())
i = 0
inputs = []
while i < t:
    y,x = (map(int, input().split(" ")))
    inputs.append([y,x])
    i += 1

############################

#loop through inputs
for currinp in inputs:

    #calculate anchor - closest square minus diff
    x = int(currinp[0])
    y = int(currinp[1])
    mx = y if (y > x) else x
    anchor_val = mx**2 - (mx - 1)

    #calculate relative value using odd-even algo
    if (mx) % 2 == 0:
        rel_pos_val = anchor_val + (x - y)
    else:
        rel_pos_val = anchor_val + (y - x)

    #md = (-1)**(mx % 2) #1 even -1 odd
    #rel_pos_val = anchor_val + md*(x - y)

    print(rel_pos_val)
