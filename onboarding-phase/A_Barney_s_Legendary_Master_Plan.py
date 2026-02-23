test_cases = int(input())

for _ in range(test_cases):
    n = int(input())

    array = list(map(int, input().split()))

    dist_vals = set(array)

    print(2 * len(dist_vals) - 1)

