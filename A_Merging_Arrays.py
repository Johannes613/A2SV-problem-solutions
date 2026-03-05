l1,l2 = map(int, input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))


new_arr = []

p1 = 0
p2 = 0

while p1 < l1 or p2 < l2:
    if p1 >= l1:
        new_arr.append(arr2[p2])
        p2 += 1
    elif p2 >= l2:
        new_arr.append(arr1[p1])
        p1 += 1
    elif arr1[p1] <=  arr2[p2]:
        new_arr.append(arr1[p1])
        p1 += 1
    else:
        new_arr.append(arr2[p2])
        p2 += 1 

print(" ".join(map(str,new_arr)))



    




