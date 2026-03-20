tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
        
    if n == 1 and m == 1:
        print("-1")
        
    else:
        for i in range(n):
            row = [arr[(i + 1) % n][(j + 1) % m] for j in range(m)]
            print(" ".join(map(str, row)))