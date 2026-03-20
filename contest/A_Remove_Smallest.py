n = int(input())

for i in range(n):
    size = int(input())
    array = list(map(int,input().split()))

    array.sort()
    cont = True
    for j in range(1,len(array)):
        if array[j] - array[j - 1] > 1:
            cont = False
            break
    if cont:
        print("YES")
    else:
        print("NO")