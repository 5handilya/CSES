result = 0
array_size = int(input())
array = input()
ns_str = array.split()
array = list(map(int,ns_str))

i = 0
while i < len(array)-1:
    if (array[i] > array[i+1]):
        result += (array[i] - array[i+1])
        array[i+1] = array[i]
    i += 1

print(result)