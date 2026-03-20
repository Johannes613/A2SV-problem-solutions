tc = int(input())

for _ in range(tc):

    n = int(input())
    vals = list(map(int, input().split()))

    vals.sort()

    min_opt = float('inf')

    for i in range(n - 2):
        first = vals[i]
        second = vals[i + 1]
        third = vals[i + 2]

        opt_req = third - first

        if opt_req < min_opt:
            min_opt = opt_req

    print(min_opt)