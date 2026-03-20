n = int(input())
s = input().strip()

if n == 1:
    print("Yes")
else:
    occurrence = {}
    for ch in s:
        if ch in occurrence:
            occurrence[ch] += 1
        else:
            occurrence[ch] = 1

    for c in occurrence.values():
        if c >= 2:
            print("Yes")   
            break
    else:
        print("No")