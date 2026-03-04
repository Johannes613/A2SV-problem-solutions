test_cases = int(input())

for _ in range(test_cases):

    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    distinct_count = 1 

    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            distinct_count += 1

    if distinct_count % 2 == 1:
        print("YES")
    else:
        print("NO")