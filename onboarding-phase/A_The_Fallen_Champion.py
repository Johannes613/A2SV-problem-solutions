w,t = map(int, input().split())

n = int(input().strip())

for _ in range(n):
    win, time = map(int,input().split())
    if w < win:
        print("The Fallen Champion")
        exit()
    elif w > win:
        continue
    elif t <= time:
        continue
    else:
        print("The Fallen Champion")
        exit()
print("The Champion Saves the Accused")

    