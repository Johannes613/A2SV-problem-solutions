n,tc = map(int,input().split())
arr = list(map(int,input().split()))


cur,max_val,left = 0,0,0

for i in range(n):
    cur += arr[i]
    while cur > tc: 
        cur -= arr[left]
        left+=1
    
    max_val = max(max_val,i - left + 1)

print(max_val)