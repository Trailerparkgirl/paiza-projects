input_line = input()
values = input_line.split(" ")
N = int(values[0])


cap = []
for i in range(N):
    cap = (input())


M = int(values[1])
people = []
for B in range(M):
    people.append(input())


for gondola in cap:
    if gondola < people[0]:
        people[0] = people[0] - gondola


print(cap)
print(people)
print(N)