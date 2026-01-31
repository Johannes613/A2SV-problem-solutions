password = input().strip()
n = int(input().strip())

first_found = False
sec_found = False



for i in range(n):
    inp = input().strip()
    if inp == password:
        print("YES")
        exit()
    
    if inp[1] == password[0]:
        first_found = True
    if inp[0] == password[1]:
        sec_found = True
if first_found and sec_found:
    print("YES")
else:
    print("NO")






