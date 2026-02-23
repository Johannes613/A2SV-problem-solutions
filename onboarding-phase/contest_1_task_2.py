input_val = input().split()
k = int(input_val[0])
n = int(input_val[1])
w = int(input_val[2])

total_cost = 0

for i in range(w):
    total_cost += (i+1) * k

if total_cost > n:
    print(total_cost - n)
else: 
    print(0)

