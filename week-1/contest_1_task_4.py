input_val = input().split()
n = int(input_val[0])
k = int(input_val[1])

odds = (n + 1) // 2

if k <= odds: print(2 * k -1)
else: 
    result = k - odds
    print(2 * result)

