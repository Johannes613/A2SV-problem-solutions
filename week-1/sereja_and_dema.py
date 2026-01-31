n = int(input().strip())

cards = input().split()

for i in range(n):
    cards[i] = int(cards[i])

first  = 0
last = n - 1

ser = 0
dim = 0
turn_ser = True

while first <= last:
    if cards[first] >= cards[last]:
        take = cards[first]
        first += 1
    else:
        take = cards[last]
        last -= 1
    if turn_ser:
        ser += take
    else:
        dim += take
    
    turn_ser = not turn_ser

print(ser,dim)

    
