with open('1.txt') as f:
    lines = f.readlines()


for i in range(len(lines)):
    lines[i] = int(lines[i].strip())

counter = 0
for i in range(len(lines)-3):
    first = lines[i] + lines[i+1] + lines[i+2]
    second = lines[i+1] + lines[i+2] + lines[i+3]

    if(second > first):
        counter += 1

print(counter)