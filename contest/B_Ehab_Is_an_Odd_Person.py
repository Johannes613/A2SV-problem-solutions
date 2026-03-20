n = int(input().strip())

arr = list(map(int,input().split()))

even_exits,odd_exists = False, False

for num in arr:
    if num % 2 == 0:
        even_exits = True
    else:
        odd_exists = True

if even_exits and odd_exists:
    arr.sort()
print(" ".join(map(str,arr)))