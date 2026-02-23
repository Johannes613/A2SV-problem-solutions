test_cases = int(input())

for each_tc in range(test_cases):
    test_case = input().split()
    first = int(test_case[0])
    sec = int(test_case[1])
    third = int(test_case[2])

    for i in range(5):
        if first <= sec and first <= third:
            first += 1
        elif sec <= first and sec <= third:
            sec += 1
        else:
            third += 1
    print(first * sec * third)
