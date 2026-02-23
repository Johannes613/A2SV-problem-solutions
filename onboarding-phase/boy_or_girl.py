name = input().strip()
hash_set = set()

for ch in name:
    hash_set.add(ch)
if len(hash_set) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

