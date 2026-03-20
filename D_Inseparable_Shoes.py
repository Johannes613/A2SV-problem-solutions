tc = int(input())
for _ in range(tc):
    n = int(input())
    s = list(map(int, input().split()))
    
    hash_map = {}
    for val in s:
        if val in hash_map: hash_map[val] += 1
        else: hash_map[val] = 1
            
    pos = True
    for val in hash_map:
        if hash_map[val] == 1:
            pos = False
            break
            
    if not pos: print("-1")
    else:
        ans = []
        i = 0
        while i < n:
            size = hash_map[s[i]]
            
            group = []
            for j in range(size):
                group.append(str(i + j + 1))
                
            chang = [group[-1]] + group[:-1]
            ans.extend(chang)
            
            i += size
            
        print(" ".join(ans))