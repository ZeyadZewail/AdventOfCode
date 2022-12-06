with open('3.txt') as f:
    lines = f.readlines()


for i in range(len(lines)):
    lines[i] = lines[i].strip()


counter = []

for i in range(len(lines[0])):
    counter.append({0:0, 1:0})


for i in range(len(lines)):
    for j in range(len(lines[i])):
        counter[j][int(lines[i][j])] += 1

gamma = ""
epsilon = ""

for i in counter:
    zero = i[0]
    one = i[1]
    if( zero > one ):
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

gamma = int(gamma,2)

epsilon = int(epsilon,2)

print(gamma*epsilon)
