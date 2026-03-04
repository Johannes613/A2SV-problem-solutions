n, k = map(int, input().split())
array = list(map(int, input().split()))

curr_sub = 0
index = 0 
array.sort()



for _ in range(k):

    while index < n:
        if array[index] - curr_sub > 0:
            break
        index += 1

    if index == n:
        print(0)
    else:
        value = array[index] - curr_sub
        
        curr_sub += value
        print(value)