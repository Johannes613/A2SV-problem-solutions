tc = int(input())

for _ in range(tc):
    n = int(input())
    players = list(map(int, input().split()))
    players.sort()

    left = 0
    right = n - 1

    elites_sum = 0
    crowds_sum = 0

    found = False

    while left <= right:
        if elites_sum > crowds_sum:
            crowds_sum += players[left]
            left += 1
        else:
            elites_sum += players[right]
            right -= 1

        if elites_sum > crowds_sum and (n - 1 - right) < left:
            found = True
            break

    if found:
        print("YES")
    else:
        print("NO")