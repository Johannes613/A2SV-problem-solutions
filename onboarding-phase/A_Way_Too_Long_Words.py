n = int(input())

for i in range(n):
    word = input().strip()
    size = len(word)
    if size > 10:
        print("".join([word[0],str(size - 2),word[size - 1]]))
    else:
        print(word)