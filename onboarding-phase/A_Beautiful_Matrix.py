for i in range(5):
    lis = list(map(int,input().split()))
    idx = lis.index(1) if 1 in lis else -1
    if idx != -1:
        swaps = abs(i - 2) + abs(idx - 2)
print(swaps)