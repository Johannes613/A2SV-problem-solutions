test_cases = int(input())

for _ in range(test_cases):
    n = int(input())

    array = list(map(int,input().split()))
    sum = 0
    for x in array:
        sum += x
    if sum % n != 0:
        print(-1)
        continue

    avg = sum / n
    k = 0

    for x in array:
        if x > avg:
            k += 1
    print(k)
    

