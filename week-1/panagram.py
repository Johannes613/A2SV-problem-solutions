number_of_ch = int(input().strip())
word = input().strip().lower()
hash_set = set()

for ch in word:
    hash_set.add(ch)
if len(hash_set) == 26:
    print("YES")
else:
    print("NO")
    


