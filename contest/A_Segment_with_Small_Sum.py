n,s = map(int,input().split())

nums = list(map(int, input().split()))


left = 0
longest = 0
prefix_sum = 0

for right in range(n):
    prefix_sum += nums[right]

    while prefix_sum > s:
        prefix_sum -= nums[left]
        left += 1
    longest = max(right - left + 1,longest)

print(longest)


    
            
