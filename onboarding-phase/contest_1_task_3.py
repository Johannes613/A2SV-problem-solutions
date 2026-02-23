test_cases = int(input())

for each_tc in range(test_cases):
    test_case = input().strip()
    if len(test_case) > 10:
        result = test_case[0] + str(len(test_case) - 2) + test_case[len(test_case) - 1]
        print(result)
    else:
        print(test_case)
