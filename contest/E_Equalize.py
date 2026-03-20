tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr = sorted(list(set(arr)))
    
    m = len(arr)
    ans = 0
    left = 0
    
    for right in range(m):
        while arr[right] - arr[left] >= n:
            left += 1
            
        curr_len = right - left + 1
        if curr_len > ans: ans = curr_len
            
    print(ans)