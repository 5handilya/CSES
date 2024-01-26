from math import comb
k = int(input())
for i in range(1, k+1):
    if(i == 1):
        print("0")
    else:
        #n_total is the total number of ways two knights can be placed in an i x i square
        n_total = comb(i**2,2)
        #n_rect is the number of 3 x 2 or 2 x 3 rectangles that can fit inside an n x n square
        n_rect = 2*(i-1)*(i-2)
        #2 conflict combinations per rect
        n_conflict = n_rect * 2
        print(n_total - n_conflict)
