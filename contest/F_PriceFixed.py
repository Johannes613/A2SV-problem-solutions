n = int(input())
prod = []
for _ in range(n):
    a, b = map(int, input().split())
    prod.append([a, b])
    
prod.sort(key=lambda x: x[1])

left,cost,bght= 0,0,0
right = n - 1


while left <= right:
    if bght >=prod[left][1]:
        cost +=prod[left][0]
        bght +=prod[left][0]
        prod[left][0] = 0
        left += 1
    else:
        take =min(prod[left][1] - bght, prod[right][0])
        bght += take
        cost +=take * 2
        prod[right][0] -= take
        if prod[right][0]== 0:
            right -= 1

print(cost)