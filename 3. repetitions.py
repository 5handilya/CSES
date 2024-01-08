seq = str(input())
maxcount = 1
i = 0
loccount = 1
while i < len(seq) - 1:
    if seq[i] == seq[i+1]:
        loccount += 1
    else:
        loccount = 1
    if loccount > maxcount:
        maxcount = loccount
    i += 1
print(maxcount)