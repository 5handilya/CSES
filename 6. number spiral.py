############################
t = int(input())
import sys
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
    mx = max(x,y)
    anchor_val = mx**2 - (mx - 1)

    #calculate relative value using odd-even algo
    anchor_pos = [max(x,y),max(x,y)]
    if (anchor_pos[0]) % 2 == 0:
        rel_pos_val = anchor_val + (anchor_pos[0] - y) - (anchor_pos[0] - x)
    else:
        rel_pos_val = anchor_val + (anchor_pos[0] - x) - (anchor_pos[0] - y)

    print(rel_pos_val)
