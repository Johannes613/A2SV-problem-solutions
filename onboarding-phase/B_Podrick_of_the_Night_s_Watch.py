n = int(input())

hash_map = {}

for _ in range(n):
    m  = int(input())
    for _ in range(m):
        message = "".join(input().split())
        hash_map[message] = hash_map.get(message,0) + 1
        if hash_map[message] >= 0.8 * n:
            print("YES")
            exit()
print("NO")           