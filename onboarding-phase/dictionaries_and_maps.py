# Enter your code here. Read input from STDIN. Print output to STDOUT
count = int(input())
dictionary = {}

for i in range(count):
    entry = input().split()
    dictionary[entry[0]] = entry[1]

while True:
    try:
        val = input().strip()
        if val in dictionary:
            print(f"{val}={dictionary[val]}")
        else:
            print("Not found")
    except EOFError:
        break
