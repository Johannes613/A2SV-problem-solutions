n = int(input())

cards= list(map(int,input().split()))

start = 0
end = n - 1

sereja_score = 0
dima_score = 0

sereja_turn = True

while start <= end:
    if cards[start] <= cards[end]:
        if sereja_turn: 
            sereja_score += cards[end]
        else: 
            dima_score += cards[end]
        end -= 1
    else:
        if sereja_turn: 
            sereja_score += cards[start]
        else: 
            dima_score += cards[start]
        start += 1
    sereja_turn = not sereja_turn
    

print(sereja_score,dima_score)

