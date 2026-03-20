l1,l2 = map(int, input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))


new_arr = []

p1 = 0
p2 = 0


while p2 < l2:
    while p1 < l1 and arr1[p1] < arr2[p2]:
        p1 += 1
    new_arr.append(p1)
    p2 += 1

print(" ".join(map(str,new_arr)))

