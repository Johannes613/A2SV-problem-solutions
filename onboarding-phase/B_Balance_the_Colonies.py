n = int(input())

for i in range(n):
    num_people = int(input())
    if num_people == 2 or num_people == 3:
        print(num_people)
    elif num_people % 2 == 0:
        print(0)
    else:
        print(1)

   
