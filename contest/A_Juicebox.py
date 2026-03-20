tc = int(input())

for i in range(tc):
    n, k = map(int, input().split())
    
    total = [0] * (k + 1)
    
    for j in range(k):
        b, c = map(int, input().split())
        total[b] += c
    
    values = sorted(total, reverse=True)
    
    print(sum(values[:n]))